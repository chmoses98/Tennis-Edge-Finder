#!/usr/bin/env python3
"""Wave 4 Phase 0: is there a free, current, legally usable external tennis price feed at all?

Runs on a GitHub Actions runner; the research sandbox has no egress to any of these hosts.

The order of operations is the point. For every host this fetches **robots.txt first** and records what
it says. A data endpoint is requested only where robots.txt does not disallow the path, and a host that
disallows is recorded as REFUSED_BY_ROBOTS with no further request made -- a source we may not use is not
a source, whatever it contains.

For each candidate the probe records reachability, auth, what tennis it actually covers (tour, level,
discipline), which market families appear, whether prices are two-sided (an exchange) or offered odds
(a book), whether the payload carries its own timestamp, and the rate-limit headers. Everything is
written raw and gzipped so a later reader can check this file's conclusions against the bytes.
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
from datetime import datetime, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UA = "tennis-edge-finder/1.0 (research; +https://github.com/chmoses98/Tennis-Edge-Finder)"

#: (name, host, data url, why we care, what independence it would give us)
CANDIDATES = [
    ("espn_odds_atp",
     "https://site.api.espn.com",
     "https://site.api.espn.com/apis/site/v2/sports/tennis/atp/scoreboard",
     "ESPN's scoreboard sometimes carries an `odds` block from a book; we already use this host for "
     "results and first-ball, so its terms are already assessed",
     "a sportsbook line, dependent on whichever book ESPN sources"),
    ("espn_odds_wta",
     "https://site.api.espn.com",
     "https://site.api.espn.com/apis/site/v2/sports/tennis/wta/scoreboard",
     "same, women's board",
     "as above"),
    ("polymarket_gamma",
     "https://gamma-api.polymarket.com",
     "https://gamma-api.polymarket.com/events?closed=false&limit=100&tag_slug=tennis",
     "a public, keyless prediction-market API; genuinely a different venue from Kalshi with different "
     "participants",
     "an independent prediction market -- the strongest available independence"),
    ("polymarket_gamma_search",
     "https://gamma-api.polymarket.com",
     "https://gamma-api.polymarket.com/markets?closed=false&limit=100",
     "the market-level endpoint, in case tennis is not tagged as an event",
     "as above"),
    ("bovada_tennis",
     "https://www.bovada.lv",
     "https://www.bovada.lv/services/sports/event/coupon/events/A/description/tennis?marketFilterId=def"
     "&preMatchOnly=true&lang=en",
     "a public sportsbook JSON coupon endpoint that needs no key",
     "a recreational book: useful as a second opinion, NOT as a sharp reference"),
    ("theoddsapi_keyless",
     "https://api.the-odds-api.com",
     "https://api.the-odds-api.com/v4/sports/?apiKey=",
     "an aggregator with a free tier; checked to establish whether it works without a key at all",
     "many books at once, if it were usable unattended"),
    ("betfair_public",
     "https://www.betfair.com",
     "https://www.betfair.com/sport/tennis",
     "the largest tennis exchange; checked only to record whether anything is publicly reachable "
     "without an application key",
     "a true exchange with two-sided prices"),
    ("smarkets_public",
     "https://api.smarkets.com",
     "https://api.smarkets.com/v3/events/?type=sport&sport_id=8&state=upcoming&limit=50",
     "an exchange with a documented public API",
     "a second true exchange"),
    ("pinnacle_public",
     "https://api.pinnacle.com",
     "https://api.pinnacle.com/v1/sports",
     "the classic sharp book; the mandate says do not assume it is available, so this asks",
     "the sharpest single reference, if it were open"),
]


def _req(url: str, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            hdrs = {k.lower(): v for k, v in r.headers.items()}
        return {"ok": True, "status": 200, "bytes": len(body), "ms": int((time.time() - t0) * 1000),
                "rate_limit_headers": {k: v for k, v in hdrs.items() if "ratelimit" in k or "retry" in k},
                "content_type": hdrs.get("content-type", "")}, body
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "error": str(e)[:200],
                "ms": int((time.time() - t0) * 1000)}, b""
    except Exception as e:                                                        # noqa: BLE001
        return {"ok": False, "status": None, "error": f"{type(e).__name__}: {str(e)[:160]}",
                "ms": int((time.time() - t0) * 1000)}, b""


def robots_verdict(host: str, path: str, cache: dict) -> dict:
    """Fetch robots.txt once per host and decide whether `path` is allowed for a generic agent."""
    if host not in cache:
        meta, body = _req(host.rstrip("/") + "/robots.txt", timeout=15)
        cache[host] = {"meta": meta, "text": body.decode("utf-8", "replace")[:4000] if body else ""}
    text = cache[host]["text"]
    if not cache[host]["meta"].get("ok"):
        # no robots.txt served is not permission denied, but it IS an unknown, and is recorded as one
        return {"robots_status": cache[host]["meta"].get("status"), "verdict": "NO_ROBOTS_SERVED",
                "disallow_rules": []}
    rules, in_star = [], False
    for line in text.splitlines():
        s = line.split("#", 1)[0].strip()
        if not s:
            continue
        k, _, v = s.partition(":")
        k, v = k.strip().lower(), v.strip()
        if k == "user-agent":
            in_star = (v == "*")
        elif k == "disallow" and in_star and v:
            rules.append(v)
    blocked = [r for r in rules if r == "/" or path.startswith(r)]
    return {"robots_status": 200, "verdict": "REFUSED_BY_ROBOTS" if blocked else "ALLOWED",
            "matched_disallow": blocked, "disallow_rules": rules[:25]}


def describe_tennis(name: str, body: bytes) -> dict:
    """What tennis is actually in here, and is it priced."""
    try:
        obj = json.loads(body.decode("utf-8", "replace"))
    except Exception:                                                             # noqa: BLE001
        text = body.decode("utf-8", "replace")
        return {"json": False, "looks_like_html": "<html" in text.lower()[:2000],
                "mentions_tennis": "tennis" in text.lower()}
    out = {"json": True}
    prices, names, families, timestamps = set(), set(), set(), set()

    def walk(o, depth=0):
        if depth > 12:
            return
        if isinstance(o, dict):
            for k, v in o.items():
                lk = k.lower()
                if lk in ("odds", "price", "outcomes", "moneyline", "americanodds", "decimalodds",
                          "bestbid", "bestask", "outcomeprices", "displayodds", "handicap"):
                    prices.add(k)
                if lk in ("question", "title", "name", "shortname", "description", "displayname"):
                    if isinstance(v, str) and 3 < len(v) < 160:
                        names.add(v)
                if lk in ("markettype", "market", "grouping", "descriptionkey", "slug", "category"):
                    if isinstance(v, str) and len(v) < 80:
                        families.add(v)
                if lk in ("timestamp", "updated", "updatedat", "lastupdate", "starttime", "startdate",
                          "date", "gamedate", "endtime", "eventstarttime"):
                    if isinstance(v, str) and len(v) < 40:
                        timestamps.add(f"{k}={v}")
                walk(v, depth + 1)
        elif isinstance(o, list):
            for v in o[:400]:
                walk(v, depth + 1)

    walk(obj)
    low = " ".join(list(names)[:400]).lower()
    out["price_keys"] = sorted(prices)[:12]
    out["has_prices"] = bool(prices)
    out["name_sample"] = sorted(names)[:12]
    out["family_sample"] = sorted(families)[:15]
    out["timestamp_sample"] = sorted(timestamps)[:6]
    out["mentions_tennis"] = "tennis" in json.dumps(obj)[:400000].lower()
    out["hints"] = {k: (k in low) for k in ("atp", "wta", "challenger", "itf", "qualif", "doubles",
                                            "set", "games", "spread")}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "sources", "external_odds_probe"))
    a = ap.parse_args()
    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    root = os.path.join(a.out, run)
    os.makedirs(os.path.join(root, "raw"), exist_ok=True)
    robots_cache: dict = {}
    results = []

    for name, host, url, why, independence in CANDIDATES:
        path = urllib.parse.urlparse(url).path or "/"
        rob = robots_verdict(host, path, robots_cache)
        rec = {"candidate": name, "host": host, "url": url, "why": why,
               "independence_if_usable": independence, "robots": rob}
        if rob["verdict"] == "REFUSED_BY_ROBOTS":
            rec["outcome"] = "NOT PROBED: robots.txt disallows this path for a generic agent"
            results.append(rec)
            continue
        meta, body = _req(url)
        rec.update(meta)
        if body:
            open(os.path.join(root, "raw", f"{name}.gz"), "wb").write(gzip.compress(body))
            rec["content"] = describe_tennis(name, body)
        results.append(rec)
        time.sleep(1.2)

    for host, v in robots_cache.items():
        open(os.path.join(root, "raw", f"robots_{urllib.parse.urlparse(host).netloc}.txt"), "w").write(v["text"])

    usable = [r["candidate"] for r in results
              if r.get("status") == 200 and (r.get("content") or {}).get("has_prices")]
    verdict = {"generated_at": datetime.now(timezone.utc).isoformat(), "run_id": run,
               "n_candidates": len(CANDIDATES),
               "reachable_with_prices": usable,
               "refused_by_robots": [r["candidate"] for r in results
                                     if r["robots"]["verdict"] == "REFUSED_BY_ROBOTS"],
               "candidates": results}
    json.dump(verdict, open(os.path.join(root, "manifest.json"), "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in verdict.items() if k != "candidates"}, indent=1, default=str))
    for r in results:
        c = r.get("content") or {}
        print(f"\n{r['candidate']:24s} robots={r['robots']['verdict']:18s} status={r.get('status')} "
              f"bytes={r.get('bytes')}")
        if c:
            print(f"   prices={c.get('has_prices')} keys={c.get('price_keys')} hints={c.get('hints')}")
            print(f"   names={c.get('name_sample', [])[:4]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
