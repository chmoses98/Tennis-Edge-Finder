#!/usr/bin/env python3
"""Backfill and refresh CURRENT tennis results from ESPN's public scoreboard.

Runs on a GitHub Actions runner (the research sandbox has no egress to espn.com). Walks a date range,
fetches the ATP and WTA scoreboards, stores every raw payload gzipped as evidence, parses completed
SINGLES results into Sackmann-shaped CSVs and publishes them to the `tennis-data` branch.

Two things make this cheap. A scoreboard for one date returns the WHOLE tournament board, so the walk
steps several days at a time rather than daily. And the parser deduplicates on (tourney_id, match_num),
so overlapping boards cost bandwidth but never duplicate rows.

This refreshes the RESULT record only. ESPN publishes no serve statistics and no surface on the
scoreboard, and its player ids mean nothing outside ESPN, so the rows enter the canonical table as their
own id system and are bound to canonical players by the fail-closed name crosswalk.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import sys
import time
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import pandas as pd                                                        # noqa: E402
from tennis_edge.data.espn_results import parse_scoreboard, summarise      # noqa: E402
from tennis_edge.firstball.probe import fetch                              # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
URL = "https://site.api.espn.com/apis/site/v2/sports/tennis/{league}/scoreboard?dates={ymd}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="", help="YYYY-MM-DD; default 2026-04-01 (before both source cutoffs)")
    ap.add_argument("--until", default="", help="YYYY-MM-DD; default today (UTC)")
    ap.add_argument("--step-days", type=int, default=4, help="a board spans a whole tournament, so stepping is safe")
    ap.add_argument("--leagues", default="atp,wta")
    ap.add_argument("--gap", type=float, default=1.5, help="seconds between requests")
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "sources", "espn"))
    ap.add_argument("--keep-raw", action="store_true", default=True)
    a = ap.parse_args()

    since = date.fromisoformat(a.since) if a.since else date(2026, 4, 1)
    until = date.fromisoformat(a.until) if a.until else datetime.now(timezone.utc).date()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = os.path.join(a.out, run_id)
    os.makedirs(os.path.join(out, "raw"), exist_ok=True)

    frames, http = [], {}
    days = []
    d = since
    while d <= until:
        days.append(d)
        d += timedelta(days=a.step_days)
    if days and days[-1] != until:
        days.append(until)

    print(f"== ESPN results {since} .. {until}, {len(days)} boards x {len(a.leagues.split(','))} leagues", flush=True)
    for d in days:
        for league in a.leagues.split(","):
            url = URL.format(league=league, ymd=d.strftime("%Y%m%d"))
            rec = fetch(url, accept="application/json")
            body = rec.pop("_body", b"")
            code = str(rec.get("status"))
            http[code] = http.get(code, 0) + 1
            if rec.get("status") != 200 or not body:
                print(f"   {d} {league:3s} -> {rec.get('status')} {rec.get('error','')[:50]}", flush=True)
                time.sleep(a.gap)
                continue
            if a.keep_raw:
                with gzip.open(os.path.join(out, "raw", f"{d:%Y%m%d}_{league}.json.gz"), "wb") as f:
                    f.write(body)
            try:
                payload = json.loads(body.decode("utf-8", "replace"))
            except ValueError as e:
                print(f"   {d} {league} unparseable: {e}", flush=True)
                time.sleep(a.gap)
                continue
            df = parse_scoreboard(payload, league)
            frames.append(df)
            print(f"   {d} {league:3s} -> {len(df):4d} completed singles ({len(body)//1024} KiB)", flush=True)
            time.sleep(a.gap)

    manifest = {"run_id": run_id, "since": str(since), "until": str(until), "step_days": a.step_days,
                "http": http, "source": "ESPN site API public scoreboard",
                "note": "results only: no serve statistics, no surface, ESPN-local player ids",
                "finished_at": datetime.now(timezone.utc).isoformat(), "files": {}}
    if frames:
        allrows = pd.concat(frames, ignore_index=True)
        before = len(allrows)
        allrows = allrows.drop_duplicates(subset=["tourney_id", "match_num"], keep="last")
        manifest["rows_before_dedupe"] = int(before)
        manifest["rows"] = int(len(allrows))
        manifest["summary"] = summarise(allrows)
        for tour in ("ATP", "WTA"):
            sub = allrows[allrows["_tour"] == tour].drop(columns=["_tour"])
            if not len(sub):
                continue
            for year, chunk in sub.groupby(sub["tourney_date"].astype(str).str[:4]):
                fn = f"espn_matches_{tour}_{year}.csv.gz"
                chunk.to_csv(os.path.join(out, fn), index=False, compression="gzip")
                manifest["files"][fn] = int(len(chunk))
    json.dump(manifest, open(os.path.join(out, "manifest.json"), "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in manifest.items() if k != "summary"}, indent=1, default=str))
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
