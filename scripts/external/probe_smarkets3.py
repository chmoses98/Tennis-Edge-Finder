#!/usr/bin/env python3
"""Wave 5 Phase 1/2/7: the decisive Smarkets measurement.

Round two found the shortcut. Matches are not reachable by walking the tennis tree in any practical way
-- 2,626 tournament nodes, none dated -- but a single global query returns them directly:

    GET /v3/events/?type=tennis_match&state=upcoming&limit=N

So the traversal a capture job would actually use is:

    events(type=tennis_match, state=upcoming)   the board
      -> /v3/events/{ids}/markets/              what is priced on each match
      -> /v3/markets/{ids}/contracts/           the two sides
      -> /v3/markets/{ids}/quotes/              THE ORDER BOOK
      -> /v3/markets/{ids}/last_executed_prices/  what actually traded

This probe runs that path over the whole upcoming board and answers the three questions that decide the
wave: how much tennis is there, how much of it has a genuine two-sided book with size behind it, and how
fresh the prices are. It measures; it does not integrate.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import statistics as st
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UA = "tennis-edge-finder/1.0 (research; +https://github.com/chmoses98/Tennis-Edge-Finder)"
BASE = "https://api.smarkets.com"
PAUSE = 0.3


class Api:
    def __init__(self, root):
        self.root = root
        self.trace = []
        os.makedirs(os.path.join(root, "raw"), exist_ok=True)

    def get(self, path, note="", save_as=None):
        url = path if path.startswith("http") else BASE + path
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        rec = {"hop": len(self.trace) + 1, "url": url[:180], "note": note}
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
                rec["stopped"] = "authentication required; path not public"
        except Exception as e:                                                  # noqa: BLE001
            rec.update({"status": None, "error": f"{type(e).__name__}: {str(e)[:120]}"})
        self.trace.append(rec)
        if body and save_as:
            open(os.path.join(self.root, "raw", f"{save_as}.gz"), "wb").write(gzip.compress(body))
        time.sleep(PAUSE)
        if not body:
            return None
        try:
            return json.loads(body.decode("utf-8", "replace"))
        except json.JSONDecodeError:
            return None

    def batched(self, ids, template, note, key, save_prefix=None, chunk=20):
        out = []
        for i in range(0, len(ids), chunk):
            part = ",".join(ids[i:i + chunk])
            obj = self.get(template.format(ids=part), note=note,
                           save_as=f"{save_prefix}_{i}" if (save_prefix and i == 0) else None)
            if obj:
                got = obj.get(key)
                if isinstance(got, list):
                    out += got
                elif isinstance(got, dict):
                    out.append(got)
                elif key == "__raw__":
                    out.append(obj)
        return out


def price_to_prob(x):
    """Smarkets quotes prices in hundredths of a percent: 5000 -> 50.00%."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v / 10000.0 if v > 1.5 else v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "sources", "smarkets_probe"))
    ap.add_argument("--max-events", type=int, default=300)
    ap.add_argument("--quote-events", type=int, default=120, help="how many matches to price")
    a = ap.parse_args()
    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-r3"
    root = os.path.join(a.out, run)
    api = Api(root)
    now = datetime.now(timezone.utc)
    res = {"generated_at": now.isoformat(), "run_id": run,
           "traversal": ["GET /v3/events/?type=tennis_match&state=upcoming&limit=N (+pagination)",
                         "GET /v3/events/{ids}/markets/", "GET /v3/markets/{ids}/contracts/",
                         "GET /v3/markets/{ids}/quotes/",
                         "GET /v3/markets/{ids}/last_executed_prices/",
                         "GET /v3/events/{parent_ids}/ to name the competition"]}

    # ------------------------------------------------------------------ 1. the board
    events, cursor = [], None
    for page in range(12):
        q = "/v3/events/?type=tennis_match&state=upcoming&limit=100"
        if cursor:
            q += f"&pagination_last_id={cursor}"
        obj = api.get(q, note="the upcoming tennis board", save_as=f"events_{page}" if page < 2 else None)
        if not obj:
            break
        evs = obj.get("events") or []
        events += evs
        nxt = (obj.get("pagination") or {}).get("next_page")
        if not evs or not nxt or len(events) >= a.max_events:
            break
        cursor = (urllib.parse.parse_qs(nxt.lstrip("?")).get("pagination_last_id") or [None])[0]
        if not cursor:
            break

    def when(e):
        try:
            return datetime.fromisoformat(str(e.get("start_datetime")).replace("Z", "+00:00"))
        except (TypeError, ValueError):
            return None
    horizons = Counter()
    for e in events:
        d = when(e)
        if d is None:
            horizons["no_start_time"] += 1
        elif d < now:
            horizons["already_started"] += 1
        elif d - now <= timedelta(hours=24):
            horizons["within_24h"] += 1
        elif d - now <= timedelta(days=7):
            horizons["within_7d"] += 1
        else:
            horizons["beyond_7d"] += 1
    res["board"] = {"events": len(events), "horizons": dict(horizons),
                    "keys": sorted(events[0]) if events else [],
                    "sample": [{k: e.get(k) for k in ("id", "name", "start_datetime", "state",
                                                      "bettable", "bet_allowed", "parent_id")}
                               for e in events[:6]]}

    # ------------------------------------------------------------------ 2. what level is each match
    parents = sorted({str(e.get("parent_id")) for e in events if e.get("parent_id")})
    pnodes = {p["id"]: p for p in api.batched(parents[:200], "/v3/events/{ids}/", "name the round node",
                                              "events", save_prefix="parents")}
    grandparents = sorted({str(p.get("parent_id")) for p in pnodes.values() if p.get("parent_id")})
    gnodes = {p["id"]: p for p in api.batched(grandparents[:200], "/v3/events/{ids}/",
                                              "name the tournament", "events")}
    ggparents = sorted({str(p.get("parent_id")) for p in gnodes.values() if p.get("parent_id")})
    ggnodes = {p["id"]: p for p in api.batched(ggparents[:60], "/v3/events/{ids}/", "name the category",
                                               "events")}

    def category_of(e):
        p = pnodes.get(str(e.get("parent_id")))
        g = gnodes.get(str((p or {}).get("parent_id")))
        gg = ggnodes.get(str((g or {}).get("parent_id")))
        return (gg or {}).get("name") or (g or {}).get("name") or "?"

    def tournament_of(e):
        p = pnodes.get(str(e.get("parent_id")))
        return (gnodes.get(str((p or {}).get("parent_id"))) or {}).get("name") or "?"

    res["coverage_by_category"] = dict(Counter(category_of(e) for e in events).most_common(20))
    res["doubles_matches"] = sum(1 for e in events if "/" in (e.get("name") or ""))
    res["sample_tournaments"] = sorted({tournament_of(e) for e in events})[:15]

    # ------------------------------------------------------------------ 3. markets per match
    soon = [e for e in events if (when(e) or now) - now <= timedelta(days=3)]
    soon.sort(key=lambda e: when(e) or now)
    target = soon[:a.quote_events] or events[:a.quote_events]
    ids = [str(e["id"]) for e in target]
    markets = api.batched(ids, "/v3/events/{ids}/markets/", "markets per match", "markets",
                          save_prefix="markets")
    res["markets"] = {"n": len(markets), "for_events": len(ids),
                      "keys": sorted(markets[0]) if markets else [],
                      "families": dict(Counter(m.get("name") for m in markets).most_common(15)),
                      "states": dict(Counter(m.get("state") for m in markets)),
                      "sample": [{k: m.get(k) for k in ("id", "event_id", "name", "state", "settled",
                                                        "bet_allowed")} for m in markets[:5]]}

    winner = [m for m in markets if "winner" in (m.get("name") or "").lower()] or markets
    mids = [str(m["id"]) for m in winner[:120]]
    contracts = api.batched(mids, "/v3/markets/{ids}/contracts/", "the two sides", "contracts",
                            save_prefix="contracts")
    res["contracts"] = {"n": len(contracts), "keys": sorted(contracts[0]) if contracts else [],
                        "sample": [{k: c.get(k) for k in ("id", "market_id", "name", "slug")}
                                   for c in contracts[:6]]}

    # ------------------------------------------------------------------ 4. THE ORDER BOOK
    books = {}
    for i in range(0, len(mids), 20):
        obj = api.get("/v3/markets/{}/quotes/".format(",".join(mids[i:i + 20])),
                      note="order book", save_as=f"quotes_{i}" if i == 0 else None)
        if isinstance(obj, dict):
            books.update(obj)
    two_sided, one_sided, empty = 0, 0, 0
    spreads, depths, samples = [], [], []
    for cid, side in books.items():
        if not isinstance(side, dict):
            continue
        bids = side.get("bids") or []
        offers = side.get("offers") or []
        if bids and offers:
            two_sided += 1
            bb = max(price_to_prob(b.get("price")) or 0 for b in bids)
            ba = min(price_to_prob(o.get("price")) or 1 for o in offers)
            spreads.append(ba - bb)
            depths.append(min(sum(float(b.get("quantity", 0)) for b in bids),
                              sum(float(o.get("quantity", 0)) for o in offers)))
            if len(samples) < 4:
                samples.append({"contract": cid, "best_bid": bb, "best_ask": ba,
                                "bid_levels": len(bids), "ask_levels": len(offers),
                                "raw_first_bid": bids[0], "raw_first_offer": offers[0]})
        elif bids or offers:
            one_sided += 1
        else:
            empty += 1
    res["order_books"] = {
        "contracts_returned": len(books), "two_sided": two_sided, "one_sided": one_sided,
        "empty": empty,
        "two_sided_share": round(two_sided / len(books), 4) if books else None,
        "median_spread": round(st.median(spreads), 4) if spreads else None,
        "p25_spread": round(sorted(spreads)[len(spreads) // 4], 4) if spreads else None,
        "median_min_depth": round(st.median(depths), 1) if depths else None,
        "depth_over_100": sum(1 for d in depths if d >= 100),
        "samples": samples}

    lep = {}
    for i in range(0, len(mids), 20):
        obj = api.get("/v3/markets/{}/last_executed_prices/".format(",".join(mids[i:i + 20])),
                      note="what actually traded", save_as=f"lep_{i}" if i == 0 else None)
        if isinstance(obj, dict):
            lep.update(obj)
    res["last_executed"] = {"entries": len(lep), "sample": dict(list(lep.items())[:3])}

    # ------------------------------------------------------------------ 5. freshness
    mstate = api.batched(mids[:60], "/v3/markets/{ids}/", "market records, for timestamps", "markets",
                         save_prefix="market_records")
    ts_fields = Counter()
    for m in mstate:
        for k, v in m.items():
            if isinstance(v, str) and len(v) >= 19 and v[4] == "-" and v[10] in ("T", " "):
                ts_fields[k] += 1
    res["freshness"] = {"market_record_keys": sorted(mstate[0]) if mstate else [],
                        "timestamp_fields": dict(ts_fields),
                        "sample": {k: mstate[0].get(k) for k in
                                   ("id", "name", "state", "created", "modified", "settled",
                                    "bet_allowed", "market_type")} if mstate else {}}
    res["requests_made"] = len(api.trace)
    res["non_200"] = [t for t in api.trace if t.get("status") != 200][:10]
    res["trace_tail"] = api.trace[-5:]
    json.dump(res, open(os.path.join(root, "manifest.json"), "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in res.items() if k not in ("trace_tail",)}, indent=1,
                     default=str)[:12000])
    return 0


def _guarded():
    import traceback
    try:
        return main()
    except Exception:                                                           # noqa: BLE001
        run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-r3-crash"
        root = os.path.join(PROJ, "data", "sources", "smarkets_probe", run)
        os.makedirs(root, exist_ok=True)
        json.dump({"generated_at": datetime.now(timezone.utc).isoformat(), "crashed": True,
                   "traceback": traceback.format_exc()[-4000:]},
                  open(os.path.join(root, "manifest.json"), "w"), indent=1)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(_guarded())
