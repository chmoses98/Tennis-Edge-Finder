#!/usr/bin/env python3
"""What happened after we flagged a dislocation.

Two questions, in order of how quickly they can be answered:

1. **Did Kalshi move toward the external reference?** Answerable within hours, from the ledger itself,
   because the scan re-observes every ticker every pass. If an independent venue's disagreement carries
   information, the Kalshi price should drift toward it before the match starts. If it does not, the
   disagreement is noise or the two venues simply price differently.
2. **Who was right?** Answerable only at settlement, and reported separately when outcomes exist.

Both are MONITORING. This script does not tune anything, and the confirmation period is not a period
during which rules may be changed.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJ)


def _iso(x):
    try:
        return datetime.fromisoformat(str(x).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def boot_ci(x, n_boot=4000, seed=20260915):
    import numpy as np
    x = np.asarray([v for v in x if v is not None], float)
    if len(x) < 3:
        return [None, None]
    rng = np.random.default_rng(seed)
    m = x[rng.integers(0, len(x), size=(n_boot, len(x)))].mean(axis=1)
    return [round(float(np.percentile(m, 2.5)), 5), round(float(np.percentile(m, 97.5)), 5)]


def load(root):
    rows = []
    for f in sorted(glob.glob(os.path.join(root, "*.jsonl"))):
        for line in open(f):
            if line.strip():
                rows.append(json.loads(line))
    return rows


def follow_ups(rows, min_gap_min=20.0):
    """For each observation, the SAME ticker's Kalshi mid at least `min_gap_min` later."""
    by_ticker = defaultdict(list)
    for r in rows:
        t = _iso(r.get("generated_at"))
        if t and r.get("kalshi_mid") is not None:
            by_ticker[r["kalshi_ticker"]].append((t, r))
    for v in by_ticker.values():
        v.sort(key=lambda x: x[0])
    out = []
    for tk, seq in by_ticker.items():
        for i, (t, r) in enumerate(seq):
            if r.get("external_fair") is None:
                continue
            later = next(((t2, r2) for t2, r2 in seq[i + 1:]
                          if (t2 - t) >= timedelta(minutes=min_gap_min)), None)
            if not later:
                continue
            t2, r2 = later
            gap = (t2 - t).total_seconds() / 60.0
            move = r2["kalshi_mid"] - r["kalshi_mid"]
            gapsign = 1.0 if r["external_fair"] > r["kalshi_mid"] else -1.0
            out.append({**r, "follow_up_minutes": gap, "kalshi_move": move,
                        "move_toward_external": gapsign * move,
                        "kalshi_mid_later": r2["kalshi_mid"],
                        "closed_gap_fraction": (gapsign * move) / max(abs(r["external_fair"] - r["kalshi_mid"]), 1e-9)})
    return out


def describe(rows, label):
    if not rows:
        return {"subset": label, "n": 0}
    d = [r["external_vs_kalshi"] for r in rows if r.get("external_vs_kalshi") is not None]
    e = [r["external_edge"] for r in rows if r.get("external_edge") is not None]
    out = {"subset": label, "n": len(rows)}
    if d:
        out.update({"ext_vs_kalshi_median": round(st.median(d), 5),
                    "ext_vs_kalshi_mean": round(st.mean(d), 5),
                    "ext_vs_kalshi_p90_abs": round(sorted(abs(x) for x in d)[int(0.9 * (len(d) - 1))], 5),
                    "share_over_2c": round(sum(1 for x in d if abs(x) > 0.02) / len(d), 4),
                    "share_over_5c": round(sum(1 for x in d if abs(x) > 0.05) / len(d), 4)})
    if e:
        out.update({"external_edge_median": round(st.median(e), 5),
                    "external_edge_max": round(max(e), 5),
                    "share_edge_over_2c": round(sum(1 for x in e if x >= 0.02) / len(e), 4)})
    mv = [r["move_toward_external"] for r in rows if r.get("move_toward_external") is not None]
    if mv:
        out.update({"n_with_follow_up": len(mv), "move_toward_external_mean": round(st.mean(mv), 5),
                    "move_toward_external_ci": boot_ci(mv),
                    "share_moved_toward": round(sum(1 for x in mv if x > 0) / len(mv), 4),
                    "median_follow_up_minutes": round(st.median(
                        [r["follow_up_minutes"] for r in rows if r.get("follow_up_minutes")]), 1)})
    return out


