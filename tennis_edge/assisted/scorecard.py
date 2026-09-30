"""The assisted-handicapping scorecard and the CEO scoreboard (Parts 9 and 10).

The PRIMARY UNIT is the recorded decision (and, for money, the reported wager). Raw model observations
never enter: a thousand shadow-board rows cannot outvote one decision here, because they are not read.

Populations
-----------
* HEADLINE decisions: fingerprint intact, not a confirmed post-start decision, not recorded after the
  first ball. Everything else is counted and reported as excluded, never silently dropped.
* A metric is reported with its N. Below CEO_MIN_N the CEO answer is INSUFFICIENT_EVIDENCE whatever the
  sign of the number, and no answer ever says "profitable" unless the 95% interval of the relevant mean
  excludes zero. The bootstrap uses the confirmation layer's fixed seed, so a rebuild on the same inputs
  reproduces every number (Part 15: scorecard reproducibility).
"""
from __future__ import annotations

import json
import math
import os
from collections import defaultdict
from datetime import datetime, timezone

from tennis_edge.confirmation.stats import mean_ci, paired_ci

from . import AUTONOMOUS_REAL_MONEY_AUTHORITY, CHATGPT_ASSISTED_TRACK, TRACK_NAME
from .schema import (AGREED_WITH_MODEL, AGREEMENT_STATES, FACTOR_TAGS, LEVEL_BUCKETS, MARKET_EXPRESSIONS,
                     MODEL_AND_CHATGPT_BOTH_PASS, OVERRULED_MODEL, SURFACE_BUCKETS)
from .settle import latest_settlements
from .store import RecordStore, canonical_hash, load_track_start

SCORECARD_VERSION = "assisted_scorecard_v1"
CEO_MIN_N = 30
#: "ChatGPT followed the model": an AGREED bet whose ChatGPT probability is within this of the model's
MODEL_FOLLOW_TOLERANCE = 0.02


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def _brier(p, y):
    return (p - y) ** 2


def _r(x, n=5):
    return round(x, n) if isinstance(x, float) and not math.isnan(x) else x


def _ci(xs):
    c = mean_ci(xs)
    return {k: _r(c[k]) for k in ("n", "mean", "median", "ci_low", "ci_high", "excludes_zero")}


def _group_stats(rows) -> dict:
    """N, settled, strict CLV and unit P&L of a group of joined decision rows."""
    settled = [r for r in rows if r["settlement"] and r["settlement"].get("net_pnl") is not None]
    clv = [r["settlement"]["strict_executable_clv"] for r in rows
           if r["settlement"] and r["settlement"].get("strict_executable_clv") is not None]
    units = [r["units_pnl"] for r in settled if r["units_pnl"] is not None]
    wager_net = [s["net_pnl"] for r in rows for s in r["wager_settlements"] if s.get("net_pnl") is not None]
    return {"n": len(rows), "settled": len(settled), "strict_clv_n": len(clv), "strict_clv": _ci(clv),
            "unit_net_per_contract": _r(_mean([r["settlement"]["net_pnl"] for r in settled])),
            "units_pnl": _r(sum(units)) if units else 0.0,
            "wins": sum(1 for r in settled if r["settlement"].get("side_won") is True),
            "losses": sum(1 for r in settled if r["settlement"].get("side_won") is False),
            "actual_wager_net_pnl": _r(sum(wager_net)) if wager_net else 0.0}


