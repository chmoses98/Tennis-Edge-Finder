#!/usr/bin/env python3
"""Phase 0: probe candidate ACTUAL-first-ball sources and publish the evidence.

Runs on a GitHub Actions runner (the research sandbox has no egress to tennis hosts). Probes every
candidate in tennis_edge.firstball.catalogue across several rounds separated in time, stores the raw
payloads, and writes a machine-readable summary that docs/FIRST_BALL_SOURCES.md is built from.

Nothing here decides whether a source is trustworthy. It gathers evidence; a human-readable authority
matrix is written from that evidence afterwards.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import sys
import time
from datetime import datetime, timezone, timedelta, date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.firstball.catalogue import CANDIDATES, HOSTS          # noqa: E402
from tennis_edge.firstball.probe import fetch, analyse, robots_for, _fmt_urls   # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "firstball", "probe"))
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--round-gap", type=int, default=120, help="seconds between rounds")
    ap.add_argument("--per-request-gap", type=float, default=1.5)
    ap.add_argument("--only", default="", help="comma-separated candidate ids")
    a = ap.parse_args()

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = os.path.join(a.out, run_id)
    os.makedirs(os.path.join(out, "raw"), exist_ok=True)
    only = {x for x in a.only.split(",") if x}
    cands = [c for c in CANDIDATES if not only or c.id in only]
    today = datetime.now(timezone.utc).date()

    summary = {"run_id": run_id, "started_at": datetime.now(timezone.utc).isoformat(),
               "rounds": a.rounds, "round_gap_s": a.round_gap, "probe_date_utc": today.isoformat(),
               "candidates": {}, "robots": {}}

    print(f"== robots.txt for {len(HOSTS)} hosts", flush=True)
    for h in HOSTS:
        try:
            summary["robots"][h] = robots_for(h)
        except Exception as e:                                    # a probe must never abort the mission
            summary["robots"][h] = {"error": f"{type(e).__name__}: {e}"[:200]}
        time.sleep(a.per_request_gap)

    for rnd in range(a.rounds):
        print(f"== round {rnd} ({len(cands)} candidates)", flush=True)
        for c in cands:
            url = _fmt_urls(c, today)
            try:
                rec = analyse(fetch(url, accept=c.accept, referer=c.referer), c.expect)
            except Exception as e:
                rec = {"url": url, "status": None, "error": f"probe-crash {type(e).__name__}: {e}"[:300]}
            body_key = f"{c.id}.r{rnd}"
            slot = summary["candidates"].setdefault(c.id, {
                "name": c.name, "host_class": c.host_class, "levels": list(c.levels),
                "answers": list(c.answers), "auth": c.auth, "notes": c.notes, "url_template": c.url,
                "rounds": []})
            slot["rounds"].append(rec)
            print(f"   {c.id:28s} {str(rec.get('status')):>5}  {rec.get('latency_ms','-')}ms  "
                  f"{rec.get('parse','')} {rec.get('error','')[:60]}", flush=True)
            time.sleep(a.per_request_gap)
        # second date probe on the first round only: yesterday, to test historical recovery
        if rnd == 0:
            y = today - timedelta(days=1)
            for c in cands:
                if "{date" not in c.url and "{year}" not in c.url:
                    continue
                url = _fmt_urls(c, y)
                try:
                    rec = analyse(fetch(url, accept=c.accept, referer=c.referer), c.expect)
                except Exception as e:
                    rec = {"url": url, "status": None, "error": f"probe-crash {type(e).__name__}: {e}"[:300]}
                summary["candidates"][c.id]["historical_probe"] = rec
                print(f"   [hist] {c.id:24s} {str(rec.get('status')):>5}", flush=True)
                time.sleep(a.per_request_gap)
        if rnd < a.rounds - 1:
            time.sleep(a.round_gap)

    # roll up
    for cid, slot in summary["candidates"].items():
        codes = [r.get("status") for r in slot["rounds"]]
        ok = [r for r in slot["rounds"] if r.get("status") == 200 and r.get("parse") in ("json", "html")]
        lat = [r["latency_ms"] for r in slot["rounds"] if r.get("latency_ms") is not None]
        slot["rollup"] = {
            "status_codes": codes,
            "success_rounds": len(ok),
            "total_rounds": len(slot["rounds"]),
            "reliability": round(len(ok) / len(slot["rounds"]), 3) if slot["rounds"] else 0.0,
            "latency_ms_min": min(lat) if lat else None,
            "latency_ms_max": max(lat) if lat else None,
            "timestamp_fields": sorted({k for r in ok for k in (r.get("timestamp_fields") or {})})[:40],
            "historical_status": (slot.get("historical_probe") or {}).get("status"),
        }
    summary["finished_at"] = datetime.now(timezone.utc).isoformat()
    with open(os.path.join(out, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1, default=str)
    print(json.dumps({k: v["rollup"] for k, v in summary["candidates"].items()}, indent=1)[:4000])
    print("wrote", out)


if __name__ == "__main__":
    main()