def settlements(capture_root: str, discovery_root: str) -> dict:
    """{ticker: 1.0/0.0} for markets that have settled.

    NOT from the quote stream. The capture fetches the ACTIVE board, so a settled market simply stops
    appearing there and its result is never written into a capture file -- 30,961 captured quote rows
    across an evening contained exactly zero results, which is how this was found. Settlements live in
    the discovery snapshot's `historical_markets`, refreshed daily by the conductor. The capture is still
    scanned as a fallback in case that ever changes.
    """
    import gzip
    out = {}
    for f in sorted(glob.glob(os.path.join(discovery_root, "*", "historical_markets", "*.json"))
                    + sorted(glob.glob(os.path.join(discovery_root, "*", "markets", "*.json")))):
        try:
            obj = json.load(open(f))
        except (OSError, json.JSONDecodeError):
            continue
        for blk in (obj.values() if isinstance(obj, dict) and "markets" not in obj else [obj]):
            if not isinstance(blk, dict):
                continue
            for m in blk.get("markets") or []:
                if m.get("result") in ("yes", "no"):
                    out[m["ticker"]] = 1.0 if m["result"] == "yes" else 0.0
    for f in sorted(glob.glob(os.path.join(capture_root, "*", "*.quotes.jsonl.gz"))):
        with gzip.open(f, "rt") as fh:
            for line in fh:
                if not line.strip():
                    continue
                m = json.loads(line)
                if m.get("result") in ("yes", "no"):
                    out[m["ticker"]] = 1.0 if m["result"] == "yes" else 0.0
    return out


