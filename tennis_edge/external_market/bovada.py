"""Bovada's public tennis coupon, parsed into ExternalMarketObservation rows.

What this source is, stated plainly so nothing downstream over-reads it: Bovada is a RECREATIONAL
sportsbook. Its line is a genuine independent opinion about a tennis match, formed by people who are not
on Kalshi, and that is exactly the independence Wave 4 needs -- but it is not a sharp line. A
disagreement between Bovada and Kalshi is evidence that two venues disagree, not evidence that Kalshi is
wrong.

Structure: a list of path groups, each with events; each event has displayGroups, each of those has
markets, each market has outcomes carrying american and decimal prices and, for handicap markets, the
line. The event's `lastModified` is a real per-event timestamp in epoch milliseconds, so staleness is
measurable rather than assumed.

Only markets whose full outcome set is present are de-vigged. A market where one side is suspended is
carried with its raw implied probability and no de-vigged value; the missing side is never invented.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone

from tennis_edge.external_market.devig import devig_all
from tennis_edge.external_market.schema import ExternalMarketObservation, SPORTSBOOK

SOURCE = "bovada"

#: Bovada descriptionKey -> our family. Anything not listed is skipped rather than guessed at.
FAMILY_MAP = {
    "Head To Head": "MATCH_WINNER",
    "Handicap - Asian - Games": "GAME_SPREAD",
    "Alternate Game Spread": "GAME_SPREAD",
    "Main Dynamic Over/Under": "TOTAL_GAMES",
    "Total Games O/U": "TOTAL_GAMES",
    "Alternate Total Games": "TOTAL_GAMES",
    "Total Sets": "TOTAL_SETS",
    "Set Betting": "EXACT_SET_SCORE",
    "Set Correct Score": "EXACT_SET_SCORE",
    "Set Spread": "SET_SPREAD",
    "Alternate Set Spread": "SET_SPREAD",
}

#: only whole-match markets. A first-set or in-play line prices a different question than a Kalshi
#: match-scope contract, and comparing them would be the quietest possible way to invent a dislocation.
MATCH_PERIODS = ("Match",)


def _hash(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _iso_ms(ms) -> str | None:
    try:
        return datetime.fromtimestamp(float(ms) / 1000.0, tz=timezone.utc).isoformat()
    except (TypeError, ValueError):
        return None


def parse_coupon(payload, *, observed_at: str, evidence_location: str = "",
                 raw_bytes: bytes = b"") -> tuple[list, dict]:
    """(observations, stats). Mapping to our physical matches happens later and separately."""
    ev_hash = _hash(raw_bytes) if raw_bytes else ""
    out, stats = [], {"events": 0, "markets": 0, "skipped_family": 0, "skipped_period": 0,
                      "skipped_live": 0, "one_sided": 0, "rows": 0, "devigged": 0}
    for group in payload if isinstance(payload, list) else []:
        path = " / ".join(p.get("description", "") for p in (group.get("path") or []))
        for e in group.get("events") or []:
            stats["events"] += 1
            if e.get("live"):
                stats["skipped_live"] += 1
                continue
            comps = e.get("competitors") or []
            if len(comps) != 2:
                continue
            a, b = comps[0].get("name"), comps[1].get("name")
            start_iso = _iso_ms(e.get("startTime"))
            src_ts = _iso_ms(e.get("lastModified"))
            for dg in e.get("displayGroups") or []:
                for m in dg.get("markets") or []:
                    stats["markets"] += 1
                    fam = FAMILY_MAP.get(m.get("descriptionKey"))
                    if not fam:
                        stats["skipped_family"] += 1
                        continue
                    period = (m.get("period") or {}).get("description")
                    if period not in MATCH_PERIODS or (m.get("period") or {}).get("live"):
                        stats["skipped_period"] += 1
                        continue
                    outs = [o for o in (m.get("outcomes") or []) if o.get("status") == "O"]
                    decs = [_f((o.get("price") or {}).get("decimal")) for o in outs]
                    if not outs or any(d is None or d <= 1.0 for d in decs):
                        stats["one_sided"] += 1
                        continue
                    dv = None
                    if len(outs) >= 2:
                        try:
                            dv = devig_all(decs)
                            stats["devigged"] += 1
                        except ValueError:
                            dv = None
                    for i, o in enumerate(outs):
                        price = o.get("price") or {}
                        strike = _f(price.get("handicap"))
                        out.append(ExternalMarketObservation(
                            source=SOURCE, source_kind=SPORTSBOOK,
                            source_event_id=str(e.get("id")), observed_at=observed_at,
                            physical_match_id=None, participant_a=a, participant_b=b,
                            market_family=fam, side=o.get("description") or "", strike=strike,
                            decimal_odds=decs[i], american_odds=_f(price.get("american")),
                            implied_probability=1.0 / decs[i],
                            devigged_probability=(dv.probabilities[i] if dv else None),
                            devig_method=(dv.method if dv else ""),
                            source_margin=(dv.margin if dv else None),
                            n_sides_in_market=(dv.n_sides if dv else len(outs)),
                            line=f"{path} | {m.get('description')}",
                            status=m.get("status") or "", is_pregame=not bool(e.get("live")),
                            source_timestamp=src_ts, raw_evidence_hash=ev_hash,
                            raw_evidence_location=evidence_location))
                        stats["rows"] += 1
    return out, stats


def event_index(payload) -> list[dict]:
    """A light index of the coupon's events, for mapping and coverage reporting."""
    rows = []
    for group in payload if isinstance(payload, list) else []:
        path = [p.get("description", "") for p in (group.get("path") or [])]
        for e in group.get("events") or []:
            comps = e.get("competitors") or []
            if len(comps) != 2:
                continue
            rows.append({"source_event_id": str(e.get("id")), "description": e.get("description"),
                         "a": comps[0].get("name"), "b": comps[1].get("name"),
                         "start_utc": _iso_ms(e.get("startTime")),
                         "last_modified_utc": _iso_ms(e.get("lastModified")),
                         "path": path, "competition": path[0] if path else "",
                         "level_hint": path[1] if len(path) > 1 else "",
                         "live": bool(e.get("live"))})
    return rows
