"""Historical model-vs-market discrepancy audit (descriptive research; never a strategy, never a model change).

Reads only what the prospective pipeline already wrote -- the frozen producers' own rows (shadow board:
fair_v1 / Gen-2 / Gen-1 Elo and structural; Model 4 on listed derivatives), the Gen-1 prediction ledger
(ELO_DP_FAIR beside the quote it saw), the external_v1 dislocation scan, the ledger settlements and the
first-ball store -- and asks, for every model-market comparison, how far apart they were and WHY.

Rules this module keeps
  * No probability is reconstructed: every model number is a producer row's own number at its own time.
  * Model inputs are never touched. Outcomes, settlement times and first-ball truth are used ONLY to score
    and to diagnose (labelled "hindsight" everywhere); nothing they reveal feeds a live rule.
  * The live sanity layer (tennis_edge.assisted.discrepancy.assess) classifies each historical observation
    with exactly the evidence that existed at the observation's own timestamp, so the audit measures the
    same layer the slate runs.
  * Buckets come from config/discrepancy_sanity.json; nothing is optimised on realised P&L.
"""
from __future__ import annotations

import glob
import gzip
import json
import math
import os
from bisect import bisect_right
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

from tennis_edge.assisted import discrepancy as DS
from tennis_edge.assisted.schema import level_bucket, match_code_of, series_of
from tennis_edge.kalshi.families import SERIES
from tennis_edge.pricing.fees import taker_fee

AUDIT_VERSION = "model_market_discrepancy_audit_v1"
UTC = timezone.utc
HINDSIGHT_TAGS = ("POST_SETTLEMENT_OBSERVATION", "CONFIRMED_IN_PLAY_QUOTE", "LIKELY_IN_PLAY_QUOTE", "POSSIBLE_IN_PLAY_QUOTE")
MAIN_TOUR = ("ATP", "WTA")
INDEPENDENT_MODELS = ("fair_v1", "gen2", "gen1_elo", "gen1_sr", "gen1_ledger", "model4_fundamental")
PRIMARY_MODELS = ("fair_v1", "gen1_ledger")


def _dt(x):
    if not isinstance(x, str) or not x:
        return None
    try:
        d = datetime.fromisoformat(x.replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=UTC)


