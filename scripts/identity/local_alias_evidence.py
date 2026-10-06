#!/usr/bin/env python3
"""Data-derived evidence for player-alias candidates. Decides nothing.

For every candidate in research/projection_v2/alias_review/candidates.json, from the evidence already on disk:

* SHARED MATCHES -- the same match recorded by both sources: the foreign id and the proposed canonical id each
  beat (or lost to) the same opponent within +/-10 days (TML dates Challengers by the final day, Sackmann by the
  first; ESPN by the match day). Opponents are compared by normalised name, by token set (family-name order), or
  by the crosswalk. A shared match is evidence two records describe one person playing one match; a namesake
  cannot produce one.
* ACTIVITY -- first/last result and row counts for each id (an old namesake shows up as non-overlapping careers).
* BIOGRAPHY -- Sackmann's players file (dob, ioc, wikidata id) for the canonical id; for a TML id, the TML ATP
  database record (ATP-site id, ATP's own spelling of the name, birth date, ioc); for an ESPN id, the country ESPN
  reports on its rows; and per-row ages/ioc where the source carries them.

Output: research/projection_v2/alias_review/local_evidence.json
"""
from __future__ import annotations

import argparse
import csv
import glob
import gzip
import io
import json
import os
import sys
from datetime import timedelta

import pandas as pd

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJ)
from tennis_edge.identity.names import normalize_name  # noqa: E402

OUT = os.path.join(PROJ, "research", "projection_v2", "alias_review")
WINDOW_DAYS = 10


def _csv(p):
    return csv.DictReader(io.TextIOWrapper(gzip.open(p), encoding="utf-8", errors="replace") if p.endswith(".gz") else open(p))


def _newest(data_root, pattern):
    hits = sorted(glob.glob(os.path.join(data_root, "sources", *pattern.split("/"))))
    return hits[-1] if hits else None


def sackmann_bios(data_root):
    out = {}
    for t in ("atp", "wta"):
        p = _newest(data_root, f"*/sackmann/tennis_{t}/{t}_players.csv*")
        if p:
            for r in _csv(p):
                out[str(r["player_id"])] = {k: r.get(k) for k in ("name_first", "name_last", "dob", "ioc", "wikidata_id", "hand")} | {"tour": t.upper()}
    return out


def tml_bios(data_root):
    p = _newest(data_root, "*/tml/ATP_Database.csv*")
    return {r["id"]: {k: r.get(k) for k in ("player", "atpname", "birthdate", "ioc", "birthplace", "turnedpro", "hand")}
            for r in _csv(p)} if p else {}


def _tok(k):
    return frozenset(str(k).split())


def side_rows(m: pd.DataFrame, pid: str, system: str) -> pd.DataFrame:
    """One row per match for player `pid` in `system`: date, won, opponent name key / id, tourney, level, age, ioc."""
    mm = m[m["id_system"] == system]
    parts = []
    for me, op, won in (("winner", "loser", True), ("loser", "winner", False)):
        s = mm[mm[f"{me}_id"].astype(str) == pid]
        if s.empty:
            continue
        d = pd.DataFrame({"date": pd.to_datetime(s["tourney_date"].astype(str), errors="coerce"),
                          "won": won, "opp_key": s[f"{op}_name"].map(normalize_name), "opp_id": s[f"{op}_id"].astype(str),
                          "opp_canon": s.get(f"canonical_{op}_id"), "tourney": s["tourney_name"], "level": s.get("level_canonical"),
                          "round": s["round"], "tour": s["tour"],
                          "age": s.get(f"{me}_age"), "ioc": s.get(f"{me}_ioc")})
        parts.append(d)
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def shared_matches(f: pd.DataFrame, c: pd.DataFrame, f_opp_canon: dict) -> list:
    out = []
    if f.empty or c.empty:
        return out
    for r in f.itertuples(index=False):
        if pd.isna(r.date):
            continue
        near = c[(c["date"] - r.date).abs() <= timedelta(days=WINDOW_DAYS)]
        for q in near.itertuples(index=False):
            same_opp = (q.opp_key == r.opp_key or (_tok(q.opp_key) == _tok(r.opp_key) and len(_tok(r.opp_key)) >= 2)
                        or (f_opp_canon.get(r.opp_id) and f_opp_canon.get(r.opp_id) == q.opp_id))
            if same_opp and q.won == r.won:
                out.append({"foreign_date": str(r.date.date()), "canonical_date": str(q.date.date()), "won": bool(r.won),
                            "opponent": r.opp_key, "foreign_tourney": r.tourney, "canonical_tourney": q.tourney, "round": q.round})
                break
    return out