def accuracy(rows, settled: dict) -> dict:
    """Who was closer to the truth: the external venue, Kalshi, or us. First observation per contract."""
    seen, recs = set(), []
    for r in sorted(rows, key=lambda x: x["generated_at"]):
        tk = r["kalshi_ticker"]
        if tk in seen or tk not in settled or r.get("external_fair") is None:
            continue
        seen.add(tk)
        recs.append((settled[tk], r))
    if not recs:
        return {"n": 0, "note": "no observed contract has settled yet"}
    def brier(get):
        vals = [(get(r) - y) ** 2 for y, r in recs if get(r) is not None]
        return (round(st.mean(vals), 5), len(vals)) if vals else (None, 0)
    b_ext, n_ext = brier(lambda r: r["external_fair"])
    b_kal, n_kal = brier(lambda r: r["kalshi_mid"])
    b_mod, n_mod = brier(lambda r: r.get("model_fair"))
    paired = [((r["external_fair"] - y) ** 2) - ((r["kalshi_mid"] - y) ** 2) for y, r in recs]
    paired_model = [((r["model_fair"] - y) ** 2) - ((r["kalshi_mid"] - y) ** 2)
                    for y, r in recs if r.get("model_fair") is not None]
    return {"n": len(recs), "external_brier": b_ext, "kalshi_brier": b_kal, "model_brier": b_mod,
            "n_model": n_mod,
            "external_minus_kalshi": round(st.mean(paired), 5), "external_minus_kalshi_ci": boot_ci(paired),
            "model_minus_kalshi": round(st.mean(paired_model), 5) if paired_model else None,
            "model_minus_kalshi_ci": boot_ci(paired_model) if paired_model else [None, None]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=os.path.join(PROJ, "data", "research", "external", "dislocations"))
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "external_market"))
    ap.add_argument("--min-gap-min", type=float, default=20.0)
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"),
                    help="capture root; scanned for settlements only as a fallback")
    ap.add_argument("--discovery", default=os.path.join(PROJ, "data", "kalshi", "discovery"),
                    help="discovery root: where settled results actually live")
    a = ap.parse_args()
    rows = load(a.ledger)
    if not rows:
        print("::warning::no dislocation rows on disk")
        return 0
    fu = follow_ups(rows, a.min_gap_min)
    fu_by_key = {(r["kalshi_ticker"], r["generated_at"]): r for r in fu}
    merged = [fu_by_key.get((r["kalshi_ticker"], r["generated_at"]), r) for r in rows]
    withref = [r for r in merged if r.get("external_fair") is not None]

    res = {"generated_at": datetime.now(timezone.utc).isoformat(),
           "rows": len(rows), "rows_with_reference": len(withref),
           "distinct_tickers": len({r["kalshi_ticker"] for r in rows}),
           "distinct_matches": len({r["physical_match_id"] for r in rows}),
           "window": [min(r["generated_at"] for r in rows), max(r["generated_at"] for r in rows)],
           "decisions": {k: sum(1 for r in rows if r["decision"] == k)
                         for k in ("PASS", "WATCH", "SHADOW_BET")},
           "triangulation": {}, "overall": describe(withref, "all rows with a reference"),
           "by_triangulation": [], "scorecards": {}}
    for cls in sorted({r["triangulation"] for r in merged}):
        sub = [r for r in merged if r["triangulation"] == cls]
        res["triangulation"][cls] = len(sub)
        res["by_triangulation"].append(describe([r for r in sub if r.get("external_fair") is not None], cls))

    # monitoring scorecards. Reported, never acted on during the confirmation period.
    for name, keyfn in (("by_day", lambda r: r["generated_at"][:10]),
                        ("by_week", lambda r: _iso(r["generated_at"]).strftime("%G-W%V")),
                        ("by_tour", lambda r: r["physical_match_id"].split(":")[0]),
                        ("by_family", lambda r: r["market_family"])):
        buckets = defaultdict(list)
        for r in withref:
            buckets[keyfn(r)].append(r)
        res["scorecards"][name] = [describe(v, k) for k, v in sorted(buckets.items())]

    settled = settlements(a.capture if os.path.isdir(a.capture) else "",
                          a.discovery if os.path.isdir(a.discovery) else "")
    res["settled_contracts_seen"] = len(settled)
    res["accuracy"] = accuracy(withref, settled)
    res["accuracy_kalshi_outlier"] = accuracy(
        [r for r in withref if r["triangulation"] == "KALSHI_LONE_OUTLIER"], settled)
    res["accuracy_model_outlier"] = accuracy(
        [r for r in withref if r["triangulation"] == "MODEL_LONE_OUTLIER"], settled)

    os.makedirs(a.out, exist_ok=True)
    json.dump(res, open(os.path.join(a.out, "scorecard.json"), "w"), indent=1, default=str)

    L = ["# External dislocation scorecard", "",
         f"{res['rows']} observations over {res['distinct_matches']} matches "
         f"({res['distinct_tickers']} contracts), {res['window'][0][:16]}Z to {res['window'][1][:16]}Z. "
         f"**Monitoring only.** Nothing here authorises a rule change.", "",
         f"Decisions: " + ", ".join(f"{k} {v}" for k, v in res["decisions"].items()), "",
         "## How far apart are the two venues", "",
         "| subset | n | median ext-Kalshi | mean | share >2c | share >5c | median edge after fees | share edge >=2c |",
         "|---|---|---|---|---|---|---|---|"]
    for s in [res["overall"]] + res["by_triangulation"]:
        if not s.get("n"):
            continue
        L.append(f"| {s['subset']} | {s['n']} | {s.get('ext_vs_kalshi_median', float('nan')):+.4f} | "
                 f"{s.get('ext_vs_kalshi_mean', float('nan')):+.4f} | {s.get('share_over_2c', 0):.3f} | "
                 f"{s.get('share_over_5c', 0):.3f} | {s.get('external_edge_median', float('nan')):+.4f} | "
                 f"{s.get('share_edge_over_2c', 0):.3f} |")
    L += ["", "## Did Kalshi move toward the external reference", "",
          "| subset | n | mean move toward | 95% CI | share moved toward | median gap (min) |",
          "|---|---|---|---|---|---|"]
    for s in [res["overall"]] + res["by_triangulation"]:
        if not s.get("n_with_follow_up"):
            continue
        L.append(f"| {s['subset']} | {s['n_with_follow_up']} | {s['move_toward_external_mean']:+.5f} | "
                 f"[{s['move_toward_external_ci'][0]}, {s['move_toward_external_ci'][1]}] | "
                 f"{s['share_moved_toward']:.3f} | {s['median_follow_up_minutes']:.0f} |")
    acc = res["accuracy"]
    if acc.get("n"):
        L += ["", "## Who was right, where contracts have settled", "",
              f"{acc['n']} settled contracts, first observation of each.", "",
              "| forecaster | Brier |", "|---|---|",
              f"| Kalshi mid | {acc['kalshi_brier']} |",
              f"| external reference | {acc['external_brier']} |",
              f"| our frozen model | {acc['model_brier']} |", "",
              f"External minus Kalshi: **{acc['external_minus_kalshi']:+.5f}** "
              f"CI [{acc['external_minus_kalshi_ci'][0]}, {acc['external_minus_kalshi_ci'][1]}]. "
              + (f"Model minus Kalshi: **{acc['model_minus_kalshi']:+.5f}** "
                 f"CI [{acc['model_minus_kalshi_ci'][0]}, {acc['model_minus_kalshi_ci'][1]}]."
                 if acc.get("model_minus_kalshi") is not None else "")]
    else:
        L += ["", "## Who was right", "", "No observed contract has settled yet."]
    open(os.path.join(a.out, "SCORECARD.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
