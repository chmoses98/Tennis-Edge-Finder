"""Read-only access to the Kalshi capture and the first-ball store for the assisted lane.

Everything here READS evidence other jobs wrote. The capture conductor writes only markets that CHANGED
in a pass, so "the board at time t" is the carry-forward accumulation of every record captured up to t.
"""
from __future__ import annotations

import glob
import gzip
import json
import os
from datetime import datetime, timedelta, timezone

from tennis_edge.ledger.close import Quote
from tennis_edge.ledger.quotes import book_top

from .schema import match_code_of


def iso(x) -> datetime | None:
    if isinstance(x, datetime):
        return x if x.tzinfo else x.replace(tzinfo=timezone.utc)
    if isinstance(x, str) and x:
        try:
            d = datetime.fromisoformat(x.replace("Z", "+00:00"))
        except ValueError:
            return None
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    return None


def fnum(x, *, open_unit: bool = False):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    if open_unit and not (0.0 < v < 1.0):
        return None
    return v


def capture_days(capture_root: str) -> list[str]:
    return sorted(os.path.basename(d) for d in glob.glob(os.path.join(capture_root, "*")) if os.path.isdir(d))


def _iter_stream(capture_root: str, days, stream: str):
    for day in days:
        for f in sorted(glob.glob(os.path.join(capture_root, day, f"*.{stream}.jsonl.gz"))):
            try:
                with gzip.open(f, "rt") as fh:
                    for line in fh:
                        if line.strip():
                            try:
                                yield json.loads(line)
                            except ValueError:
                                continue
            except (OSError, EOFError):
                continue                               # a truncated capture file never poisons the read


def board(capture_root: str, *, at: datetime | None = None, days: list[str] | None = None) -> dict[str, dict]:
    """ticker -> latest captured market record at or before `at` (carry-forward over the given days;
    default: the latest capture day)."""
    if days is None:
        all_days = capture_days(capture_root)
        days = all_days[-1:] if at is None else [d for d in all_days
                                                  if d <= at.strftime("%Y-%m-%d")][-2:]
    out: dict[str, dict] = {}
    cutoff = at.isoformat() if at else None
    for r in _iter_stream(capture_root, days, "quotes"):
        t = r.get("ticker")
        if not t:
            continue
        ca = r.get("captured_at") or ""
        if cutoff and iso(ca) and iso(ca) > at:
            continue
        prev = out.get(t)
        if prev is None or (prev.get("captured_at") or "") <= ca:
            out[t] = r
    return out


def quote_record_at(capture_root: str, ticker: str, at: datetime) -> dict | None:
    """The latest capture record of one ticker at or before `at` (same and previous UTC day)."""
    days = [(at - timedelta(days=1)).strftime("%Y-%m-%d"), at.strftime("%Y-%m-%d")]
    best = None
    for r in _iter_stream(capture_root, days, "quotes"):
        if r.get("ticker") != ticker:
            continue
        ts = iso(r.get("captured_at"))
        if ts is None or ts > at:
            continue
        if best is None or ts >= iso(best["captured_at"]):
            best = r
    return best


def quote_timelines(capture_root: str, tickers: set[str], days: list[str]) -> dict[str, list[Quote]]:
    """ticker -> chronologically sorted EXECUTABLE quotes (market records and order-book tops) over `days`.
    Same construction as tennis_edge.ledger.quotes.quotes_from_capture, restricted to the days a decision
    can need so a settle pass never rescans the whole capture history."""
    out: dict[str, list[Quote]] = {}
    for r in _iter_stream(capture_root, days, "quotes"):
        t, ts = r.get("ticker"), iso(r.get("captured_at"))
        if t not in tickers or ts is None:
            continue
        q = Quote(ts, fnum(r.get("yes_bid_dollars"), open_unit=True), fnum(r.get("yes_ask_dollars"), open_unit=True),
                  yes_bid_size=fnum(r.get("yes_bid_size_fp")), yes_ask_size=fnum(r.get("yes_ask_size_fp")),
                  source="market_record")
        if q.executable:
            out.setdefault(t, []).append(q)
    for r in _iter_stream(capture_root, days, "books"):
        t, ts = r.get("ticker"), iso(r.get("captured_at"))
        if t not in tickers or ts is None:
            continue
        top = book_top(r)
        if top is None:
            continue
        yb, yb_sz, nb, nb_sz = top
        q = Quote(ts, yb, 1.0 - nb, yes_bid_size=yb_sz, yes_ask_size=nb_sz, no_bid=nb, no_ask=1.0 - yb,
                  source="orderbook")
        if q.executable:
            out.setdefault(t, []).append(q)
    for t in out:
        out[t].sort(key=lambda q: q.ts)
    return out


def settlements(capture_root: str, tickers: set[str] | None = None) -> dict[str, dict]:
    """ticker -> the exchange's own settlement record (capture `status=settled` sweep). Nothing inferred."""
    out: dict[str, dict] = {}
    for day in capture_days(capture_root):
        for r in _iter_stream(capture_root, [day], "settlements"):
            t = r.get("ticker")
            if not t or (tickers is not None and t not in tickers):
                continue
            if (r.get("result") or "") not in ("yes", "no", "scalar") or r.get("settlement_value_dollars") in (None, ""):
                continue
            out.setdefault(t, r)
    return out


# ---------------------------------------------------------------------------------------------- first ball
def load_truths(store_root: str) -> dict:
    if not os.path.isdir(os.path.join(store_root, "truths")):
        return {}
    from tennis_edge.firstball.store import FirstBallStore
    return FirstBallStore(store_root).latest_truths()


def truth_for(truths: dict, ticker_or_event: str):
    """The first-ball truth of the physical match a ticker belongs to. Truths are keyed by match-winner
    event ticker; every series of one match shares its date+players code. When several truths share the
    code (the same match listed under several events), a truth that OBSERVED PLAY wins, the one with the
    earliest possible first ball first: that is the conservative reading for "did this decision precede the
    first ball?". Only when none observed play is a pregame-only truth returned (it bounds nothing)."""
    code = match_code_of(ticker_or_event)
    if not code:
        return None
    played, other = None, None
    for mid, t in truths.items():
        if match_code_of(mid) != code or t.no_play:
            continue
        b = first_ball_bound(t)
        if b is not None:
            if played is None or b < first_ball_bound(played):
                played = t
            continue
        lb = t.lower_bound_utc
        if lb is not None and (other is None or lb < other.lower_bound_utc):
            other = t
    return played or other


def first_ball_bound(truth) -> datetime | None:
    """Earliest instant the match may have started, from a truth that OBSERVED PLAY (refusal direction).

    Only a truth with an upper bound (play seen, at any confidence) bounds the first ball. A pregame-only
    truth -- a lower bound and no upper bound -- says the match had NOT started by that instant; reading it
    as "may have started" (as this function did until 2026-10-02) hid every pregame match ESPN was
    watching from the assisted slate and refused every decision on it. Whether such a match is still
    pregame NOW is answered by tennis_edge.firstball.start_times, which needs a recent live reading."""
    if truth is None or truth.upper_bound_utc is None:
        return None
    return truth.lower_bound_utc or truth.upper_bound_utc
