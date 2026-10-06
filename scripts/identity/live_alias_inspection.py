#!/usr/bin/env python3
"""Before/after coverage and the live sanity review of reviewed aliases on a production board. Changes nothing.

Compares two projection runs (data/research/projections/<run>.json): projectable markets, identity exclusions,
singles/doubles, V2 uncertainty grades, alias use, review queue -- and, for every ACCEPTED crosswalk alias whose
canonical player appears on the AFTER board, lists canonical id, name, rating history, opponent, event, level,
surface, recent results, grade, the probability change vs the BEFORE board and the model-market gap (flagging
> 20 pp). Also lists still-unresolved review names that appear live.

Output: research/projection_v2/alias_review/coverage_before_after.json (+ a markdown block for the results report).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter

import pandas as pd

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJ)
from tennis_edge.identity.names import normalize_name  # noqa: E402

OUT = os.path.join(PROJ, "research", "projection_v2", "alias_review", "coverage_before_after.json")


def stats(p: dict) -> dict:
    rows = p.get("projections") or []
    ex = p.get("excluded") or []
    ident = [e for e in ex if e.get("stage") == "identity"]
    kinds = Counter(k for e in ident for k in (e.get("identity_kinds") or ["UNCLASSIFIED"]))
    unmapped_names = set()
    for e in ident:
        for part in e["reason"].split("; "):
            if ": UNMAPPED" in part or ": AMBIGUOUS" in part:
                unmapped_names.add(normalize_name(part.split(": ")[0]))
    singles = [r for r in rows if "|" not in str(r.get("player_a_id"))]
    doubles = [r for r in rows if "|" in str(r.get("player_a_id"))]
    hard = [e for e in ex if e.get("stage") in ("event", "identity", "format", "pricing", "doubles")]
    return {"run_id": p.get("run_id"), "git_sha": p.get("git_sha"), "generated_at": p.get("generated_at"),
            "projected": len(rows), "projected_singles": len(singles), "projected_doubles": len(doubles),
            "not_projected_hard": len(hard), "projectable_open_pregame": len(rows) + len(hard),
            "identity_excluded_markets": len(ident), "identity_kinds": dict(kinds),
            "doubles_excluded_markets": sum(1 for e in ex if e.get("stage") == "doubles"),
            "unresolved_singles_players": len(unmapped_names),
            "v2_grades": dict(Counter((r.get("v2") or {}).get("grade") for r in singles if r.get("family") == "MATCH_WINNER")),
            "quality_grades": dict(Counter((r.get("quality") or {}).get("grade") for r in rows)),
            "alias_review_queue": len(p.get("alias_review_queue") or []),
            "coverage": p.get("coverage"),
            "coefficients_fingerprints": sorted({(r.get("v2") or {}).get("coefficients_fingerprint") for r in rows if r.get("v2")} - {None}),
            "spec_fingerprints": sorted({(r.get("v2") or {}).get("spec_fingerprint") for r in rows if r.get("v2")} - {None})}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", required=True)
    ap.add_argument("--after", required=True)
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    pb, pa = json.load(open(a.before)), json.load(open(a.after))
    sb, sa = stats(pb), stats(pa)
    al = json.load(open(os.path.join(PROJ, "data", "identity", "reviewed_aliases.json")))
    acc = [x for x in al.get("crosswalk_aliases") or [] if x.get("review_status") == "ACCEPTED"]
    acc_ids = {(x["tour"], x["canonical_id"]): x for x in acc}
    dec = json.load(open(os.path.join(PROJ, "research", "projection_v2", "ALIAS_REVIEW_DECISION.json")))
    unresolved = {(d["tour"], normalize_name(d["foreign_name"])): d for d in dec["decisions"] if d["decision"] != "ACCEPTED"}
    states = {t: json.load(open(os.path.join(a.data_root, "processed", f"ratings_{t}.json"))) for t in ("ATP", "WTA")}
    m = pd.read_parquet(os.path.join(a.data_root, "processed", "matches.parquet"),
                        columns=["tour", "tourney_date", "tourney_name", "level_canonical", "round", "surface", "canonical_winner_id",
                                 "canonical_loser_id", "winner_name", "loser_name", "canonical_id_status", "id_system"])
    m = m[m.canonical_id_status == "MAPPED"]
    before_rows = {r["ticker"]: r for r in pb.get("projections") or []}
    live = []
    for r in pa.get("projections") or []:
        if r.get("family") != "MATCH_WINNER" or "|" in str(r.get("player_a_id")):
            continue
        for side, pid, opp, oid in (("A", r["player_a_id"], r["player_b"], r["player_b_id"]), ("B", r["player_b_id"], r["player_a"], r["player_a_id"])):
            x = acc_ids.get((r["tour"], str(pid)))
            if not x:
                continue
            st = states[r["tour"]]["players"].get(str(pid), {})
            mm = m[(m.tour == r["tour"]) & ((m.canonical_winner_id == str(pid)) | (m.canonical_loser_id == str(pid)))].sort_values("tourney_date")
            recent = [f"{t.tourney_date} {t.tourney_name} {t.round} {'W' if t.canonical_winner_id == str(pid) else 'L'} v "
                      f"{t.loser_name if t.canonical_winner_id == str(pid) else t.winner_name} [{t.id_system}]"
                      for t in mm.tail(5).itertuples(index=False)]
            p_now = r["models"].get("PRODUCTION")
            b = before_rows.get(r["ticker"])
            p_before = (b or {}).get("models", {}).get("PRODUCTION")
            mid = r["models"].get("MARKET_MID")
            p_side = p_now if side == "A" else (None if p_now is None else 1 - p_now)
            fair_yes = r["v2"].get("fair_yes") if r.get("v2") else None
            gap = None if (fair_yes is None or mid is None) else round(100 * (fair_yes - mid), 1)
            live.append({"ticker": r["ticker"], "event": r["event_ticker"], "tour": r["tour"], "level": r["level"],
                         "competition": r.get("competition"), "round": r.get("round"), "surface": r.get("surface"),
                         "alias": f"{x['foreign_system']}/{x['foreign_id']} {x['foreign_name']!r}",
                         "canonical_id": str(pid), "kalshi_name": r["player_a"] if side == "A" else r["player_b"],
                         "registry_name": st.get("name"), "rated_matches": st.get("n"), "elo": round(st.get("elo", 0), 1),
                         "last_result": st.get("last_date"), "opponent": opp, "opponent_id": oid,
                         "recent_results": recent, "rows_by_source": {k: int(v) for k, v in mm["id_system"].value_counts().items()},
                         "p_win_after": None if p_side is None else round(p_side, 4),
                         "p_production_before": p_before, "p_production_after": p_now,
                         "dp_pp": None if (p_before is None or p_now is None) else round(100 * (p_now - p_before), 1),
                         "v2_grade": (r.get("v2") or {}).get("grade"), "v2_tags": (r.get("v2") or {}).get("tags"),
                         "quality_grade": (r.get("quality") or {}).get("grade"),
                         "model_market_gap_pp": gap, "gap_over_20pp": gap is not None and abs(gap) > 20,
                         "quote_freshness": r["market_quote"].get("quote_freshness")})
    unresolved_live = []
    for e in pa.get("excluded") or []:
        if e.get("stage") != "identity":
            continue
        tour = "WTA" if ("WTA" in e["ticker"] or "ITFW" in e["ticker"]) else "ATP"
        for part in e["reason"].split("; "):
            k = (tour, normalize_name(part.split(": ")[0]))
            if k in unresolved:
                unresolved_live.append({"ticker": e["ticker"], "name": part.split(": ")[0], "decision": unresolved[k]["decision"]})
    # any market whose probability changed materially on the same ticker
    moved = []
    for t, r in ((r["ticker"], r) for r in pa.get("projections") or []):
        b = before_rows.get(t)
        if b and r.get("family") == "MATCH_WINNER" and r["models"].get("PRODUCTION") is not None and b["models"].get("PRODUCTION") is not None:
            d = r["models"]["PRODUCTION"] - b["models"]["PRODUCTION"]
            if abs(d) >= 0.05:
                moved.append({"ticker": t, "players": f"{r['player_a']} v {r['player_b']}", "ids": [r["player_a_id"], r["player_b_id"]],
                              "dp_pp": round(100 * d, 1), "involves_alias": any((r["tour"], str(i)) in acc_ids for i in (r["player_a_id"], r["player_b_id"]))})
    res = {"before": sb, "after": sa, "accepted_aliases": len(acc),
           "accepted_alias_canonicals_live": sorted({x["canonical_id"] for x in live}),
           "live_alias_rows": live, "unresolved_names_live": unresolved_live, "material_moves_ge_5pp": moved}
    md = ["| | before | after |", "|---|---|---|"]
    for k in ("run_id", "git_sha", "projectable_open_pregame", "projected", "projected_singles", "projected_doubles",
              "not_projected_hard", "identity_excluded_markets", "unresolved_singles_players", "doubles_excluded_markets",
              "alias_review_queue", "v2_grades", "identity_kinds", "coefficients_fingerprints"):
        md.append(f"| {k} | {sb.get(k)} | {sa.get(k)} |")
    md += ["", f"Accepted aliases whose player is on the after board: {len(res['accepted_alias_canonicals_live'])} players, "
           f"{len(live)} match-winner rows; rows with a > 20 pp model-market gap: {sum(1 for x in live if x['gap_over_20pp'])}; "
           f"markets moved >= 5 pp vs the before board: {len(moved)}."]
    res["markdown"] = "\n".join(md)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(res, open(a.out, "w"), indent=1, default=str)
    print(res["markdown"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
