"""Harvesters for the five candidates whose frozen producers only started running on 2026-09-28.

Each one does exactly what the Wave harvesters do, on the producer's own append-only rows:

  * no experiment-start record -> the producer never ran in production -> UNSCORABLE, as before;
  * otherwise only rows predicted AT OR AFTER `effective_scorable_start` are read. Everything between the
    original confirmation_start and that instant stays permanently UNSCORABLE and is reported as such;
  * the frozen rule is applied to fields written AT PREDICTION TIME by the frozen producer; nothing is
    recomputed, and no probability from any other lane is substituted;
  * the decision unit is fixed here, before any outcome, and mirrors the discovery unit: W3 = the FIRST
    observation of each contract (the discovery set priced each contract once, at a fixed cutoff, and
    selected on edge at that moment); EC-003 = the first observation of each physical match; EC-001/002 =
    the first prediction run for each physical match.

Prospective invariant (evidence accounting, 2026-10-01): an observation timestamped AT OR AFTER the
exchange's own recorded settlement of its contract cannot be prospective pregame evidence. Where no
first-ball source exists (Challenger / WTA125 / ITF, and some main-tour matches) the timing class is
START_UNKNOWN, so the first-ball checks alone let such a row through. The decision unit is unchanged: a
contaminated FIRST observation makes the unit EXCLUDED (MARKET_SETTLED_BEFORE_OBSERVATION); a later
observation is never substituted for it.

Thresholds are transcribed from the frozen text as constants beside it, never taken as arguments.
"""
from __future__ import annotations

import os
from collections import Counter, defaultdict
from datetime import timedelta, timezone

from tennis_edge.confirmation import evidence as ev
from tennis_edge.confirmation import sources as src
from tennis_edge.confirmation import stats
from tennis_edge.confirmation.status import (KIND_ABSTENTION, KIND_PRICING, KIND_TRADE,
                                             UNSCORABLE_MISSING_HISTORICAL_FIELDS, ScoreSummary, assign_status)
from tennis_edge.firstball.classify import AMBIGUOUS, POST_START, STRICT_PREGAME
from tennis_edge.producers.records import CANDIDATE_PRODUCER, load_start_records

# frozen text, transcribed
EC3_MIN_EVIDENCE, EC3_MAX_EVIDENCE = 1000.0, 20000.0      # "between 1,000 and 20,000 observed serve points"
EC3_BRIER_GAIN = 0.0015                                   # "Brier below Gen-1 Elo by >= 0.0015"
EC3_MARKET_TOL = 0.005                                    # "not worse than the market by more than 0.005"
EC1_LL_GAIN = 0.010                                       # "log loss below the fundamental lane by >= 0.010"
EC1_MKT_BAND = (0.05, 0.95)                               # "de-vigs to a probability in [0.05, 0.95]"
EC2_MAE_GAIN = 0.05                                       # "MAE ... below the fundamental lane by >= 0.05 games"

PRODUCER_DIRS = {"shadow_board_v1": "shadow_board", "model4_board_v1": "model4"}


def _producer_rows(ctx, producer: str, since: str) -> tuple[list, int]:
    root = os.path.join(ctx.data_root, "research", "frozen_producers", PRODUCER_DIRS[producer])
    rows, before = [], 0
    for _f, h, r in src.iter_jsonl(os.path.join(root, "*.jsonl")):
        if (r.get("predicted_at") or "") < since:
            before += 1
            continue
        rows.append({**r, "_line_hash": h})
    rows.sort(key=lambda r: (r["predicted_at"], r.get("ticker") or ""))
    return rows, before


def _start(ctx, cid: str):
    return load_start_records(os.path.join(ctx.data_root, "research", "experiment_starts")).get(cid)


def _utc(d):
    return d.replace(tzinfo=timezone.utc) if (d is not None and d.tzinfo is None) else d


def _settled_before_observation(ctx, ticker, predicted_at) -> tuple[bool, str | None]:
    """(was the contract already terminal when observed?, the recorded settlement_ts).

    Reads ONLY the exchange's preserved settlement timestamp via sources.settlement_payout; nothing is
    inferred from a schedule, a price, a result, file order or the current time. True only when a real,
    parseable settlement_ts exists and settlement_ts <= predicted_at (the same instant fails closed). A
    missing or malformed timestamp never declares a row post-settlement on its own."""
    if not ticker:
        return False, None
    _res, _pay, sat = src.settlement_payout(ctx.settlements.get(ticker))
    st, obs = _utc(src.iso(sat)), _utc(src.iso(predicted_at))
    if st is None or obs is None:
        return False, sat if st is not None else None
    return st <= obs, sat


