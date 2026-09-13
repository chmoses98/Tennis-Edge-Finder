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

---

## Smarkets, resolved (Wave 5)

Wave 4 left Smarkets as "DEFERRED — a real exchange, reachable, but a price needs a multi-hop walk". It
does. Here is the walk, and what is at the end of it.

### The traversal

The tennis tree is real but useless for capture: **Tennis (id 102016) → 19 category nodes** (ATP, WTA,
Challenger, ITF Men, ITF Women, WTA 125K, Davis Cup, Fed Cup, …) **→ 2,626 tournament nodes → round
nodes** ("Fixtures", "Round of 32", "Qualification") **→ matches**. Every node down to the match is
`type: generic` and carries no date, so finding today's tennis by walking means thousands of requests.

There is a shortcut, and it is the whole reason Smarkets is usable:

```
GET /v3/events/?type=tennis_match&state=upcoming&limit=100   (+ pagination_last_id)
GET /v3/events/{event_ids}/markets/
GET /v3/markets/{market_ids}/contracts/
GET /v3/markets/{market_ids}/quotes/                 <- the order book
GET /v3/markets/{market_ids}/last_executed_prices/   <- what actually traded, with a timestamp
```

`type=tennis_match` is not visible anywhere in the tree — every node the walk returns is `generic` — but
the global query accepts it and returns matches directly. Recorded in
`tennis_edge/external_market/smarkets.py:TRAVERSAL` and asserted by a test, because losing it would cost
another wave to rediscover.

### Authentication

**None.** Every endpoint above answers an unauthenticated GET. `api.smarkets.com` serves no robots.txt
(404); `smarkets.com`'s does not disallow these paths. No control was bypassed and no path returned 401
or 403.

### What is there

| measure | value |
|---|---|
| upcoming tennis matches | **162** (105 within 24h, 57 within 7 days) |
| doubles | 6 |
| markets over the 120 soonest matches | **715** |
| Match winner | **120 — one on every match priced** |
| derivatives | Set 1 winner (81), Correct score Set 1 (68), set betting, exact sets, game spreads, over/under 20.5–23.0 |
| contracts with a book | 242 |
| **two-sided books** | **215 (88.8%)** |
| one-sided / empty | 4 / 23 |
| depth | every two-sided contract had size on both sides |

Richer derivative coverage than Kalshi, on the same levels.

### And the number that decides it

| | Smarkets | Kalshi |
|---|---|---|
| median match-winner spread | **10.3c** | **2c** |
| 25th percentile spread | 9.7c | — |

A representative book: best bid 0.3472 / best ask 0.4348 on one side, 0.5495 / 0.6536 on the other.

A ten-cent spread puts five cents of uncertainty on the midpoint — larger than any cross-venue gap this
project has ever measured (Wave 4: median 0.8c, max 4.1c). So the Smarkets midpoint is a legitimate
independent **opinion** and is not an executable reference, and its executable side is nowhere near it.

### Timestamps

The order book carries **no timestamp**. `source_timestamp` is therefore None — honestly unknown, never
quietly set to the capture time. The market record has `created`/`modified`, which track when the market
was edited rather than when the book moved, and `last_executed_prices` carries a real per-trade timestamp
which is kept beside the quote as the different fact it is.

### How it is used

Stored as its own independent witness group (`smarkets`, kind EXCHANGE), so the consensus can be a median
of two groups rather than one. A spread bound of 6c on exchange rows keeps a wide book out of decisions
while still recording it; that bound applies only to exchange rows, since a sportsbook's overround is a
different quantity from a book's width.
