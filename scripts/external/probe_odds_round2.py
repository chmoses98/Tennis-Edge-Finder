#!/usr/bin/env python3
"""Wave 4 Phase 0, round two: how deep does Polymarket tennis actually go, and were Bovada and Smarkets
rejected on their merits or on my parameters?

Round one found Polymarket listing tennis at every level Kalshi lists -- and, on the first page of 100
events, only five of ninety matches with any accepting two-sided market, most of them quoting a
placeholder 47/53. Before concluding that a whole venue is untradeable, this pages through the entire
tennis tag and asks the CLOB order book directly, because the gamma summary's bestBid/bestAsk may be a
cached derivative rather than the live book.

Bovada returned an empty array and Smarkets a 400. Both are more likely my URL than their absence, so
each gets a small set of documented alternatives. robots.txt was already checked in round one and neither
host disallows these paths.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UA = "tennis-edge-finder/1.0 (research; +https://github.com/chmoses98/Tennis-Edge-Finder)"


def _req(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return {"status": 200}, r.read()
    except urllib.error.HTTPError as e:
        try:
            detail = e.read()[:400].decode("utf-8", "replace")
        except Exception:                                                       # noqa: BLE001
            detail = ""
        return {"status": e.code, "error": str(e)[:150], "body": detail}, b""
    except Exception as e:                                                      # noqa: BLE001
        return {"status": None, "error": f"{type(e).__name__}: {str(e)[:150]}"}, b""


def polymarket_full(root):
    """Every open tennis event, then the live CLOB book for each side that is accepting orders."""
    events, offset = [], 0
    while offset < 2000:
        meta, body = _req(f"https://gamma-api.polymarket.com/events?closed=false&limit=100"
                          f"&offset={offset}&tag_slug=tennis")
        if meta["status"] != 200 or not body:
            break
        page = json.loads(body)
        if not page:
            break
        events += page
        open(os.path.join(root, "raw", f"poly_events_{offset}.gz"), "wb").write(gzip.compress(body))
        offset += 100
        time.sleep(0.4)

    matches = [e for e in events if " vs " in (e.get("title") or "").lower()]
    accepting, books, sample = [], [], []
    for e in matches:
        for m in e.get("markets") or []:
            if not m.get("acceptingOrders"):
                continue
            accepting.append((e, m))
    for e, m in accepting[:120]:
        toks = m.get("clobTokenIds")
        try:
            toks = json.loads(toks) if isinstance(toks, str) else (toks or [])
        except Exception:                                                       # noqa: BLE001
            toks = []
        if not toks:
            continue
        meta, body = _req(f"https://clob.polymarket.com/book?token_id={toks[0]}")
        rec = {"event": e.get("title"), "question": m.get("question"),
               "end_date": e.get("endDate"), "gamma_bid": m.get("bestBid"),
               "gamma_ask": m.get("bestAsk"), "updated_at": m.get("updatedAt"),
               "clob_status": meta["status"]}
        if body:
            try:
                bk = json.loads(body)
                bids = bk.get("bids") or []
                asks = bk.get("asks") or []
                rec["clob_best_bid"] = max((float(x["price"]) for x in bids), default=None)
                rec["clob_best_ask"] = min((float(x["price"]) for x in asks), default=None)
                rec["clob_bid_depth"] = sum(float(x["size"]) for x in bids)
                rec["clob_ask_depth"] = sum(float(x["size"]) for x in asks)
                rec["clob_timestamp"] = bk.get("timestamp")
            except Exception as ex:                                             # noqa: BLE001
                rec["clob_parse_error"] = str(ex)[:120]
        books.append(rec)
        if len(sample) < 5 and body:
            sample.append(rec)
        time.sleep(0.25)

    two_sided = [b for b in books if b.get("clob_best_bid") and b.get("clob_best_ask")]
    real = [b for b in two_sided
            if (b["clob_best_ask"] - b["clob_best_bid"]) <= 0.10
            and min(b.get("clob_bid_depth") or 0, b.get("clob_ask_depth") or 0) >= 50]
    return {"events_open_tennis": len(events), "match_style_events": len(matches),
            "markets_accepting_orders": len(accepting), "clob_books_fetched": len(books),
            "books_two_sided": len(two_sided),
            "books_two_sided_within_10c_and_50_size": len(real),
            "examples": sample,
            "tradeable_examples": real[:8]}


ALTERNATES = {
    "bovada": [
        "https://www.bovada.lv/services/sports/event/coupon/events/A/description/tennis?lang=en",
        "https://www.bovada.lv/services/sports/event/v2/events/A/description/tennis?lang=en",
        "https://www.bovada.lv/services/sports/event/coupon/events/A/description/tennis/atp?lang=en",
    ],
    "smarkets": [
        "https://api.smarkets.com/v3/events/",
        "https://api.smarkets.com/v3/popular_events/",
        "https://api.smarkets.com/v3/events/?state=upcoming&type=sport&limit=20",
    ],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "sources", "external_odds_probe"))
    a = ap.parse_args()
    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-round2"
    root = os.path.join(a.out, run)
    os.makedirs(os.path.join(root, "raw"), exist_ok=True)

    out = {"generated_at": datetime.now(timezone.utc).isoformat(), "run_id": run}
    out["polymarket"] = polymarket_full(root)
    out["alternates"] = {}
    for name, urls in ALTERNATES.items():
        rows = []
        for u in urls:
            meta, body = _req(u)
            rec = {"url": u, **meta, "bytes": len(body)}
            if body:
                open(os.path.join(root, "raw", f"{name}_{len(rows)}.gz"), "wb").write(gzip.compress(body))
                txt = body.decode("utf-8", "replace")
                rec["mentions_tennis"] = "tennis" in txt.lower()
                rec["head"] = txt[:300]
            rows.append(rec)
            time.sleep(1.0)
        out["alternates"][name] = rows

    json.dump(out, open(os.path.join(root, "manifest.json"), "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str)[:7000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
