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
        ob = ((r.get("orderbook") or {}).get("orderbook") or r.get("orderbook") or {})
        if not t or ts is None or not isinstance(ob, dict):
            continue
        yes, no = ob.get("yes") or [], ob.get("no") or []
        def top(levels):
            best = None
            for lv in levels:
                try:
                    p, sz = float(lv[0]), float(lv[1])
                except (TypeError, ValueError, IndexError):
                    continue
                if best is None or p > best[0]:
                    best = (p, sz)
            return best
        ty, tn = top(yes), top(no)
        if ty and tn:
            # Kalshi books quote each side's BID in cents; the YES ask is 100 minus the NO bid.
            add(t, Quote(ts, ty[0] / 100.0, 1.0 - tn[0] / 100.0, yes_bid_size=ty[1], yes_ask_size=tn[1],
                         no_bid=tn[0] / 100.0, no_ask=1.0 - ty[0] / 100.0, source="orderbook"))

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
