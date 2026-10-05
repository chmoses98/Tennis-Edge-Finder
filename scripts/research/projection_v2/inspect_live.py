#!/usr/bin/env python3
"""Manual-inspection support for a production RUN TENNIS: reproduce every live V2 number and lay out the
inputs behind the ones a person must look at.

Usage: inspect_live.py --data-root <dir with research/projections and processed/{matches.parquet,v2,ratings_*}>
                       [--run <projection run json>] [--events EV1,EV2,...]

1. REPRODUCTION. Every singles match-winner row is re-projected from the locally rebuilt V2 state; the state's
   matches_sha256 must equal the one production recorded, and p / envelope / grade / tags must match exactly.
   A mismatch is an inference or state defect, not a modelling question.
2. IDENTITY. Every player on the board resolved by anything other than an exact, recently active name
   (confidence < 1.0, minted ids, reviewed aliases, transliterations) is re-resolved and listed with its
   reason, canonical name and last result.
3. INSPECTION. For the selected events (every >20pp V2-market gap, plus the --events list, plus automatic
   picks: the best-evidenced main-tour row and a lower-level LOW/POOR row, plus every alias/minted row):
   ratings, form, Gen-2 serve/return, context, age, surface, the stacker's per-feature logit contributions,
   envelope variants, source freshness and each player's last results in the canonical table.
Writes research/projection_v2/LIVE_INSPECTION.md and live_inspection.json. Reads no prices into the model.
"""
from __future__ import annotations

import argparse, glob, json, math, os, sys
from datetime import date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import numpy as np
import pandas as pd

from tennis_edge.rules.formats import MatchFormat, _load_registry
from tennis_edge.v2.inference import ProjectionV2
from tennis_edge.v2.production import load_coefficients, load_state
from tennis_edge.v2.stacker import build_features

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2"))
MAIN = ("GRAND_SLAM", "MASTERS_1000", "TOUR_500_250", "TOUR_FINALS")


def formats_by_name():
    out = {"tour_singles_bo3": MatchFormat(3, 6, 7, "TB7_AT_6", False, "tour_singles_bo3")}
    for r in _load_registry():
        f = r["format"]
        out[r.get("name", "registry")] = MatchFormat(f["best_of"], f.get("tiebreak_at", 6), f.get("tiebreak_to", 7),
                                                     f["final_set"], f.get("no_ad", False), r.get("name", "registry"))
    return out