def _join(store_root: str):
    store = RecordStore(store_root)
    decisions = store.records("decisions")
    wagers = [w for w in store.records("wagers") if w.get("_fingerprint_ok")]
    sets = latest_settlements(store_root)
    by_dec_w = defaultdict(list)
    for w in wagers:
        by_dec_w[w["decision_id"]].append(w)
    rows, excluded = [], defaultdict(int)
    for d in decisions:
        if not d.get("_fingerprint_ok"):
            excluded["integrity_violation"] += 1
            continue
        s = sets.get(("DECISION", d["decision_id"], None))
        if s and s.get("post_start_violation"):
            excluded["post_start_decision"] += 1
            continue
        if any(str(w).startswith("RECORDED_AFTER_FIRST_BALL") for w in d.get("warnings") or []):
            excluded["recorded_after_first_ball"] += 1
            continue
        roi = (s or {}).get("roi")
        stake = d.get("stake_units_if_bet") or 0.0
        rows.append({"d": d, "settlement": s,
                     "units_pnl": (roi * stake) if (roi is not None and d["decision"] == "BET") else None,
                     "wagers": by_dec_w.get(d["decision_id"], []),
                     "wager_settlements": [sets[("WAGER", d["decision_id"], w["wager_id"])]
                                           for w in by_dec_w.get(d["decision_id"], [])
                                           if ("WAGER", d["decision_id"], w["wager_id"]) in sets]})
    return decisions, wagers, sets, rows, dict(excluded)


def _brier_block(rows) -> dict:
    """Brier of every forecaster on the SAME settled binary decisions (paired where both exist)."""
    out = {}
    fc = {"chatgpt": "chatgpt_fair_probability", "model": "model_probability_yes", "kalshi_mid": "kalshi_mid",
          "external": "external_consensus", "gen1": "gen1_probability", "gen2": "gen2_probability",
          "fair_v1": "fair_v1_probability", "model4": "model4_probability_if_applicable"}
    sett = [r for r in rows if r["settlement"] and r["settlement"].get("outcome_yes") in (0, 1)]
    for name, key in fc.items():
        pairs = [(r["d"].get(key), r["settlement"]["outcome_yes"]) for r in sett if isinstance(r["d"].get(key), (int, float))]
        out[name] = {"n": len(pairs), "brier": _r(_mean([_brier(p, y) for p, y in pairs]))}
    for name, key in fc.items():
        if name == "kalshi_mid":
            continue
        a, b = [], []
        for r in sett:
            p, k = r["d"].get(key), r["d"].get("kalshi_mid")
            if isinstance(p, (int, float)) and isinstance(k, (int, float)):
                y = r["settlement"]["outcome_yes"]
                a.append(_brier(p, y)); b.append(_brier(k, y))
        c = paired_ci(a, b)
        out[f"{name}_minus_kalshi"] = {"n": c["n"], "mean_brier_diff": _r(c["mean"]), "ci_low": _r(c["ci_low"]),
                                       "ci_high": _r(c["ci_high"]), "note": "negative = better calibrated than Kalshi on these rows"}
    return out


