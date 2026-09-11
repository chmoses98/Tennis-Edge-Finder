#!/usr/bin/env python3
"""Discover the ITF live-scores data feed by watching the page load it.

The ITF live-scores page is a React shell; its scoreboard is served by the ITF's own data provider
(api.itf-production.sports-data.stadion.io). The bundle builds request paths dynamically, so reading
them out of the minified JavaScript is guesswork. Loading the page in a headless browser and recording
the network is not guesswork: it observes exactly what the official site requests, which is the only
honest way to answer "is there a public ITF feed we may read?".

This is a one-off RESEARCH probe, dispatch-only, never part of the production loop. It records request
URLs, methods, status codes, request headers we would have to reproduce, and response bodies for JSON
responses, so the evidence can be audited later.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import sys
from datetime import datetime, timezone

DEFAULT_PAGES = [
    "https://live.itftennis.com/en/live-scores/",
    "https://www.itftennis.com/en/live-scores/",
    "https://www.itftennis.com/en/world-tennis-tour-live/",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "..", "data", "firstball", "browser_probe"))
    ap.add_argument("--pages", default=",".join(DEFAULT_PAGES))
    ap.add_argument("--wait-ms", type=int, default=15000)
    a = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("::error::playwright is not installed")
        return 2

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = os.path.abspath(os.path.join(a.out, run_id))
    os.makedirs(os.path.join(out, "bodies"), exist_ok=True)
    summary = {"run_id": run_id, "started_at": datetime.now(timezone.utc).isoformat(), "pages": {}}

    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=["--no-sandbox"])
        for page_url in a.pages.split(","):
            ctx = browser.new_context(viewport={"width": 1400, "height": 1000})
            page = ctx.new_page()
            calls = []

            def on_response(resp, calls=calls):
                url = resp.url
                if any(k in url for k in (".png", ".jpg", ".svg", ".woff", ".css", "doubleclick", "google")):
                    return
                rec = {"url": url, "status": resp.status, "method": resp.request.method,
                       "resource_type": resp.request.resource_type,
                       "request_headers": {k: v for k, v in resp.request.headers.items()
                                           if k.lower() in ("origin", "referer", "accept", "authorization",
                                                            "x-api-key", "x-requested-with")},
                       "content_type": resp.headers.get("content-type", "")}
                if "json" in rec["content_type"]:
                    try:
                        body = resp.body()
                        rec["bytes"] = len(body)
                        name = str(abs(hash(url)))[:16] + ".json.gz"
                        with gzip.open(os.path.join(out, "bodies", name), "wb") as f:
                            f.write(body)
                        rec["body_file"] = f"bodies/{name}"
                        try:
                            parsed = json.loads(body.decode("utf-8", "replace"))
                            rec["top_keys"] = list(parsed)[:20] if isinstance(parsed, dict) else f"list[{len(parsed)}]"
                        except ValueError:
                            pass
                    except Exception as e:
                        rec["body_error"] = f"{type(e).__name__}: {e}"[:200]
                calls.append(rec)

            page.on("response", on_response)
            try:
                page.goto(page_url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(a.wait_ms)
                title = page.title()
            except Exception as e:
                title = f"ERROR {type(e).__name__}: {e}"[:200]
            api = [c for c in calls if "stadion.io" in c["url"] or "/api/" in c["url"]]
            summary["pages"][page_url] = {"title": title, "n_requests": len(calls), "api_calls": api,
                                          "all_hosts": sorted({c["url"].split("/")[2] for c in calls})}
            print(f"== {page_url}\n   title={title}\n   requests={len(calls)} api-ish={len(api)}", flush=True)
            for c in api[:25]:
                print(f"     {c['status']} {c['method']} {c['url'][:150]}", flush=True)
            ctx.close()
        browser.close()

    summary["finished_at"] = datetime.now(timezone.utc).isoformat()
    with open(os.path.join(out, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1, default=str)
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