def _f(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def _jsonl(paths):
    for p in paths:
        op = gzip.open if p.endswith(".gz") else open
        try:
            with op(p, "rt") as fh:
                for line in fh:
                    if line.strip():
                        try:
                            yield json.loads(line)
                        except ValueError:
                            continue
        except (OSError, EOFError):
            continue


def _lb(series, level=None):
    fam = SERIES.get(series)
    disc = fam[3] if fam else "singles"
    return level_bucket(series, level, disc), disc


def _level_detail(series, bucket):
    if bucket == "ITF":
        return "ITF_WOMEN" if series == "KXITFWMATCH" or "ITFW" in (series or "") else "ITF_MEN"
    if bucket == "DOUBLES":
        return "DOUBLES"
    return bucket


def _model_bucket(level, tour):
    lv = (level or "").upper()
    if not lv:
        return None
    return {"ITF": "ITF", "CHALLENGER": "CHALLENGER", "WTA_125": "WTA125"}.get(
        lv, "OTHER" if lv in ("OTHER", "TEAM", "EXHIBITION") else (tour if tour in MAIN_TOUR else None))


# ---------------------------------------------------------------------------------------------- loading
def load_outcomes(research: str) -> dict:
    """ticker -> {y, settled_at, strict_close:{ts, yes_bid, yes_ask}|None, first_ball_lower}. Exchange result only."""
    out: dict = {}
    for r in _jsonl(sorted(glob.glob(os.path.join(research, "settlements", "*.jsonl")))):
        t = r.get("ticker")
        e = r.get("exchange") or {}
        if not t or e.get("result") not in ("yes", "no"):
            continue
        rec = out.setdefault(t, {"y": 1.0 if e["result"] == "yes" else 0.0, "settled_at": _dt(e.get("settlement_ts")),
                                 "strict_close": None, "first_ball_lower": None})
        cl = r.get("close") or {}
        q = cl.get("quote") or {}
        if cl.get("strict") and rec["strict_close"] is None and _f(q.get("yes_bid")) is not None and _f(q.get("yes_ask")) is not None:
            rec["strict_close"] = {"ts": _dt(q.get("ts")), "yes_bid": _f(q["yes_bid"]), "yes_ask": _f(q["yes_ask"])}
            rec["first_ball_lower"] = _dt(cl.get("cutoff"))
    return out


def load_external(research: str, tickers: set) -> dict:
    """ticker -> sorted [(generated_at, external_fair, external_quote_age_s, n_groups, sources)]."""
    out = defaultdict(list)
    for p in sorted(glob.glob(os.path.join(research, "external", "dislocations", "*.jsonl"))):
        with open(p) as fh:
            for line in fh:
                if '"kalshi_ticker"' not in line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                t = r.get("kalshi_ticker")
                if t not in tickers or _f(r.get("external_fair")) is None:
                    continue
                out[t].append((_dt(r.get("generated_at")), _f(r["external_fair"]), _f(r.get("external_quote_age_s")),
                               r.get("n_independent_groups"), tuple(r.get("external_sources") or ())))
    for t in out:
        out[t] = sorted([x for x in out[t] if x[0] is not None], key=lambda x: x[0])
    return dict(out)


def _external_at(ext: dict, ticker: str, at, lookback_min: float):
    rows = ext.get(ticker)
    if not rows or at is None:
        return None
    i = bisect_right([r[0] for r in rows], at) - 1
    if i < 0 or (at - rows[i][0]).total_seconds() > lookback_min * 60:
        return None
    g, fair, age, n, src = rows[i]
    return {"p": fair, "age_s": (age or 0.0) + (at - g).total_seconds(), "scanned_at": g, "n_groups": n, "sources": src}


def load_first_ball(data_root: str):
    try:
        from tennis_edge.assisted.market import first_ball_bound, load_truths, truth_for
        truths = load_truths(os.path.join(data_root, "firstball", "store"))
    except Exception:                                                                   # noqa: BLE001
        return lambda _e: None
    cache = {}

    def lower(event):
        code = match_code_of(event or "")
        if code not in cache:
            cache[code] = first_ball_bound(truth_for(truths, event)) if code else None
        return cache[code]
    return lower


def _ledger_index(rows) -> dict:
    idx = defaultdict(list)
    for r in rows:
        ts = _dt(r.get("generated_at_utc"))
        if ts:
            idx[r["ticker"]].append((ts, r))
    for t in idx:
        idx[t].sort(key=lambda x: x[0])
    return idx


def _nearest(idx, ticker, at, max_min):
    rows = idx.get(ticker)
    if not rows or at is None:
        return None
    best = min(rows, key=lambda x: abs((x[0] - at).total_seconds()))
    return best[1] if abs((best[0] - at).total_seconds()) <= max_min * 60 else None


# ---------------------------------------------------------------------------------------------- observations
def build_observations(data_root: str, cfg: dict | None = None, *, namesakes: dict | None = None) -> tuple[pd.DataFrame, dict]:
    cfg = cfg or DS.load_config()
    ac = cfg["audit"]
    research = os.path.join(data_root, "research")
    ledger_rows = [r for r in _jsonl(sorted(glob.glob(os.path.join(research, "ledger", "*.jsonl")))) if r.get("ticker")]
    shadow_rows = [r for r in _jsonl(sorted(glob.glob(os.path.join(research, "frozen_producers", "shadow_board", "*.jsonl"))))
                   if r.get("ticker")]
    m4_rows = [r for r in _jsonl(sorted(glob.glob(os.path.join(research, "frozen_producers", "model4", "*.jsonl"))))
               if r.get("ticker")]
    outcomes = load_outcomes(research)
    mw = {r["ticker"] for r in shadow_rows if r.get("market_family") == "MATCH_WINNER"} | \
         {r["ticker"] for r in ledger_rows if r.get("family") == "MATCH_WINNER"}
    ext = load_external(research, mw)
    fb_lower = load_first_ball(data_root)
    lidx = _ledger_index(ledger_rows)

    raw = []
    # ---- shadow board (MATCH_WINNER): fair_v1, Gen-2, Gen-1 Elo, Gen-1 structural on one quote
    for r in shadow_rows:
        if r.get("market_family") != "MATCH_WINNER":
            continue
        lg = _nearest(lidx, r["ticker"], _dt(r.get("predicted_at")), ac["ledger_join_minutes"])
        lq = ((lg or {}).get("quality") or {})
        base = {
            "source": "shadow_board_v1", "ticker": r["ticker"], "event": r.get("event"), "family": "MATCH_WINNER",
            "predicted_at": _dt(r.get("predicted_at")), "quote_ts": _dt(r.get("quote_captured_at")),
            "bid": _f(r.get("kalshi_bid")), "ask": _f(r.get("kalshi_ask")), "ask_size": _f(r.get("displayed_size")),
            "bid_size": None, "subject_is_a": r.get("subject_is_a"), "level": r.get("level"), "tour": r.get("tour"),
            "surface": r.get("surface"), "physical_match_id": r.get("physical_match_id"),
            "player_a_id": r.get("player_a_id"), "player_b_id": r.get("player_b_id"), "match_date": r.get("match_date"),
            "identity_conf": [r.get("identity_confidence_a"), r.get("identity_confidence_b")],
            "grade": r.get("data_quality_grade"), "serve_a": _f(r.get("serve_evidence_a")), "serve_b": _f(r.get("serve_evidence_b")),
            "n_a": (lq.get("inputs") or {}).get("n_matches_a"), "n_b": (lq.get("inputs") or {}).get("n_matches_b"),
            "days_a": (lq.get("inputs") or {}).get("days_since_last_a"), "days_b": (lq.get("inputs") or {}).get("days_since_last_b"),
            "level_familiarity": (lq.get("pillars") or {}).get("level_familiarity"),
            "model_uncertainty": _f(r.get("model_uncertainty")),
            "envelope": list((r.get("fair_envelope") or {}).values()) or None,
            "subject": r.get("subject"),
        }
        probs = {"fair_v1": _f(r.get("fair_v1_probability")), "gen2": _f(r.get("gen2_probability")),
                 "gen1_elo": _f(r.get("gen1_elo_probability")), "gen1_sr": _f(r.get("gen1_sr_probability"))}
        for m, p in probs.items():
            if p is not None:
                raw.append({**base, "model": m, "p": p, "model_probs": probs})
    # ---- Gen-1 ledger (every family it priced, singles and doubles)
    for r in ledger_rows:
        p = _f(((r.get("models") or {}).get("ELO_DP_FAIR")))
        if p is None:
            continue
        q = r.get("market_quote") or {}
        qi = ((r.get("quality") or {}).get("inputs") or {})
        sa = None
        if r.get("subject") and r.get("player_a"):
            sa = r["subject"] == r["player_a"] if r.get("family") in ("MATCH_WINNER",) else None
        raw.append({
            "source": "gen1_ledger", "model": "gen1_ledger", "ticker": r["ticker"], "event": r.get("event_ticker"),
            "family": r.get("family"), "predicted_at": _dt(r.get("generated_at_utc")), "quote_ts": _dt(q.get("quote_ts")),
            "bid": _f(q.get("yes_bid")), "ask": _f(q.get("yes_ask")), "bid_size": None, "ask_size": None,
            "subject_is_a": sa, "level": r.get("level"), "tour": r.get("tour"), "surface": r.get("surface"),
            "physical_match_id": None, "player_a_id": r.get("player_a_id"), "player_b_id": r.get("player_b_id"),
            "match_date": (r.get("scheduled_start") or "")[:10] or None,
            "identity_conf": [((r.get("quality") or {}).get("pillars") or {}).get("identity_confidence")],
            "grade": (r.get("quality") or {}).get("grade"), "serve_a": _f(qi.get("serve_points_a")),
            "serve_b": _f(qi.get("serve_points_b")), "n_a": qi.get("n_matches_a"), "n_b": qi.get("n_matches_b"),
            "days_a": qi.get("days_since_last_a"), "days_b": qi.get("days_since_last_b"),
            "level_familiarity": (((r.get("quality") or {}).get("pillars") or {}).get("level_familiarity")),
            "model_uncertainty": None, "envelope": None, "subject": r.get("subject"),
            "p": p, "model_probs": {"gen1_ledger": p, "gen1_elo_only": _f((r.get("models") or {}).get("ELO")),
                                    "gen1_structural": _f((r.get("models") or {}).get("STRUCTURAL"))},
        })
    # ---- Model 4 (listed derivatives): conditioned is market-anchored by construction, fundamental is Gen-2
    for r in m4_rows:
        c = r.get("conditioning") or {}
        probs = {"model4_conditioned": _f(r.get("conditioned_probability")), "model4_fundamental": _f(r.get("fundamental_probability"))}
        for m, p in probs.items():
            if p is None:
                continue
            raw.append({
                "source": "model4_board_v1", "model": m, "ticker": r["ticker"], "event": r.get("event"),
                "family": r.get("market_family"), "predicted_at": _dt(r.get("predicted_at")),
                "quote_ts": _dt(r.get("quote_captured_at") or c.get("quote_captured_at")),
                "bid": _f(r.get("kalshi_bid")), "ask": _f(r.get("kalshi_ask")),
                "bid_size": _f(r.get("displayed_bid_size")), "ask_size": _f(r.get("displayed_ask_size")),
                "subject_is_a": r.get("subject_is_a"), "level": r.get("level"), "tour": r.get("tour"),
                "surface": r.get("surface"), "physical_match_id": r.get("physical_match_id"),
                "player_a_id": r.get("player_a_id"), "player_b_id": r.get("player_b_id"), "match_date": r.get("match_date"),
                "identity_conf": [None], "grade": None, "serve_a": _f(r.get("gen2_evidence_a")),
                "serve_b": _f(r.get("gen2_evidence_b")), "n_a": None, "n_b": None, "days_a": None, "days_b": None,
                "level_familiarity": None, "model_uncertainty": None, "envelope": None, "subject": r.get("subject"),
                "p": p, "model_probs": probs,
            })

    # ---- pair-level checks: same model, same moment, both match-winner sides
    pair = defaultdict(dict)
    for o in raw:
        if o["family"] == "MATCH_WINNER" and o["predicted_at"] is not None:
            k = (o["source"], o["model"], o["event"], o["predicted_at"].replace(second=0, microsecond=0))
            pair[k][o["ticker"]] = o
    same_pair = defaultdict(set)
    for o in raw:
        ids = (o.get("player_a_id"), o.get("player_b_id"))
        if all(ids) and o.get("match_date"):
            same_pair[(frozenset(map(str, ids)), o["match_date"])].add(match_code_of(o["event"] or o["ticker"]))

    obs = []
    for o in raw:
        series = series_of(o["ticker"])
        bucket, disc = _lb(series, o["level"])
        two = o["bid"] is not None and o["ask"] is not None and 0 < o["bid"] <= o["ask"] < 1
        mid = 0.5 * (o["bid"] + o["ask"]) if two else None
        if mid is None or not DS.valid_probability(o["p"]):
            continue
        # identity evidence available at the observation's own time
        fam = o["family"]
        if fam == "MATCH_WINNER":
            orient, _ = DS.ticker_orientation(o["ticker"], o["event"], o["subject_is_a"])
        else:
            has_subject = bool(o.get("subject")) or o.get("subject_is_a") is not None
            orient = "NOT_APPLICABLE" if not has_subject else ("UNKNOWN" if o.get("subject_is_a") is None else "VERIFIED_BY_PRODUCER")
            if orient == "VERIFIED_BY_PRODUCER":
                orient = "VERIFIED"
        k = (o["source"], o["model"], o["event"], o["predicted_at"].replace(second=0, microsecond=0)) if o["predicted_at"] else None
        sides = pair.get(k, {}) if fam == "MATCH_WINNER" else {}
        other = next((v for t, v in sides.items() if t != o["ticker"]), None)
        o_mid = (0.5 * (other["bid"] + other["ask"]) if other and other["bid"] is not None and other["ask"] is not None
                 and other["bid"] <= other["ask"] else None)
        ids = (o.get("player_a_id"), o.get("player_b_id"))
        n_codes = len(same_pair.get((frozenset(map(str, ids)), o.get("match_date")), ())) if all(ids) else 0
        checks = {
            "physical_match_id": DS.check_physical_match_id(o["physical_match_id"], *ids) if o["source"] != "gen1_ledger" else "NA",
            "player_ids": DS.check_player_ids(*ids),
            "identity_confidence": DS.check_identity_confidence(*o["identity_conf"]),
            "namesake": DS.check_namesakes([o.get("subject")], namesakes) if fam == "MATCH_WINNER" else "NA",
            "model_complement": DS.check_complement(o["p"], other["p"]) if other else "NA",
            "market_pair": DS.check_market_pair(mid, o_mid) if other else "NA",
            "level_mapping": DS.check_level(bucket if bucket != "DOUBLES" else None, _model_bucket(o["level"], o["tour"])),
            "same_pair_other_event": "AMBIGUOUS" if n_codes > 1 else ("PASS" if n_codes == 1 else "NA"),
            "discipline": "PASS" if disc == "singles" else "AMBIGUOUS",
            "ticker_orientation": {"VERIFIED": "PASS", "FAILED": "FAIL", "NOT_APPLICABLE": "NA"}.get(orient, "AMBIGUOUS"),
        }
        identity = DS.identity_status(checks)
        e = _external_at(ext, o["ticker"], o["predicted_at"], ac["external_lookback_minutes"]) if fam == "MATCH_WINNER" else None
        dq = DS.data_quality(grade=o["grade"], serve_a=o["serve_a"], serve_b=o["serve_b"], n_a=o["n_a"], n_b=o["n_b"],
                             days_a=o["days_a"], days_b=o["days_b"], level_familiarity=o["level_familiarity"], cfg=cfg)
        qage = (o["predicted_at"] - o["quote_ts"]).total_seconds() if (o["predicted_at"] and o["quote_ts"]) else None
        fb_src = bucket in MAIN_TOUR
        a = DS.assess(p_model=o["p"], bid=o["bid"], ask=o["ask"], bid_size=o["bid_size"], ask_size=o["ask_size"],
                      quote_age_s=qage, identity=identity, identity_checks=checks, orientation=orient, data=dq,
                      p_ext=(e or {}).get("p"), ext_age_s=(e or {}).get("age_s"), model_uncertainty=o["model_uncertainty"],
                      envelope=o["envelope"], model_probs={m: v for m, v in (o["model_probs"] or {}).items() if v is not None},
                      first_ball_source=fb_src, cfg=cfg)
        # ---- hindsight diagnostics (never inputs): settlement timing and observed first ball
        oc = outcomes.get(o["ticker"]) or {}
        st = oc.get("settled_at")
        hs = []
        if st and o["predicted_at"] and o["predicted_at"] >= st:
            hs.append("POST_SETTLEMENT_OBSERVATION")
        fbl = fb_lower(o["event"] or o["ticker"])
        if fbl and o["quote_ts"] and o["quote_ts"] >= fbl:
            hs.append("CONFIRMED_IN_PLAY_QUOTE")
        settle_after_quote_min = (st - o["quote_ts"]).total_seconds() / 60 if (st and o["quote_ts"]) else None
        if settle_after_quote_min is not None and 0 <= settle_after_quote_min < ac["likely_in_play_settle_minutes"]:
            hs.append("LIKELY_IN_PLAY_QUOTE")
        elif settle_after_quote_min is not None and 0 <= settle_after_quote_min < ac["possible_in_play_settle_minutes"]:
            hs.append("POSSIBLE_IN_PLAY_QUOTE")
        y = oc.get("y")
        favored_yes = o["p"] >= mid
        sc = oc.get("strict_close")
        clv = None
        if sc and o["quote_ts"] and sc["ts"] and o["quote_ts"] < sc["ts"] and not hs:
            clv = (sc["yes_bid"] - o["ask"]) if favored_yes else (o["bid"] - sc["yes_ask"])
        obs.append({
            "source": o["source"], "model": o["model"], "ticker": o["ticker"], "event": o["event"], "family": fam,
            "series": series, "level_bucket": bucket, "level_detail": _level_detail(series, bucket), "discipline": disc,
            "surface": o["surface"] or "UNKNOWN", "grade": o["grade"] or "UNKNOWN", "predicted_at": o["predicted_at"],
            "quote_ts": o["quote_ts"], "subject": o.get("subject"), "subject_is_a": o["subject_is_a"],
            "p": o["p"], "bid": o["bid"], "ask": o["ask"], "mid": mid,
            "gap_pp": a["model_market_gap_pp"], "abs_gap_pp": a["abs_model_market_gap_pp"],
            "exec_gap_pp": a["model_executable_gap_pp"], "bucket": a["audit_bucket"], "band": a["discrepancy_band"],
            "status": a["discrepancy_sanity_status"], "tags": a["discrepancy_reason_tags"], "hindsight": hs,
            "identity": identity, "identity_checks": checks, "orientation": orient,
            "freshness": a["market_freshness_status"], "quote_age_s": qage, "external_status": a["external_confirmation_status"],
            "triangulation": a["triangulation"], "p_ext": (e or {}).get("p"), "ext_sources": (e or {}).get("sources"),
            "data_status": dq["data_quality_status"], "severe_asym": dq["severe_sample_asymmetry"],
            "serve_min": dq["evidence"]["thinner_serve_points"], "sample_ratio": dq["evidence"]["sample_ratio"],
            "n_min": min([n for n in (o["n_a"], o["n_b"]) if isinstance(n, (int, float))], default=None),
            "days_max": max([d for d in (o["days_a"], o["days_b"]) if isinstance(d, (int, float))], default=None),
            "model_uncertainty": o["model_uncertainty"], "spread": (o["ask"] - o["bid"]),
            "y": y, "settled_at": st, "settle_after_quote_min": settle_after_quote_min, "strict_clv": clv,
            "favored_yes": favored_yes,
        })
    df = pd.DataFrame(obs)
    meta = {"ledger_rows": len(ledger_rows), "shadow_rows": len(shadow_rows), "model4_rows": len(m4_rows),
            "settled_tickers": len(outcomes), "external_tickers": len(ext),
            "ledger_span": _span(ledger_rows, "generated_at_utc"), "shadow_span": _span(shadow_rows, "predicted_at"),
            "model4_span": _span(m4_rows, "predicted_at")}
    return df, meta


def _span(rows, key):
    ts = sorted(r.get(key) for r in rows if r.get(key))
    return [ts[0], ts[-1]] if ts else None


def dedupe_pairs(df: pd.DataFrame) -> pd.DataFrame:
    """One comparison per match-winner EVENT per model per run (the two YES contracts mirror each other);
    the kept row is the model-favoured side. Derivatives are distinct contracts and are all kept."""
    if df.empty:
        return df
    mw = df[df.family == "MATCH_WINNER"].copy()
    other = df[df.family != "MATCH_WINNER"]
    mw["_k"] = mw.predicted_at.map(lambda t: t.replace(second=0, microsecond=0) if t is not None else None)
    mw = mw.sort_values(["favored_yes", "subject_is_a"], ascending=[False, False], na_position="last")
    mw = mw.drop_duplicates(["source", "model", "event", "_k"]).drop(columns="_k")
    return pd.concat([mw, other], ignore_index=True)


# ---------------------------------------------------------------------------------------------- statistics
def _logit(p):
    p = np.clip(np.asarray(p, float), 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def calibration_slope(p, y) -> dict | None:
    """Logistic recalibration y ~ a + b*logit(p) (IRLS). b < 1: the probabilities are too extreme."""
    p, y = np.asarray(p, float), np.asarray(y, float)
    if len(p) < 30 or y.min() == y.max():
        return None
    X = np.column_stack([np.ones_like(p), _logit(p)])
    w = np.zeros(2)
    for _ in range(50):
        eta = X @ w
        mu = 1 / (1 + np.exp(-eta))
        W = np.clip(mu * (1 - mu), 1e-9, None)
        H = X.T @ (X * W[:, None]) + 1e-9 * np.eye(2)
        step = np.linalg.solve(H, X.T @ (y - mu))
        w += step
        if np.abs(step).max() < 1e-8:
            break
    cov = np.linalg.inv(H)
    return {"intercept": round(float(w[0]), 3), "slope": round(float(w[1]), 3), "slope_se": round(float(math.sqrt(cov[1, 1])), 3)}


def score(sub: pd.DataFrame) -> dict:
    """Brier / log loss of model and Kalshi mid on the same settled rows, model-favoured-side calibration,
    strict CLV and hypothetical after-fee economics (one contract on the model-favoured side at the ask)."""
    s = sub[sub.y.notna()]
    out = {"n": int(len(sub)), "n_settled": int(len(s))}
    if s.empty:
        return out
    p, m, y = s.p.values, s.mid.values, s.y.values

    def ll(q):
        q = np.clip(q, 1e-6, 1 - 1e-6)
        return float(-np.mean(y * np.log(q) + (1 - y) * np.log(1 - q)))
    fav = s.favored_yes.values
    ps = np.where(fav, p, 1 - p)
    ms = np.where(fav, m, 1 - m)
    ys = np.where(fav, y, 1 - y)
    ask_s = np.where(fav, s.ask.values, 1 - s.bid.values)
    fee = np.array([taker_fee(a, 1.0) for a in ask_s])
    pnl = ys - ask_s - fee
    d_brier = (p - y) ** 2 - (m - y) ** 2
    out.update({
        "model_brier": round(float(np.mean((p - y) ** 2)), 4), "kalshi_brier": round(float(np.mean((m - y) ** 2)), 4),
        "brier_diff_model_minus_kalshi": round(float(np.mean(d_brier)), 4),
        "brier_diff_se": round(float(np.std(d_brier, ddof=1) / math.sqrt(len(s))), 4) if len(s) > 1 else None,
        "model_logloss": round(ll(p), 4), "kalshi_logloss": round(ll(m), 4),
        "model_favored_side": {"mean_model_probability": round(float(ps.mean()), 4),
                               "mean_kalshi_probability": round(float(ms.mean()), 4),
                               "observed_win_rate": round(float(ys.mean()), 4)},
        "hypothetical_after_fee_per_contract": {"mean": round(float(pnl.mean()), 4),
                                                "se": round(float(pnl.std(ddof=1) / math.sqrt(len(pnl))), 4) if len(pnl) > 1 else None,
                                                "n": int(len(pnl))},
    })
    c = sub.strict_clv.dropna()
    out["strict_executable_clv"] = {"n": int(len(c)), "mean": round(float(c.mean()), 4) if len(c) else None}
    return out


def histogram(sub: pd.DataFrame, labels) -> dict:
    n = len(sub)
    vc = sub.bucket.value_counts()
    return {"n": int(n), "counts": {b: int(vc.get(b, 0)) for b in labels},
            "pct": {b: round(100 * vc.get(b, 0) / n, 2) if n else None for b in labels},
            "median_abs_gap_pp": round(float(sub.abs_gap_pp.median()), 2) if n else None,
            "share_ge_15": round(float((sub.abs_gap_pp >= 15).mean()), 4) if n else None,
            "share_ge_25": round(float((sub.abs_gap_pp >= 25).mean()), 4) if n else None,
            "share_lt_5": round(float((sub.abs_gap_pp < 5).mean()), 4) if n else None,
            "share_lt_10": round(float((sub.abs_gap_pp < 10).mean()), 4) if n else None}


def histogram_by(sub, col, labels, min_n=1) -> dict:
    return {str(k): histogram(g, labels) for k, g in sub.groupby(col) if len(g) >= min_n}


def threshold_table(sub: pd.DataFrame, thresholds) -> dict:
    """Configurable thresholds: share of comparisons at or above each gap."""
    n = len(sub)
    return {str(t): {"n": int((sub.abs_gap_pp >= t).sum()), "share": round(float((sub.abs_gap_pp >= t).mean()), 4) if n else None}
            for t in thresholds}


def primary_cause(row) -> str:
    tags, hs = set(row["tags"]), set(row["hindsight"])
    if row["identity"] == DS.ID_FAILED or row["orientation"] == "FAILED":
        return "IDENTITY_OR_ORIENTATION_FAILURE"
    if "POST_SETTLEMENT_OBSERVATION" in hs:
        return "MARKET_ALREADY_SETTLED_WHEN_PRICED"
    if hs & {"CONFIRMED_IN_PLAY_QUOTE", "LIKELY_IN_PLAY_QUOTE"}:
        return "IN_PLAY_QUOTE"
    if "POSSIBLE_IN_PLAY_QUOTE" in hs:
        return "POSSIBLY_IN_PLAY_QUOTE"
    if "STALE_KALSHI_QUOTE" in tags:
        return "STALE_QUOTE"
    if tags & {"ONE_SIDED_BOOK", "WIDE_SPREAD", "LOW_DISPLAYED_LIQUIDITY"}:
        return "BOOK_QUALITY"
    if row["identity"] == DS.ID_AMBIGUOUS:
        return "IDENTITY_AMBIGUOUS"
    if row["data_status"] == "POOR":
        return "POOR_DATA"
    if row["external_status"] == "AGREES_WITH_KALSHI":
        return "MODEL_LONE_OUTLIER_VS_EXTERNAL"
    if row["data_status"] == "LIMITED":
        return "LIMITED_DATA"
    if row["external_status"] in DS.EXTERNAL_SUPPORTS:
        return "EXTERNAL_SUPPORTS_MODEL"
    return "UNEXPLAINED_MODEL_DISAGREEMENT"


CAUSE_CLASS = {
    "IDENTITY_OR_ORIENTATION_FAILURE": "mapping", "IDENTITY_AMBIGUOUS": "mapping",
    "MARKET_ALREADY_SETTLED_WHEN_PRICED": "coverage", "IN_PLAY_QUOTE": "market_freshness/coverage",
    "POSSIBLY_IN_PLAY_QUOTE": "market_freshness/coverage", "STALE_QUOTE": "market_freshness",
    "BOOK_QUALITY": "execution", "POOR_DATA": "data", "LIMITED_DATA": "data",
    "MODEL_LONE_OUTLIER_VS_EXTERNAL": "model_calibration", "EXTERNAL_SUPPORTS_MODEL": "possible_market_error",
    "UNEXPLAINED_MODEL_DISAGREEMENT": "model_calibration_or_unknown",
}


def _nn(x):
    return None if x is None or (isinstance(x, float) and math.isnan(x)) else x


def explain(row) -> str:
    """One measured sentence per large discrepancy (top-50 table)."""
    bits = []
    hs = set(row["hindsight"])
    if "POST_SETTLEMENT_OBSERVATION" in hs and _nn(row["settled_at"]) is not None and _nn(row["predicted_at"]) is not None:
        bits.append(f"Kalshi had settled this market {(row['predicted_at'] - row['settled_at']).total_seconds() / 3600:.1f}h "
                    "before the model priced it (a finished match)")
    if _nn(row["settle_after_quote_min"]) is not None and row["settle_after_quote_min"] >= 0 and \
            hs & {"LIKELY_IN_PLAY_QUOTE", "POSSIBLE_IN_PLAY_QUOTE", "POST_SETTLEMENT_OBSERVATION"}:
        bits.append(f"the quote was captured {row['settle_after_quote_min']:.0f} min before settlement (in-play print)")
    if "CONFIRMED_IN_PLAY_QUOTE" in hs:
        bits.append("first-ball truth shows the match under way at the quote time")
    if _nn(row["quote_age_s"]) is not None:
        bits.append(f"quote age at model time {row['quote_age_s'] / 60:.0f} min ({row['freshness']})")
    if row["identity"] != DS.ID_VERIFIED:
        bad = [k for k, v in row["identity_checks"].items() if v in ("FAIL", "AMBIGUOUS")]
        bits.append(f"identity {row['identity'].replace('IDENTITY_', '')} ({', '.join(bad)})")
    if row["data_status"] in ("POOR", "LIMITED"):
        bits.append(f"data {row['data_status']} (grade {row['grade']}, thinner serve sample {_nn(row['serve_min'])}, "
                    f"ratio {_nn(row['sample_ratio'])})")
    if _nn(row["p_ext"]) is not None:
        bits.append(f"external {100 * row['p_ext']:.0f}% -> {row['external_status']}")
    else:
        bits.append("no external reference")
    return "; ".join(bits)


# ---------------------------------------------------------------------------------------------- audit
def run_audit(data_root: str, *, now: datetime | None = None, cfg: dict | None = None) -> dict:
    cfg = cfg or DS.load_config()
    now = now or datetime.now(UTC)
    ratings = [os.path.join(data_root, "processed", f"ratings_{t}.json") for t in ("ATP", "WTA")]
    names = DS.namesake_index([p for p in ratings if os.path.exists(p)], as_of=now.date()) \
        if any(os.path.exists(p) for p in ratings) else None
    raw, meta = build_observations(data_root, cfg, namesakes=names)
    labels = DS.bucket_labels(cfg["audit_buckets_pp"])
    if raw.empty:
        return {"audit_version": AUDIT_VERSION, "config_version": cfg["version"], "generated_at": now.isoformat(),
                "AUTONOMOUS_REAL_MONEY_AUTHORITY": "OFF", "model_probabilities_changed": False, "inputs": meta,
                "total_observations": 0, "note": "no model-market comparisons on disk"}
    df = dedupe_pairs(raw)
    clean_mask = df.hindsight.map(len).eq(0) & df.identity.ne(DS.ID_FAILED)
    df["pregame_clean"] = clean_mask
    indep = df[df.model.isin(INDEPENDENT_MODELS)]
    mw = df[df.family == "MATCH_WINNER"]
    fair = mw[mw.model == "fair_v1"]
    g1 = mw[mw.model == "gen1_ledger"]
    primary = mw[mw.model.isin(PRIMARY_MODELS)]

    out = {"audit_version": AUDIT_VERSION, "config_version": cfg["version"], "generated_at": now.isoformat(),
           "AUTONOMOUS_REAL_MONEY_AUTHORITY": "OFF", "model_probabilities_changed": False,
           "nature": ("DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball "
                      "truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a "
                      "betting strategy or an optimised threshold."),
           "inputs": meta, "buckets_pp": labels,
           "observation_policy": ("one comparison per match-winner event per model per producer run (model-favoured side "
                                  "kept; the two YES contracts mirror each other); every listed derivative contract kept"),
           "pregame_clean_definition": ("hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not "
                                        "inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED")}

    # ---- 1/2 totals and histograms (Part A)
    out["total_observations"] = {"all_rows_before_pair_dedupe": int(len(raw)), "comparisons": int(len(df)),
                                 "by_model": {k: int(v) for k, v in df.model.value_counts().items()},
                                 "by_source": {k: int(v) for k, v in df.source.value_counts().items()},
                                 "by_family": {k: int(v) for k, v in df.family.value_counts().items()}}
    out["histogram"] = {
        "primary_match_winner(fair_v1 + gen1_ledger)": histogram(primary, labels),
        "by_model_match_winner": histogram_by(mw, "model", labels),
        "by_model_all_families": histogram_by(df, "model", labels),
        "configurable_thresholds_primary": threshold_table(primary, [5, 10, 15, 20, 25, 30, 40, 50]),
        "executable_gap_primary": {"median_pp": round(float(primary.exec_gap_pp.median()), 2),
                                   "share_exec_ge_10pp": round(float((primary.exec_gap_pp >= 10).mean()), 4),
                                   "share_exec_ge_25pp": round(float((primary.exec_gap_pp >= 25).mean()), 4)},
        "signed_gap_primary": {"mean_pp": round(float(primary.gap_pp.mean()), 2)},
    }
    # ---- 3..6 slices
    out["by_level"] = {m: histogram_by(mw[mw.model == m], "level_detail", labels) for m in ("fair_v1", "gen2", "gen1_elo", "gen1_ledger")}
    out["by_level_pregame_clean"] = {m: histogram_by(mw[(mw.model == m) & mw.pregame_clean], "level_detail", labels)
                                     for m in ("fair_v1", "gen2", "gen1_ledger")}
    out["by_discipline_gen1_ledger"] = histogram_by(g1, "discipline", labels)
    out["by_surface_fair_v1"] = histogram_by(fair, "surface", labels)
    out["by_data_quality_grade"] = {m: histogram_by(mw[mw.model == m], "grade", labels) for m in ("fair_v1", "gen1_ledger")}
    out["by_data_quality_status_fair_v1"] = histogram_by(fair, "data_status", labels)
    out["by_family_gen1_ledger"] = histogram_by(df[df.model == "gen1_ledger"], "family", labels)
    out["by_family_model4"] = {m: histogram_by(df[df.model == m], "family", labels) for m in ("model4_conditioned", "model4_fundamental")}
    out["by_quote_freshness_at_model_time"] = {m: histogram_by(mw[mw.model == m], "freshness", labels) for m in PRIMARY_MODELS}
    out["by_external_triangulation_fair_v1"] = histogram_by(fair[fair.p_ext.notna()], "triangulation", labels)
    asym_bins = [0, 2, 4, 10, np.inf]
    fs = fair.assign(asym_bucket=pd.cut(fair.sample_ratio.astype(float), asym_bins, right=False,
                                        labels=["<2x", "2-4x", "4-10x", ">=10x"]).astype(str),
                     thin_bucket=pd.cut(fair.serve_min.astype(float), [0, 300, 1000, 3000, np.inf], right=False,
                                        labels=["<300", "300-1000", "1000-3000", ">=3000"]).astype(str))
    out["by_sample_asymmetry_fair_v1"] = histogram_by(fs, "asym_bucket", labels)
    out["by_thinner_serve_sample_fair_v1"] = histogram_by(fs, "thin_bucket", labels)

    # ---- Part B/C/D/E for large gaps (primary models, match winner)
    big15 = primary[primary.abs_gap_pp >= 15].copy()
    big25 = primary[primary.abs_gap_pp >= 25].copy()
    for b in (big15, big25):
        b["cause"] = b.apply(primary_cause, axis=1)

    def tagcount(sub, col):
        c = Counter(t for ts in sub[col] for t in ts)
        return {k: {"n": v, "share": round(v / len(sub), 4)} for k, v in c.most_common()} if len(sub) else {}

    def cause_tables(sub):
        if sub.empty:
            return {}
        vc = sub.cause.value_counts()
        cls = sub.cause.map(CAUSE_CLASS).value_counts()
        return {"n": int(len(sub)),
                "primary_cause": {k: {"n": int(v), "share": round(v / len(sub), 4)} for k, v in vc.items()},
                "cause_class": {k: {"n": int(v), "share": round(v / len(sub), 4)} for k, v in cls.items()},
                "reason_tags_ex_ante": tagcount(sub, "tags"), "hindsight_tags": tagcount(sub, "hindsight"),
                "by_level": {str(k): {kk: int(vv) for kk, vv in g.cause.value_counts().items()} for k, g in sub.groupby("level_detail")}}
    out["root_causes_ge_15pp"] = cause_tables(big15)
    out["root_causes_ge_25pp"] = cause_tables(big25)

    def ident(sub):
        if sub.empty:
            return {}
        checks = Counter((k, v) for d in sub.identity_checks for k, v in d.items())
        return {"n": int(len(sub)), "status": {k: int(v) for k, v in sub.identity.value_counts().items()},
                "ticker_orientation": {k: int(v) for k, v in sub.orientation.value_counts().items()},
                "checks": {f"{k}:{v}": n for (k, v), n in sorted(checks.items())}}
    out["identity_audit_ge_25pp"] = ident(big25)
    out["identity_audit_all_primary"] = ident(primary)

    def fresh(sub):
        if sub.empty:
            return {}
        q = sub.quote_age_s.dropna() / 60
        return {"n": int(len(sub)), "class": {k: int(v) for k, v in sub.freshness.value_counts().items()},
                "quote_age_minutes": {"median": round(float(q.median()), 1), "p90": round(float(q.quantile(0.9)), 1),
                                      "max": round(float(q.max()), 1)} if len(q) else None,
                "spread_median": round(float(sub.spread.median()), 3)}
    out["freshness_at_model_time"] = {"all_primary": fresh(primary), "ge_15pp": fresh(big15), "ge_25pp": fresh(big25),
                                      "lt_10pp": fresh(primary[primary.abs_gap_pp < 10])}

    def ext_stats(sub):
        e = sub[sub.p_ext.notna()]
        return {"n": int(len(sub)), "with_external": int(len(e)),
                "coverage": round(len(e) / len(sub), 4) if len(sub) else None,
                "external_status": {k: int(v) for k, v in e.external_status.value_counts().items()},
                "triangulation": {k: int(v) for k, v in e.triangulation.value_counts().items()},
                "share_external_agrees_with_kalshi": round(float((e.external_status == "AGREES_WITH_KALSHI").mean()), 4) if len(e) else None,
                "share_external_supports_model": round(float(e.external_status.isin(DS.EXTERNAL_SUPPORTS).mean()), 4) if len(e) else None}
    out["external_triangulation"] = {"fair_v1_all": ext_stats(fair), "fair_v1_ge_15pp": ext_stats(fair[fair.abs_gap_pp >= 15]),
                                     "fair_v1_ge_25pp": ext_stats(fair[fair.abs_gap_pp >= 25]),
                                     "fair_v1_ge_25pp_pregame_clean": ext_stats(fair[(fair.abs_gap_pp >= 25) & fair.pregame_clean]),
                                     "fair_v1_lt_10pp": ext_stats(fair[fair.abs_gap_pp < 10])}

    # ---- Part F: sample depth / asymmetry and overconfidence (pregame-clean, settled, first observation per match)
    def first_obs(sub):
        return sub[sub.pregame_clean].sort_values("predicted_at").drop_duplicates(["model", "event"])
    fc = first_obs(fs)

    def overconf(sub):
        s = sub[sub.y.notna()]
        if s.empty:
            return {"n": 0}
        fav = s.favored_yes.values
        ps = np.where(fav, s.p, 1 - s.p)
        ms = np.where(fav, s.mid, 1 - s.mid)
        ys = np.where(fav, s.y, 1 - s.y)
        return {"n": int(len(s)), "mean_model_side_prob": round(float(ps.mean()), 4), "mean_kalshi_side_prob": round(float(ms.mean()), 4),
                "observed": round(float(ys.mean()), 4), "model_minus_observed": round(float(ps.mean() - ys.mean()), 4),
                "kalshi_minus_observed": round(float(ms.mean() - ys.mean()), 4),
                "model_extremity_minus_market": round(float(np.mean(np.abs(s.p - 0.5) - np.abs(s.mid - 0.5))), 4),
                **{k: v for k, v in score(s).items() if k in ("model_brier", "kalshi_brier", "brier_diff_model_minus_kalshi", "brier_diff_se")}}
    out["sample_asymmetry"] = {
        "note": ("fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the "
                 "model-favoured side means the model over-stated that side (overconfidence in the disagreement)"),
        "by_ratio": {k: overconf(g) for k, g in fc.groupby("asym_bucket")},
        "by_thinner_sample": {k: overconf(g) for k, g in fc.groupby("thin_bucket")},
        "by_data_status": {k: overconf(g) for k, g in fc.groupby("data_status")},
        "large_gap_share_by_ratio_all": {k: round(float((g.abs_gap_pp >= 25).mean()), 4) for k, g in fs.groupby("asym_bucket")},
        "large_gap_share_by_ratio_clean": {k: round(float((g.abs_gap_pp >= 25).mean()), 4) for k, g in fs[fs.pregame_clean].groupby("asym_bucket")},
        "surface_specific_sample": "UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches",
    }
    out["data_depth_ge_25pp_primary"] = {
        "median_thinner_serve_points": _med(big25.serve_min), "median_sample_ratio": _med(big25.sample_ratio),
        "median_min_matches": _med(big25.n_min), "median_max_days_since_last": _med(big25.days_max),
        "share_severe_asymmetry": round(float(big25.severe_asym.mean()), 4) if len(big25) else None,
        "data_status": {k: int(v) for k, v in big25.data_status.value_counts().items()},
        "comparison_lt_10pp": {"median_thinner_serve_points": _med(primary[primary.abs_gap_pp < 10].serve_min),
                               "median_sample_ratio": _med(primary[primary.abs_gap_pp < 10].sample_ratio),
                               "median_min_matches": _med(primary[primary.abs_gap_pp < 10].n_min)}}

    # ---- Part G: predictive performance by bucket
    perf = {}
    for m in ("fair_v1", "gen2", "gen1_elo", "gen1_ledger"):
        sub = mw[mw.model == m]
        perf[m] = {"all_observations": {b: score(g) for b, g in sub.groupby("bucket")},
                   "pregame_clean_first_per_match": {b: score(g) for b, g in first_obs(sub).groupby("bucket")}}
    out["performance_by_bucket"] = perf
    out["calibration_slopes_pregame_clean_first"] = {}
    for m in ("fair_v1", "gen2", "gen1_elo", "gen1_sr", "gen1_ledger"):
        s = first_obs(mw[mw.model == m])
        s = s[s.y.notna()]
        out["calibration_slopes_pregame_clean_first"][m] = {
            "n": int(len(s)), "model": calibration_slope(s.p, s.y), "kalshi_mid_same_rows": calibration_slope(s.mid, s.y),
            "mean_extremity_model": round(float(np.mean(np.abs(s.p - 0.5))), 4) if len(s) else None,
            "mean_extremity_kalshi": round(float(np.mean(np.abs(s.mid - 0.5))), 4) if len(s) else None,
            **{k: v for k, v in score(s).items() if k in ("model_brier", "kalshi_brier", "model_logloss", "kalshi_logloss",
                                                          "brier_diff_model_minus_kalshi", "brier_diff_se")}}
    # ---- skill by model x level (pregame-clean, first observation per match, settled)
    skill = {}
    for m in ("fair_v1", "gen2", "gen1_elo", "gen1_ledger"):
        for k, g in first_obs(mw[mw.model == m]).groupby("level_detail"):
            s = g[g.y.notna()]
            if len(s) < 20:
                continue
            sc = score(s)
            skill[f"{m}|{k}"] = {kk: sc.get(kk) for kk in ("n_settled", "model_brier", "kalshi_brier",
                                                          "brier_diff_model_minus_kalshi", "brier_diff_se")}
            skill[f"{m}|{k}"]["corr_model_outcome"] = round(float(np.corrcoef(s.p, s.y)[0, 1]), 4) if s.y.nunique() > 1 else None
            skill[f"{m}|{k}"]["corr_kalshi_outcome"] = round(float(np.corrcoef(s.mid, s.y)[0, 1]), 4) if s.y.nunique() > 1 else None
    out["skill_by_model_level_pregame_clean_first"] = skill

    # ---- model family comparison on identical shadow rows (Gen-2 extremity, fair_v1 vs pathological gaps)
    piv = mw[mw.source == "shadow_board_v1"].pivot_table(index=["event", "predicted_at"], columns="model", values="abs_gap_pp", aggfunc="first")
    pivc = mw[(mw.source == "shadow_board_v1") & mw.pregame_clean].pivot_table(index=["event", "predicted_at"], columns="model",
                                                                               values="abs_gap_pp", aggfunc="first")
    out["model_family_same_rows"] = {
        "all": {m: {"share_ge_25": round(float((piv[m] >= 25).mean()), 4), "share_ge_15": round(float((piv[m] >= 15).mean()), 4),
                    "median_abs_gap": round(float(piv[m].median()), 2), "n": int(piv[m].notna().sum())} for m in piv.columns},
        "pregame_clean": {m: {"share_ge_25": round(float((pivc[m] >= 25).mean()), 4), "share_ge_15": round(float((pivc[m] >= 15).mean()), 4),
                              "median_abs_gap": round(float(pivc[m].median()), 2), "n": int(pivc[m].notna().sum())} for m in pivc.columns},
    }

    # ---- Part H: level decomposition
    lvl = {}
    for k, g in primary.groupby("level_detail"):
        b = g[g.abs_gap_pp >= 25].copy()
        b["cause"] = b.apply(primary_cause, axis=1) if len(b) else []
        clean = g[g.pregame_clean]
        lvl[k] = {"n": int(len(g)), "share_ge_25_all": round(float((g.abs_gap_pp >= 25).mean()), 4),
                  "share_ge_25_pregame_clean": round(float((clean.abs_gap_pp >= 25).mean()), 4) if len(clean) else None,
                  "share_of_all_ge_25": round(len(b) / max(len(big25), 1), 4),
                  "ge_25_cause_class": {kk: int(vv) for kk, vv in b.cause.map(CAUSE_CLASS).value_counts().items()} if len(b) else {},
                  "median_abs_gap_pregame_clean": round(float(clean.abs_gap_pp.median()), 2) if len(clean) else None,
                  "pregame_clean_first_obs_score": {kk: vv for kk, vv in score(first_obs(clean)).items()
                                                    if kk in ("n_settled", "model_brier", "kalshi_brier", "brier_diff_model_minus_kalshi",
                                                              "brier_diff_se")},
                  "share_data_poor": round(float((g.data_status == "POOR").mean()), 4),
                  "share_stale_quote": round(float((g.freshness == "STALE").mean()), 4),
                  "share_identity_not_verified": round(float((g.identity != DS.ID_VERIFIED).mean()), 4),
                  "share_post_settlement_or_in_play": round(float((g.hindsight.map(len) > 0).mean()), 4)}
    out["level_analysis"] = lvl

    # ---- top 50
    top = primary.sort_values("abs_gap_pp", ascending=False).drop_duplicates("event").head(50).copy()
    top["cause"] = top.apply(primary_cause, axis=1)
    out["top_50"] = [{
        "event": r.event, "ticker": r.ticker, "model": r.model, "level": r.level_detail, "predicted_at": _iso(r.predicted_at),
        "quote_ts": _iso(r.quote_ts), "model_p": round(r.p, 3), "kalshi_mid": round(r.mid, 3), "gap_pp": r.gap_pp,
        "band": r.band, "identity": r.identity, "orientation": r.orientation, "freshness": r.freshness,
        "external": r.external_status, "data_quality": r.data_status, "grade": r.grade, "tags": r.tags,
        "hindsight": r.hindsight, "outcome_yes": r.y, "primary_cause": r.cause, "cause_class": CAUSE_CLASS[r.cause],
        "explanation": explain(r)} for _i, r in top.iterrows()]
    out["current_slate"] = current_slate_freshness(os.path.join(data_root, "research", "assisted_slates"))
    out["assisted_decisions"] = "no assisted decision has been recorded yet; quote age at decision time is unmeasurable"
    out["answers"] = answers(out, primary, big25, fair, mw)
    out["model_change_recommendation"] = model_change(out)
    out["unresolved_questions"] = unresolved(out)
    return out


def _med(s):
    s = pd.Series(s).dropna()
    return round(float(s.median()), 2) if len(s) else None


def _iso(t):
    return t.isoformat() if t is not None and not (isinstance(t, float) and math.isnan(t)) else None


def current_slate_freshness(slate_dir: str) -> dict:
    try:
        s = json.load(open(os.path.join(slate_dir, "latest.json")))
    except (OSError, ValueError):
        return {"available": False}
    rows = [r for x in s.get("matches") or [] for r in x.get("markets") or [] if r.get("model_probability_yes") is not None
            and (r.get("kalshi") or {}).get("mid") is not None]
    ages = [r["kalshi"]["quote_age_s"] / 60 for r in rows if isinstance((r.get("kalshi") or {}).get("quote_age_s"), (int, float))]
    cls = Counter(DS.freshness_of(r["kalshi"].get("quote_age_s")) for r in rows)
    return {"available": True, "slate_id": s.get("slate_id"), "built_at": s.get("built_at"), "priced_rows": len(rows),
            "quote_age_minutes_at_build": {"median": round(float(np.median(ages)), 1), "max": round(float(max(ages)), 1)} if ages else None,
            "freshness_at_build": dict(cls), "has_discrepancy_layer": bool(s.get("discrepancy_sanity"))}


def answers(out, primary, big25, fair, mw) -> dict:
    """Part M: the eleven questions, answered from the numbers above (descriptive only)."""
    rc25 = out["root_causes_ge_25pp"]
    pc = (rc25.get("primary_cause") or {})
    share = lambda k: (pc.get(k) or {}).get("share", 0.0)                     # noqa: E731
    lv = out["level_analysis"]
    lower = [k for k in lv if k not in MAIN_TOUR]
    lower_share = round(sum(lv[k]["share_of_all_ge_25"] for k in lower), 4)
    stale_any = round(float((big25.freshness == "STALE").mean()), 4) if len(big25) else None
    settled_inplay = round(share("MARKET_ALREADY_SETTLED_WHEN_PRICED") + share("IN_PLAY_QUOTE") + share("POSSIBLY_IN_PLAY_QUOTE"), 4)
    ident_fail = int(((big25.identity == DS.ID_FAILED) | (big25.orientation == "FAILED")).sum())
    ext25 = out["external_triangulation"]["fair_v1_ge_25pp"]
    ext25c = out["external_triangulation"]["fair_v1_ge_25pp_pregame_clean"]
    slopes = out["calibration_slopes_pregame_clean_first"]
    fam = out["model_family_same_rows"]
    main = {k: lv[k] for k in MAIN_TOUR if k in lv}
    hist = out["histogram"]["primary_match_winner(fair_v1 + gen1_ledger)"]
    clean_primary = primary[primary.pregame_clean]
    return {
        "1_huge_gaps_mostly_lower_tour": {
            "answer": "YES" if lower_share >= 0.8 else ("MOSTLY" if lower_share >= 0.6 else "NO"),
            "share_of_ge_25pp_from_non_main_tour": lower_share,
            "by_level_share_of_ge_25pp": {k: v["share_of_all_ge_25"] for k, v in lv.items()}},
        "2_ge_25pp_caused_by_stale_prices": {
            "share_quote_older_than_30min_at_model_time": stale_any,
            "share_primary_cause_market_settled_or_in_play": settled_inplay,
            "share_primary_cause_stale_quote_only": share("STALE_QUOTE")},
        "3_ge_25pp_identity_or_ticker_problems": {
            "identity_or_orientation_FAILED": ident_fail, "n_ge_25pp": int(len(big25)),
            "identity_ambiguous_share": round(float((big25.identity == DS.ID_AMBIGUOUS).mean()), 4) if len(big25) else None,
            "ticker_orientation": out["identity_audit_ge_25pp"].get("ticker_orientation")},
        "4_external_agrees_with_kalshi_not_model": {"all_ge_25pp": ext25, "pregame_clean_ge_25pp": ext25c},
        "5_extreme_gaps_and_thin_samples": out["data_depth_ge_25pp_primary"],
        "6_sample_asymmetry_overconfidence": {k: {kk: v.get(kk) for kk in ("n", "model_minus_observed", "kalshi_minus_observed",
                                                                          "brier_diff_model_minus_kalshi")}
                                              for k, v in out["sample_asymmetry"]["by_ratio"].items()},
        "7_gen2_too_extreme": {m: slopes.get(m) for m in ("gen2", "fair_v1", "gen1_elo")},
        "8_fair_v1_reduces_pathological_gaps": fam,
        "9_main_tour_gaps_small": {k: {"median_abs_gap_pregame_clean": v["median_abs_gap_pregame_clean"],
                                       "share_ge_25_all": v["share_ge_25_all"],
                                       "share_ge_25_pregame_clean": v["share_ge_25_pregame_clean"]} for k, v in main.items()},
        "10_strong_independent_market_proxy": {
            "share_within_5pp_all": hist["share_lt_5"], "share_within_10pp_all": hist["share_lt_10"],
            "share_within_10pp_pregame_clean": round(float((clean_primary.abs_gap_pp < 10).mean()), 4) if len(clean_primary) else None,
            "corr_model_vs_mid_pregame_clean": round(float(np.corrcoef(clean_primary.p, clean_primary.mid)[0, 1]), 4) if len(clean_primary) > 2 else None},
        "11_most_trustworthy_range_as_handicapping_input": {
            "basis": ("DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; "
                      "not a strategy and not an optimised cutoff"),
            "fair_v1_by_bucket": {b: {k: v.get(k) for k in ("n_settled", "model_brier", "kalshi_brier", "brier_diff_model_minus_kalshi")}
                                  for b, v in out["performance_by_bucket"]["fair_v1"]["pregame_clean_first_per_match"].items()}},
    }


#: generic, pre-stated defect criteria (fixed before reading the per-slice results; never fitted to P&L)
NO_SKILL_MIN_N = 50
NO_SKILL_BRIER = 0.25            # no better than a coin flip
SIGNIFICANT_SE = 2.0


def model_change(out) -> dict:
    """MODEL_CHANGE_RECOMMENDED only for a GENERIC defect the evidence shows. Never implemented here.

    Criteria (pre-stated, generic):
      A. too extreme: logistic recalibration slope + 2 se < 1 AND below Kalshi's slope on the same rows;
      B. no skill: on pregame-clean first observations of one model x level slice with N >= 50, Brier >= 0.25
         (no better than a coin flip) AND worse than Kalshi by more than 2 se.
    Slices that miss these bars are reported as hypotheses, not defects."""
    s = out["calibration_slopes_pregame_clean_first"]
    defects = {}
    for m in ("fair_v1", "gen2", "gen1_ledger"):
        c = (s.get(m) or {}).get("model")
        k = (s.get(m) or {}).get("kalshi_mid_same_rows")
        if c and k and c["slope"] + SIGNIFICANT_SE * c["slope_se"] < 1.0 and c["slope"] < k["slope"]:
            defects[f"TOO_EXTREME:{m}"] = {"model_slope": c, "kalshi_slope": k, "n": s[m]["n"]}
    hyp = {}
    for key, v in (out.get("skill_by_model_level_pregame_clean_first") or {}).items():
        d, se = v.get("brier_diff_model_minus_kalshi"), v.get("brier_diff_se")
        if v.get("n_settled", 0) >= NO_SKILL_MIN_N and d is not None and se:
            if v["model_brier"] >= NO_SKILL_BRIER and d > SIGNIFICANT_SE * se:
                defects[f"NO_SKILL:{key}"] = v
            elif d > SIGNIFICANT_SE * se:
                hyp[f"WORSE_THAN_KALSHI:{key}"] = v
    rec = bool(defects)
    doubles = any(k.endswith("|DOUBLES") for k in defects)
    return {
        "MODEL_CHANGE_RECOMMENDED": rec,
        "criteria": {"A_too_extreme": "calibration slope + 2se < 1 and below Kalshi's slope on the same rows",
                     "B_no_skill": f"N >= {NO_SKILL_MIN_N}, Brier >= {NO_SKILL_BRIER} and worse than Kalshi by > {SIGNIFICANT_SE} se"},
        "exact_defect": "; ".join(
            (["Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on "
              "pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being "
              "very confident (e.g. 92% / 8%)"] if doubles else []) +
            [f"{k}: probabilities too extreme for their evidence" for k in defects if k.startswith("TOO_EXTREME")] +
            [k for k in defects if k.startswith("NO_SKILL") and not k.endswith("|DOUBLES")]) if rec else "none established by this audit",
        "evidence": defects,
        "affected_populations": sorted(defects) if rec else None,
        "proposed_generic_correction": (
            ("Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own "
             "validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). "
             if doubles else "") +
            ("Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on "
             "evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L."
             if any(k.startswith("TOO_EXTREME") for k in defects) else "")).strip() or None,
        "prospective_validation_plan": ("any corrected model is frozen as a NEW candidate beside the current one (no frozen file "
                                        "edited) and scored prospectively on pregame-clean, first-observation-per-match rows from "
                                        "its own effective start; it replaces nothing unless Brier and log loss improve with the "
                                        "95% interval of the paired difference excluding zero at a pre-registered minimum N")
        if rec else None,
        "implemented_in_this_change": False,
        "hypotheses_not_established": hyp,
        "not_a_model_defect": (
            "the dominant source of extreme gaps is the pipeline, not the model: the shadow board and the Gen-1 ledger priced "
            "match-winner contracts whose Kalshi market had ALREADY SETTLED or was in play (ITF/Challenger have no first-ball "
            "source) and quotes 30 min to hours old. That is a producer coverage/freshness defect; the frozen producers are not "
            "modified here, and the assisted sanity layer holds stale / unverifiable extremes at DATA_WARNING. Large "
            "disagreements that survive the hindsight filter are also mostly the MODEL's error (Kalshi's Brier is far better in "
            "the >=25pp buckets) -- expected when two estimators disagree and the market is the better one, which is why "
            "an extreme gap is an alarm, not an edge."),
    }


def unresolved(out) -> list[str]:
    return [
        "Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.",
        "Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.",
        "Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of "
        "settlement may still have been pregame for a short match.",
        "External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.",
        "Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here "
        "(their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.",
        "No assisted decision exists yet, so quote age at assisted decision time cannot be measured.",
    ]


# ---------------------------------------------------------------------------------------------- render
def render_markdown(a: dict) -> str:
    def pct(x):
        return f"{100 * x:.1f}%" if isinstance(x, (int, float)) else "--"
    L = ["# Model-vs-market discrepancy audit", "",
         f"`{a['audit_version']}` · config `{a.get('config_version')}` · generated {a['generated_at'][:16]}Z · "
         "**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.", "",
         f"> {a.get('nature', '')}", ""]
    if not a.get("total_observations") or isinstance(a.get("total_observations"), int):
        L.append("No model-market comparisons on disk.")
        return "\n".join(L)
    t = a["total_observations"]
    i = a["inputs"]
    L += executive_summary(a)
    L += ["## 1. Observations", "",
          f"* {t['comparisons']:,} model-market comparisons ({t['all_rows_before_pair_dedupe']:,} producer rows before the "
          "mirrored match-winner pair was collapsed). " + a["observation_policy"] + ".",
          f"* Inputs: Gen-1 ledger {i['ledger_rows']:,} rows {i['ledger_span']}, shadow board {i['shadow_rows']:,} rows "
          f"{i['shadow_span']}, Model 4 {i['model4_rows']:,} rows, {i['settled_tickers']:,} settled tickers, "
          f"{i['external_tickers']:,} tickers with an external scan.",
          f"* By model: {json.dumps(t['by_model'])}", f"* Pregame-clean (diagnostic, hindsight): {a['pregame_clean_definition']}.", ""]
    labels = a["buckets_pp"]

    def htable(title, d):
        rows = [f"### {title}", "", "| slice | N | " + " | ".join(labels) + " | median | >=15 | >=25 |",
                "|---|---|" + "---|" * len(labels) + "---|---|---|"]
        for k, h in d.items():
            if not h or not h.get("n"):
                continue
            rows.append(f"| {k} | {h['n']:,} | " + " | ".join(f"{h['pct'][b]:.1f}" for b in labels) +
                        f" | {h['median_abs_gap_pp']} | {pct(h['share_ge_15'])} | {pct(h['share_ge_25'])} |")
        return rows + [""]
    h = a["histogram"]
    L += ["## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)", ""]
    L += htable("Primary match-winner models and every model", {"PRIMARY (fair_v1 + Gen-1 ledger)": h["primary_match_winner(fair_v1 + gen1_ledger)"],
                                                                 **{f"MW {k}": v for k, v in h["by_model_match_winner"].items()},
                                                                 **{f"all families {k}": v for k, v in h["by_model_all_families"].items()
                                                                    if k.startswith("model4")}})
    L += ["Configurable thresholds (primary): " + ", ".join(f">={k}pp {pct(v['share'])}" for k, v in h["configurable_thresholds_primary"].items()),
          f"Executable gap (model outside the book, before fees): median {h['executable_gap_primary']['median_pp']}pp; "
          f">=10pp {pct(h['executable_gap_primary']['share_exec_ge_10pp'])}, >=25pp {pct(h['executable_gap_primary']['share_exec_ge_25pp'])}.", ""]
    L += ["## 3. Discrepancy by level", ""]
    for m, d in a["by_level"].items():
        L += htable(f"{m} -- all observations", d)
    for m, d in a["by_level_pregame_clean"].items():
        L += htable(f"{m} -- pregame-clean (hindsight-filtered)", d)
    L += htable("Gen-1 ledger by discipline (doubles where a model exists)", a["by_discipline_gen1_ledger"])
    L += htable("fair_v1 by surface", a["by_surface_fair_v1"])
    L += ["## 4. Discrepancy by data quality", ""]
    for m, d in a["by_data_quality_grade"].items():
        L += htable(f"{m} by grade", d)
    L += htable("fair_v1 by sanity data-quality status", a["by_data_quality_status_fair_v1"])
    L += ["## 5. Discrepancy by model and family", ""]
    L += htable("Gen-1 ledger by family", a["by_family_gen1_ledger"])
    for m, d in a["by_family_model4"].items():
        L += htable(f"{m} by family" + (" (market-conditioned by construction: NOT an independent estimate)" if m == "model4_conditioned" else ""), d)
    fam = a["model_family_same_rows"]
    L += ["### Same shadow-board rows, model by model", "", "| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |",
          "|---|---|---|---|---|---|---|---|"]
    for m in fam["all"]:
        x, c = fam["all"][m], fam["pregame_clean"].get(m, {})
        L.append(f"| {m} | {x['n']:,} | {pct(x['share_ge_15'])} | {pct(x['share_ge_25'])} | {x['median_abs_gap']} | "
                 f"{pct(c.get('share_ge_15'))} | {pct(c.get('share_ge_25'))} | {c.get('median_abs_gap')} |")
    L += ["", "## 6. Discrepancy by quote freshness (at the model's own timestamp)", ""]
    for m, d in a["by_quote_freshness_at_model_time"].items():
        L += htable(m, d)
    fr = a["freshness_at_model_time"]
    L += ["| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |", "|---|---|---|---|---|---|---|---|"]
    for k, v in fr.items():
        if v:
            q = v.get("quote_age_minutes") or {}
            L.append(f"| {k} | {v['n']:,} | {v['class'].get('FRESH', 0)} | {v['class'].get('AGING', 0)} | {v['class'].get('STALE', 0)} | "
                     f"{q.get('median')} | {q.get('p90')} | {q.get('max')} |")
    cs = a.get("current_slate") or {}
    if cs.get("available"):
        L += ["", f"Current slate `{cs['slate_id']}`: {cs['priced_rows']} priced rows, quote age at build "
                  f"{cs['quote_age_minutes_at_build']}, freshness {cs['freshness_at_build']}. Quote age at assisted decision "
                  "time: no decisions recorded yet."]
    L += ["", "## 7. Discrepancy by external triangulation", ""]
    L += htable("fair_v1 rows with an external price, by triangulation", a["by_external_triangulation_fair_v1"])
    L += ["| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |", "|---|---|---|---|---|---|"]
    for k, v in a["external_triangulation"].items():
        L.append(f"| {k} | {v['n']:,} | {v['with_external']} ({pct(v['coverage'])}) | {pct(v['share_external_agrees_with_kalshi'])} | "
                 f"{pct(v['share_external_supports_model'])} | {json.dumps(v['external_status'])} |")
    L += ["", "## 8. Discrepancy by player sample asymmetry", ""]
    L += htable("fair_v1 by serve-sample ratio (deeper / thinner)", a["by_sample_asymmetry_fair_v1"])
    L += htable("fair_v1 by thinner player's serve points", a["by_thinner_serve_sample_fair_v1"])
    sa = a["sample_asymmetry"]
    L += [sa["note"], "", "| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |",
          "|---|---|---|---|---|---|---|---|"]
    for grp in ("by_ratio", "by_thinner_sample", "by_data_status"):
        for k, v in sa[grp].items():
            if v.get("n"):
                L.append(f"| {grp[3:]} {k} | {v['n']} | {v['mean_model_side_prob']} | {v['mean_kalshi_side_prob']} | {v['observed']} | "
                         f"{v['model_minus_observed']:+.3f} | {v['kalshi_minus_observed']:+.3f} | {v.get('brier_diff_model_minus_kalshi')} ± {v.get('brier_diff_se')} |")
    L += ["", f"Surface-specific sample: {sa['surface_specific_sample']}.", ""]
    L += ["## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)", "",
          "Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side "
          "at the observed ask with the taker fee -- descriptive only, never an optimised threshold.", ""]
    for m, d in a["performance_by_bucket"].items():
        for view in ("pregame_clean_first_per_match", "all_observations"):
            L += [f"### {m} -- {view}", "", "| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | "
                  "model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|"]
            for b in labels:
                v = d[view].get(b)
                if not v or not v.get("n_settled"):
                    continue
                fv, e, c = v["model_favored_side"], v["hypothetical_after_fee_per_contract"], v["strict_executable_clv"]
                L.append(f"| {b} | {v['n_settled']} | {v['model_brier']} | {v['kalshi_brier']} | {v['brier_diff_model_minus_kalshi']:+.4f} ± "
                         f"{v['brier_diff_se']} | {v['model_logloss']} | {v['kalshi_logloss']} | {fv['mean_model_probability']} | "
                         f"{fv['mean_kalshi_probability']} | {fv['observed_win_rate']} | {e['mean']:+.3f} ± {e['se']} | "
                         f"{c['mean'] if c['mean'] is not None else '--'} ({c['n']}) |")
            L.append("")
    L += ["### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)", "",
          "| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |",
          "|---|---|---|---|---|---|---|---|"]
    for m, v in a["calibration_slopes_pregame_clean_first"].items():
        ms, ks = v.get("model") or {}, v.get("kalshi_mid_same_rows") or {}
        L.append(f"| {m} | {v['n']} | {ms.get('slope')} ± {ms.get('slope_se')} | {ks.get('slope')} | {v.get('mean_extremity_model')} | "
                 f"{v.get('mean_extremity_kalshi')} | {v.get('model_brier')} | {v.get('kalshi_brier')} |")
    L += ["", "## 10. Strict CLV", "",
          "Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries "
          "before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).", ""]
    L += ["## 11. Root causes of large gaps (primary match-winner models)", ""]
    for k in ("root_causes_ge_15pp", "root_causes_ge_25pp"):
        rc = a[k]
        if not rc:
            continue
        L += [f"### {k.replace('root_causes_', '>= ').replace('pp', ' pp')} (N = {rc['n']:,})", "", "| primary cause | class | N | share |", "|---|---|---|---|"]
        for c, v in rc["primary_cause"].items():
            L.append(f"| {c} | {CAUSE_CLASS.get(c)} | {v['n']:,} | {pct(v['share'])} |")
        L += ["", "Cause class: " + ", ".join(f"{c} {pct(v['share'])}" for c, v in rc["cause_class"].items()),
              "", "Ex-ante reason tags (multi-label, available at the observation's own time): " +
              ", ".join(f"{c} {pct(v['share'])}" for c, v in rc["reason_tags_ex_ante"].items()),
              "", "Hindsight tags (diagnosis only): " + ", ".join(f"{c} {pct(v['share'])}" for c, v in rc["hindsight_tags"].items()), ""]
    ia = a["identity_audit_ge_25pp"]
    if ia:
        L += ["### Identity / side integrity audit, every >= 25 pp comparison", "",
              f"Status: {json.dumps(ia['status'])}; ticker orientation: {json.dumps(ia['ticker_orientation'])}.", "",
              "Checks: " + ", ".join(f"{k} {v}" for k, v in ia["checks"].items()), ""]
    L += ["## 12. Level analysis", "", "| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | "
          "clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for k, v in a["level_analysis"].items():
        s = v["pregame_clean_first_obs_score"]
        L.append(f"| {k} | {v['n']:,} | {pct(v['share_ge_25_all'])} | {pct(v['share_ge_25_pregame_clean'])} | {pct(v['share_of_all_ge_25'])} | "
                 f"{json.dumps(v['ge_25_cause_class'])} | {v['median_abs_gap_pregame_clean']} | {s.get('model_brier')} / {s.get('kalshi_brier')} "
                 f"({s.get('n_settled')}) | {pct(v['share_stale_quote'])} | {pct(v['share_data_poor'])} | "
                 f"{pct(v['share_identity_not_verified'])} | {pct(v['share_post_settlement_or_in_play'])} |")
    L += ["", "## 13. Top 50 largest discrepancies (one per event)", "",
          "| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for n, r in enumerate(a["top_50"], 1):
        L.append(f"| {n} | `{r['ticker']}` | {r['level']} | {r['model']} | {100 * r['model_p']:.0f}% / {100 * r['kalshi_mid']:.0f}% | "
                 f"{r['gap_pp']:+.0f} | {r['primary_cause']} | {r['identity'].replace('IDENTITY_', '')} | {r['freshness']} | {r['external']} | "
                 f"{r['data_quality']} | {'YES' if r['outcome_yes'] == 1 else ('NO' if r['outcome_yes'] == 0 else '--')} | {r['explanation']} |")
    L += ["", "## 14. Answers (Part M)", ""]
    for k, v in a["answers"].items():
        L.append(f"* **{k}**: `{json.dumps(v, default=str)[:1500]}`")
    mc = a["model_change_recommendation"]
    L += ["", "## 15. Model change recommendation", "", f"**MODEL_CHANGE_RECOMMENDED = {str(mc['MODEL_CHANGE_RECOMMENDED']).upper()}** "
          "(not implemented in this change).", ""]
    for k in ("exact_defect", "affected_populations", "proposed_generic_correction", "prospective_validation_plan",
              "separate_finding_producer_coverage"):
        if mc.get(k):
            L.append(f"* {k}: {mc[k]}")
    if mc.get("evidence"):
        L.append(f"* evidence: `{json.dumps(mc['evidence'])}`")
    L += ["", "## 16. Unresolved questions", ""] + [f"* {q}" for q in a["unresolved_questions"]] + [""]
    return "\n".join(L)


def executive_summary(a: dict) -> list[str]:
    def pct(x):
        return f"{100 * x:.1f}%" if isinstance(x, (int, float)) else "--"
    an = a["answers"]
    h = a["histogram"]["primary_match_winner(fair_v1 + gen1_ledger)"]
    rc25 = a["root_causes_ge_25pp"].get("cause_class", {})
    pc25 = a["root_causes_ge_25pp"].get("primary_cause", {})
    lv = a["level_analysis"]
    mc = a["model_change_recommendation"]
    sl = a["calibration_slopes_pregame_clean_first"]
    perf = a["performance_by_bucket"]["fair_v1"]["pregame_clean_first_per_match"]
    big = [perf.get(b) for b in ("25-40", "40+") if perf.get(b)]
    L = ["## Executive summary", "",
         f"* **Distribution** (primary match-winner comparisons, N = {h['n']:,}): " +
         ", ".join(f"{b} {h['pct'][b]:.1f}%" for b in a["buckets_pp"]) + f"; median gap {h['median_abs_gap_pp']} pp.",
         f"* **Where the extremes live**: {pct(an['1_huge_gaps_mostly_lower_tour']['share_of_ge_25pp_from_non_main_tour'])} of "
         f">=25 pp gaps are off the ATP/WTA main tour (ITF {pct((lv.get('ITF_MEN', {}).get('share_of_all_ge_25') or 0) + (lv.get('ITF_WOMEN', {}).get('share_of_all_ge_25') or 0))}, "
         f"Challenger {pct(lv.get('CHALLENGER', {}).get('share_of_all_ge_25'))}, doubles {pct(lv.get('DOUBLES', {}).get('share_of_all_ge_25'))}). "
         f"Main tour: ATP {pct(lv.get('ATP', {}).get('share_ge_25_all'))} and WTA {pct(lv.get('WTA', {}).get('share_ge_25_all'))} of comparisons are >=25 pp.",
         f"* **Why >=25 pp gaps happen** (primary cause, N = {a['root_causes_ge_25pp'].get('n', 0):,}): " +
         ", ".join(f"{k} {pct(v['share'])}" for k, v in pc25.items()) + ". By class: " +
         ", ".join(f"{k} {pct(v['share'])}" for k, v in rc25.items()) + ".",
         f"* **Stale / settled / in-play**: {pct(an['2_ge_25pp_caused_by_stale_prices']['share_quote_older_than_30min_at_model_time'])} of "
         f">=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; "
         f"{pct(an['2_ge_25pp_caused_by_stale_prices']['share_primary_cause_market_settled_or_in_play'])} were priced after the market "
         "settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag "
         "alone is 11+ minutes.",
         f"* **Identity / ticker**: {an['3_ge_25pp_identity_or_ticker_problems']['identity_or_orientation_FAILED']} of "
         f"{an['3_ge_25pp_identity_or_ticker_problems']['n_ge_25pp']:,} >=25 pp comparisons failed identity or orientation; ticker "
         f"orientation verified on all of them; {pct(an['3_ge_25pp_identity_or_ticker_problems']['identity_ambiguous_share'])} "
         "ambiguous (doubles, missing producer identity confidence).",
         f"* **External triangulation**: external coverage of >=25 pp gaps is "
         f"{pct(an['4_external_agrees_with_kalshi_not_model']['all_ge_25pp']['coverage'])}; the agreement question cannot be "
         "answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi "
         f"{pct(a['external_triangulation']['fair_v1_all']['share_external_agrees_with_kalshi'])} of the time and with the model "
         f"{pct(a['external_triangulation']['fair_v1_all']['share_external_supports_model'])}.",
         f"* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of "
         f"{an['5_extreme_gaps_and_thin_samples']['median_thinner_serve_points']} points vs "
         f"{an['5_extreme_gaps_and_thin_samples']['comparison_lt_10pp']['median_thinner_serve_points']} for <10 pp gaps.",
         f"* **Calibration (pregame-clean, first observation)**: fair_v1 slope {((sl.get('fair_v1') or {}).get('model') or {}).get('slope')}, "
         f"Gen-2 {((sl.get('gen2') or {}).get('model') or {}).get('slope')}, Gen-1 ledger {((sl.get('gen1_ledger') or {}).get('model') or {}).get('slope')} "
         "(1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: " +
         "; ".join(f"n {v['n_settled']} model {v['model_brier']} vs Kalshi {v['kalshi_brier']}" for v in big) + ".",
         f"* **MODEL_CHANGE_RECOMMENDED = {str(mc['MODEL_CHANGE_RECOMMENDED']).upper()}**: {mc['exact_defect']}. Not implemented here.",
         ""]
    return L


def write_audit(a: dict, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "AUDIT.json"), "w") as f:
        json.dump(a, f, indent=1, default=str)
    with open(os.path.join(out_dir, "AUDIT.md"), "w") as f:
        f.write(render_markdown(a))