def _level_bucket(ticker) -> str:
    from tennis_edge.assisted.schema import level_bucket
    return level_bucket((ticker or "").split("-")[0])


def _not_post_start(truth, tc) -> bool:
    return tc.timing_class not in (POST_START, AMBIGUOUS)


def _y(sres):
    return 1.0 if sres == "yes" else (0.0 if sres == "no" else None)


def _pnl(ctx, ticker, ask, fee):
    sres, payout, _ = src.settlement_payout(ctx.settlements.get(ticker))
    return sres, payout, (None if payout is None else payout - ask - fee)


def _base(cid, cand, start, r, **kw):
    from tennis_edge.confirmation.candidates import HARVESTER_VERSION, _cand_fp
    return ev.EvidenceRow(
        candidate_id=cid, observation_id=r.get("row_hash") or r["_line_hash"],
        physical_match_id=r.get("physical_match_id"), ticker=r.get("ticker"),
        market_family=r.get("market_family"), side=r.get("side") or r.get("subject"),
        captured_at=r["predicted_at"], candidate_freeze_at=cand["frozen_at"],
        confirmation_start=start["effective_scorable_start"], candidate_fingerprint=_cand_fp(cand),
        source_hashes={"producer_row_hash": r.get("row_hash"), "producer_fingerprint": r.get("fingerprint"),
                       "experiment_start_fingerprint": start.get("fingerprint")},
        harvester_version=HARVESTER_VERSION, **kw)


def _not_started(ctx, cand, kind, legacy):
    """No start record: the producer has never run in production. Keep the historical verdict."""
    res = legacy(ctx, cand)
    if res.status != UNSCORABLE_MISSING_HISTORICAL_FIELDS:
        # whatever the (possibly empty) historical universe looks like, no producer means nothing scorable
        res.status = UNSCORABLE_MISSING_HISTORICAL_FIELDS
        res.status_reason = "the frozen producer has never run in production; no observation is scorable"
    res.notes.append(f"producer {CANDIDATE_PRODUCER[cand['candidate_id']]} has not written an experiment-start "
                     "record: it has not run in production yet")
    res.universe["experiment_start"] = None
    return res


def _history(ctx, cand, start, before_n) -> dict:
    return {"permanently_unscorable_period": [cand["confirmation_start"], start["effective_scorable_start"]],
            "reason": start.get("reason_prior_period_unscorable"),
            "producer_rows_before_effective_start": before_n}


def _finish(res, cand, kind, *, eligible_n, settled_n=0, strict_n=0, unsettled=0, clv_pending=0,
            acc=None, clv=None, econ=None, clv_required=False):
    res.summary = ScoreSummary(kind=kind, minimum_n=int(cand["minimum_n"]), eligible_n=eligible_n,
                               settled_n=settled_n, strict_clv_n=strict_n, unsettled_n=unsettled,
                               clv_pending_n=clv_pending, accuracy_pass=acc, clv_pass=clv,
                               economics_pass=econ, clv_required=clv_required)
    res.status, res.status_reason = assign_status(res.summary)
    return res


def _ci_pass(m, sign):
    if m is None or m.get("mean") is None or m.get("excludes_zero") is not True:
        return False
    return m["mean"] > 0 if sign > 0 else m["mean"] < 0


