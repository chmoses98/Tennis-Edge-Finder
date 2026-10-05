"""Which physical matches has the first-ball store already seen start?

Used by every PREGAME producer to refuse a price on a match that is under way. A nominal start hours in
the future is not evidence the match has not started: Challenger and ITF occurrence times are routinely
hours late (TENNIS-6 found 330 ledger rows priced in play that way before this guard existed).
"""
from __future__ import annotations

import os


def match_code(event_ticker: str) -> str:
    """The date+players code a physical match shares across every series it is listed under
    (KXATPMATCH-26SEP11ZVEKHA, KXATPSETWINNER-26SEP11ZVEKHA-2 -> 26SEP11ZVEKHA)."""
    parts = (event_ticker or "").split("-")
    return parts[1] if len(parts) > 1 else event_ticker


def matches_already_started(store_root: str, now) -> set[str]:
    """Match codes the store has seen START before `now`: an actual first ball, or an UPPER bound (the first
    ball happened at or before it), at or before `now`.

    Any confidence counts here, including C: this set is only ever used to REFUSE a pregame price, and a
    refusal on an indirect bound is the conservative direction. A no-play truth never counts as started.

    A LOWER bound alone is not evidence of a start -- it says the match had NOT started when last seen. Until
    2026-10-05 it was read as one, so every match the first-ball conductor had polled while still "Scheduled"
    was refused as under way: 552 of the 2026-10-05 tour board's open markets (matches on 6-7 October)."""
    if not os.path.isdir(store_root):
        return set()
    from tennis_edge.firstball.store import FirstBallStore
    out = set()
    for mid, t in FirstBallStore(store_root).latest_truths().items():
        if t.no_play:
            continue
        bound = t.actual_first_ball_at_utc or t.upper_bound_utc
        if bound is not None and bound <= now:
            out.add(match_code(mid))
    return out
