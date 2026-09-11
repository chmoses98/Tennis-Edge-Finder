#!/usr/bin/env python3
"""Settlement, strict pregame classification, canonical close and CLV v2.

Never edits a ledger row. Everything here is DERIVED and written to separate, versioned tables, so that
first-ball truth recovered days later changes a label without rewriting a single historical byte:

  data/research/timing/<run>.jsonl       one row per ledger row: STRICT_PREGAME | POST_START |
                                         AMBIGUOUS | START_UNKNOWN, with the truth confidence, the
                                         derivation version and the classifier version that produced it
  data/research/clv/<run>.jsonl          CLV v2 records, strict flag and exclusion reason on every row
  data/research/horizons/<run>.jsonl     canonical decision horizons relative to the ACTUAL first ball
  data/research/settlements/<run>.jsonl  exchange/sports settlement (unchanged in spirit, extended)
  data/research/segments/coverage.json   the segmented COVERAGE schema for the next research wave

Nothing is dropped. Rows that cannot be classified are kept and labelled; that is the difference between
a research record and a highlight reel.
"""
from __future__ import annotations

import argparse
import glob
import gzip
import json
import os
import sys
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.eval.metrics import summary                                   # noqa: E402
from tennis_edge.firstball.classify import classify, STRICT_PREGAME            # noqa: E402
from tennis_edge.firstball.horizons import horizon_quotes                      # noqa: E402
from tennis_edge.firstball.store import FirstBallStore                         # noqa: E402
from tennis_edge.ledger.close import Quote, canonical_close                    # noqa: E402
from tennis_edge.ledger.clv import clv_record                                  # noqa: E402
from tennis_edge.ledger.predictions import PredictionLedger                    # noqa: E402
from tennis_edge.ledger.quotes import quotes_from_capture                      # noqa: E402
from tennis_edge.ledger.truth import ExchangeTruth, SportsTruth                # noqa: E402
from tennis_edge.pricing.fees import FeeSchedule                               # noqa: E402

SEGMENT_KEYS = ("tour", "level", "family", "surface", "discipline", "timing_class", "truth_confidence",
                "close_basis", "data_quality_grade", "spread_bucket", "liquidity_bucket",
                "time_to_first_ball_bucket", "implied_prob_bucket", "favourite_side", "disagreement_bucket")


