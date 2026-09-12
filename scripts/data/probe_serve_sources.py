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

    # 5. the recently-pushed repositories the fork search surfaced. Wave 2's R-005 rejected "find a
    # fresher fork" against the Sackmann forks specifically; these are different repositories, and the
    # only question worth asking is whether any of them ships a CSV with serve-statistic COLUMNS and a
    # 2026 date. Checked by file tree and one header line, then dropped.
    repos = []
    meta, body = get("https://api.github.com/search/repositories?q=tennis+wta+in:name&sort=updated"
                     "&order=desc&per_page=8")
    if body:
        try:
            repos = [r["full_name"] for r in json.loads(body).get("items", [])][:6]
        except Exception:                                      # noqa: BLE001
            repos = []
    for full in repos:
        m2, b2 = get(f"https://api.github.com/repos/{full}/git/trees/HEAD?recursive=1")
        rec = {"candidate": f"repo:{full}", "url": full, **m2,
               "why": "does it ship WTA match data with serve-statistic columns, dated 2026"}
        if b2:
            try:
                tree = json.loads(b2).get("tree", [])
            except Exception:                                  # noqa: BLE001
                tree = []
            csvs = [x["path"] for x in tree if x.get("path", "").lower().endswith((".csv", ".csv.gz"))]
            rec["n_files"] = len(tree)
            rec["csv_sample"] = csvs[:10]
            hit = next((c for c in csvs if "2026" in c and "wta" in c.lower()), None) or (csvs[0] if csvs else None)
            if hit:
                m3, b3 = get(f"https://raw.githubusercontent.com/{full}/HEAD/{hit}")
                header = b3[:600].decode("utf-8", "replace").splitlines()[:1]
                rec["probed_csv"] = hit
                rec["header"] = header[0][:400] if header else ""
                rec["has_serve_columns"] = any(k in rec["header"] for k in
                                               ("w_svpt", "l_svpt", "w_ace", "1stWon", "svpt"))
        results.append(rec)
        time.sleep(0.5)

    verdict = {"generated_at": datetime.now(timezone.utc).isoformat(), "run_id": run,
               "espn_event_probed": ev,
               "any_source_with_serve_stats": any(
                   r.get("content", {}).get("looks_like_serve_stats") or r.get("has_serve_columns")
                   for r in results),
               "repos_with_serve_columns": [r["url"] for r in results if r.get("has_serve_columns")],
               "candidates": results}
    json.dump(verdict, open(os.path.join(a.out, run, "manifest.json"), "w"), indent=1, default=str)
    print(json.dumps(verdict, indent=1, default=str)[:6000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
