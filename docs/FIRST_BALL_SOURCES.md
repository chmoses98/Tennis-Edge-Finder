# First-ball sources: what is actually reachable, and what is not

Every claim in this document is backed by a probe run whose raw evidence is on the `tennis-data` branch
under `tennis-edge-finder/data/firstball/probe/<run_id>/`. Probes were executed from GitHub Actions
runners, because the research sandbox has no egress to tennis hosts. Each candidate was requested
several times, spaced in time, so that a single lucky response could not be mistaken for reliability,
and each host's `robots.txt` was read in the same run.

**Probe runs**

| run | scope |
|---|---|
| `20260911T193614Z` | 24 candidates across 17 hosts, 3 rounds, plus a yesterday-dated probe of every date-keyed endpoint |
| `20260911T195032Z` | 13 candidates, 2 rounds, raw payloads stored |
| `20260911T195702Z` | 6 candidates chasing ITF and Challenger, raw payloads stored |

One correction worth recording: in the first run ESPN's WTA scoreboard looked broken (HTTP 200, unparseable).
It was not. The response is 2,000,001 bytes and the prober's own 2 MB cap truncated it. The cap is now
16 MB. A probe that silently truncates evidence produces false negatives, which is the same failure mode
this whole wave exists to eliminate.

## Authority matrix

| source | class | reachable | tours/levels proven | answers | timestamp semantics | latency | reliability | historical | terms / access |
|---|---|---|---|---|---|---|---|---|---|
| **ESPN site API, ATP scoreboard** | broadcaster | **yes** | ATP main tour, Grand Slam | live state (`pre`/`in`/`post`), `Walkover`, `Retired`, scheduled time | ISO 8601 with an explicit `Z` | 119-530 ms | 5/5 rounds | yes, dated queries work | undocumented public JSON; `robots.txt` itself returns 403, so no directive either way |
| **ESPN site API, WTA scoreboard** | broadcaster | **yes** | WTA main tour, Grand Slam | same | same | 141-324 ms | 2/2 rounds after the cap fix | yes | same |
| ESPN core API (`sports.core.api.espn.com`) | broadcaster | yes | ATP, WTA | index of `$ref` links only, one hop per event | n/a | ~130 ms | 3/3 | yes | same |
| ESPN league index | broadcaster | yes | **exactly `atp` and `wta`** | n/a | n/a | ~230 ms | 2/2 | n/a | same |
| ATP Tour live/current scores | official tour | **no** | - | - | - | - | 0/5 | - | Cloudflare interstitial ("Just a moment..."), HTTP 403; `robots.txt` also disallows `*/ajax/*` |
| protennislive | official tour | **no** | - | - | - | - | 0/5 | - | HTTP 404 on the guessed feed, HTTP 503 on the site over both https and http |
| WTA API (`api.wtatennis.com`) | official tour | **no** | - | - | - | - | 0/5 | - | HTTP 404 on every path tried |
| ITF `TournamentApi/GetCalendar` | official tour | yes | ITF calendar metadata | tournament start/end dates only, **no match state** | naive ISO, date-only | 59-1605 ms | 5/5 | - | `robots.txt` disallows only `/umbraco/` |
| ITF `LiveScoresApi` / `MatchesApi` | official tour | **no** | - | - | - | - | 0/5 | - | HTTP 404: the controller names were guesses |
| ITF live scoreboard (stadion.io) | official tour | **not yet** | ITF, qualifying | would answer live state | unknown | - | root returns 403 | - | the page is a React shell; the data host is `api.itf-production.sports-data.stadion.io` with a 5 s refetch interval, but the bundle builds paths dynamically. A headless-browser discovery probe is the open thread. |
| SofaScore (`api.`, `www.`, `api.sofascore.app`) | aggregator | **no** | - | - | - | - | 0/7 across three hosts | - | HTTP 403 to runner IPs on every host, including `robots.txt` |
| flashscore feed | aggregator | **no** | - | - | - | - | 0/3 | - | HTTP 401 (signed requests) |
| livescore.com public API | aggregator | **no** | - | - | - | - | 0/3 | - | HTTP 503 |
| TheSportsDB | aggregator | yes, but empty | none | returned `{"events": null}` for tennis on the probe date | n/a | 53-76 ms | 3/3 | 200 | free public key |
| tennisexplorer match board | aggregator | yes (HTML) | ATP, WTA, Challenger, ITF | in-play vs scheduled, by scraping a 500 KB page | page-local | 1.1-1.6 s | 5/5 | dated URLs work | `robots.txt` allows `/matches/` and `/live/`; HTML scraping, no API |
| Grand-slam official feeds (US Open, Wimbledon, AO, RG) | official event | **no** | - | - | - | - | 0/12 | - | US Open timed out at 25 s; Wimbledon returns the site HTML; AO and RG return 404. All four are out of season paths. |
| Kalshi (corroboration only) | exchange | yes | all | in-play trading activity | epoch, exchange clock | 73-119 ms | 3/3 | yes | already used by this project; **never sports truth on its own** |