def _ts(x):
    if isinstance(x, str) and x:
        try:
            return datetime.fromisoformat(x.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


def load_stream(kind):
    out = []
    for f in sorted(glob.glob(os.path.join(PROJ, "data", "kalshi", "capture", "*", f"*.{kind}*.jsonl.gz"))):
        with gzip.open(f, "rt") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        out.append(json.loads(line))
                    except ValueError:
                        continue
    return out


def _bucket(v, edges, labels, none_label="UNKNOWN"):
    if v is None:
        return none_label
    try:
        v = float(v)                      # capture records carry some numeric fields as strings
    except (TypeError, ValueError):
        return none_label
    for e, lab in zip(edges, labels):
        if v <= e:
            return lab
    return labels[-1]


def segment_of(row: dict) -> dict:
    sp, lq = row.get("entry_spread"), row.get("entry_depth")
    return {
        "tour": row.get("tour") or "UNKNOWN",
        "level": row.get("level") or "UNKNOWN",
        "family": row.get("family") or "UNKNOWN",
        "surface": row.get("surface") or "UNKNOWN",
        "discipline": "doubles" if row.get("doubles") else "singles",
        "timing_class": row.get("timing_class") or "START_UNKNOWN",
        "truth_confidence": row.get("truth_confidence") or "UNKNOWN",
        "close_basis": row.get("close_basis") or "NONE",
        "data_quality_grade": row.get("data_quality_grade") or "UNKNOWN",
        "spread_bucket": _bucket(sp, [0.02, 0.05, 0.10], ["<=2c", "<=5c", "<=10c", ">10c"]),
        "liquidity_bucket": _bucket(lq, [10, 100, 1000], ["<=10", "<=100", "<=1000", ">1000"]),
        "time_to_first_ball_bucket": _bucket(row.get("seconds_entry_to_first_ball"),
                                             [900, 3600, 10800, 21600], ["<=15m", "<=1h", "<=3h", "<=6h", ">6h"]),
        "implied_prob_bucket": _bucket(row.get("market_mid_at_entry"),
                                       [0.1, 0.25, 0.5, 0.75, 0.9], ["<=10%", "<=25%", "<=50%", "<=75%", "<=90%", ">90%"]),
        "favourite_side": ("FAVOURITE" if (row.get("market_mid_at_entry") or 0) > 0.5 else "UNDERDOG")
                          if row.get("market_mid_at_entry") is not None else "UNKNOWN",
        "disagreement_bucket": _bucket(abs(row["model_market_disagreement"]) if row.get("model_market_disagreement") is not None else None,
                                       [0.02, 0.05, 0.10], ["<=2pp", "<=5pp", "<=10pp", ">10pp"]),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=os.path.join(PROJ, "data", "research", "ledger"))
    ap.add_argument("--firstball-store", default=os.path.join(PROJ, "data", "firstball", "store"))
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"))
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "research"))
    a = ap.parse_args()

    rows = list(PredictionLedger(a.ledger).rows()) if os.path.isdir(a.ledger) else []
    truths = FirstBallStore(a.firstball_store).latest_truths() if os.path.isdir(a.firstball_store) else {}
    tickers = {r["ticker"] for r in rows}
    qmap = quotes_from_capture(a.capture, tickers) if os.path.isdir(a.capture) else {}
    settlements = {s["ticker"]: s for s in load_stream("settlements")}
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    for sub in ("timing", "clv", "horizons", "settlements", "segments"):
        os.makedirs(os.path.join(a.out, sub), exist_ok=True)

    done = set()
    for f in glob.glob(os.path.join(a.out, "settlements", "*.jsonl")):
        for line in open(f):
            try:
                done.add(json.loads(line)["prediction_id"])
            except ValueError:
                pass

    timing_rows, clv_rows, horizon_rows, settled = [], [], [], []
    for r in rows:
        mid, tk = r["match_id"], r["ticker"]
        truth = truths.get(mid)
        gen = _ts(r["generated_at_utc"])
        timing = classify(gen, truth)
        timing_rows.append({"run_id": run_id, "prediction_id": r["prediction_id"], "match_id": mid, "ticker": tk,
                            "generated_at_utc": r["generated_at_utc"], **timing.to_dict(),
                            "first_ball_lower_utc": truth.lower_bound_utc.isoformat() if (truth and truth.lower_bound_utc) else None,
                            "first_ball_upper_utc": truth.upper_bound_utc.isoformat() if (truth and truth.upper_bound_utc) else None,
                            "contradiction_status": truth.contradiction_status if truth else "NONE",
                            "scheduled_start": r.get("scheduled_start"), "legacy_start_basis": r.get("start_basis")})

        qs = qmap.get(tk, [])
        cc = canonical_close(qs, truth)
        dq = r.get("market_quote") or {}
        entry = Quote(gen, dq.get("yes_bid"), dq.get("yes_ask"),
                      yes_bid_size=dq.get("liquidity"), yes_ask_size=dq.get("liquidity"),
                      no_bid=dq.get("no_bid"), no_ask=dq.get("no_ask"))
        fs = FeeSchedule(fee_type=(r.get("fee_type") or "quadratic"))
        rec = clv_record(prediction_id=r["prediction_id"], ticker=tk, match_id=mid, family=r["family"],
                         entry=entry, close=cc, truth=truth, timing=timing, tour=r.get("tour", ""),
                         level=r.get("level", ""), model_prob=(r.get("models") or {}).get("ELO_DP_FAIR"),
                         data_quality_grade=(r.get("quality") or {}).get("grade", ""), fee_schedule=fs)
        d = rec.to_dict()
        d.update(run_id=run_id, surface=r.get("surface"), doubles=bool(r.get("doubles")),
                 n_quotes=cc.n_quotes_considered, n_executable=cc.n_executable_considered)
        clv_rows.append(d)

        for h in horizon_quotes(qs, truth):
            horizon_rows.append({"run_id": run_id, "prediction_id": r["prediction_id"], "match_id": mid,
                                 "ticker": tk, **h.to_dict()})

        if r["prediction_id"] in done or tk not in settlements:
            continue
        s = settlements[tk]
        ex = ExchangeTruth.from_market({**s, "ticker": tk}, s.get("run_id", ""))
        if not ex.terminal:
            continue
        st = None
        if r["family"] == "MATCH_WINNER" and ex.binary:
            subj_won = ex.result == "yes"
            st = SportsTruth(mid, r["player_a_id"] if subj_won == (r["subject"] == r["player_a"]) else r["player_b_id"],
                             None, "COMPLETED", "", source="kalshi_result", confidence=0.9,
                             actual_first_ball_at=truth.actual_first_ball_at_utc if truth else None)
        settled.append({"prediction_id": r["prediction_id"], "ticker": tk, "family": r["family"],
                        "generated_at_utc": r["generated_at_utc"], "exchange": ex.to_dict(),
                        "sports": st.to_dict() if st else None, "gradeable": bool(ex.binary),
                        "y_yes": 1.0 if ex.result == "yes" else (0.0 if ex.result == "no" else None),
                        "fair_yes": (r.get("models") or {}).get("ELO_DP_FAIR"),
                        "market_mid_at_decision": (r.get("models") or {}).get("MARKET_MID"),
                        "close": cc.to_dict(), "clv": d, "timing_class": timing.timing_class,
                        "truth_confidence": timing.truth_confidence, "settled_run": run_id})

    def write(sub, rows_):
        if rows_:
            with open(os.path.join(a.out, sub, f"{run_id}.jsonl"), "a") as f:
                for x in rows_:
                    f.write(json.dumps(x, default=str) + "\n")

    write("timing", timing_rows)
    write("clv", clv_rows)
    write("horizons", horizon_rows)
    write("settlements", settled)

    # ---------------- coverage scorecard: counts only, deliberately no performance by bucket yet
    seg_counts: dict[str, dict[str, dict]] = {k: {} for k in SEGMENT_KEYS}
    for d in clv_rows:
        seg = segment_of(d)
        for k in SEGMENT_KEYS:
            b = seg_counts[k].setdefault(seg[k], {"n": 0, "strict": 0, "with_close": 0, "with_clv": 0})
            b["n"] += 1
            b["strict"] += int(bool(d["strict"]))
            b["with_close"] += int(d["close_ts"] is not None)
            b["with_clv"] += int(d["clv_executable"] is not None)
    timing_counts: dict[str, int] = {}
    for t in timing_rows:
        timing_counts[t["timing_class"]] = timing_counts.get(t["timing_class"], 0) + 1
    coverage = {
        "run_id": run_id, "generated_at": datetime.now(timezone.utc).isoformat(),
        "ledger_rows": len(rows), "matches_with_truth": len(truths),
        "matches_with_strict_truth": sum(1 for t in truths.values() if t.strict_eligible),
        "timing_classes": timing_counts,
        "strict_pregame_observations": timing_counts.get(STRICT_PREGAME, 0),
        "executable_close_rows": sum(1 for d in clv_rows if d["close_ts"] is not None),
        "strict_clv_rows": sum(1 for d in clv_rows if d["strict"]),
        "contradictions": sum(1 for t in truths.values() if t.contradiction_status == "MATERIAL"),
        "horizons_populated": sum(1 for h in horizon_rows if h["populated"]),
        "horizons_total": len(horizon_rows),
        "segments": seg_counts,
        "authority": "RESEARCH_ONLY_NO_REAL_MONEY",
    }
    with open(os.path.join(a.out, "segments", "coverage.json"), "w") as f:
        json.dump(coverage, f, indent=1, default=str)

    # ---------------- human scorecard (unchanged discipline: no scores below 30 gradeable rows)
    allrows = []
    for f in sorted(glob.glob(os.path.join(a.out, "settlements", "*.jsonl"))):
        for line in open(f):
            try:
                allrows.append(json.loads(line))
            except ValueError:
                pass
    grad = [x for x in allrows if x.get("gradeable") and x.get("fair_yes") is not None and x.get("market_mid_at_decision") is not None]
    L = [f"# Prospective scorecard ({datetime.now(timezone.utc).isoformat()})", "",
         f"ledger rows: {len(rows)}; settled rows: {len(allrows)}; gradeable with market mid: {len(grad)}", "",
         "## First-ball truth coverage", "",
         f"| metric | value |", "|---|---|",
         f"| matches with any first-ball truth | {coverage['matches_with_truth']} |",
         f"| matches with STRICT-eligible truth (A/B) | {coverage['matches_with_strict_truth']} |",
         f"| STRICT_PREGAME observations | {timing_counts.get('STRICT_PREGAME', 0)} |",
         f"| POST_START observations | {timing_counts.get('POST_START', 0)} |",
         f"| AMBIGUOUS observations | {timing_counts.get('AMBIGUOUS', 0)} |",
         f"| START_UNKNOWN observations | {timing_counts.get('START_UNKNOWN', 0)} |",
         f"| rows with an executable close | {coverage['executable_close_rows']} |",
         f"| STRICT CLV rows | {coverage['strict_clv_rows']} |",
         f"| material contradictions | {coverage['contradictions']} |", ""]
    if len(grad) >= 30:
        import numpy as np
        y = np.array([x["y_yes"] for x in grad]); pm = np.array([x["fair_yes"] for x in grad])
        mk = np.array([x["market_mid_at_decision"] for x in grad])
        L += ["## Forecast accuracy", "", "| forecaster | n | brier | log_loss | cal_slope |", "|---|---|---|---|---|"]
        for name, p in (("market mid at decision", mk), ("model fair", pm)):
            s = summary(y, p)
            L.append(f"| {name} | {s['n']} | {s['brier']:.4f} | {s['log_loss']:.4f} | {s['cal_slope']:.3f} |")
        strict_clv = [x["clv"]["clv_executable"] for x in grad
                      if x.get("clv") and x["clv"].get("strict") and x["clv"].get("clv_executable") is not None]
        L += ["", f"STRICT executable CLV rows: {len(strict_clv)}"
              + (f"; mean {np.mean(strict_clv):+.4f}" if len(strict_clv) >= 30 else
                 " (fewer than 30: no CLV mean reported, multiple-testing discipline)")]
    else:
        L.append("Fewer than 30 gradeable settled predictions: no scores reported (multiple-testing discipline).")
    open(os.path.join(a.out, "settlements", "SCORECARD.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    print(f"timing rows {len(timing_rows)}; clv rows {len(clv_rows)}; horizons {len(horizon_rows)}; newly settled {len(settled)}")


if __name__ == "__main__":
    main()
