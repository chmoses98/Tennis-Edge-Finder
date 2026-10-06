#!/usr/bin/env python3
"""Flatten raw alias evidence (evidence_raw/*.json + local_evidence.json) into one comparable row per candidate pair.

Pure extraction: it reports what each source says (name, date of birth, nationality, governing-body ids, shared
matches). It never outputs a decision; ALIAS_REVIEW_DECISION.json is written by the reviewer.
Output: research/projection_v2/alias_review/evidence_summary.json
"""
from __future__ import annotations

import glob
import json
import os
import sys

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = os.path.join(PROJ, "research", "projection_v2", "alias_review")


def _dob(x):
    if not x:
        return None
    x = str(x).lstrip("+")
    return x[:10] if "-" in x[:10] else (f"{x[:4]}-{x[4:6]}-{x[6:8]}" if len(x) >= 8 and x[:8].isdigit() else None)


def wta_api(profiles):
    for p in profiles or []:
        if "api.wtatennis.com" in p.get("url", "") and p.get("status") == 200 and isinstance(p.get("json"), dict):
            j = p["json"]
            return {"wta_id": j.get("id"), "name": j.get("fullName"), "dob": j.get("dateOfBirth"), "country": j.get("countryCode"),
                    "url": p["url"], "fetched_at": p.get("fetched_at")}
    return None


def wd(s):
    s = (s or {}).get("summary") or {}
    if not s:
        return None
    return {"qid": s.get("qid"), "label": s.get("label_en"), "label_zh": s.get("label_zh"), "aliases": s.get("aliases_en"),
            "atp_id": s.get("atp_id"), "wta_id": s.get("wta_id"), "itf_id": s.get("itf_id"),
            "dob": [_dob(x) for x in s.get("date_of_birth") or []]}


def main():
    local = {(c["foreign_system"], c["foreign_id"]): c for c in json.load(open(os.path.join(D, "local_evidence.json")))["candidates"]}
    out = []
    for f in sorted(glob.glob(os.path.join(D, "evidence_raw", "*.json"))):
        if os.path.basename(f).startswith("_"):
            continue
        e = json.load(open(f))
        key = (e["foreign_system"], e["foreign_id"])
        loc = local.get(key) or {}
        tours = loc.get("foreign_tours") or ([e["foreign_id"].split(":")[1]] if e["foreign_system"] == "kalshi" else [])
        row = {"foreign_system": e["foreign_system"], "foreign_id": e["foreign_id"], "foreign_name": e["foreign_name"],
               "tours": tours, "raw_file": os.path.relpath(f, PROJ), "foreign": {}, "canonical": {}}
        fo = e.get("foreign") or {}
        if e["foreign_system"] == "espn":
            a = ((fo.get("espn_athlete") or [{}])[0].get("json")) or {}
            row["foreign"]["espn"] = {"id": a.get("id"), "name": a.get("fullName"), "dob": _dob(a.get("dateOfBirth")),
                                      "birthplace": (a.get("birthPlace") or {}).get("summary"),
                                      "country": (a.get("citizenshipCountry") or {}).get("abbreviation") or (a.get("flag") or {}).get("alt"),
                                      "debut_year": a.get("debutYear"),
                                      "url": (fo.get("espn_athlete") or [{}])[0].get("url")}
        if loc.get("foreign_bio"):
            row["foreign"]["tml_atp_database"] = loc["foreign_bio"]
        row["foreign"]["wikidata_items_with_this_atp_id"] = fo.get("wikidata_items_with_this_atp_id")
        ws = fo.get("wikidata_search") or {}
        row["foreign"]["wikidata_search"] = {"status": ws.get("status"), "hits": ws.get("hits"),
                                             "players": [wd(p) for p in ws.get("players") or []]} if ws else None
        if fo.get("tour_profiles"):
            row["foreign"]["wta_api"] = wta_api(fo.get("tour_profiles"))
        row["foreign"]["activity"] = loc.get("foreign_activity")
        for cid, per_tour in (e.get("canonical") or {}).items():
            lc = next((x for x in loc.get("candidates") or [] if x["canonical_id"] == cid), {})
            for tour in tours:
                te = (per_tour or {}).get(tour) or {}
                pr = te.get("sackmann_players_row") or {}
                srch = te.get("wikidata_search") or {}
                row["canonical"].setdefault(cid, {})[tour] = {
                    "sackmann": {"name": f"{pr.get('name_first', '')} {pr.get('name_last', '')}".strip() or None,
                                 "dob": _dob(pr.get("dob")), "ioc": pr.get("ioc"), "wikidata_id": pr.get("wikidata_id") or None},
                    "wikidata": wd(te.get("wikidata")),
                    "wikidata_search": {"status": srch.get("status"), "players": [wd(p) for p in srch.get("players") or []]} if srch else None,
                    "wta_api": wta_api(te.get("tour_profiles")),
                    "shared_matches": lc.get("shared_matches"), "shared_match_examples": lc.get("shared_match_examples"),
                    "activity": lc.get("canonical_activity")}
        out.append(row)
    json.dump(out, open(os.path.join(D, "evidence_summary.json"), "w"), indent=1, default=str)
    print(len(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