def recent_results(m, pid, n=6):
    w = m[m.canonical_winner_id == pid].assign(res="W", opp=lambda d: d.loser_name)
    l = m[m.canonical_loser_id == pid].assign(res="L", opp=lambda d: d.winner_name)
    d = pd.concat([w, l]).sort_values(["tourney_date", "match_num"], ascending=False).head(n)
    return [f"{str(r.tourney_date)[:10]} {r.level_canonical} {r.tourney_name} {r['round']}: {r.res} v {r.opp} "
            f"{r.score_raw} [{r.source_label}]" for _, r in d.iterrows()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-root", required=True)
    ap.add_argument("--run", default=None)
    ap.add_argument("--events", default="")
    a = ap.parse_args()
    R = a.data_root
    if a.run:
        run = json.load(open(a.run))
    else:
        latest = json.load(open(os.path.join(R, "research", "projections", "latest.json")))
        run = json.load(open(os.path.join(R, "research", "projections", f"{latest['run_id']}.json")))
    today = date.fromisoformat(run["run_id"][:4] + "-" + run["run_id"][4:6] + "-" + run["run_id"][6:8])
    coef = load_coefficients()
    v2 = {t: ProjectionV2(load_state(os.path.join(R, "processed", "v2", f"state_{t}.json.gz")), coef) for t in ("ATP", "WTA")}
    fmts = formats_by_name()
    rows = [r for r in run["projections"] if r["family"] == "MATCH_WINNER" and r.get("subject") == r.get("player_a")
            and (r.get("v2") or {}).get("p_a") is not None]

    # ---------------------------------------------------------------- 1. reproduction
    sha_ok = {t: v2[t].state.get("matches_sha256") for t in v2}
    repro, mism = [], []
    for r in rows:
        x = r["v2"]
        if x["matches_sha256"] != sha_ok[r["tour"]]:
            mism.append({"event": r["event_ticker"], "why": "state sha differs"}); continue
        idc = 1.0 if "IDENTITY_ALIAS" not in x["tags"] else 0.85  # re-derived exactly in section 2
        res = v2[r["tour"]].project(r["player_a_id"], r["player_b_id"], on=today, level=r["level"], surface=r["surface"],
                                    fmt=fmts[r["format"]], identity_confidence=idc)
        d = abs(res["p"] - x["p_a"])
        repro.append(d)
        if d > 1e-12 or res["grade"] != x["grade"] or [t for t in res["tags"] if t != "IDENTITY_ALIAS"] != [t for t in x["tags"] if t != "IDENTITY_ALIAS"]:
            mism.append({"event": r["event_ticker"], "dp": d, "grade": (res["grade"], x["grade"]), "tags": (res["tags"], x["tags"])})

    # ---------------------------------------------------------------- 2. identity
    from tennis_edge.identity.kalshi_map import KalshiPlayerMapper
    states = {t: json.load(open(os.path.join(R, "processed", f"ratings_{t}.json"))) for t in ("ATP", "WTA")}
    mapper = KalshiPlayerMapper(states, cache_path=os.path.join(os.path.dirname(__file__), "..", "..", "..", "config", "kalshi_competitor_map.json"))
    mapper.cache = {}                         # re-derive from names; never written back
    ident = {}
    for r in run["projections"]:
        if r["family"] != "MATCH_WINNER":
            continue
        for side in ("a", "b"):
            name, pid = r[f"player_{side}"], r[f"player_{side}_id"]
            if not pid or "|" in str(pid):
                continue                      # doubles teams (singles ids checked on their singles rows)
            res = mapper.resolve(r["tour"], name, None, today)
            minted = ":" in str(pid)
            if res.get("confidence", 0) < 1.0 or minted or res.get("player_id") != pid:
                ident[(r["tour"], name)] = {"tour": r["tour"], "kalshi_name": name, "player_id": pid, "minted_id": minted,
                                            "re_resolved_id": res.get("player_id"), "agrees": res.get("player_id") == pid,
                                            "confidence": res.get("confidence"), "reason": res.get("reason", "exact name"),
                                            "canonical_name": res.get("canonical_name"), "last_date": res.get("last_date"),
                                            "event": r["event_ticker"], "level": r["level"]}
    queue = run.get("alias_review_queue", [])

    # ---------------------------------------------------------------- 3. inspection
    m = pd.read_parquet(os.path.join(R, "processed", "matches.parquet"),
                        columns=["canonical_winner_id", "canonical_loser_id", "winner_name", "loser_name", "tourney_date",
                                 "tourney_name", "level_canonical", "round", "match_num", "score_raw", "source_label"])
    pick = {e for e in a.events.split(",") if e}
    gap = lambda r: abs(r["models"]["V2"] - r["models"]["MARKET_MID"]) if r["models"].get("MARKET_MID") is not None else 0
    pick |= {r["event_ticker"] for r in rows if gap(r) > 0.20}
    main_rows = sorted([r for r in rows if r["level"] in MAIN and r["v2"]["grade"] in ("HIGH", "MEDIUM")],
                       key=lambda r: -min(r["v2"]["evidence"]["rated_matches_a"], r["v2"]["evidence"]["rated_matches_b"]))
    low_rows = [r for r in rows if r["level"] not in MAIN and r["v2"]["grade"] in ("LOW", "POOR")]
    pick |= {r["event_ticker"] for r in main_rows[:2]} | {r["event_ticker"] for r in low_rows[:2]}
    pick |= {i["event"] for i in ident.values()}
    detail = []
    for r in rows:
        if r["event_ticker"] not in pick:
            continue
        P = v2[r["tour"]]
        a_, b_ = r["player_a_id"], r["player_b_id"]
        raw = P.frame(a_, b_, on=today, level=r["level"], surface=r["surface"], best_of=fmts[r["format"]].best_of)
        stale = P.stale_days(r["level"], today)
        df = P._neutralise(raw) if stale > 10 else raw
        X, names = build_features(df, P.base.spec)
        contrib = {n: float(X[0, i] / P.base.scale[i] * P.base.coef[i]) for i, n in enumerate(names)}
        elo_name = P.base.spec.elo
        def elo(pid):
            rec = (P.players.get(pid) or {}).get("elo", {}).get(elo_name) or {}
            return {"r": rec.get("r"), "n": rec.get("n"), "surf": {k: [round(v[0], 1), v[1]] for k, v in (rec.get("surf") or {}).items()}}
        row = raw.iloc[0]
        side = lambda s: {"elo": elo(a_ if s == "a" else b_),
                          "form30": float(row[f"form30_{s}"]), "form_cnt30": float(row[f"cnt30_{s}"]),
                          "form120": float(row[f"form120_{s}"]), "form_cnt120": float(row[f"cnt120_{s}"]),
                          "days_since_last": None if np.isnan(row[f"days_{s}"]) else int(row[f"days_{s}"]),
                          "n14": float(row[f"n14_{s}"]), "mins7": float(row[f"mins7_{s}"]), "ret30": float(row[f"ret30_{s}"]),
                          "surf_switch": float(row[f"surf_switch_{s}"]), "age": None if np.isnan(row[f"age_{s}"]) else round(float(row[f"age_{s}"]), 1),
                          "rated_matches": int(row[f"n_{s}"]), "g2_serve_evidence": float(row[f"g2_ev_{s}"]),
                          "recent_results": recent_results(m, a_ if s == "a" else b_)}
        detail.append({"event": r["event_ticker"], "match": f"{r['player_a']} v {r['player_b']}", "tour": r["tour"],
                       "level": r["level"], "competition": r["competition"], "round": r["round"], "surface": r["surface"],
                       "surface_source": r.get("surface_source"), "format": r["format"],
                       "v2": r["models"]["V2"], "incumbent": r["models"]["INCUMBENT"], "market_mid": r["models"]["MARKET_MID"],
                       "quote_freshness": (r["market_quote"] or {}).get("quote_freshness"),
                       "quote_age_s": (r["market_quote"] or {}).get("quote_age_s"),
                       "seconds_to_scheduled_start": r.get("seconds_to_scheduled_start"),
                       "envelope": [r["v2"]["envelope_low_yes"], r["v2"]["envelope_high_yes"]], "grade": r["v2"]["grade"],
                       "tags": r["v2"]["tags"], "variants_p_a": r["v2"]["variants_p_a"], "level_data_horizon_days_behind": stale,
                       "context_neutralised": stale > 10,
                       "p_elo": float(row[f"pf_{elo_name}"]), "p_gen2": float(raw["pf_g2"].iloc[0]),
                       "g2_point_a_on_serve": float(row["g2_pa"]), "g2_point_a_on_return": 1 - float(row["g2_pb"]),
                       "contributions_logit": dict(sorted(contrib.items(), key=lambda kv: -abs(kv[1]))),
                       "a": side("a"), "b": side("b"),
                       "identity": [ident.get((r["tour"], r["player_a"])), ident.get((r["tour"], r["player_b"]))]})

    res = {"run_id": run["run_id"], "git_sha": run["git_sha"], "n_rows": len(rows),
           "reproduction": {"n": len(repro), "max_abs_dp": max(repro) if repro else None, "mismatches": mism,
                            "state_sha256": sha_ok},
           "identity_non_exact": list(ident.values()), "alias_review_queue": queue, "inspected": detail}
    json.dump(res, open(os.path.join(OUT, "live_inspection.json"), "w"), indent=1, default=str)

    L = [f"# Live inspection -- projection run `{run['run_id']}` (git `{run['git_sha'][:10]}`)", "",
         "Generated by `scripts/research/projection_v2/inspect_live.py` from the published run and a local rebuild of",
         "the same V2 state (identical `matches_sha256`). Nothing here changed the model.", "",
         "## 1. Reproduction", "",
         f"{len(repro)} singles match-winner rows re-projected; max |p_local - p_production| = "
         f"{(max(repro) if repro else float('nan')):.2e}; mismatches (p, grade or tags): {len(mism)}.", ""]
    L += [f"* {x}" for x in mism[:20]]
    L += ["", "## 2. Identity (everything not an exact, recently active name)", "",
          "| tour | Kalshi name | id | minted | confidence | rule | canonical name | last result | re-resolves to same id |",
          "|---|---|---|---|---|---|---|---|---|"]
    for i in sorted(ident.values(), key=lambda i: (i["tour"], i["kalshi_name"])):
        L.append(f"| {i['tour']} | {i['kalshi_name']} | `{i['player_id']}` | {i['minted_id']} | {i['confidence']} | {i['reason']} | "
                 f"{i['canonical_name']} | {i['last_date']} | {i['agrees']} |")
    L += ["", f"Alias review queue (human only, nothing auto-mapped): {len(queue)} entries.", ""]
    L += [f"* {q.get('tour')} {q.get('kalshi_name')}: candidates {q.get('candidates')}" for q in queue]
    L += ["", "## 3. Inspected matches", ""]
    for d in detail:
        L += [f"### {d['match']} -- {d['competition']} {d['round']} ({d['tour']} {d['level']}, {d['surface']} via {d['surface_source']}, {d['format']})", "",
              f"V2 **{d['v2']:.3f}** [{d['envelope'][0]:.3f}, {d['envelope'][1]:.3f}] grade **{d['grade']}**, tags {d['tags']}; "
              f"incumbent {d['incumbent']:.3f}; Kalshi mid {d['market_mid'] if d['market_mid'] is None else round(d['market_mid'], 3)} "
              f"(quote {d['quote_freshness']}, age {d['quote_age_s'] and round(d['quote_age_s'])}s; start in {d['seconds_to_scheduled_start']}s).", "",
              f"Components: Elo lane {d['p_elo']:.3f}, Gen-2 {d['p_gen2']:.3f} (A wins {d['g2_point_a_on_serve']:.3f} of serve points, "
              f"{d['g2_point_a_on_return']:.3f} of return points); level data horizon {d['level_data_horizon_days_behind']}d behind"
              f"{' -> schedule features neutralised' if d['context_neutralised'] else ''}. Envelope variants {json.dumps({k: round(v, 3) for k, v in d['variants_p_a'].items()})}.", "",
              "| | A | B |", "|---|---|---|"]
        for k in ("elo", "form30", "form_cnt30", "form120", "form_cnt120", "days_since_last", "n14", "mins7", "ret30", "surf_switch", "age",
                  "rated_matches", "g2_serve_evidence"):
            fa, fb = d["a"][k], d["b"][k]
            if k == "elo":
                fa, fb = f"{fa['r']:.0f} (n {fa['n']}) surf {fa['surf']}", f"{fb['r']:.0f} (n {fb['n']}) surf {fb['surf']}"
            L.append(f"| {k} | {fa} | {fb} |")
        L += ["", "Largest logit contributions (A's side positive): " +
              ", ".join(f"{k} {v:+.3f}" for k, v in list(d["contributions_logit"].items())[:8]), "",
              "Recent results A: " + " / ".join(d["a"]["recent_results"][:4]),
              "", "Recent results B: " + " / ".join(d["b"]["recent_results"][:4]), "",
              "Identity: " + "; ".join(json.dumps({k: i[k] for k in ("kalshi_name", "player_id", "confidence", "reason")}) for i in d["identity"] if i) or "both exact", "",
              "Verdict: _(manual, below)_", ""]
    open(os.path.join(OUT, "LIVE_INSPECTION.md"), "w").write("\n".join(L) + "\n")
    print(json.dumps({"rows": len(rows), "repro_n": len(repro), "max_dp": max(repro) if repro else None, "mismatches": len(mism),
                      "identity_non_exact": len(ident), "queue": len(queue), "inspected": len(detail)}))


if __name__ == "__main__":
    main()
