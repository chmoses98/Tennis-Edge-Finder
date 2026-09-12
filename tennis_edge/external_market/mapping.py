"""Deciding that an external venue's event and a Kalshi event are the same tennis match, or refusing to.

The rule is the strictest one available rather than a new one: BOTH names on BOTH sides are resolved
through the same canonical player registry Kalshi mapping already uses, and the match is identified by
the pair of canonical player ids plus the calendar date. Two venues agree that this is the same match
only when they agree about who is playing, in a system that has already refused every name it could not
place safely.

Consequences, all deliberate:

* a venue name that resolves to nobody, or to two people, maps to nothing -- there is no surname
  fallback, no fuzzy distance, no "probably him";
* a match where only one player resolves maps to nothing, because half an identification is not one;
* doubles requires all four players and is refused here, since the singles registry cannot carry a pair.

The date is the local UTC date of the scheduled start. Venues occasionally disagree by a day across the
midnight boundary, so a one-day tolerance is allowed ONLY when the two starts are within six hours of
each other; that is a clock difference, not a different match.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

MAPPED = "MAPPED"
UNMAPPED_PLAYER = "UNMAPPED_PLAYER"
AMBIGUOUS_PLAYER = "AMBIGUOUS_PLAYER"
DOUBLES_UNSUPPORTED = "DOUBLES_UNSUPPORTED"
NO_COUNTERPART = "NO_COUNTERPART"
DATE_MISMATCH = "DATE_MISMATCH"

#: two venues may disagree about the calendar date only if their start times are this close
MAX_START_GAP_S = 6 * 3600


@dataclass(frozen=True)
class MappedEvent:
    source: str
    source_event_id: str
    physical_match_id: str | None
    player_a_id: str | None
    player_b_id: str | None
    status: str
    confidence: float
    reason: str = ""


def _is_doubles(name: str) -> bool:
    return "/" in (name or "")


def _iso(x):
    if not x:
        return None
    try:
        return datetime.fromisoformat(str(x).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def physical_key(tour: str, pid_a: str, pid_b: str, day) -> str:
    lo, hi = sorted((str(pid_a), str(pid_b)))
    return f"{tour}:{lo}:{hi}:{day}"


def map_event(mapper, *, source: str, source_event_id: str, tour: str, name_a: str, name_b: str,
              start_utc, today=None) -> MappedEvent:
    """Resolve one external event to a physical match key, or say why not."""
    if _is_doubles(name_a) or _is_doubles(name_b):
        return MappedEvent(source, source_event_id, None, None, None, DOUBLES_UNSUPPORTED, 0.0,
                           "doubles pairs need four identities; the singles registry carries two")
    start = _iso(start_utc)
    day = (start.date() if start else (today or datetime.utcnow().date()))
    ra = mapper.resolve(tour, name_a, None, day)
    rb = mapper.resolve(tour, name_b, None, day)
    for r, nm in ((ra, name_a), (rb, name_b)):
        if r["status"] == "AMBIGUOUS":
            return MappedEvent(source, source_event_id, None, None, None, AMBIGUOUS_PLAYER, 0.0,
                               f"{nm}: {r.get('reason', '')}")
        if r["status"] != "MAPPED":
            return MappedEvent(source, source_event_id, None, None, None, UNMAPPED_PLAYER, 0.0,
                               f"{nm}: {r.get('reason', '')}")
    conf = min(ra["confidence"], rb["confidence"])
    return MappedEvent(source, source_event_id,
                       physical_key(tour, ra["player_id"], rb["player_id"], day),
                       ra["player_id"], rb["player_id"], MAPPED, conf)


def join_to_kalshi(external: dict, kalshi: dict) -> dict:
    """Join two {physical_match_id: record} views, allowing a one-day slip only for near-simultaneous starts.

    Returns {physical_match_id_on_the_kalshi_side: (kalshi_record, external_record, note)}.
    """
    out = {}
    by_pair_ext = {}
    for key, rec in external.items():
        tour, a, b, day = key.split(":", 3)
        by_pair_ext.setdefault((tour, a, b), []).append((day, key, rec))
    for key, krec in kalshi.items():
        tour, a, b, day = key.split(":", 3)
        if key in external:
            out[key] = (krec, external[key], "exact")
            continue
        cands = by_pair_ext.get((tour, a, b)) or []
        for eday, ekey, erec in cands:
            try:
                d1 = datetime.fromisoformat(day).date()
                d2 = datetime.fromisoformat(eday).date()
            except ValueError:
                continue
            if abs((d1 - d2).days) != 1:
                continue
            ks, es = _iso(krec.get("start_utc")), _iso(erec.get("start_utc"))
            if ks and es and abs((ks - es).total_seconds()) <= MAX_START_GAP_S:
                out[key] = (krec, erec, f"one-day slip accepted: starts {abs((ks - es).total_seconds()):.0f}s apart")
                break
    return out


def audit(mapped) -> dict:
    """Mapping statistics, including every refusal reason, because the refusals are the useful half."""
    from collections import Counter
    c = Counter(m.status for m in mapped)
    reasons = Counter(m.reason.split(":")[0] for m in mapped if m.status != MAPPED and m.reason)
    n = len(mapped) or 1
    return {"total": len(mapped), "by_status": dict(c), "mapped_rate": round(c[MAPPED] / n, 4),
            "top_refusal_subjects": dict(reasons.most_common(10))}
