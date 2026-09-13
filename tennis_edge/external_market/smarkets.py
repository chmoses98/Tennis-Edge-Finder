"""Smarkets: a genuine exchange, and a much wider one than Kalshi.

What the Wave 5 probe established, because it changes how this source may be used:

* the board is real -- 162 upcoming tennis matches, a Match winner market on every one of them, plus a
  derivative set (set winner, correct score, game spreads, totals) that is richer than Kalshi's;
* the books are real -- 89% of match-winner contracts quote both sides, with genuine depth behind them;
* and the median spread is **10 cents**, against Kalshi's 2.

That last number is the whole story. A ten-cent spread means the midpoint carries five cents of
uncertainty, which is larger than any cross-venue gap this project has ever measured, and it means the
executable price is nowhere near the midpoint. So a Smarkets midpoint is a legitimate independent
OPINION and is not an executable reference: it is stored, reported, and prevented from driving a
decision by the spread bound in the consensus layer.

The venue publishes no timestamp on the order book. `source_timestamp` is therefore None -- honestly
unknown rather than quietly set to the capture time -- while the last TRADED price does carry one and is
kept beside it.

Prices arrive as integers in hundredths of a percent (3472 -> 34.72%); the last-traded endpoint uses a
decimal percent string ("45.45"). Quantities are in the venue's own units and are stored raw.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone

from tennis_edge.external_market.schema import EXCHANGE, ExternalMarketObservation

SOURCE = "smarkets"
BASE = "https://api.smarkets.com"

#: the traversal, written down because it is not discoverable from the docs alone
TRAVERSAL = (
    "GET /v3/events/?type=tennis_match&state=upcoming&limit=100 (+pagination_last_id)",
    "GET /v3/events/{event_ids}/markets/",
    "GET /v3/markets/{market_ids}/contracts/",
    "GET /v3/markets/{market_ids}/quotes/",
    "GET /v3/markets/{market_ids}/last_executed_prices/",
)

#: Smarkets market name -> our family. Anything unlisted is skipped rather than guessed at.
FAMILY_MAP = {
    "Match winner": "MATCH_WINNER",
    "Set betting": "EXACT_SET_SCORE",
    "Exact sets best of 3": "TOTAL_SETS",
    "Exact sets best of 5": "TOTAL_SETS",
}

#: markets whose name encodes a line, matched by prefix
PREFIX_FAMILIES = (("Over/under ", "TOTAL_GAMES"),)


def price_to_prob(x) -> float | None:
    """3472 -> 0.3472. A bare percent string ("45.45") -> 0.4545."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    if v <= 0:
        return None
    if v > 100:                       # integer hundredths of a percent
        return v / 10000.0
    if v > 1.0:                       # decimal percent
        return v / 100.0
    return v


def family_of(market_name: str) -> tuple[str | None, float | None]:
    """(family, strike). Set-scoped and in-play markets are deliberately unmapped: they price a
    different question than a match-scope Kalshi contract."""
    name = (market_name or "").strip()
    if name in FAMILY_MAP:
        return FAMILY_MAP[name], None
    for pref, fam in PREFIX_FAMILIES:
        if name.startswith(pref):
            try:
                return fam, float(name[len(pref):].split()[0])
            except (ValueError, IndexError):
                return fam, None
    if " games" in name and (" +" in name or " -" in name):
        return "GAME_SPREAD", None
    return None, None


def book_of(quote) -> dict:
    """best bid, best ask, depth and level counts from one contract's book."""
    bids = (quote or {}).get("bids") or []
    offers = (quote or {}).get("offers") or []
    bb = max((price_to_prob(b.get("price")) for b in bids if price_to_prob(b.get("price"))), default=None)
    ba = min((price_to_prob(o.get("price")) for o in offers if price_to_prob(o.get("price"))), default=None)
    return {"bid": bb, "ask": ba,
            "mid": (0.5 * (bb + ba)) if (bb is not None and ba is not None) else None,
            "spread": (ba - bb) if (bb is not None and ba is not None) else None,
            "bid_size": sum(float(b.get("quantity", 0) or 0) for b in bids),
            "ask_size": sum(float(o.get("quantity", 0) or 0) for o in offers),
            "bid_levels": len(bids), "ask_levels": len(offers)}