# --------------------------------------------------------------------------------------- W3-001 / W3-002
def harvest_w3_live(ctx, cand):
    from tennis_edge.confirmation.candidates import HarvestResult, _strict_close, _timing, harvest_w3
    cid = cand["candidate_id"]
    is_001 = cid.startswith("W3-2026-001")
    kind = KIND_ABSTENTION if is_001 else KIND_TRADE
    start = _start(ctx, cid)
    if start is None:
        return _not_started(ctx, cand, kind, harvest_w3)
    res = HarvestResult(cid, kind)
    rows, before = _producer_rows(ctx, "shadow_board_v1", start["effective_scorable_start"])
    res.universe = {"experiment_start": start, "history": _history(ctx, cand, start, before),
                    "stream": "research/frozen_producers/shadow_board (fair_v1 + selector_v1, frozen)",
                    "rows_after_effective_start": len(rows)}
    first = {}
    for r in rows:
        if r.get("market_family") == "MATCH_WINNER":
            first.setdefault(r["ticker"], r)
    res.universe["contracts_first_observed"] = len(first)
    ctx.quotes(set(first))                         # ONE pass over the capture for every contract
    res.exclusion_counts[ev.R_REOBSERVATION] = sum(1 for r in rows if r.get("market_family") == "MATCH_WINNER") - len(first)
    post_settled = Counter()
    out = []
    for tk, r in first.items():
        reasons = []
        if not (r.get("fee_adjusted_edge") is not None and r["fee_adjusted_edge"] > 0):
            reasons.append(ev.R_RULE_FAILED)
        if not is_001 and (r.get("level") == "ITF" or not r.get("qualification_ok")):
            reasons.append(ev.R_RULE_FAILED)
        truth, tc = _timing(r["predicted_at"], r["event"], ctx.truths)
        if not _not_post_start(truth, tc):
            reasons.append(ev.R_TIMING_POST if tc.timing_class == POST_START else ev.R_TIMING_AMBIG)
        post_settle, settled_at = _settled_before_observation(ctx, tk, r["predicted_at"])
        if post_settle:                     # the FIRST observation is the unit: excluded, never replaced
            reasons.append(ev.R_SETTLED_BEFORE_OBSERVATION)
            post_settled[_level_bucket(tk)] += 1
        sres, payout, pnl = _pnl(ctx, tk, r["kalshi_ask"], r["fee"])
        cc, clv = _strict_close(ctx, tk, truth, r["predicted_at"], r["kalshi_bid"], r["kalshi_ask"],
                                r.get("displayed_size"), tc)
        reasons = tuple(dict.fromkeys(reasons))
        for x in reasons:
            res.exclusion_counts[x] += 1
        out.append(_base(cid, cand, start, r, model_version="gen2_dyn_hier_sr_v1+fair_v1+selector_v1",
                         fair_probability=r["fair_v1_probability"], kalshi_bid=r["kalshi_bid"],
                         kalshi_ask=r["kalshi_ask"], kalshi_mid=r.get("kalshi_mid"), kalshi_spread=r.get("spread"),
                         fee=r["fee"], displayed_size=r.get("displayed_size"),
                         kalshi_quote_age_s=r.get("quote_age_seconds"), decision_edge=r.get("fee_adjusted_edge"),
                         extra={"level": r.get("level"), "qualification_ok": r.get("qualification_ok"),
                                "selector_decision": r.get("selector_decision"),
                                "identity_confidence": r.get("identity_confidence")},
                         first_ball_confidence=truth.confidence if truth else None, timing_class=tc.timing_class,
                         close_basis=cc.close_basis,
                         strict_clv_executable=clv.clv_executable if clv.strict else None,
                         strict_clv_midpoint=clv.clv_midpoint if clv.strict else None,
                         settlement_result=sres, settlement_value=payout,
                         settled_at=settled_at if post_settle else None, after_fee_pnl=pnl,
                         inclusion_result=ev.EXCLUDED if reasons else ev.INCLUDED, exclusion_reasons=reasons))
    res.evidence_rows = out
    res.universe["post_settlement_first_observations_excluded"] = sum(post_settled.values())
    res.universe["post_settlement_first_observations_by_level"] = dict(sorted(post_settled.items()))
    inc = [r for r in out if r.inclusion_result == ev.INCLUDED]
    settled = [r for r in inc if r.after_fee_pnl is not None]
    if is_001:
        itf = [r for r in settled if r.extra["level"] == "ITF"]
        non = [r for r in settled if r.extra["level"] != "ITF"]
        m_itf, m_non = stats.mean_ci([r.after_fee_pnl for r in itf]), stats.mean_ci([r.after_fee_pnl for r in non])
        m_all = stats.mean_ci([r.after_fee_pnl for r in settled])
        n_itf = sum(1 for r in inc if r.extra["level"] == "ITF")
        acc = (_ci_pass(m_itf, -1) and m_non["mean"] is not None and m_itf["mean"] < m_non["mean"]) if itf else None
        econ = (m_non["mean"] is not None and m_all["mean"] is not None and m_non["mean"] > m_all["mean"]) if (non and settled) else None
        res.metrics = {"eligible_itf_n": n_itf, "eligible_all_n": len(inc), "settled_itf_n": len(itf),
                       "settled_non_itf_n": len(non), "itf_after_fee_pnl": m_itf, "non_itf_after_fee_pnl": m_non,
                       "combined_after_fee_pnl": m_all,
                       "minimum_n_applies_to": "ITF positive-edge rows (the subset the abstention is about)"}
        return _finish(res, cand, kind, eligible_n=n_itf, settled_n=len(itf),
                       unsettled=n_itf - len(itf), acc=acc, econ=econ)
    binary = [r for r in settled if r.settlement_result in ("yes", "no")]
    y = [_y(r.settlement_result) for r in binary]
    b_fair = stats.brier_terms([r.fair_probability for r in binary], y)
    b_mid = stats.brier_terms([r.kalshi_mid for r in binary], y)
    strict = [r for r in inc if r.strict_clv_executable is not None]
    clv = stats.mean_ci([r.strict_clv_executable for r in strict])
    pnl = stats.mean_ci([r.after_fee_pnl for r in settled])
    acc = (sum(b_fair) / len(b_fair) <= sum(b_mid) / len(b_mid)) if binary else None
    res.metrics = {"eligible_n": len(inc), "settled_n": len(settled), "strict_clv_n": len(strict),
                   "brier_fair_v1": (sum(b_fair) / len(b_fair)) if b_fair else None,
                   "brier_kalshi_mid": (sum(b_mid) / len(b_mid)) if b_mid else None,
                   "strict_executable_clv": clv, "after_fee_pnl": pnl,
                   "accuracy_condition_binding": "selected-row Brier must be no worse than the Kalshi mid's"}
    return _finish(res, cand, kind, eligible_n=len(inc), settled_n=len(settled), strict_n=len(strict),
                   unsettled=len(inc) - len(settled),
                   clv_pending=sum(1 for r in inc if r.strict_clv_executable is None and r.settlement_value is None),
                   acc=acc, clv=_ci_pass(clv, +1) if strict else None, econ=_ci_pass(pnl, +1) if settled else None,
                   clv_required=True)