def activity(d: pd.DataFrame) -> dict:
    if d.empty:
        return {"n_matches": 0}
    ages = pd.to_numeric(d["age"], errors="coerce") if "age" in d else pd.Series(dtype=float)
    birth = (d["date"] - pd.to_timedelta(ages * 365.25, unit="D")).dropna() if len(ages.dropna()) else pd.Series(dtype="datetime64[ns]")
    return {"n_matches": int(len(d)), "first": str(d["date"].min().date()), "last": str(d["date"].max().date()),
            "tours": sorted(d["tour"].dropna().unique().tolist()),
            "levels": {k: int(v) for k, v in d["level"].value_counts().items()} if "level" in d else {},
            "ioc_on_rows": {k: int(v) for k, v in d["ioc"].dropna().astype(str).value_counts().head(3).items()} if "ioc" in d else {},
            "birth_date_implied_by_row_ages": str(birth.median().date()) if len(birth) else None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--matches", default=None)
    ap.add_argument("--candidates", default=os.path.join(OUT, "candidates.json"))
    ap.add_argument("--out", default=os.path.join(OUT, "local_evidence.json"))
    a = ap.parse_args()
    m = pd.read_parquet(a.matches or os.path.join(a.data_root, "processed", "matches.parquet"))
    cw = pd.read_parquet(os.path.join(os.path.dirname(a.matches or os.path.join(a.data_root, "processed", "x")), "player_crosswalk.parquet"))
    canon_of = {(r.foreign_id_system, str(r.foreign_id)): str(r.canonical_id) for r in cw.itertuples(index=False)
                if r.canonical_id is not None and r.status in ("MAPPED", "MINTED_NEW_PLAYER", "REVIEWED_ALIAS")}
    sb, tb = sackmann_bios(a.data_root), tml_bios(a.data_root)
    cands = json.load(open(a.candidates))["candidates"]
    res = []
    for c in cands:
        sysn, fid = c["foreign_system"], c["foreign_id"]
        f = side_rows(m, fid, sysn)
        f_opp = {oid: canon_of.get((sysn, oid)) for oid in f["opp_id"].unique()} if not f.empty else {}
        cw_row = cw[(cw.foreign_id_system == sysn) & (cw.foreign_id.astype(str) == fid)]
        e = {"foreign_system": sysn, "foreign_id": fid, "foreign_name": c["foreign_name"],
             "crosswalk_status": cw_row["status"].iloc[0] if len(cw_row) else None,
             "foreign_activity": activity(f),
             "foreign_bio": tb.get(fid) if sysn == "tml" else None, "candidates": []}
        for cand in c["candidates"]:
            cid = cand["canonical_id"]
            cr = side_rows(m, cid, "sackmann")
            sm = shared_matches(f, cr, f_opp)
            e["candidates"].append({"canonical_id": cid, "canonical_name": cand["canonical_name"],
                                    "sackmann_bio": sb.get(cid), "canonical_activity": activity(cr),
                                    "shared_matches": len(sm), "shared_match_examples": sm[:5]})
        res.append(e)
        print(sysn, fid, c["foreign_name"], [(x["canonical_id"], x["shared_matches"]) for x in e["candidates"]])
    json.dump({"window_days": WINDOW_DAYS, "matches_rows": int(len(m)), "candidates": res}, open(a.out, "w"), indent=1, default=str)
    return 0


if __name__ == "__main__":
    sys.exit(main())
