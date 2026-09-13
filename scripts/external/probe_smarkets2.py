#!/usr/bin/env python3
"""Wave 5 Phase 0, round two: from a round node to an executable price, and find a query that skips the walk.

Round one mapped the tree: Tennis (102016) -> 19 category nodes (ATP, WTA, Challenger, ITF Men, ITF
Women, WTA 125K, Davis Cup, ...) -> 2,626 tournament nodes -> round nodes ("Fixtures", "Round of 32",
"Qualification"). Every node so far is type `generic`; nothing is type `event`, which is why round one
found no matches to price.

Two questions here, and the second one decides whether unattended capture is even possible:

  1. what is under a round node, and does it carry a market with an order book;
  2. is there a query that returns today's tennis matches directly, so a capture job does not have to
     walk thousands of tournament nodes every ten minutes.

Bounded and spaced, as before, and any 401/403 stops that path.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UA = "tennis-edge-finder/1.0 (research; +https://github.com/chmoses98/Tennis-Edge-Finder)"
BASE = "https://api.smarkets.com"
PAUSE = 0.35
TENNIS = "102016"


class Walk:
    def __init__(self, root):
        self.root = root
        self.trace = []
        os.makedirs(os.path.join(root, "raw"), exist_ok=True)

    def get(self, path, note="", save_as=None):
        url = path if path.startswith("http") else BASE + path
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        rec = {"hop": len(self.trace) + 1, "url": url, "note": note}
        body = b""
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read()
                rec.update({"status": r.status, "bytes": len(body)})
        except urllib.error.HTTPError as e:
            try:
                rec["body"] = e.read()[:300].decode("utf-8", "replace")
            except Exception:                                                   # noqa: BLE001
                pass
            rec.update({"status": e.code, "error": str(e)[:120]})
            if e.code in (401, 403):
                rec["stopped"] = "authentication required; not public"
        except Exception as e:                                                  # noqa: BLE001
            rec.update({"status": None, "error": f"{type(e).__name__}: {str(e)[:120]}"})
        self.trace.append(rec)
        if body and save_as:
            open(os.path.join(self.root, "raw", f"{save_as}.gz"), "wb").write(gzip.compress(body))
        time.sleep(PAUSE)
        if not body:
            return rec, None
        try:
            return rec, json.loads(body.decode("utf-8", "replace"))
        except json.JSONDecodeError:
            return rec, None


def kids(w, pid, limit=100, save=None):
    rec, obj = w.get(f"/v3/events/?parent_id={pid}&limit={limit}", note=f"children of {pid}", save_as=save)
    return (obj or {}).get("events") or []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "sources", "smarkets_probe"))
    a = ap.parse_args()
    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-r2"
    root = os.path.join(a.out, run)
    w = Walk(root)
    res = {"generated_at": datetime.now(timezone.utc).isoformat(), "run_id": run}

    # ------------------------------------------------------- 1. can we query matches directly?
    today = datetime.now(timezone.utc).date()
    tomorrow = today + timedelta(days=1)
    direct = []
    for q, note in (
        (f"/v3/events/?type=tennis_match&state=upcoming&limit=50", "global query by a guessed leaf type"),
        (f"/v3/events/?parent_id={TENNIS}&type=tennis_match&limit=50", "leaf type under the tennis node"),
        (f"/v3/events/?type_domain=tennis&state=upcoming&limit=50", "type_domain, seen in some docs"),
        (f"/v3/events/?state=upcoming&start_datetime_max={tomorrow}T00:00:00Z&limit=50",
         "everything starting before tomorrow, any sport"),
        (f"/v3/events/?parent_id={TENNIS}&recursive=true&limit=50", "a recursive flag, if one exists"),
        (f"/v3/events/root/", "documented root listing"),
    ):
        rec, obj = w.get(q, note=note, save_as=None)
        evs = (obj or {}).get("events") or []
        direct.append({"query": q, "note": note, "status": rec.get("status"), "n_events": len(evs),
                       "types": dict(Counter(e.get("type") for e in evs)),
                       "error_body": rec.get("body", "")[:200],
                       "sample": [{k: e.get(k) for k in ("id", "name", "type", "start_datetime")}
                                  for e in evs[:4]]})
    res["direct_queries"] = direct

    # ------------------------------------------------------- 2. walk down to a leaf the slow way
    cats = kids(w, TENNIS, save="categories")
    res["categories"] = [{"id": c["id"], "name": c.get("name")} for c in cats]
    # prefer the categories most likely to be running right now
    order = ["ATP", "WTA", "Challenger", "ITF Men", "ITF Women", "WTA 125K"]
    cats.sort(key=lambda c: order.index(c.get("name")) if c.get("name") in order else 99)

    leaves, tournaments_seen, rounds_seen = [], 0, 0
    leaf_types = Counter()
    for cat in cats[:4]:
        tours = kids(w, cat["id"])
        # tournament nodes carry no dates, so take the highest ids: Smarkets allocates them in order,
        # which makes the newest tournaments the last ones created.
        tours.sort(key=lambda e: int(e["id"]))
        for tour in tours[-4:]:
            tournaments_seen += 1
            rounds = kids(w, tour["id"])
            for rnd in rounds[-4:]:
                rounds_seen += 1
                ch = kids(w, rnd["id"], save=f"leaf_{rnd['id']}" if not leaves else None)
                for e in ch:
                    leaf_types[e.get("type")] += 1
                    e["_path"] = f"{cat.get('name')} / {tour.get('name')} / {rnd.get('name')}"
                leaves += ch
                if len(leaves) >= 40:
                    break
            if len(leaves) >= 40:
                break
        if len(leaves) >= 40:
            break
    res["walk"] = {"tournaments_walked": tournaments_seen, "rounds_walked": rounds_seen,
                   "leaves": len(leaves), "leaf_types": dict(leaf_types),
                   "sample": [{k: e.get(k) for k in ("id", "name", "type", "state", "start_datetime",
                                                     "_path")} for e in leaves[:10]]}

    # ------------------------------------------------------- 3. leaf -> markets -> contracts -> quotes
    now = datetime.now(timezone.utc)
    def soon(e):
        try:
            d = datetime.fromisoformat(str(e.get("start_datetime")).replace("Z", "+00:00"))
        except (TypeError, ValueError):
            return False
        return timedelta(hours=-6) <= (d - now) <= timedelta(days=3)
    upcoming = [e for e in leaves if soon(e)] or leaves[:20]
    res["upcoming_leaves"] = {"n": len(upcoming),
                              "sample": [{k: e.get(k) for k in ("id", "name", "start_datetime", "state")}
                                         for e in upcoming[:8]]}
    ids = [str(e["id"]) for e in upcoming[:20]]
    markets = []
    if ids:
        rec, obj = w.get(f"/v3/events/{','.join(ids)}/markets/", note="markets for those leaves",
                         save_as="markets")
        markets = (obj or {}).get("markets") or []
    res["markets"] = {"n": len(markets), "keys": sorted(markets[0]) if markets else [],
                      "names": dict(Counter(m.get("name") for m in markets).most_common(12)),
                      "sample": [{k: m.get(k) for k in ("id", "event_id", "name", "state",
                                                        "bet_allowed", "settled")} for m in markets[:6]]}
    mids = [str(m["id"]) for m in markets[:20]]
    if mids:
        rec, obj = w.get(f"/v3/markets/{','.join(mids)}/contracts/", note="contracts", save_as="contracts")
        cons = (obj or {}).get("contracts") or []
        res["contracts"] = {"n": len(cons), "keys": sorted(cons[0]) if cons else [],
                            "sample": [{k: c.get(k) for k in ("id", "market_id", "name", "slug")}
                                       for c in cons[:6]]}
        rec, q = w.get(f"/v3/markets/{','.join(mids)}/quotes/", note="THE ORDER BOOK", save_as="quotes")
        res["quotes_raw_keys"] = sorted(q)[:6] if isinstance(q, dict) else None
        if isinstance(q, dict):
            books, twosided, depth = 0, 0, []
            sample = None
            for cid, side in q.items():
                if not isinstance(side, dict):
                    continue
                books += 1
                bids = side.get("bids") or []
                offers = side.get("offers") or []
                if bids and offers:
                    twosided += 1
                    depth.append((sum(float(b.get("quantity", 0)) for b in bids),
                                  sum(float(o.get("quantity", 0)) for o in offers)))
                if sample is None and (bids or offers):
                    sample = {cid: side}
            res["quotes"] = {"contracts_with_a_book": books, "two_sided": twosided,
                             "median_depth": sorted(depth)[len(depth) // 2] if depth else None,
                             "sample": sample}
        rec, lep = w.get(f"/v3/markets/{','.join(mids)}/last_executed_prices/", note="last traded",
                         save_as="last_executed")
        res["last_executed"] = {"present": bool(lep), "sample": dict(list((lep or {}).items())[:2])}

    res["trace"] = w.trace
    json.dump(res, open(os.path.join(root, "manifest.json"), "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in res.items() if k != "trace"}, indent=1, default=str)[:11000])
    print("\n--- non-200 hops ---")
    for t in w.trace:
        if t.get("status") != 200:
            print(f"  {t.get('status')} {t['url'][:100]} {t.get('body', t.get('error', ''))[:120]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