def build_scorecard(store_root: str, *, now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    track = load_track_start(store_root)
    decisions, wagers, sets, rows, excluded = _join(store_root)
    bets = [r for r in rows if r["d"]["decision"] == "BET"]
    passes = [r for r in rows if r["d"]["decision"] == "PASS"]
    watches = [r for r in rows if r["d"]["decision"] == "WATCH"]

    # ---- actual wagers (money): the person's own reported fills
    live_w = [w for w in wagers if w["status"] in ("FILLED", "PARTIAL_FILL", "VOIDED_BY_EXCHANGE")]
    wset = [sets[("WAGER", w["decision_id"], w["wager_id"])] for w in live_w if ("WAGER", w["decision_id"], w["wager_id"]) in sets]
    stake = sum(w["stake_dollars"] for w in live_w)
    settled_cost = sum((s.get("stake_dollars") or 0) + (s.get("fees") or 0) for s in wset)
    net = sum(s["net_pnl"] for s in wset)
    wager_clv = [s["strict_executable_clv"] for s in wset if s.get("strict_executable_clv") is not None]
    actual = {"number": len(live_w), "settled": len(wset), "open": len(live_w) - len(wset),
              "stake_dollars": _r(stake, 2), "fees_dollars": _r(sum(s.get("fees") or 0 for s in wset), 2),
              "wins": sum(1 for s in wset if s.get("side_won") is True),
              "losses": sum(1 for s in wset if s.get("side_won") is False),
              "pushes_voids": sum(1 for s in wset if s.get("side_won") is None),
              "net_pnl_dollars": _r(net, 2), "roi": _r(net / settled_cost) if settled_cost else None,
              "net_pnl_per_wager": _ci([s["net_pnl"] for s in wset]),
              "strict_executable_clv": _ci(wager_clv),
              "cancelled_not_counted": sum(1 for w in wagers if w["status"] == "CANCELLED")}

    # ---- pricing (decision unit: BET decisions)
    bclv = [r["settlement"]["strict_executable_clv"] for r in bets if r["settlement"] and r["settlement"].get("strict_executable_clv") is not None]
    bmid = [r["settlement"]["midpoint_clv"] for r in bets if r["settlement"] and r["settlement"].get("midpoint_clv") is not None]
    settled_bets = [r for r in bets if r["settlement"] and r["settlement"].get("net_pnl") is not None]
    pricing = {"unit": "BET decisions, one contract of the decision's side at its executable price",
               "strict_executable_clv": _ci(bclv),
               "strict_clv_coverage": _r(len(bclv) / len(settled_bets)) if settled_bets else None,
               "mean_midpoint_clv": _r(_mean(bmid)), "midpoint_clv_n": len(bmid)}

    # ---- selective disagreement, agreement, overrides, model follow
    mat = [r for r in bets if r["d"].get("material_disagreement_with_kalshi")]
    agree = [r for r in bets if r["d"]["model_agreement_state"] == AGREED_WITH_MODEL]
    follow = [r for r in agree if isinstance(r["d"].get("model_probability_yes"), (int, float))
              and isinstance(r["d"].get("chatgpt_fair_probability"), (int, float))
              and abs(r["d"]["chatgpt_fair_probability"] - r["d"]["model_probability_yes"]) <= MODEL_FOLLOW_TOLERANCE]
    override = [r for r in bets if r["d"]["model_agreement_state"] == OVERRULED_MODEL]
    sel = _group_stats(mat)
    sel["brier_vs_kalshi"] = _brier_block(mat).get("chatgpt_minus_kalshi")

    # ---- passes: did the model's apparent edges we declined make or lose money?
    declined = [r for r in passes + watches if r["d"].get("model_preferred_side") in ("YES", "NO")]
    dsett = [r for r in declined if r["settlement"] and (r["settlement"].get("model_side_unit") or {}).get("net_pnl") is not None]
    pass_block = {"passes": len(passes), "watches": len(watches),
                  "passed_positive_model_edge": len(declined), "settled": len(dsett),
                  "hypothetical_model_side_net_per_contract": _ci([r["settlement"]["model_side_unit"]["net_pnl"] for r in dsett]),
                  "hypothetical_model_side_strict_clv": _ci([r["settlement"].get("model_side_strict_executable_clv") for r in dsett
                                                             if r["settlement"].get("model_side_strict_executable_clv") is not None]),
                  "both_pass": sum(1 for r in passes + watches if r["d"]["model_agreement_state"] == MODEL_AND_CHATGPT_BOTH_PASS),
                  "note": "negative hypothetical P&L on declined model edges = passing them helped"}

    def by(key_fn, keys):
        out = {}
        for k in keys:
            g = [r for r in bets if key_fn(r) == k]
            if g:
                out[k] = _group_stats(g)
        return out
    factors = {}
    for t in FACTOR_TAGS:
        g = [r for r in bets if t in (r["d"].get("factor_tags") or [])]
        if g:
            factors[t] = _group_stats(g)
    body = {
        "scorecard_version": SCORECARD_VERSION, "track": TRACK_NAME,
        "AUTONOMOUS_REAL_MONEY_AUTHORITY": AUTONOMOUS_REAL_MONEY_AUTHORITY,
        "CHATGPT_ASSISTED_TRACK": CHATGPT_ASSISTED_TRACK,
        "track_effective_start": (track or {}).get("effective_start"),
        "primary_unit": "the recorded decision; money questions use the person's reported wagers",
        "evidence_state": "NO_DECISIONS_YET" if not decisions else ("NO_SETTLED_DECISIONS" if not any(r["settlement"] for r in rows) else "ACCUMULATING"),
        "total_decisions": {"recorded": len(decisions), "headline": len(rows), "bets": len(bets), "passes": len(passes),
                            "watches": len(watches), "excluded": excluded},
        "actual_wagers": actual,
        "pricing": pricing,
        "probability_quality": _brier_block(rows),
        "selective_disagreement": sel,
        "agreement": _group_stats(agree),
        "overrides": _group_stats(override),
        "model_follow": _group_stats(follow),
        "by_agreement_state": by(lambda r: r["d"]["model_agreement_state"], AGREEMENT_STATES),
        "passes": pass_block,
        "expression": by(lambda r: r["d"]["chosen_expression"], MARKET_EXPRESSIONS),
        "factors": factors,
        "level": by(lambda r: r["d"]["level_bucket"], LEVEL_BUCKETS),
        "surface": by(lambda r: r["d"]["surface_bucket"], SURFACE_BUCKETS),
        "confidence": by(lambda r: r["d"].get("chatgpt_confidence"), ("LOW", "MEDIUM", "HIGH")),
    }
    body["ceo"] = ceo_scoreboard(body)
    body["inputs_sha256"] = canonical_hash([[d.get("fingerprint") for d in decisions], [w.get("fingerprint") for w in wagers],
                                            sorted((str(k), v.get("fingerprint")) for k, v in sets.items())])
    body["content_sha256"] = canonical_hash(body)
    body["generated_at"] = now.isoformat()
    return body


def _answer(n, ci, *, positive_means, negative_means) -> str:
    if n < CEO_MIN_N or not ci or ci.get("mean") is None:
        return f"INSUFFICIENT_EVIDENCE (n={n}, need {CEO_MIN_N})"
    tail = f"mean {ci['mean']:+.4f}, 95% CI [{ci['ci_low']:+.4f}, {ci['ci_high']:+.4f}], n={n}"
    if ci.get("excludes_zero") and ci["mean"] > 0:
        return f"{positive_means}: {tail}"
    if ci.get("excludes_zero") and ci["mean"] < 0:
        return f"{negative_means}: {tail}"
    return f"NOT_DISTINGUISHABLE_FROM_ZERO: {tail}"


def ceo_scoreboard(s: dict) -> list[dict]:
    aw, pr, pq = s["actual_wagers"], s["pricing"], s["probability_quality"]
    ck = pq.get("chatgpt_minus_kalshi") or {}
    q = []
    q.append({"q": "1. Are ChatGPT-assisted bets profitable after fees?",
              "a": _answer(aw["settled"], aw["net_pnl_per_wager"], positive_means="PROFITABLE_SO_FAR",
                           negative_means="LOSING"),
              "net_pnl_dollars": aw["net_pnl_dollars"], "roi": aw["roi"]})
    q.append({"q": "2. Is strict executable CLV positive?",
              "a": _answer(pr["strict_executable_clv"]["n"], pr["strict_executable_clv"], positive_means="POSITIVE",
                           negative_means="NEGATIVE")})
    q.append({"q": "3. Are our probabilities better calibrated than Kalshi on the bets we select?",
              "a": _answer(ck.get("n") or 0, {"mean": ck.get("mean_brier_diff"), "ci_low": ck.get("ci_low"),
                                              "ci_high": ck.get("ci_high"),
                                              "excludes_zero": (ck.get("ci_low") is not None and (ck["ci_low"] > 0 or ck["ci_high"] < 0))},
                           positive_means="WORSE_THAN_KALSHI", negative_means="BETTER_THAN_KALSHI")})
    mk = pq.get("model_minus_kalshi") or {}
    q.append({"q": "4. Does using model information improve our decisions?",
              "a": (f"INSUFFICIENT_EVIDENCE (n={ck.get('n') or 0})" if (ck.get("n") or 0) < CEO_MIN_N else
                    f"ChatGPT Brier {pq['chatgpt']['brier']} vs model {pq['model']['brier']} vs Kalshi {pq['kalshi_mid']['brier']} "
                    f"on the same decisions (model-Kalshi diff {mk.get('mean_brier_diff')}); descriptive, not causal")})
    ag, ov = s["agreement"], s["overrides"]
    comp = (f"agreement n={ag['n']} CLV {ag['strict_clv']['mean']} units {ag['units_pnl']}; "
            f"overrides n={ov['n']} CLV {ov['strict_clv']['mean']} units {ov['units_pnl']}")
    enough = min(ag["settled"], ov["settled"]) >= CEO_MIN_N
    q.append({"q": "5. Do model-agreement bets outperform model-overrides?",
              "a": comp if enough else f"INSUFFICIENT_EVIDENCE ({comp})"})
    q.append({"q": "6. Are overrides adding value?",
              "a": _answer(ov["strict_clv_n"], ov["strict_clv"], positive_means="POSITIVE_CLV",
                           negative_means="NEGATIVE_CLV")})
    inputs = sorted(((k, pq[f"{k}_minus_kalshi"]) for k in ("gen1", "gen2", "fair_v1", "model4", "external")
                     if pq.get(f"{k}_minus_kalshi", {}).get("n")), key=lambda kv: kv[1]["mean_brier_diff"])
    q.append({"q": "7. Which model inputs appear most useful?",
              "a": ("; ".join(f"{k}: Brier-Kalshi {v['mean_brier_diff']:+.4f} (n={v['n']})" for k, v in inputs)
                    if inputs and max(v["n"] for _, v in inputs) >= CEO_MIN_N else
                    f"INSUFFICIENT_EVIDENCE (largest n={max((v['n'] for _, v in inputs), default=0)})")})
    fam = {k: v for k, v in s["expression"].items() if v["settled"] >= CEO_MIN_N}
    q.append({"q": "8. Which market families are most profitable?",
              "a": ("; ".join(f"{k}: units {v['units_pnl']} (n={v['settled']})" for k, v in
                              sorted(fam.items(), key=lambda kv: -kv[1]["units_pnl"])) if fam else
                    "INSUFFICIENT_EVIDENCE: " + (", ".join(f"{k} n={v['settled']}" for k, v in s["expression"].items()) or "no bets"))})
    harm = [f"{dim}:{k} units {v['units_pnl']} (n={v['settled']})" for dim in ("level", "surface")
            for k, v in s[dim].items() if v["settled"] >= CEO_MIN_N and v["units_pnl"] < 0]
    q.append({"q": "9. Which levels/surfaces are harmful?",
              "a": "; ".join(harm) if harm else f"NONE_IDENTIFIED_AT_MIN_N_{CEO_MIN_N}"})
    ps = s["passes"]
    q.append({"q": "10. Does the model help us PASS bad apparent edges?",
              "a": _answer(ps["settled"], ps["hypothetical_model_side_net_per_contract"],
                           positive_means="NO: the model edges we declined made money",
                           negative_means="YES: the model edges we declined lost money")})
    return q


# ---------------------------------------------------------------------------------------------- render
def render_markdown(s: dict) -> str:
    L = [f"# Assisted handicapping scorecard ({s['generated_at'][:16]}Z)", "",
         f"**AUTONOMOUS_REAL_MONEY_AUTHORITY = {s['AUTONOMOUS_REAL_MONEY_AUTHORITY']} · "
         f"CHATGPT_ASSISTED_TRACK = {s['CHATGPT_ASSISTED_TRACK']}** · track start "
         f"{s['track_effective_start'] or 'not yet fixed (the first production RUN TENNIS writes it)'} · "
         f"evidence state **{s['evidence_state']}**", "",
         "Primary unit: the recorded decision (money: the person's reported wagers). Nothing below is a finding "
         f"until its N clears {CEO_MIN_N} and its 95% interval excludes zero.", "",
         "## CEO scoreboard", ""]
    for x in s["ceo"]:
        L.append(f"* **{x['q']}** {x['a']}")
    t, a, p = s["total_decisions"], s["actual_wagers"], s["pricing"]
    L += ["", "## Decisions", "",
          f"recorded {t['recorded']} · headline {t['headline']} · BET {t['bets']} · PASS {t['passes']} · WATCH {t['watches']} · "
          f"excluded {json.dumps(t['excluded'])}", "",
          "## Actual wagers", "",
          f"number {a['number']} (settled {a['settled']}, open {a['open']}) · stake ${a['stake_dollars']} · wins {a['wins']} · "
          f"losses {a['losses']} · pushes/voids {a['pushes_voids']} · net P&L ${a['net_pnl_dollars']} · ROI {a['roi']}", "",
          "## Pricing (BET decisions)", "",
          f"strict executable CLV: {json.dumps(p['strict_executable_clv'])} · coverage {p['strict_clv_coverage']} · "
          f"mean midpoint CLV {p['mean_midpoint_clv']} (n={p['midpoint_clv_n']})", "",
          "## Probability quality (Brier, same settled decisions)", "",
          "| forecaster | n | Brier |", "|---|---|---|"]
    for k in ("chatgpt", "model", "kalshi_mid", "external", "gen1", "gen2", "fair_v1", "model4"):
        v = s["probability_quality"][k]
        L.append(f"| {k} | {v['n']} | {v['brier']} |")

    def table(title, d):
        out = ["", f"## {title}", "", "| group | n | settled | strict CLV n | mean strict CLV | units P&L | W-L | actual $ |",
               "|---|---|---|---|---|---|---|---|"]
        for k, v in d.items():
            out.append(f"| {k} | {v['n']} | {v['settled']} | {v['strict_clv_n']} | {v['strict_clv']['mean']} | "
                       f"{v['units_pnl']} | {v['wins']}-{v['losses']} | {v['actual_wager_net_pnl']} |")
        if not d:
            out.append("| (none yet) | | | | | | | |")
        return out
    L += table("Selective disagreement vs agreement vs overrides",
               {"material disagreement with Kalshi": s["selective_disagreement"], "agreed with model": s["agreement"],
                "overrode model": s["overrides"], "followed model (within 2pp)": s["model_follow"]})
    ps = s["passes"]
    L += ["", "## Passes", "", f"PASS {ps['passes']} · WATCH {ps['watches']} · declined positive-model-edge rows "
          f"{ps['passed_positive_model_edge']} (settled {ps['settled']}) · hypothetical model-side net/contract "
          f"{json.dumps(ps['hypothetical_model_side_net_per_contract'])} · both pass {ps['both_pass']}"]
    L += table("By market expression", s["expression"])
    L += table("By factor tag", s["factors"])
    L += table("By level", s["level"])
    L += table("By surface", s["surface"])
    L += table("By ChatGPT confidence", s["confidence"])
    L += ["", f"inputs sha256 `{s['inputs_sha256'][:16]}` · content sha256 `{s['content_sha256'][:16]}`", ""]
    return "\n".join(L)


def write_scorecard(s: dict, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "SCORECARD.json"), "w") as f:
        json.dump(s, f, indent=1, default=str)
    with open(os.path.join(out_dir, "SCORECARD.md"), "w") as f:
        f.write(render_markdown(s))