# --------------------------------------------------------------------------------------- EC-003
def harvest_ec3_live(ctx, cand):
    from tennis_edge.confirmation.candidates import HarvestResult, _strict_close, _timing, harvest_ec3
    cid = cand["candidate_id"]
    start = _start(ctx, cid)
    if start is None:
        return _not_started(ctx, cand, KIND_TRADE, harvest_ec3)
    res = HarvestResult(cid, KIND_TRADE)
    rows, before = _producer_rows(ctx, "shadow_board_v1", start["effective_scorable_start"])
    res.universe = {"experiment_start": start, "history": _history(ctx, cand, start, before),
                    "rows_after_effective_start": len(rows)}
    runs = defaultdict(dict)                 # physical match -> first prediction run -> {is_a: row}
    first_run = {}
    for r in rows:
        if r.get("market_family") != "MATCH_WINNER" or r.get("tour") not in ("ATP", "WTA"):
            continue
        pm = r["physical_match_id"]
        first_run.setdefault(pm, r["predicted_at"])
        if r["predicted_at"] == first_run[pm]:
            runs[pm][bool(r.get("subject_is_a"))] = r
    ctx.quotes({s["ticker"] for sides in runs.values() for s in sides.values()})   # one capture pass
    post_settled = Counter()
    out = []
    for pmid, sides in runs.items():
        a = sides.get(True)
        if a is None:
            continue
        reasons = []
        thin = a.get("thinner_serve_points")
        if thin is None or not (EC3_MIN_EVIDENCE <= thin <= EC3_MAX_EVIDENCE):
            reasons.append(ev.R_RULE_FAILED)
        truth, tc = _timing(a["predicted_at"], a["event"], ctx.truths)
        if not _not_post_start(truth, tc):
            reasons.append(ev.R_TIMING_POST if tc.timing_class == POST_START else ev.R_TIMING_AMBIG)
        # the unit is the FIRST run of the physical match: if ANY of its match-winner contracts was already
        # terminal at that run's own timestamp, the whole observation is contaminated (no later run instead)
        settled_at = None
        hits = sorted(sat for s in sides.values()
                      for post, sat in [_settled_before_observation(ctx, s["ticker"], a["predicted_at"])] if post)
        if hits:
            reasons.append(ev.R_SETTLED_BEFORE_OBSERVATION)
            settled_at = hits[0]
            post_settled[_level_bucket(a["ticker"])] += 1
        sres, payout, _ = _pnl(ctx, a["ticker"], a["kalshi_ask"], a["fee"])
        # the position, if any: the side whose frozen fee-adjusted edge is positive at the ask
        pos = max((s for s in sides.values() if (s.get("fee_adjusted_edge") or -1) > 0),
                  key=lambda s: s["fee_adjusted_edge"], default=None)
        p_clv = p_pnl = None
        if pos is not None:
            cc, clv = _strict_close(ctx, pos["ticker"], truth, pos["predicted_at"], pos["kalshi_bid"],
                                    pos["kalshi_ask"], pos.get("displayed_size"), tc)
            p_clv = clv.clv_executable if clv.strict else None
            p_pnl = _pnl(ctx, pos["ticker"], pos["kalshi_ask"], pos["fee"])[2]
        reasons = tuple(dict.fromkeys(reasons))
        for x in reasons:
            res.exclusion_counts[x] += 1
        out.append(_base(cid, cand, start, a, model_version="gen2_dyn_hier_sr_v1",
                         fair_probability=a["gen2_blend_probability"], model_probability=a["gen1_elo_probability"],
                         kalshi_bid=a["kalshi_bid"], kalshi_ask=a["kalshi_ask"], kalshi_mid=a.get("kalshi_mid"),
                         kalshi_spread=a.get("spread"), fee=a["fee"], displayed_size=a.get("displayed_size"),
                         decision_edge=pos["fee_adjusted_edge"] if pos else None,
                         extra={"thinner_serve_points": thin, "position_ticker": pos["ticker"] if pos else None,
                                "position_pnl": p_pnl},
                         first_ball_confidence=truth.confidence if truth else None, timing_class=tc.timing_class,
                         strict_clv_executable=p_clv, settlement_result=sres, settlement_value=payout,
                         settled_at=settled_at, after_fee_pnl=p_pnl,
                         inclusion_result=ev.EXCLUDED if reasons else ev.INCLUDED, exclusion_reasons=reasons))
    res.evidence_rows = out
    res.universe["post_settlement_first_runs_excluded"] = sum(post_settled.values())
    res.universe["post_settlement_first_runs_by_level"] = dict(sorted(post_settled.items()))
    inc = [r for r in out if r.inclusion_result == ev.INCLUDED]
    binary = [r for r in inc if r.settlement_result in ("yes", "no")]
    y = [_y(r.settlement_result) for r in binary]
    bg = stats.brier_terms([r.fair_probability for r in binary], y)
    be = stats.brier_terms([r.model_probability for r in binary], y)
    bm = stats.brier_terms([r.kalshi_mid for r in binary], y)
    d_elo, d_mkt = stats.paired_ci(bg, be), stats.paired_ci(bg, bm)
    strict = [r for r in inc if r.strict_clv_executable is not None]
    clv = stats.mean_ci([r.strict_clv_executable for r in strict])
    ev_pos = stats.mean_ci([r.decision_edge for r in inc if r.decision_edge is not None])
    acc = None
    if binary:
        acc = bool(d_elo["mean"] is not None and d_elo["mean"] <= -EC3_BRIER_GAIN and d_elo["ci_high"] is not None
                   and d_elo["ci_high"] < 0 and d_mkt["mean"] <= EC3_MARKET_TOL)
    res.metrics = {"eligible_n": len(inc), "settled_n": len(binary), "strict_clv_n": len(strict),
                   "brier_gen2_blend": (sum(bg) / len(bg)) if bg else None,
                   "brier_gen1_elo": (sum(be) / len(be)) if be else None,
                   "brier_kalshi_mid": (sum(bm) / len(bm)) if bm else None,
                   "paired_gen2_minus_gen1": d_elo, "paired_gen2_minus_market": d_mkt,
                   "strict_executable_clv": clv, "after_fee_ev_of_positions": ev_pos,
                   "positions": sum(1 for r in inc if r.decision_edge is not None)}
    return _finish(res, cand, KIND_TRADE, eligible_n=len(inc), settled_n=len(binary), strict_n=len(strict),
                   unsettled=len(inc) - len(binary),
                   clv_pending=sum(1 for r in inc if r.strict_clv_executable is None and r.settlement_value is None),
                   acc=acc, clv=_ci_pass(clv, +1) if strict else None,
                   econ=(ev_pos["mean"] is not None and ev_pos["mean"] > 0) if ev_pos["n"] else None,
                   clv_required=True)