def last_traded_index(payload) -> dict:
    """{contract_id: (probability, iso timestamp)} from /last_executed_prices/."""
    out = {}
    blocks = (payload or {}).get("last_executed_prices") or {}
    for _market_id, rows in blocks.items():
        for r in rows or []:
            p = price_to_prob(r.get("last_executed_price"))
            if p is not None:
                out[str(r.get("contract_id"))] = (p, r.get("timestamp"))
    return out


def observations(*, events, markets, contracts, quotes, last_executed, observed_at: str,
                 evidence_location: str = "", raw_bytes: bytes = b"") -> tuple[list, dict]:
    """Build ExternalMarketObservation rows. Mapping to physical matches happens separately."""
    ev_hash = hashlib.sha256(raw_bytes).hexdigest() if raw_bytes else ""
    ev_by_id = {str(e["id"]): e for e in events}
    con_by_market: dict = {}
    for c in contracts:
        con_by_market.setdefault(str(c.get("market_id")), []).append(c)
    traded = last_traded_index(last_executed)

    rows = []
    stats = {"markets": 0, "skipped_family": 0, "no_contracts": 0, "no_book": 0, "rows": 0,
             "two_sided": 0, "one_sided": 0}
    for m in markets:
        stats["markets"] += 1
        fam, strike = family_of(m.get("name"))
        if not fam:
            stats["skipped_family"] += 1
            continue
        ev = ev_by_id.get(str(m.get("event_id")))
        if not ev:
            continue
        cons = con_by_market.get(str(m.get("id"))) or []
        if not cons:
            stats["no_contracts"] += 1
            continue
        title = ev.get("name") or ""
        a, _, b = title.partition(" vs ")
        for c in cons:
            bk = book_of(quotes.get(str(c.get("id"))))
            if bk["bid"] is None and bk["ask"] is None:
                stats["no_book"] += 1
                continue
            stats["two_sided" if bk["mid"] is not None else "one_sided"] += 1
            lt = traded.get(str(c.get("id")))
            rows.append(ExternalMarketObservation(
                source=SOURCE, source_kind=EXCHANGE, source_event_id=str(ev.get("id")),
                observed_at=observed_at, physical_match_id=None,
                participant_a=a.strip() or title, participant_b=b.strip(),
                market_family=fam, side=c.get("name") or "", strike=strike,
                back_price=bk["ask"], lay_price=bk["bid"],
                implied_probability=bk["mid"],
                # an exchange midpoint is already free of a bookmaker's margin, so the "de-vigged"
                # value IS the midpoint -- but only when BOTH sides of the book exist. A one-sided
                # book yields no reference, and its opposite side is not invented.
                devigged_probability=bk["mid"],
                devig_method="exchange_midpoint" if bk["mid"] is not None else "",
                source_margin=bk["spread"], n_sides_in_market=2 if bk["mid"] is not None else 1,
                line=f"{m.get('name')} | market {m.get('id')} | contract {c.get('id')}",
                status=m.get("state") or "", is_pregame=True,
                # the venue stamps no time on the order book. The last TRADED price does, and that is
                # a different fact, so it is carried in the line rather than pretending it is a quote.
                source_timestamp=None,
                raw_evidence_hash=ev_hash, raw_evidence_location=evidence_location))
            stats["rows"] += 1
            if lt:
                rows[-1] = rows[-1].evolve(
                    line=rows[-1].line + f" | last traded {lt[0]:.4f} at {lt[1]}")
    return rows, stats


def event_index(events) -> list[dict]:
    out = []
    for e in events:
        title = e.get("name") or ""
        a, sep, b = title.partition(" vs ")
        if not sep:
            continue
        out.append({"source_event_id": str(e.get("id")), "description": title, "a": a.strip(),
                    "b": b.strip(), "start_utc": e.get("start_datetime"),
                    "last_modified_utc": e.get("modified"), "state": e.get("state"),
                    "bettable": bool(e.get("bettable"))})
    return out