## Chosen source hierarchy

1. **ESPN site API** is the production source for ATP and WTA main tour and Grand Slam, singles.
   It is the only reachable feed that gives a per-match state (`pre` / `in` / `post`) with a stable
   schema, sub-second latency and a payload that covers a whole tournament in one request.
2. **Kalshi** may narrow a bracket ESPN has already established. It can never create one. Sports truth
   and exchange truth stay separate objects, as they have from the start of this project.
3. **Nothing else is wired in.** tennisexplorer is the only remaining candidate for Challenger and ITF,
   and it would require HTML scraping of a page whose structure is not a contract. It is recorded here
   as a candidate and deliberately not implemented in this wave.

## Coverage by level: the honest picture

| level | first-ball source | status |
|---|---|---|
| ATP main tour (250/500/1000/Finals) | ESPN | **solved**, state transitions |
| WTA main tour | ESPN | **solved**, state transitions |
| Grand Slam singles | ESPN | **solved** (the probe returned all 478 US Open matches from one request, with `Final`, `Retired`, `Walkover` and `In Progress` states) |
| Doubles | ESPN | **unverified.** The US Open board parsed zero doubles rows. Either ESPN does not carry them or it shapes them differently (`roster` rather than `athlete`). Until that is checked against a board with live doubles, doubles matches fall through to START_UNKNOWN. |
| ATP Challenger | none | **unsolved.** ESPN provably does not carry it: its tennis league index contains `atp` and `wta` only, and `atp-challenger` returns HTTP 400. ATP's own site is behind Cloudflare, protennislive is down, SofaScore blocks runner IPs. |
| ITF men / ITF women | none | **unsolved.** Same blocks, plus the ITF's own live feed is served by a provider whose paths the site builds dynamically. |
| Qualifying | none | **unsolved**, for the same reasons. |

This is the outcome the brief anticipated: **ATP and WTA first-ball truth is solved; Challenger, ITF and
qualifying are not.** Those levels keep failing closed as START_UNKNOWN. Their start times are not
guessed, back-filled from the nominal time, or approximated from the market. That is the whole point:
a gap that is visible is a research limitation, while a gap that is filled with a guess is a false claim.

## Rules this research imposes on itself

* **One success is not production-readiness.** Every candidate was probed repeatedly, across rounds
  separated in time, and the reliability column reports rounds-succeeded over rounds-attempted.
* **An undocumented field is a claim, not a fact.** No source here documents its semantics. A source's
  own "start" field is therefore only promoted to confidence A when it falls inside a bracket our own
  polling observed independently, or when the source has been added to a validated list on evidence.
  That list is currently empty.
* **Every feed lags, in the dangerous direction.** A feed still reporting "not started" after play began
  pushes the observed lower bound later than the true first ball, which would turn post-start
  observations into apparently strict pregame ones. Until a source's real latency is measured, the
  lower bound carries a recorded 120 s allowance.
* **Two endpoints from one provider are one witness.** ESPN's ATP and WTA boards return the same
  combined event during a Grand Slam; counting them as agreeing sources would manufacture confidence.
* **Politeness is a design constraint.** Boards are megabytes, so the poller uses conditional requests
  (`If-None-Match` / `If-Modified-Since`), fetches one date for a board that already spans a tournament,
  and scales request volume with the number of sources rather than the number of matches.
