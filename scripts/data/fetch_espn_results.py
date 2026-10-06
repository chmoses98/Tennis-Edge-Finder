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

Modes (2026-10-07). Every daily run used to refetch 2026-04-01..today (96 boards by October). Measured over the 23
consecutive daily full snapshots 2026-09-13..10-06: 841 of 842 newly appearing results were published 0-1 day after
the match, no row ever changed or disappeared, and one result (WTA Nottingham, 2026-06-14) appeared 113 days late.
  incremental  fetch the last --window-days (14: a whole Slam fortnight plus margin; never less overlap with the base
               snapshot than its own end date) and CARRY FORWARD every row of the newest valid snapshot, so each
               snapshot stays a complete consolidated record (the canonical build reads only the newest one). A fetched
               row replaces the carried row with the same (tourney_id, match_num); no carried row is ever dropped.
  full         the whole range from --since; it also writes an audit of what differs from the base snapshot (rows
               added, changed, or missing from the refetch -- the latter are kept, flagged, never silently deleted).
  auto         full on --full-weekday (Sunday) or when there is no usable base; incremental otherwise.
Raw payloads of every board fetched remain evidence; no earlier snapshot is ever modified.
"""
from __future__ import annotations

import argparse
import glob
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
    ap.add_argument("--mode", default="auto", choices=["auto", "incremental", "full"])
    ap.add_argument("--window-days", type=int, default=14)
    ap.add_argument("--full-weekday", type=int, default=6, help="weekday (Mon=0) of the periodic full audit")
    ap.add_argument("--base-root", default=None, help="where earlier snapshots are (default: --out)")
    a = ap.parse_args()

    until = date.fromisoformat(a.until) if a.until else datetime.now(timezone.utc).date()
    base_dir, base_man = newest_base(a.base_root or a.out)
    mode = choose_mode(a.mode, base_man, until, a.window_days, a.full_weekday, explicit_since=bool(a.since))
    if mode == "full":
        since = date.fromisoformat(a.since) if a.since else date(2026, 4, 1)
    else:
        base_until = date.fromisoformat(str(base_man.get("until")))
        since = min(until - timedelta(days=a.window_days), base_until - timedelta(days=1))
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

    manifest = {"run_id": run_id, "mode": mode, "since": str(since), "until": str(until), "step_days": a.step_days,
                "fetch_since": str(since), "requests": int(sum(http.values())),
                "base_snapshot": os.path.basename(base_dir) if base_dir else None,
                "http": http, "source": "ESPN site API public scoreboard",
                "note": "results only: no serve statistics, no surface, ESPN-local player ids",
                "finished_at": datetime.now(timezone.utc).isoformat(), "files": {}}
    if frames:
        fetched = pd.concat(frames, ignore_index=True)
        before = len(fetched)
        fetched = fetched.drop_duplicates(subset=["tourney_id", "match_num"], keep="last")
        manifest["rows_before_dedupe"] = int(before)
        manifest["rows_fetched"] = int(len(fetched))
        base = load_snapshot(base_dir) if base_dir else None
        allrows, audit = consolidate(base, fetched, since, until)
        manifest["audit"] = audit
        if mode == "incremental":
            # the consolidated record spans the base's whole range: the canonical build reads only the newest snapshot
            manifest["since"] = str(base_man.get("since"))
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


KEY = ["tourney_id", "match_num"]
COMPARE = ["winner_id", "loser_id", "score", "tourney_date", "round"]


def newest_base(root: str):
    """(dir, manifest) of the newest valid snapshot: has result CSVs, is not quarantined, and has a manifest."""
    runs = sorted(d for d in glob.glob(os.path.join(root, "*")) if os.path.isdir(d)
                  and glob.glob(os.path.join(d, "espn_matches_*.csv.gz")) and not os.path.exists(os.path.join(d, "QUARANTINED.md"))
                  and os.path.exists(os.path.join(d, "manifest.json")))
    if not runs:
        return None, {}
    return runs[-1], json.load(open(os.path.join(runs[-1], "manifest.json")))


def choose_mode(requested: str, base_man: dict, until: date, window_days: int, full_weekday: int,
                explicit_since: bool = False) -> str:
    if requested != "auto":
        return requested if (requested == "full" or base_man) else "full"
    if explicit_since or not base_man or not base_man.get("until") or not base_man.get("since"):
        return "full"
    if until.weekday() == full_weekday:
        return "full"
    return "incremental"


def load_snapshot(d: str) -> pd.DataFrame:
    parts = []
    for p in sorted(glob.glob(os.path.join(d, "espn_matches_*.csv.gz"))):
        tour = os.path.basename(p).split("_")[2]
        df = pd.read_csv(p, dtype=str)
        df["_tour"] = tour
        parts.append(df)
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def consolidate(base: pd.DataFrame | None, fetched: pd.DataFrame, since: date, until: date):
    """Union of the base snapshot and the fetched window; a fetched row wins on its key, no base row is dropped.
    The audit says what the fetch added, changed, or no longer listed (inside the fetched date range)."""
    f = fetched.copy()
    for c in KEY:
        f[c] = f[c].astype(str)
    if base is None or not len(base):
        return f, {"base_rows": 0, "added": int(len(f)), "changed": 0, "missing_in_refetch": 0, "examples": []}
    b = base.copy()
    for c in KEY:
        b[c] = b[c].astype(str)
    bk = b.set_index(KEY)
    fk = f.set_index(KEY)
    added = fk.index.difference(bk.index)
    both = fk.index.intersection(bk.index)
    cmp = [c for c in COMPARE if c in fk.columns and c in bk.columns]
    fa = fk.loc[both, cmp].fillna("").astype(str)
    ba = bk.loc[both, cmp].fillna("").astype(str)
    changed = both[(fa.values != ba.values).any(axis=1)] if len(both) else both
    d = pd.to_datetime(b["tourney_date"].astype(str), format="%Y%m%d", errors="coerce").dt.date
    in_range = b[(d >= since) & (d <= until)].set_index(KEY).index
    missing = in_range.difference(fk.index)
    examples = [{"kind": "changed", "key": list(k), "before": ba.loc[k].to_dict(), "after": fa.loc[k].to_dict()} for k in list(changed)[:10]]
    examples += [{"kind": "missing_in_refetch", "key": list(k)} for k in list(missing)[:10]]
    out = pd.concat([b[~b.set_index(KEY).index.isin(fk.index)], f], ignore_index=True)
    return out, {"base_rows": int(len(b)), "added": int(len(added)), "changed": int(len(changed)),
                 "missing_in_refetch": int(len(missing)), "carried_forward": int(len(b) - len(both)), "examples": examples}


if __name__ == "__main__":
    raise SystemExit(main())