# --------------------------------------------------------------------------------------- EC-001 / EC-002
def _match_truth(ctx):
    """Completed-match sports truth from the canonical table (later truth, never an input to a prediction)."""
    if getattr(ctx, "_match_truth", None) is not None:
        return ctx._match_truth
    path = os.path.join(ctx.data_root, "processed", "matches.parquet")
    idx = defaultdict(list)
    if os.path.exists(path):
        import pandas as pd
        cols = ["winner_id", "loser_id", "tourney_date", "games_w", "games_l", "sets_w", "sets_l",
                "outcome_type", "completed"]
        df = pd.read_parquet(path, columns=cols)
        # the canonical table stores tourney_date as datetime.date objects: normalise once, never compare
        # a Timestamp with a date (that TypeError took the 2026-09-28 05:46Z harvest down)
        df["tourney_date"] = pd.to_datetime(df["tourney_date"], errors="coerce")
        df = df[df.tourney_date >= pd.Timestamp("2026-09-01")]
        for r in df.itertuples(index=False):
            key = tuple(sorted((str(r.winner_id), str(r.loser_id))))
            idx[key].append(r)
    ctx._match_truth = idx
    return idx


def _find_result(ctx, a_id, b_id, match_date):
    """The one completed match between these two players whose tournament started within three weeks
    before the match date. Zero or several candidates -> no truth (never a guess)."""
    import pandas as pd
    day = pd.Timestamp(match_date)
    cands = [r for r in _match_truth(ctx).get(tuple(sorted((str(a_id), str(b_id)))), [])
             if not pd.isna(r.tourney_date) and day - timedelta(days=21) <= pd.Timestamp(r.tourney_date) <= day]
    if len(cands) != 1:
        return None, ("NO_RESULT" if not cands else "AMBIGUOUS_RESULT")
    r = cands[0]
    if not r.completed or r.outcome_type != "COMPLETED":
        return None, "NOT_COMPLETED"
    a_won = str(r.winner_id) == str(a_id)
    return ({"sets_a": r.sets_w if a_won else r.sets_l, "sets_b": r.sets_l if a_won else r.sets_w,
             "games_a": r.games_w if a_won else r.games_l, "games_b": r.games_l if a_won else r.games_w}, "OK")


