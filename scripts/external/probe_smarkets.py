#!/usr/bin/env python3
"""Wave 5 Phase 0: reverse the Smarkets data path, from the public surface to an executable tennis price.

Wave 4 got as far as `GET /v3/events/`, which returns a paginated event tree in which Tennis is a
top-level node. It did not reach a price. This walks the rest of the way and writes down every hop, so
the traversal is a documented fact rather than a guess.

Discipline, because this is someone else's service:

* robots.txt for every host, fetched first;
* no undocumented identifier is invented -- every id used here came out of a previous response;
* fan-out is bounded and every request is spaced, so one run is a few hundred requests, not a scrape;
* if a path demands authentication the walk STOPS there and records it. Nothing is bypassed.

The output is a trace: each hop's URL, status, shape and a sample, plus the raw bytes for anything
interesting. One run should be enough to say whether an executable tennis price exists at the end of it.
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
from datetime import datetime, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UA = "tennis-edge-finder/1.0 (research; +https://github.com/chmoses98/Tennis-Edge-Finder)"
BASE = "https://api.smarkets.com"
PAUSE = 0.35


class Walk:
    def __init__(self, root):
        self.root = root
        self.trace = []
        self.n = 0
        os.makedirs(os.path.join(root, "raw"), exist_ok=True)

    def get(self, path: str, note: str = "", save_as: str | None = None):
        url = path if path.startswith("http") else BASE + path
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        t0 = time.time()
        rec = {"hop": len(self.trace) + 1, "url": url, "note": note}
        body = b""
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read()
                rec.update({"status": r.status, "bytes": len(body),
                            "content_type": r.headers.get("content-type", ""),
                            "rate_limit": {k: v for k, v in r.headers.items()
                                           if "ratelimit" in k.lower() or "retry" in k.lower()}})
        except urllib.error.HTTPError as e:
            detail = b""
            try:
                detail = e.read()[:500]
            except Exception:                                                   # noqa: BLE001
                pass
            rec.update({"status": e.code, "error": str(e)[:160],
                        "body": detail.decode("utf-8", "replace")})
            if e.code in (401, 403):
                rec["stopped"] = "authentication or authorisation required; this path is not public"
        except Exception as e:                                                  # noqa: BLE001
            rec.update({"status": None, "error": f"{type(e).__name__}: {str(e)[:160]}"})
        rec["ms"] = int((time.time() - t0) * 1000)
        self.trace.append(rec)
        self.n += 1
        if body and save_as:
            open(os.path.join(self.root, "raw", f"{save_as}.gz"), "wb").write(gzip.compress(body))
        time.sleep(PAUSE)
        if not body:
            return rec, None
        try:
            return rec, json.loads(body.decode("utf-8", "replace"))
        except json.JSONDecodeError:
            rec["not_json"] = True
            return rec, None


def robots(w: Walk, host: str) -> dict:
    rec, _ = w.get(f"{host}/robots.txt", note="robots.txt, fetched before anything else")
    txt = ""
    p = os.path.join(w.root, "raw", f"robots_{urllib.parse.urlparse(host).netloc}.txt")
    try:
        req = urllib.request.Request(f"{host}/robots.txt", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r:
            txt = r.read().decode("utf-8", "replace")[:4000]
        open(p, "w").write(txt)
    except Exception:                                                           # noqa: BLE001
        pass
    rules, star = [], False
    for line in txt.splitlines():
        s = line.split("#", 1)[0].strip()
        k, _, v = s.partition(":")
        k, v = k.strip().lower(), v.strip()
        if k == "user-agent":
            star = (v == "*")
        elif k == "disallow" and star and v:
            rules.append(v)
    return {"host": host, "status": rec.get("status"), "disallow_for_star": rules[:20],
            "blocks_api_root": any(r == "/" for r in rules)}


def children(w: Walk, parent_id, limit=100, save=None):
    out, cursor = [], None
    for page in range(6):
        q = f"/v3/events/?parent_id={parent_id}&limit={limit}"
        if cursor:
            q += f"&pagination_last_id={cursor}"
        rec, obj = w.get(q, note=f"children of {parent_id}", save_as=save if page == 0 else None)
        if not obj:
            break
        evs = obj.get("events") or []
        out += evs
        nxt = (obj.get("pagination") or {}).get("next_page")
        if not nxt or not evs:
            break
        qs = urllib.parse.parse_qs(nxt.lstrip("?"))
        cursor = (qs.get("pagination_last_id") or [None])[0]
        if not cursor:
            break
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "sources", "smarkets_probe"))
    ap.add_argument("--tennis-id", default="102016", help="the Tennis top-level event id from Wave 4")
    ap.add_argument("--max-events", type=int, default=40)
    a = ap.parse_args()
    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    root = os.path.join(a.out, run)
    w = Walk(root)
    res = {"generated_at": datetime.now(timezone.utc).isoformat(), "run_id": run, "base": BASE}

    # ---------------------------------------------------------------- 0. permission
    res["robots"] = [robots(w, "https://api.smarkets.com"), robots(w, "https://smarkets.com")]
    if any(r["blocks_api_root"] for r in res["robots"]):
        res["stopped"] = "robots.txt disallows the API root for a generic agent"
        json.dump(res, open(os.path.join(root, "manifest.json"), "w"), indent=1, default=str)
        print(json.dumps(res, indent=1, default=str)); return 0

    # ---------------------------------------------------------------- 1. confirm the tennis node
    rec, obj = w.get(f"/v3/events/{a.tennis_id}/", note="the Tennis top-level node itself",
                     save_as="tennis_node")
    res["tennis_node"] = (obj or {}).get("events", [{}])[0] if obj else {"error": rec.get("error")}

    # ---------------------------------------------------------------- 2. sport -> groups -> events
    lvl1 = children(w, a.tennis_id, save="tennis_children")
    res["level1"] = {"n": len(lvl1), "types": dict(Counter(e.get("type") for e in lvl1)),
                     "sample": [{k: e.get(k) for k in ("id", "name", "type", "state", "start_datetime")}
                                for e in lvl1[:8]]}
    # a competition node is anything with children; an event is anything with a start time and no children
    lvl2, parents_walked = [], 0
    for e in lvl1:
        if parents_walked >= 12:
            break
        if e.get("type") in ("event",):
            continue
        kids = children(w, e["id"], save=None)
        parents_walked += 1
        for k in kids:
            k["_parent_name"] = e.get("name")
        lvl2 += kids
    res["level2"] = {"n": len(lvl2), "parents_walked": parents_walked,
                     "types": dict(Counter(e.get("type") for e in lvl2)),
                     "sample": [{k: e.get(k) for k in ("id", "name", "type", "state", "start_datetime",
                                                       "_parent_name")} for e in lvl2[:10]]}
    lvl3 = []
    for e in lvl2[:12]:
        if e.get("type") == "event":
            continue
        kids = children(w, e["id"])
        for k in kids:
            k["_parent_name"] = e.get("name")
        lvl3 += kids
    res["level3"] = {"n": len(lvl3), "types": dict(Counter(e.get("type") for e in lvl3)),
                     "sample": [{k: e.get(k) for k in ("id", "name", "type", "state", "start_datetime",
                                                       "_parent_name")} for e in lvl3[:10]]}

    pool = [e for e in (lvl3 + lvl2 + lvl1) if e.get("type") == "event"]
    if not pool:
        pool = [e for e in (lvl3 + lvl2) if e.get("start_datetime") and " vs " in (e.get("name") or "").lower()]
    seen, events = set(), []
    for e in pool:
        if e["id"] in seen:
            continue
        seen.add(e["id"])
        events.append(e)
    res["candidate_events"] = {"n": len(events),
                               "sample": [{k: e.get(k) for k in ("id", "name", "state",
                                                                 "start_datetime", "_parent_name")}
                                          for e in events[:12]]}

    # ---------------------------------------------------------------- 3. event -> markets
    ids = [str(e["id"]) for e in events[:a.max_events]]
    markets = []
    for i in range(0, len(ids), 20):
        chunk = ",".join(ids[i:i + 20])
        rec, obj = w.get(f"/v3/events/{chunk}/markets/", note="markets for a batch of events",
                         save_as=f"markets_{i}" if i == 0 else None)
        if obj:
            markets += obj.get("markets") or []
    res["markets"] = {"n": len(markets),
                      "name_sample": [m.get("name") for m in markets[:15]],
                      "keys": sorted(markets[0]) if markets else [],
                      "by_event": dict(Counter(str(m.get("event_id")) for m in markets).most_common(5))}

    # ---------------------------------------------------------------- 4. market -> contracts, quotes
    mids = [str(m["id"]) for m in markets[:40]]
    contracts = []
    for i in range(0, len(mids), 20):
        chunk = ",".join(mids[i:i + 20])
        rec, obj = w.get(f"/v3/markets/{chunk}/contracts/", note="contracts for a batch of markets",
                         save_as=f"contracts_{i}" if i == 0 else None)
        if obj:
            contracts += obj.get("contracts") or []
    res["contracts"] = {"n": len(contracts), "keys": sorted(contracts[0]) if contracts else [],
                        "sample": [{k: c.get(k) for k in ("id", "market_id", "name", "slug")}
                                   for c in contracts[:8]]}

    quotes_obj = {}
    for i in range(0, len(mids), 20):
        chunk = ",".join(mids[i:i + 20])
        rec, obj = w.get(f"/v3/markets/{chunk}/quotes/", note="THE ORDER BOOK",
                         save_as=f"quotes_{i}" if i == 0 else None)
        if obj:
            quotes_obj.update(obj if isinstance(obj, dict) else {})
    res["quotes"] = {"top_level_keys": sorted(quotes_obj)[:8], "n_entries": len(quotes_obj)}
    if quotes_obj:
        k0 = sorted(quotes_obj)[0]
        res["quotes"]["sample_entry"] = {k0: quotes_obj[k0]}

    rec, lep = w.get(f"/v3/markets/{','.join(mids[:20])}/last_executed_prices/",
                     note="last traded price", save_as="last_executed")
    res["last_executed_prices"] = {"present": bool(lep),
                                   "sample": dict(list((lep or {}).items())[:2])}

    res["trace"] = w.trace
    res["requests_made"] = w.n
    json.dump(res, open(os.path.join(root, "manifest.json"), "w"), indent=1, default=str)
    slim = {k: v for k, v in res.items() if k != "trace"}
    print(json.dumps(slim, indent=1, default=str)[:12000])
    print("\n--- trace ---")
    for t in w.trace:
        print(f"  {t['hop']:3d} {t.get('status')} {t.get('bytes', 0):8} {t['url'][:110]}"
              + (f"  !! {t.get('stopped') or t.get('error', '')[:60]}" if t.get("status") != 200 else ""))
    return 0


def _guarded():
    """Write a manifest even when the walk dies, so a failure is evidence rather than an absence."""
    import traceback
    try:
        return main()
    except Exception:                                                           # noqa: BLE001
        import glob as _g
        run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-crash"
        root = os.path.join(PROJ, "data", "sources", "smarkets_probe", run)
        os.makedirs(root, exist_ok=True)
        json.dump({"generated_at": datetime.now(timezone.utc).isoformat(), "crashed": True,
                   "traceback": traceback.format_exc()[-4000:]},
                  open(os.path.join(root, "manifest.json"), "w"), indent=1)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(_guarded())
