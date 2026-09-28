"""Build a per-ticker timeline of EXECUTABLE quotes from the captured evidence.

Three streams carry a two-sided price, and they are kept distinguishable because they are not equally
good:

  market_record   the open-market snapshot written by every capture pass (yes/no bid and ask, sizes).
                  Timestamped when WE captured it.
  orderbook       the depth-10 book top for match-scope markets near their start. Best depth evidence.
  candle_bidask   Kalshi's own 1-minute bid/ask candles, timestamped by the EXCHANGE. These fill the
                  gaps between our capture passes and are the only way to get a close within a minute of
                  a first ball that happened between two passes.

Trade prints and settlement values are deliberately NOT quotes: a trade tells you someone dealt, not
that you could have. Nothing here interpolates, smooths or carries a price forward.
"""
from __future__ import annotations

import glob
import gzip
import json
import os
from datetime import datetime, timezone

from .close import Quote


def _f(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if 0.0 < v < 1.0 else None


def _ts(x):
    if isinstance(x, (int, float)):
        return datetime.fromtimestamp(x, tz=timezone.utc)
    if isinstance(x, str) and x:
        try:
            return datetime.fromisoformat(x.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


def _iter(root: str, kind: str):
    for f in sorted(glob.glob(os.path.join(root, "*", f"*.{kind}*.jsonl.gz")) +
                    glob.glob(os.path.join(root, "*", f"*.{kind}*.jsonl"))):
        opener = gzip.open if f.endswith(".gz") else open
        with opener(f, "rt") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        yield json.loads(line)
                    except ValueError:
                        continue                     # a truncated tail must never poison the timeline


def book_top(record: dict) -> tuple[float, float, float, float] | None:
    """(best YES bid, its size, best NO bid, its size) in DOLLARS from one captured order-book record.

    Kalshi has served two shapes, and the capture stores whichever it got, verbatim:

      legacy   {"orderbook": {"yes": [[cents, size], ...], "no": [[cents, size], ...]}}
      current  {"orderbook_fp": {"yes_dollars": [["0.2200", "9474.65"], ...], "no_dollars": [...]}}

    Every capture pass since 2026-09-11 is the CURRENT shape. Until 2026-09-27 this module read only the
    legacy keys, so every captured book was silently skipped: the close timeline had no order-book
    quotes and the size-verified coherence scan had no sizes. Both shapes are read now, the unit is
    carried by the key (cents vs dollars) rather than guessed from the magnitude, and a book with an
    empty side returns None -- a one-sided book is not an executable quote.
    """
    body = record.get("orderbook") if isinstance(record.get("orderbook"), dict) else record
    body = body or {}
    if isinstance(body.get("orderbook_fp"), dict):
        ob, yes_k, no_k, scale = body["orderbook_fp"], "yes_dollars", "no_dollars", 1.0
    elif isinstance(body.get("orderbook"), dict):
        ob, yes_k, no_k, scale = body["orderbook"], "yes", "no", 0.01
    elif "yes" in body or "no" in body:
        ob, yes_k, no_k, scale = body, "yes", "no", 0.01
    else:
        return None

    def best(levels):
        out = None
        for lv in levels or []:
            try:
                p, sz = float(lv[0]) * scale, float(lv[1])
            except (TypeError, ValueError, IndexError):
                continue
            if not (0.0 < p < 1.0) or sz <= 0:
                continue
            if out is None or p > out[0]:
                out = (p, sz)
        return out

    y, n = best(ob.get(yes_k)), best(ob.get(no_k))
    if y is None or n is None:
        return None
    return y[0], y[1], n[0], n[1]


def quotes_from_capture(capture_root: str, tickers: set[str] | None = None) -> dict[str, list[Quote]]:
    """ticker -> chronologically sorted executable quotes from every capture stream."""
    out: dict[str, list[Quote]] = {}

    def add(t, q):
        if tickers is not None and t not in tickers:
            return
        if q.executable:
            out.setdefault(t, []).append(q)

    for r in _iter(capture_root, "quotes"):
        t = r.get("ticker")
        ts = _ts(r.get("captured_at"))
        if not t or ts is None:
            continue
        add(t, Quote(ts, _f(r.get("yes_bid_dollars")), _f(r.get("yes_ask_dollars")),
                     yes_bid_size=r.get("yes_bid_size"), yes_ask_size=r.get("yes_ask_size"),
                     no_bid=_f(r.get("no_bid_dollars")), no_ask=_f(r.get("no_ask_dollars")),
                     source="market_record"))

    for r in _iter(capture_root, "books"):
        t, ts = r.get("ticker"), _ts(r.get("captured_at"))
        if not t or ts is None:
            continue
        top = book_top(r)
        if top is None:
            continue
        yb, yb_sz, nb, nb_sz = top
        # the book quotes each side's BID; the YES ask is 1 minus the best NO bid
        add(t, Quote(ts, yb, 1.0 - nb, yes_bid_size=yb_sz, yes_ask_size=nb_sz,
                     no_bid=nb, no_ask=1.0 - yb, source="orderbook"))

    for r in _iter(capture_root, "candles"):
        t = r.get("ticker")
        if not t:
            continue
        for c in (r.get("candles_60") or []):
            if not isinstance(c, dict):
                continue
            ts = _ts(c.get("end_period_ts"))
            yb = (c.get("yes_bid") or {}).get("close_dollars")
            ya = (c.get("yes_ask") or {}).get("close_dollars")
            if ts is None:
                continue
            add(t, Quote(ts, _f(yb), _f(ya), source="candle_bidask"))

    for t in out:
        out[t].sort(key=lambda q: q.ts)
    return out