def _model4(ctx, cand, families, legacy, kind_metric):
    from tennis_edge.confirmation.candidates import HarvestResult, _timing
    cid = cand["candidate_id"]
    start = _start(ctx, cid)
    if start is None:
        return _not_started(ctx, cand, KIND_PRICING, legacy)
    res = HarvestResult(cid, KIND_PRICING)
    rows, before = _producer_rows(ctx, "model4_board_v1", start["effective_scorable_start"])
    fam_rows = [r for r in rows if r.get("market_family") in families]
    res.universe = {"experiment_start": start, "history": _history(ctx, cand, start, before),
                    "listed_contract_rows_after_effective_start": len(fam_rows),
                    "listed_contracts": len({r["ticker"] for r in fam_rows}),
                    "note": "rows exist only for contracts Kalshi actually listed; zero is a valid count"}
    first = {}
    for r in fam_rows:
        first.setdefault(r["physical_match_id"], r)       # first prediction run per physical match
    post_settled = Counter()
    out = []
    for pmid, r in first.items():
        reasons = []
        c = r.get("conditioning") or {}
        pm = c.get("p_market_a")
        if r.get("tour") not in ("ATP", "WTA") or not c.get("two_sided") or pm is None \
                or not (EC1_MKT_BAND[0] <= pm <= EC1_MKT_BAND[1]) or not r.get("conditioned_distribution"):
            reasons.append(ev.R_RULE_FAILED)
        truth, tc = _timing(r["predicted_at"], r.get("event") or "", ctx.truths)
        if not _not_post_start(truth, tc):
            reasons.append(ev.R_TIMING_POST if tc.timing_class == POST_START else ev.R_TIMING_AMBIG)
        # generic prospective invariant: the derivative or either conditioning match-winner contract already
        # terminal (exchange settlement_ts <= predicted_at) -> not prospective. Proven chronology only.
        hits = sorted(sat for t in (r.get("ticker"), c.get("mw_ticker_a"), c.get("mw_ticker_b"))
                      for post, sat in [_settled_before_observation(ctx, t, r["predicted_at"])] if post)
        if hits:
            reasons.append(ev.R_SETTLED_BEFORE_OBSERVATION)
            post_settled[_level_bucket(r.get("ticker"))] += 1
        result, why = _find_result(ctx, r["player_a_id"], r["player_b_id"], r["match_date"])
        m_fund = m_mc = None
        if result is not None and not reasons:
            m_fund, m_mc = kind_metric(r, result)
        reasons = tuple(dict.fromkeys(reasons))
        for x in reasons:
            res.exclusion_counts[x] += 1
        out.append(_base(cid, cand, start, r, model_version=r.get("model_version"),
                         fair_probability=r.get("conditioned_probability"),
                         model_probability=r.get("fundamental_probability"),
                         kalshi_bid=r.get("kalshi_bid"), kalshi_ask=r.get("kalshi_ask"),
                         kalshi_spread=r.get("spread"), fee=r.get("fee"), displayed_size=r.get("displayed_ask_size"),
                         extra={"match_code": r.get("match_code"), "result_status": why,
                                "metric_fundamental": m_fund, "metric_conditioned": m_mc,
                                "p_market_a": pm, "best_of": r.get("best_of")},
                         first_ball_confidence=truth.confidence if truth else None, timing_class=tc.timing_class,
                         settlement_result="COMPLETED" if result else None,
                         settled_at=hits[0] if hits else None,
                         inclusion_result=ev.EXCLUDED if reasons else ev.INCLUDED, exclusion_reasons=reasons))
    res.evidence_rows = out
    res.universe["post_settlement_first_runs_excluded"] = sum(post_settled.values())
    res.universe["post_settlement_first_runs_by_level"] = dict(sorted(post_settled.items()))
    inc = [r for r in out if r.inclusion_result == ev.INCLUDED]
    scored = [r for r in inc if r.extra["metric_fundamental"] is not None]
    d = stats.paired_ci([r.extra["metric_conditioned"] for r in scored], [r.extra["metric_fundamental"] for r in scored])
    return res, inc, scored, d


