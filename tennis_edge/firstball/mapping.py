"""Map our Kalshi-derived matches onto a live-score feed's matches, or refuse to.

Identity is where a first-ball system quietly goes wrong: bind "Zverev" to the wrong Zverev and every
pregame label for that match is confidently false. So this module fails closed. A mapping is produced
only when exactly one candidate on the feed fits both players strictly better than any other; a tie, a
bare-surname collision or a cross-day smear yields AMBIGUOUS and no mapping at all.

Affinity uses the project's existing name matcher in both directions, because feeds disagree on style:
ESPN writes "Alexander Zverev", SofaScore writes "Zverev A.". A wrong first initial scores 0.0 there, by
construction, which is what keeps the two Zverevs apart.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

from tennis_edge.identity.names import name_tokens, normalize_name, player_match_score
from .sources import SourceMatch

MIN_AFFINITY = 0.7
#: at or above this the pair is pinned by a verified initial on both sides; below it the match rests on a
#: bare surname and is reported as WEAK, which caps the resulting first-ball truth at confidence C
STRONG_AFFINITY = 0.9
#: a candidate must beat the runner-up by at least this much, else the pair is treated as a collision
MIN_MARGIN = 1e-9
DEFAULT_WINDOW_HOURS = 36


@dataclass(frozen=True)
class OurMatch:
    match_id: str
    player_a: str
    player_b: str
    scheduled_utc: datetime | None = None
    doubles: bool = False


@dataclass(frozen=True)
class Mapping:
    match_id: str
    status: str                    # MATCHED | WEAK | AMBIGUOUS | UNMATCHED
    source: str = ""
    source_match_id: str = ""
    score: float = 0.0
    runner_up: float = 0.0
    reason: str = ""
    swapped: bool = False


def affinity(a, b) -> float:
    """Symmetric name affinity in [0, 1]; 0.0 means "provably not the same player".

    The project's matcher was built for "Federer R." against "Roger Federer", where a missing initial is
    genuine uncertainty and scores 0.7. Live-score feeds also give FULL names on both sides, and there a
    complete token match is not uncertainty at all -- it is the strongest evidence available. Without
    this, every ESPN binding would be reported WEAK and no match could ever reach confidence A or B.
    A bare surname still scores 0.7 and still maps WEAK, which is the case that must stay cautious.
    """
    na, nb = normalize_name(a), normalize_name(b)
    if not na or not nb:
        return 0.0
    ta, tb = set(name_tokens(a)), set(name_tokens(b))
    base = max(player_match_score(a, b), player_match_score(b, a))
    if base <= 0.0:
        return 0.0
    if ta and ta == tb:
        return 1.0
    # one side is a fuller spelling of the other ("Juan Pablo Varillas" vs "Juan P. Varillas"),
    # with at least two tokens in common so a lone surname cannot qualify
    if len(ta & tb) >= 2 and (ta <= tb or tb <= ta):
        return 0.95
    return base


def pair_score(src: SourceMatch, ours: OurMatch) -> tuple[float, bool]:
    direct = min(affinity(src.player_a, ours.player_a), affinity(src.player_b, ours.player_b))
    swap = min(affinity(src.player_a, ours.player_b), affinity(src.player_b, ours.player_a))
    return (direct, False) if direct >= swap else (swap, True)


def map_match(ours: OurMatch, feed: list[SourceMatch], *, window_hours: int = DEFAULT_WINDOW_HOURS) -> Mapping:
    scored = []
    for s in feed:
        if s.doubles != ours.doubles:
            continue
        if ours.scheduled_utc and s.scheduled_utc:
            if abs((s.scheduled_utc - ours.scheduled_utc).total_seconds()) > window_hours * 3600:
                continue
        sc, swapped = pair_score(s, ours)
        if sc >= MIN_AFFINITY:
            scored.append((sc, s, swapped))
    if not scored:
        return Mapping(ours.match_id, "UNMATCHED", reason="no candidate above the affinity floor")
    scored.sort(key=lambda x: -x[0])
    best_score, best, swapped = scored[0]
    rivals = [x for x in scored[1:] if x[1].source_match_id != best.source_match_id]
    runner = rivals[0][0] if rivals else 0.0
    if rivals and best_score - runner <= MIN_MARGIN:
        return Mapping(ours.match_id, "AMBIGUOUS", source=best.source, score=best_score, runner_up=runner,
                       reason=f"{1 + len(rivals)} feed matches tie at {best_score:.2f}")
    status = "MATCHED" if best_score >= STRONG_AFFINITY else "WEAK"
    return Mapping(ours.match_id, status, source=best.source, source_match_id=best.source_match_id,
                   score=best_score, runner_up=runner, swapped=swapped,
                   reason="" if status == "MATCHED" else "surname-only fit; no initial to verify")


def map_all(ours: list[OurMatch], feed: list[SourceMatch], **kw) -> tuple[dict[str, Mapping], dict]:
    out = {m.match_id: map_match(m, feed, **kw) for m in ours}
    counts: dict[str, int] = {}
    for m in out.values():
        counts[m.status] = counts.get(m.status, 0) + 1
    # a feed match claimed by two of our matches is also a collision: nobody gets it
    claims: dict[tuple, list[str]] = {}
    for mid, m in out.items():
        if m.status in ("MATCHED", "WEAK"):
            claims.setdefault((m.source, m.source_match_id), []).append(mid)
    for key, mids in claims.items():
        if len(mids) > 1:
            for mid in mids:
                out[mid] = Mapping(mid, "AMBIGUOUS", source=key[0], score=out[mid].score,
                                   reason=f"feed match {key[1]} claimed by {len(mids)} of our matches")
            for mid in mids:
                counts[out[mid].status] = counts.get(out[mid].status, 0)
            counts["MATCHED"] = max(0, counts.get("MATCHED", 0) - sum(1 for mid in mids))
            counts["AMBIGUOUS"] = counts.get("AMBIGUOUS", 0) + len(mids)
    return out, {"counts": counts, "feed_size": len(feed), "ours": len(ours)}
