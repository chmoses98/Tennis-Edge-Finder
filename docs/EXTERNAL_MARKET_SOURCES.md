# External tennis price sources: what exists, what is usable, and what we may not touch

Wave 4 Phase 0. Probed on GitHub Actions runners on 2026-09-12; the research sandbox has no egress to any
of these hosts. Raw payloads and manifests are published to `tennis-data` under
`data/sources/external_odds_probe/`.

**robots.txt was fetched for every host before any data URL, and a disallowed path was not requested.**
A source we may not use is not a source, whatever it contains.

## Verdict

| source | kind | reachable | keyless | tennis | verdict |
|---|---|---|---|---|---|
| **Bovada** | recreational sportsbook | yes | yes | yes, deep | **ACCEPTED** |
| Polymarket | prediction market | yes | yes | listed, not traded | **REJECTED** (no liquidity) |
| Smarkets | betting exchange | partly | yes | tennis tree exists | **DEFERRED** (needs a multi-hop walk) |
| ESPN | media feed | yes | yes | no odds for tennis | REJECTED |
| The Odds API | aggregator | yes | **no** (401) | n/a | REJECTED (cannot run unattended without a key) |
| Betfair | exchange | 403 | no | n/a | REJECTED |
| Pinnacle | sharp book | **451** | no | n/a | REJECTED (unavailable for legal reasons) |

## Bovada — the one accepted source

`GET https://www.bovada.lv/services/sports/event/coupon/events/A/description/tennis?lang=en`

| property | observed |
|---|---|
| auth | none |
| robots.txt | allows this path for `*` |
| payload | ~900 KB JSON, 24 path groups, 55 events in the snapshot measured |
| ATP | yes (tour, Challenger) |
| WTA | yes (tour, WTA 125K) — the largest share of the board |
| Challenger | yes, singles and doubles |
| ITF | yes, men's and women's |
| qualifying | not separately labelled |
| doubles | yes (4 events) — **refused by our mapping**, which needs four identities |
| market families | Head To Head, Game Spread (+alternates), Total Games (+alternates), Total Sets, Set Betting / Set Correct Score, Set Spread. Also first-set and in-play markets, which we skip. |
| price form | offered odds, american and decimal, with a margin (2.4%–5.3% observed on match winner) |
| two-sided | no — offered odds on each outcome, so the margin must be removed |
| timestamps | `lastModified` per event, epoch ms. Median age at capture ~8 minutes. |
| rate limits | none advertised; we poll once per ~10 minutes |
| storable | yes; raw payloads are archived per capture |
| independent of Kalshi | yes — different venue, different customers, no shared order book |

**Bovada is a recreational book, not a sharp one.** Its line is a genuine independent opinion, and that
is the independence Wave 4 needs, but a Bovada/Kalshi disagreement is two venues disagreeing, not
evidence that Kalshi is wrong. Everything downstream says so.

## Polymarket — listed, not traded

`GET https://gamma-api.polymarket.com/events?closed=false&tag_slug=tennis` — keyless, no robots
restriction, and it lists tennis at exactly the levels Kalshi lists: ATP, WTA, Challenger, ITF,
qualifying, juniors and doubles. 247 open tennis events, 235 of them individual matches.

And then the order books:

| measure | value |
|---|---|
| markets marked "accepting orders" | 2,120 |
| CLOB books actually fetched | 120 |
| books with a two-sided price | **1** |
| books two-sided within 10c with 50+ size on both sides | **1** |

The single exception quotes 0.47/0.53 with identical 738-unit depth on each side and a timestamp shared
with every other market on the venue — a seeded book, not a market. Everything else is one-sided at 0.001
or 0.95+. Polymarket lists tennis and does not trade it. Rejected, and worth re-probing later: the
listings exist, so liquidity could arrive.

## Smarkets — deferred, not rejected

`GET https://api.smarkets.com/v3/events/` returns 200 with a paginated event tree in which Tennis is a
top-level node (id 102016). Reaching a match price needs a walk — children, competitions, events,
markets, quotes — that the Phase 0 budget did not cover. It is a genuine exchange with two-sided prices
and would be the first SHARP reference this project has ever had, so it is the highest-value item left
on this list.

## The rest

* **ESPN** carries no odds block on its tennis scoreboard, and its `summary` endpoint 400s for tennis.
* **The Odds API** returns 401 without a key. A free tier exists but requires a signed-up key; a key we
  do not have cannot run unattended, and this project does not sign up for accounts on its own.
* **Betfair** returns 403 to an unauthenticated client; the exchange requires an application key.
* **Pinnacle** returns **451 Unavailable For Legal Reasons**. The mandate said not to assume Pinnacle was
  available. It is not.

## Independence groups

Declared in `tennis_edge/external_market/consensus.py`. Sources in one group count as ONE witness however
many names they appear under, and any feed derived from Kalshi is inadmissible as a witness against
Kalshi. Today the accepted set has exactly one group, so every reference this project can build is a
single-witness reference — recorded on every row, and the first thing a second source would fix.