def _ll_exact(r, result):
    import math
    key = f"{result['sets_a']}-{result['sets_b']}"
    pf = (r["fundamental_distribution"]["set_score"] or {}).get(key, 0.0)
    pc = (r["conditioned_distribution"]["set_score"] or {}).get(key, 0.0)
    return -math.log(max(pf, 1e-6)), -math.log(max(pc, 1e-6))


def _mae_diff(r, result):
    actual = result["games_a"] - result["games_b"]
    return (abs(r["fundamental_distribution"]["e_game_diff_a"] - actual),
            abs(r["conditioned_distribution"]["e_game_diff_a"] - actual))


def harvest_ec1_live(ctx, cand):
    from tennis_edge.confirmation.candidates import harvest_ec1
    out = _model4(ctx, cand, ("EXACT_SET_SCORE",), harvest_ec1, _ll_exact)
    if not isinstance(out, tuple):
        return out
    res, inc, scored, d = out
    acc = (d["mean"] is not None and d["mean"] <= -EC1_LL_GAIN and d["ci_high"] is not None and d["ci_high"] < 0) if scored else None
    res.metrics = {"eligible_matches": len(inc), "scored_matches": len(scored),
                   "logloss_conditioned_minus_fundamental": d,
                   "after_fee_condition": "applies only to a trade derived from the candidate; none is taken"}
    return _finish(res, cand, KIND_PRICING, eligible_n=len(inc), settled_n=len(scored),
                   unsettled=len(inc) - len(scored), acc=acc)


def harvest_ec2_live(ctx, cand):
    from tennis_edge.confirmation.candidates import harvest_ec2
    out = _model4(ctx, cand, ("GAME_SPREAD", "TOTAL_GAMES"), harvest_ec2, _mae_diff)
    if not isinstance(out, tuple):
        return out
    res, inc, scored, d = out
    acc = (d["mean"] is not None and d["mean"] <= -EC2_MAE_GAIN and d["ci_high"] is not None and d["ci_high"] < 0) if scored else None
    res.metrics = {"eligible_matches": len(inc), "scored_matches": len(scored),
                   "game_diff_mae_conditioned_minus_fundamental": d,
                   "truth": "completed-match games from the canonical match table; retirements excluded"}
    return _finish(res, cand, KIND_PRICING, eligible_n=len(inc), settled_n=len(scored),
                   unsettled=len(inc) - len(scored), acc=acc)
