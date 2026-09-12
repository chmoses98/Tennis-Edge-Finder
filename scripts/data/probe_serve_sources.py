#!/usr/bin/env python3
"""A BOUNDED search for a current, free, legally usable source of WTA serve statistics.

Bounded on purpose. The Sackmann repositories are gone, the community mirror carries ATP Challenger and
ITF serve statistics to 2026-09-01 but nothing for the women, and Wave 2 already rejected "find a fresher
fork" (R-005). This probe checks the small number of remaining candidates, records exactly what each one
returned, and stops. If none of them carries serve statistics, that is the finding and TENNIS-14 stays
red rather than being redefined into green.

Each candidate records: reachability, whether serve statistics are present in the payload, how current,
and what the site's own terms and robots.txt say -- a source we may not use is not a source.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UA = "tennis-edge-finder/1.0 (research; contact via repository)"
SERVE_KEYS = ("aces", "doubleFaults", "firstServePointsWon", "servicePointsWon", "breakPointsSaved",
              "1stServe", "svpt", "firstServe")


def get(url: str, timeout=25):
    headers = {"User-Agent": UA, "Accept": "*/*"}
    if "api.github.com" in url and os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    req = urllib.request.Request(url, headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
        return {"ok": True, "status": 200, "bytes": len(body), "ms": int((time.time() - t0) * 1000)}, body
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "error": str(e), "ms": int((time.time() - t0) * 1000)}, b""
    except Exception as e:                                     # noqa: BLE001
        return {"ok": False, "status": None, "error": f"{type(e).__name__}: {e}",
                "ms": int((time.time() - t0) * 1000)}, b""


def has_serve_stats(body: bytes) -> dict:
    try:
        text = body.decode("utf-8", "replace")
    except Exception:                                          # noqa: BLE001
        return {"parsed": False}
    hits = sorted({k for k in SERVE_KEYS if k in text})
    out = {"parsed": True, "serve_keys_present": hits, "looks_like_serve_stats": len(hits) >= 2}
    try:
        obj = json.loads(text)
    except Exception:                                          # noqa: BLE001
        return out
    # ESPN summary: boxscore.players[].statistics[].stats
    names = set()
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("name", "abbreviation", "label") and isinstance(v, str):
                    names.add(v)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(obj)
    out["statistic_labels_sample"] = sorted(n for n in names if any(
        t in n.lower() for t in ("serve", "ace", "double", "break", "point")))[:20]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "sources", "serve_probe"))
    ap.add_argument("--espn-event", default="", help="an ESPN tennis event id to ask for a summary of")
    a = ap.parse_args()
    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    root = os.path.join(a.out, run, "raw")
    os.makedirs(root, exist_ok=True)
    results = []

    # 0. find a recent WTA event id from the scoreboard, so the summary probe has something real to ask
    ev = a.espn_event
    meta, body = get("https://site.api.espn.com/apis/site/v2/sports/tennis/wta/scoreboard")
    results.append({"candidate": "espn_wta_scoreboard", "url": "site.api.espn.com .../wta/scoreboard", **meta})
    if body:
        open(os.path.join(root, "espn_wta_scoreboard.json.gz"), "wb").write(gzip.compress(body))
        if not ev:
            # events[].id, not the first id in the document -- the first one is the league.
            try:
                sb = json.loads(body.decode("utf-8", "replace"))
                for e in sb.get("events") or []:
                    for g in e.get("groupings") or []:
                        for c in g.get("competitions") or []:
                            if ((c.get("status") or {}).get("type") or {}).get("completed"):
                                ev = str(c.get("id") or e.get("id") or "")
                                break
                        if ev:
                            break
                    if ev:
                        break
                    ev = str(e.get("id") or "")
            except Exception:                                  # noqa: BLE001
                ev = ""

    candidates = [
        ("espn_summary", f"https://site.api.espn.com/apis/site/v2/sports/tennis/wta/summary?event={ev}" if ev else None,
         "ESPN's own match page data; the scoreboard carries no statistics, so this is the only ESPN "
         "endpoint that could"),
        ("tennisabstract_robots", "https://www.tennisabstract.com/robots.txt",
         "whether the site permits automated access at all -- checked BEFORE any data URL"),
        ("wta_official_stats", "https://api.wtatennis.com/tennis/stats/players?page=0&pageSize=5",
         "the tour's own public JSON, if it exists and is open"),
        ("github_wta_forks", "https://api.github.com/search/repositories?q=tennis_wta+in:name+fork:true"
                             "&sort=updated&order=desc&per_page=5",
         "one more look for a live fork, three months after Wave 2 rejected the idea (R-005)"),
    ]
    for name, url, why in candidates:
        if not url:
            results.append({"candidate": name, "skipped": "no event id available", "why": why})
            continue
        meta, body = get(url)
        rec = {"candidate": name, "url": url, "why": why, **meta}
        if body:
            open(os.path.join(root, f"{name}.gz"), "wb").write(gzip.compress(body))
            rec["content"] = has_serve_stats(body)
            if name == "tennisabstract_robots":
                rec["robots_txt"] = body.decode("utf-8", "replace")[:1500]
        results.append(rec)
        time.sleep(1.0)

    verdict = {"generated_at": datetime.now(timezone.utc).isoformat(), "run_id": run,
               "espn_event_probed": ev,
               "any_source_with_serve_stats": any(
                   r.get("content", {}).get("looks_like_serve_stats") for r in results),
               "candidates": results}
    json.dump(verdict, open(os.path.join(a.out, run, "manifest.json"), "w"), indent=1, default=str)
    print(json.dumps(verdict, indent=1, default=str)[:6000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
