#!/usr/bin/env python3
"""LIVE_VERIFICATION.md + live shadow comparison from a production RUN TENNIS's published outputs.

Usage: live_report.py --data-root <dir holding research/ and app/> --run-url <actions run url>
Reads research/projections/<latest run>.json, research/health_latest.json, research/assisted_slates/latest.json,
app/latest/model_prices.json. Writes research/projection_v2/LIVE_VERIFICATION.md and live_shadow_comparison.json.
"""
from __future__ import annotations

import argparse, collections, glob, json, os

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-root", required=True)
    ap.add_argument("--run-url", default="")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    R = os.path.join(a.data_root, "research")
    latest = json.load(open(os.path.join(R, "projections", "latest.json")))
    run = json.load(open(os.path.join(R, "projections", f"{latest['run_id']}.json")))
    health = json.load(open(os.path.join(R, "health_latest.json")))
    rows = run["projections"]
    mw = [r for r in rows if r["family"] == "MATCH_WINNER" and r.get("subject") == r.get("player_a") and r.get("v2") and "p_a" in (r["v2"] or {})]
    fresh = collections.Counter((r["market_quote"] or {}).get("quote_freshness") for r in rows)
    grades = collections.Counter((r["level"], r["v2"]["grade"]) for r in mw)
    big = [r for r in mw if r["models"].get("MARKET_MID") is not None and abs(r["models"]["V2"] - r["models"]["MARKET_MID"]) > 0.20]
    diffs = [abs(r["models"]["V2"] - r["models"]["INCUMBENT"]) for r in mw if r["models"].get("INCUMBENT") is not None]
    L = ["# Live verification (production RUN TENNIS after the merge)", "",
         f"Run: {a.run_url or '(local)'} -- projection run `{run['run_id']}`, git `{run['git_sha'][:10]}`, production model "
         f"`{run.get('production_model')}`.", "", a.note, "",
         "## Coverage and lifecycle", "", "```json", json.dumps(run["coverage"], indent=1), "```", "",
         f"Lifecycle: `{json.dumps(run.get('lifecycle'))}`", "", f"Quote freshness of priced rows: {dict(fresh)}", "",
         f"Projection V2 status: `{json.dumps({k: v for k, v in (run.get('projection_v2') or {}).items() if k != 'data_horizon'})}`", "",
         f"Data horizons: `{json.dumps((run.get('projection_v2') or {}).get('data_horizon'))}`", "",
         "## V2 vs incumbent on the live board (shadow comparison)", "",
         f"{len(mw)} singles match-winner events. Mean |V2 - incumbent| = {sum(diffs) / max(1, len(diffs)):.3f}; "
         f"max {max(diffs) if diffs else 0:.3f}. Grades by level: {dict(grades)}.", "",
         "| match | level | V2 | envelope | grade | incumbent | Kalshi mid | quote | tags |", "|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(mw, key=lambda r: (r["level"], r["player_a"]))[:80]:
        v, m, q = r["v2"], r["models"], r["market_quote"]
        L.append(f"| {r['player_a']} v {r['player_b']} | {r['level']} | {m['V2']:.3f} | {v['envelope_low_yes']:.2f}-{v['envelope_high_yes']:.2f} | "
                 f"{v['grade']} | {m['INCUMBENT']:.3f} | {m['MARKET_MID'] if m['MARKET_MID'] is None else round(m['MARKET_MID'], 3)} | "
                 f"{q.get('quote_freshness')} | {', '.join(v['tags'])} |")
    L += ["", f"## Model-market disagreements > 20pp ({len(big)})", "",
          "Each one is listed with the evidence behind the model number; none was used to change the model.", ""]
    for r in big:
        v = r["v2"]
        L.append(f"* **{r['player_a']} v {r['player_b']}** ({r['competition']}, {r['level']}): V2 {r['models']['V2']:.3f} "
                 f"[{v['envelope_low_yes']:.2f}, {v['envelope_high_yes']:.2f}] grade {v['grade']}, Kalshi mid {r['models']['MARKET_MID']:.3f} "
                 f"(quote {r['market_quote'].get('quote_freshness')}), tags {v['tags']}; evidence {json.dumps(v['evidence'])}")
    L += ["", "## Health", "", "| gate | status |", "|---|---|"] + [f"| {g['gate']} {g['name']} | {g['status']} |" for g in health]
    mp_path = os.path.join(a.data_root, "app", "latest", "model_prices.json")
    if os.path.exists(mp_path):
        mp = json.load(open(mp_path))
        items = mp if isinstance(mp, list) else (mp.get("items") or mp.get("model_prices") or [])
        src = collections.Counter((i.get("model_version") or "").split(" ")[0] for i in items)
        L += ["", "## App export (edge_finder.app.v1)", "", f"model_prices by source: {dict(src)}"]
    open(os.path.join(OUT, "LIVE_VERIFICATION.md"), "w").write("\n".join(L) + "\n")
    json.dump({"run_id": run["run_id"], "n_events": len(mw), "grades": {f"{k[0]}|{k[1]}": v for k, v in grades.items()},
               "mean_abs_v2_minus_incumbent": sum(diffs) / max(1, len(diffs)),
               "events": [{"match": f"{r['player_a']} v {r['player_b']}", "level": r["level"], "v2": r["models"]["V2"],
                           "incumbent": r["models"]["INCUMBENT"], "market_mid": r["models"]["MARKET_MID"], "grade": r["v2"]["grade"],
                           "envelope": [r["v2"]["envelope_low_yes"], r["v2"]["envelope_high_yes"]]} for r in mw]},
              open(os.path.join(OUT, "live_shadow_comparison.json"), "w"), indent=1)
    print("wrote LIVE_VERIFICATION.md", len(mw), "events,", len(big), "big gaps")


if __name__ == "__main__":
    main()
