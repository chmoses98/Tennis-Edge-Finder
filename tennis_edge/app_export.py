"""Edge Finder app export for TENNIS: the assisted slate (plus human decisions, wagers and health) -> app/latest.

A PURE ADAPTER. It reads what the repository already produces and maps each internal object onto the vendored
contract (``contract/edge_finder_contract``); it computes no probability, selects nothing and changes nothing
the production pipelines write. See docs/APP_EXPORT.md.

    slate      research/assisted_slates/latest.json      -> events, markets, model_prices, research candidates
    decisions  research/assisted_decisions/records/...   -> recommendations (BET / PASS / WATCH, authority ASSISTED)
    wagers     research/assisted_decisions (AW records)  -> wagers (source MANUAL)
               <accounting-dir>/data/accounting/*.jsonl  -> wagers (source KALSHI_ROUTER) + settlements
    health     research/health_latest.json, frozen_producers/heartbeats.jsonl, assisted_decisions/PIPELINE_STATUS.json

Three different objects, never conflated: a model price is the frozen producer's number, a recommendation is a
human decision (or a research-only candidate the slate flagged), a wager is a bet the owner says they placed.

Stdlib + the repository's own stdlib-only loaders (``tennis_edge.assisted.slate``), so the slate workflow, which
installs nothing, can run it.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CONTRACT_DIR = os.path.join(REPO_ROOT, "contract")
if CONTRACT_DIR not in sys.path:
    sys.path.insert(0, CONTRACT_DIR)

from edge_finder_contract import board as cboard  # noqa: E402
from edge_finder_contract import build, freshness, ids, linkage, performance, publish, timeutil  # noqa: E402
from edge_finder_contract import health as chealth  # noqa: E402
from edge_finder_contract.routed_ledger import read_jsonl  # noqa: E402

from tennis_edge.assisted import ASSISTED_AUTHORITY, discrepancy as DS  # noqa: E402
from tennis_edge.assisted.slate import load_slate  # noqa: E402
from tennis_edge.assisted.store import SETTLEMENTS_FILE, AppendOnlyJsonl, RecordStore  # noqa: E402
from tennis_edge.firstball import start_times as ST  # noqa: E402

SPORT = "TENNIS"
SOURCE_REPO = "chmoses98/Tennis-Edge-Finder"
SOURCE_BRANCH = "tennis-data"
BET_AUTHORITY = "ASSISTED"
EVENT_SOURCE = "kalshi_event_ticker"
PARTICIPANT_SOURCE = "kalshi_player_name"
MARKET_SOURCE = "kalshi_capture (assisted slate)"
ROUTER_SETTLEMENT_SOURCE = "kalshi_router"

#: the slate's own cadence: a quote is FRESH <= 10 min and AGING <= 30 min (config/discrepancy_sanity.json);
#: the slate is rebuilt every six hours by RUN TENNIS and TENNIS-16 fails once it is 13 h old.
MARKET_THRESHOLDS = freshness.Thresholds(10 * 60, 30 * 60)
MODEL_THRESHOLDS = freshness.Thresholds(6 * 60 * 60, 13 * 60 * 60)
THRESHOLDS = {"market_data": MARKET_THRESHOLDS, "model": MODEL_THRESHOLDS}

#: a model-market gap the slate itself flags for review (REVIEW / HIGH_REVIEW / EXTREME; NORMAL and UNPRICED
#: are not disagreements). The band edges live in config/discrepancy_sanity.json; nothing is re-thresholded here.
DISAGREEMENT_BANDS = tuple(b for b in DS.BANDS if DS.BAND_RANK[b] >= DS.BAND_RANK[DS.REVIEW])
DECISION_STATUS = {"BET": "RECOMMENDED", "PASS": "PASS", "WATCH": "WATCH"}
DATA_QUALITY = {"ADEQUATE": "OK", "LIMITED": "DEGRADED", "POOR": "DEGRADED"}
ASSISTED_SETTLEMENT_RESULT = {"YES": None, "NO": None, "VOID_SCALAR": "SCALAR"}


class ExportError(RuntimeError):
    """The build cannot produce a consistent payload; the caller writes health only."""


# ---------------------------------------------------------------------------------------------- inputs
def _read_json(path: str):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def _jsonl_rows(path: str) -> list[dict]:
    rows = []
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    except OSError:
        return []
    return rows


def load_inputs(data_root: str, accounting_dir: str | None = None) -> dict:
    """Everything the export reads, with a warning (never an exception) for each OPTIONAL input that is absent.
    The slate is the one required input."""
    research = os.path.join(data_root, "research")
    warnings: list[str] = []
    slate_dir = os.path.join(research, "assisted_slates")
    slate = load_slate(slate_dir)
    if not isinstance(slate, dict) or not slate.get("slate_id") or not isinstance(slate.get("matches"), list):
        raise ExportError(f"no readable assisted slate at {os.path.join(slate_dir, 'latest.json')}")

    gates = _read_json(os.path.join(research, "health_latest.json"))
    if not isinstance(gates, list):
        warnings.append("research/health_latest.json not found: production gates are not reported")
        gates = []
    heartbeats = _jsonl_rows(os.path.join(research, "frozen_producers", "heartbeats.jsonl"))
    if not heartbeats:
        warnings.append("frozen_producers/heartbeats.jsonl not found: producer heartbeat not reported")
    store_root = os.path.join(research, "assisted_decisions")
    pipeline = _read_json(os.path.join(store_root, "PIPELINE_STATUS.json"))
    if not isinstance(pipeline, dict):
        warnings.append("assisted_decisions/PIPELINE_STATUS.json not found: assisted pipeline status not reported")
        pipeline = {}
    store = RecordStore(store_root)
    decisions = [r for r in store.records("decisions") if not r.get("_unreadable")] if os.path.isdir(store_root) else []
    assisted_wagers = [r for r in store.records("wagers") if not r.get("_unreadable")] if os.path.isdir(store_root) else []
    assisted_settlements = AppendOnlyJsonl(os.path.join(store_root, SETTLEMENTS_FILE)).rows() if os.path.isdir(store_root) else []

    routed_wagers: list[dict] = []
    routed_settlements: list[dict] = []
    if accounting_dir:
        base = Path(accounting_dir)
        routed_wagers = read_jsonl(base / "data" / "accounting" / "wagers.jsonl")
        routed_settlements = read_jsonl(base / "data" / "accounting" / "settlements.jsonl")
    else:
        warnings.append("no --accounting-dir: routed wagers (accounting-data branch) are not included")
    return {"slate": slate, "gates": gates, "heartbeats": heartbeats, "pipeline": pipeline, "decisions": decisions,
            "assisted_wagers": assisted_wagers, "assisted_settlements": assisted_settlements,
            "routed_wagers": routed_wagers, "routed_settlements": routed_settlements, "warnings": warnings}


# ---------------------------------------------------------------------------------------------- helpers
def _norm_name(name: str) -> str:
    return " ".join(str(name).split()).lower()


def _latest(stamps) -> str | None:
    real = [s for s in stamps if s]
    return max(real, key=timeutil.parse_ts) if real else None


def _participant(name, ticker) -> dict | None:
    if not name or not str(name).strip():
        return None
    return build.participant(sport=SPORT, participant_type="PLAYER", source=PARTICIPANT_SOURCE, source_id=_norm_name(name),
                             display_name=str(name).strip(), source_ids={"kalshi_match_winner_ticker": ticker})


def _start_fields(m: dict) -> tuple[str | None, str, str]:
    """(start_time_utc, start_time_source, start_time_confidence) from the slate's reconciled start block.
    A Kalshi day placeholder is PLACEHOLDER; a live schedule reading is VERIFIED / ESTIMATED by its own
    confidence; a plain Kalshi nominal is SCHEDULED."""
    st = m.get("start") or {}
    expected = st.get("current_expected_start")
    nominal = st.get("nominal_scheduled_start") or m.get("scheduled_start")
    src = st.get("start_time_source")
    conf = st.get("start_time_confidence")
    if expected and src and src != "KALSHI_NOMINAL":
        return expected, src, ("VERIFIED" if conf == ST.HIGH else "ESTIMATED" if conf in (ST.MEDIUM, ST.LOW) else "UNKNOWN")
    if expected:
        return expected, src or "KALSHI_NOMINAL", "SCHEDULED"
    if st.get("nominal_is_placeholder"):
        return nominal, "KALSHI_NOMINAL", "PLACEHOLDER"
    return nominal, "KALSHI_NOMINAL", "SCHEDULED"


def _event_status(start_status) -> str:
    if start_status == ST.STARTED:
        return "LIVE"
    if start_status == ST.NO_PLAY:
        return "CANCELLED"
    return "SCHEDULED"


def _side_value(p_yes, selection):
    if p_yes is None:
        return None
    return p_yes if selection == "YES" else round(1.0 - p_yes, 6)


def _event_from_match(m: dict, built_at) -> tuple[dict, dict] | None:
    """(event, participant ids by side) or None when the packet has no usable start time."""
    start_utc, src, conf = _start_fields(m)
    if not start_utc or not m.get("event_id"):
        return None
    mwt = m.get("match_winner_ticker") or {}
    players = m.get("players") or {}
    parts, by_side = [], {}
    for side in ("a", "b"):
        p = _participant(players.get(side), mwt.get(side))
        if p is not None:
            parts.append(p)
            by_side[side] = p["participant_id"]
    st = m.get("start") or {}
    checks = m.get("identity_checks") or {}
    dq = m.get("data_quality_check") or {}
    ev = build.event(
        sport=SPORT, source=EVENT_SOURCE, source_id=m["event_id"], start_time_utc=start_utc, participants=parts,
        league=m.get("tour"), season=str(timeutil.parse_ts(start_utc).year), competition=m.get("competition"),
        status=_event_status(st.get("start_status") or m.get("start_status")),
        start_time_source=src, start_time_confidence=conf,
        source_ids={"match_key": m.get("match_key"), "physical_match_id": m.get("physical_match_id"),
                    "match_code": m.get("match_code")},
        schedule_updated_at=st.get("evaluated_at"), last_updated_at=built_at,
        extensions={
            "level": m.get("level"), "level_bucket": m.get("level_bucket"), "discipline": m.get("discipline"),
            "round": m.get("round"), "surface": m.get("surface"), "surface_bucket": m.get("surface_bucket"),
            "start_status": st.get("start_status") or m.get("start_status"), "bet_allowed": st.get("bet_allowed"),
            "status_reasons": list(st.get("status_reasons") or []), "nominal_is_placeholder": st.get("nominal_is_placeholder"),
            "nominal_scheduled_start": st.get("nominal_scheduled_start"), "live_source_covered": st.get("live_source_covered"),
            "first_ball_status": (m.get("first_ball") or {}).get("status"),
            "match_winner_ticker": dict(mwt), "identity_check_status": DS.identity_status(checks) if checks else None,
            "data_quality_status": dq.get("data_quality_status"), "model_validity": m.get("model_validity"),
            "warnings": list(m.get("warnings") or []),
        })
    return ev, by_side


def _market_from_row(r: dict, event_id: str, by_side: dict) -> dict:
    k = r.get("kalshi") or {}
    subj = r.get("subject_is_a")
    participant_id = by_side.get("a" if subj is True else "b") if isinstance(subj, bool) else None
    return build.market(
        sport=SPORT, kalshi_ticker=r["ticker"], market_family=r.get("market_family"),
        yes_description=r.get("yes_means") or r.get("description") or f"YES on {r['ticker']}",
        source=MARKET_SOURCE, event_id=event_id, kalshi_event_ticker=r.get("event"),
        market_type=r.get("expression"), participant_id=participant_id,
        side="PARTICIPANT" if isinstance(subj, bool) else None, line=r.get("line"),
        yes_bid=k.get("bid"), yes_ask=k.get("ask"), no_ask=k.get("no_ask"), market_probability=k.get("mid"),
        volume=k.get("volume_24h"), open_interest=k.get("open_interest"), market_status="OPEN",
        captured_at=k.get("quote_captured_at"), raw_market_reference=r.get("description"),
        extensions={"set_index": r.get("set_index"), "exact_score": r.get("exact_score"), "subject": r.get("subject"),
                    "discrepancy_band": r.get("discrepancy_band"), "market_freshness_status": r.get("market_freshness_status"),
                    "spread": k.get("spread"), "bid_size": k.get("bid_size"), "ask_size": k.get("ask_size"),
                    "taker_fee_at_ask": k.get("taker_fee_at_ask"), "quote_age_s": k.get("quote_age_s"),
                    "warnings": list(r.get("warnings") or [])})


def _model_price_from_row(r: dict, market: dict, run_id: str, built_at, now) -> dict | None:
    p = r.get("model_probability_yes")
    if p is None:
        return None                                     # doubles / unmapped identity: no producer speaks for it
    src = r.get("model_probability_source")
    mo = r.get("model") or {}
    env = (mo.get("fair_v1_envelope") if (src or "").startswith("fair_v1")
           else mo.get("projection_v2_envelope") if (src or "").startswith("projection_v2") else None)
    return build.model_price(
        run_id=run_id, market_id=market["market_id"], fair_probability=p, generated_at=built_at,
        event_id=market["event_id"], model_version=src,
        lower_bound=env[0] if env else None, upper_bound=env[1] if env else None,
        market_probability=(r.get("kalshi") or {}).get("mid"), inputs_as_of=(r.get("kalshi") or {}).get("quote_captured_at"),
        freshness_status=freshness.status_for(built_at, thresholds=MODEL_THRESHOLDS, now=now),
        data_quality_status=DATA_QUALITY.get(r.get("data_quality_status"), "UNKNOWN"),
        support_status=r.get("discrepancy_sanity_status"),
        extensions={"projection_v2": mo.get("projection_v2"), "projection_v2_grade": mo.get("projection_v2_grade"),
                    "projection_v2_tags": list(mo.get("projection_v2_tags") or []),
                    "projection_v2_envelope": mo.get("projection_v2_envelope"), "incumbent": mo.get("incumbent"),
                    "gen1": mo.get("gen1"), "gen2": mo.get("gen2"), "fair_v1": mo.get("fair_v1"),
                    "model4_conditioned": mo.get("model4_conditioned"), "model4_fundamental": mo.get("model4_fundamental"),
                    "model_uncertainty": mo.get("model_uncertainty"), "selector_v1": mo.get("selector_v1"),
                    "qualification_ok": mo.get("qualification_ok"), "model_side_edges": dict(r.get("model_side_edges") or {}),
                    "model_preferred_side": r.get("model_preferred_side"), "model_market_gap_pp": r.get("model_market_gap_pp"),
                    "discrepancy_band": r.get("discrepancy_band"), "discrepancy_sanity_status": r.get("discrepancy_sanity_status"),
                    "discrepancy_reason_tags": list(r.get("discrepancy_reason_tags") or []),
                    "external_confirmation_status": r.get("external_confirmation_status"),
                    "slate_data_quality_status": r.get("data_quality_status")})


def _candidate_from_row(r: dict, m: dict, market: dict, run_id: str, slate: dict) -> dict | None:
    """A slate contract whose model-market gap the slate flags (REVIEW or worse) on a match where a bet is not
    blocked by start status. RESEARCH_ONLY: the slate says a large gap is a question, not an edge. When the
    slate's own sanity status is DATA_WARNING ("PASS UNTIL RECHECKED") the row is NOT_PLAYABLE."""
    st = m.get("start") or {}
    sel = r.get("model_preferred_side")
    if r.get("discrepancy_band") not in DISAGREEMENT_BANDS or sel not in ("YES", "NO") or not st.get("bet_allowed"):
        return None
    k = r.get("kalshi") or {}
    p_yes = r.get("model_probability_yes")
    edges = r.get("model_side_edges") or {}
    disc = r.get("discrepancy") or {}
    not_playable = r.get("discrepancy_sanity_status") == DS.DATA_WARNING
    return build.recommendation(
        sport=SPORT, source_repo=SOURCE_REPO, event_id=market["event_id"], market_id=market["market_id"], run_id=run_id,
        selection=sel, market_description=market["yes_description"], created_at=slate["built_at"],
        status="NOT_PLAYABLE" if not_playable else "RESEARCH_CANDIDATE", authority="RESEARCH_ONLY", research_only=True,
        native_id=f"{slate['slate_id']}|{r['ticker']}|{sel}",
        current_probability=_side_value(k.get("mid"), sel), current_price=k.get("ask") if sel == "YES" else k.get("no_ask"),
        fair_probability=_side_value(p_yes, sel), edge=edges.get(sel),
        reason_not_playable=disc.get("display_status") if not_playable else None,
        data_freshness=r.get("market_freshness_status") or "UNKNOWN",
        source_ids={"slate_id": slate["slate_id"], "kalshi_ticker": r["ticker"], "match_key": m.get("match_key")},
        extensions={"discrepancy_band": r.get("discrepancy_band"), "discrepancy_sanity_status": r.get("discrepancy_sanity_status"),
                    "display_status": disc.get("display_status"), "discrepancy_reason_tags": list(r.get("discrepancy_reason_tags") or []),
                    "model_market_gap_pp": r.get("model_market_gap_pp"), "model_probability_yes": p_yes,
                    "model_probability_source": r.get("model_probability_source"), "model_side_edges": dict(edges),
                    "identity_check_status": r.get("identity_check_status"), "ticker_orientation_status": r.get("ticker_orientation_status"),
                    "external_confirmation_status": r.get("external_confirmation_status"), "start_status": st.get("start_status"),
                    "slate_authority": slate.get("authority")})


def _event_from_decision(d: dict, built_at) -> dict | None:
    """A decision on a match that has left the slate still needs its event on the board."""
    if not d.get("event_id") or not d.get("scheduled_start"):
        return None
    players = d.get("players") or {}
    parts = [p for p in (_participant(players.get(s), None) for s in ("a", "b")) if p is not None]
    return build.event(sport=SPORT, source=EVENT_SOURCE, source_id=d["event_id"], start_time_utc=d["scheduled_start"],
                       participants=parts, league=d.get("tour"), season=str(timeutil.parse_ts(d["scheduled_start"]).year),
                       competition=d.get("competition"), status="UNKNOWN", start_time_source="KALSHI_NOMINAL",
                       start_time_confidence="UNKNOWN",
                       source_ids={"physical_match_id": d.get("physical_match_id"), "match_code": d.get("match_code")},
                       last_updated_at=built_at,
                       extensions={"level": d.get("level"), "level_bucket": d.get("level_bucket"), "surface": d.get("surface"),
                                   "from_decision_record": d.get("decision_id"), "warnings": ["MATCH_NOT_ON_CURRENT_SLATE"]})


def _recommendation_from_decision(d: dict, market: dict, run_id: str) -> dict:
    sel = d["side"]
    p_yes = d.get("chatgpt_fair_probability")
    mid = d.get("market_implied_probability")
    return build.recommendation(
        sport=SPORT, source_repo=SOURCE_REPO, event_id=market["event_id"], market_id=market["market_id"], run_id=run_id,
        selection=sel, market_description=d.get("market_description") or market["yes_description"],
        created_at=d["created_at"], status=DECISION_STATUS[d["decision"]], authority=BET_AUTHORITY,
        research_only=d["decision"] != "BET", native_id=d["decision_id"],
        current_probability=_side_value(mid, sel), current_price=d.get("side_entry_price"),
        fair_probability=_side_value(p_yes, sel),
        edge=(round(_side_value(p_yes, sel) - d["side_entry_price"] - (d.get("side_fee") or 0.0), 6)
              if p_yes is not None and d.get("side_entry_price") is not None else None),
        bet_up_to_probability=d.get("bet_up_to_probability"), bet_up_to_price=d.get("bet_up_to_price"),
        confidence=d.get("chatgpt_confidence"), stake_units=d.get("stake_units_if_bet"),
        reason_not_playable=None,
        data_freshness=freshness.classify(d.get("market_quote_age_seconds"), MARKET_THRESHOLDS),
        source_ids={"decision_id": d["decision_id"], "slate_id": d.get("slate_id"), "physical_match_id": d.get("physical_match_id"),
                    "kalshi_ticker": d["ticker"]},
        extensions={"decision": d["decision"], "model_agreement_state": d.get("model_agreement_state"),
                    "model_preferred_side": d.get("model_preferred_side"), "chatgpt_preferred_side": d.get("chatgpt_preferred_side"),
                    "model_probability_yes": d.get("model_probability_yes"), "model_probability_source": d.get("model_probability_source"),
                    "discrepancy_band": d.get("discrepancy_band"), "discrepancy_sanity_status": d.get("discrepancy_sanity_status"),
                    "pass_reason_if_pass": d.get("pass_reason_if_pass"), "factor_tags": list(d.get("factor_tags") or []),
                    "chosen_expression": d.get("chosen_expression"), "recommended_price": d.get("recommended_price"),
                    "actual_wagered": d.get("actual_wagered"), "start_status_at_decision": d.get("start_status_at_decision"),
                    "authority": d.get("authority") or ASSISTED_AUTHORITY, "automated_execution": False})


def _routed_wager(w: dict, event_id) -> dict:
    return build.wager(sport=SPORT, kalshi_ticker=w["market_ticker"], selection=w["side"], contracts=w["contracts"],
                       stake=w["stake"], average_price=w["execution_price"], placed_at=w["executed_at"], source="KALSHI_ROUTER",
                       destination_repo=SOURCE_REPO, source_bet_key=w["source_bet_key"], event_id=event_id,
                       side=w.get("execution_action"), fees=w.get("fees_paid"),
                       source_ids={"ledger_wager_id": w.get("wager_id"), "import_batch_id": w.get("import_batch_id")},
                       extensions={"game_date": w.get("game_date"), "entry_method": w.get("entry_method"),
                                   "fee_state": w.get("fee_state"), "venue": w.get("venue")})


def _routed_settlement(s: dict, wager: dict) -> dict:
    established = s.get("gross_return") is not None and s.get("net_profit_loss") is not None
    result = s.get("result")
    return build.settlement(wager_id=wager["wager_id"], market_id=wager["market_id"],
                            result=result if result in ("WON", "LOST") else ("SCALAR" if established else "UNKNOWN"),
                            settled_at=s["settled_at"], source=ROUTER_SETTLEMENT_SOURCE,
                            verification_status="EXCHANGE_CONFIRMED" if established else "UNVERIFIED",
                            gross_payout=s.get("gross_return"), net_pnl=s.get("net_profit_loss"),
                            refusals=s.get("refusals") or [],
                            source_ids={"ledger_settlement_id": s.get("settlement_id"), "source_bet_key": s.get("source_bet_key")},
                            extensions={"economics_version": s.get("economics_version"), "venue": s.get("venue"),
                                        "exchange_result": result})


def _assisted_wager(w: dict, event_id) -> dict:
    status = w.get("status")
    return build.wager(sport=SPORT, kalshi_ticker=w["ticker"], selection=w["side"], contracts=w["contracts"],
                       stake=w["stake_dollars"], average_price=w["entry_price"], placed_at=w["placed_at"], source="MANUAL",
                       destination_repo=SOURCE_REPO, native_id=w["wager_id"], event_id=event_id, fees=w.get("fees"),
                       settlement_status="VOID" if status in ("CANCELLED", "VOIDED_BY_EXCHANGE") else "PENDING",
                       source_ids={"assisted_wager_id": w["wager_id"], "decision_id": w.get("decision_id"),
                                   "external_order_id": w.get("external_order_id")},
                       extensions={"status": status, "entry_source": w.get("source"), "decision_was_bet": w.get("decision_was_bet"),
                                   "placed_after_first_ball": w.get("placed_after_first_ball"),
                                   "authority": w.get("authority") or ASSISTED_AUTHORITY})


def _assisted_settlement(s: dict, wager: dict) -> dict:
    res = s.get("settlement_result")
    if res in ("YES", "NO"):
        result = "WON" if s.get("side_won") else "LOST"
    else:
        result = ASSISTED_SETTLEMENT_RESULT.get(res) or "UNKNOWN"
    return build.settlement(wager_id=wager["wager_id"], market_id=wager["market_id"], result=result,
                            settled_at=s.get("exchange_settled_at") or s["settled_at"], source=str(s.get("settled_by") or "assisted_settle"),
                            verification_status="EXCHANGE_CONFIRMED" if s.get("settlement_source") == "kalshi_capture_settlements" else "UNVERIFIED",
                            winning_side=res if res in ("YES", "NO") else None, settlement_value=s.get("settlement_value_yes"),
                            fees=s.get("fees"), net_pnl=s.get("net_pnl"),
                            source_ids={"assisted_settlement_id": s.get("settlement_id"), "decision_id": s.get("decision_id"),
                                        "assisted_wager_id": s.get("wager_id")},
                            extensions={"revision": s.get("revision"), "gross_pnl": s.get("gross_pnl"), "roi": s.get("roi"),
                                        "strict_executable_clv": s.get("strict_executable_clv"),
                                        "clv_timing_class": s.get("clv_timing_class"),
                                        "post_start_violation": s.get("post_start_violation")})


def _latest_assisted_settlements(rows: list[dict]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for r in rows:
        if r.get("row_kind") != "WAGER" or not r.get("wager_id"):
            continue
        prior = out.get(r["wager_id"])
        if prior is None or (r.get("revision") or 0) > (prior.get("revision") or 0):
            out[r["wager_id"]] = r
    return out


def _settle(wager: dict, settlement: dict) -> dict:
    wager["settlement_id"] = settlement["settlement_id"]
    wager["settlement_status"] = "SETTLED"
    wager["payout"] = settlement.get("gross_payout")
    wager["profit_loss"] = settlement.get("net_pnl")
    return wager


# ---------------------------------------------------------------------------------------------- build
def build_documents(inputs: dict, *, now, commit_sha=None, workflow_run_id=None) -> dict:
    """Every app document from the loaded inputs. Deterministic for the same inputs and ``now``."""
    slate = inputs["slate"]
    built_at = timeutil.to_iso(slate["built_at"])
    now_iso = timeutil.to_iso(now)
    warnings = list(inputs.get("warnings") or [])
    run_id = ids.run_id(SPORT, SOURCE_REPO, slate["slate_id"], generated_at=built_at)

    events: list[dict] = []
    markets: list[dict] = []
    model_prices: list[dict] = []
    recommendations: list[dict] = []
    event_by_kalshi: dict[str, str] = {}
    market_by_ticker: dict[str, dict] = {}
    for m in slate["matches"]:
        built = _event_from_match(m, built_at)
        if built is None:
            warnings.append(f"match {m.get('match_key')} has no start time or event ticker; left off the board")
            continue
        ev, by_side = built
        if ev["event_id"] in event_by_kalshi.values():
            warnings.append(f"duplicate event ticker {m.get('event_id')} on the slate; second packet skipped")
            continue
        events.append(ev)
        event_by_kalshi[m["event_id"]] = ev["event_id"]
        for r in m.get("markets") or []:
            if r.get("ticker") in market_by_ticker:
                warnings.append(f"duplicate ticker {r.get('ticker')} on the slate; second row skipped")
                continue
            mk = _market_from_row(r, ev["event_id"], by_side)
            markets.append(mk)
            market_by_ticker[mk["kalshi_ticker"]] = mk
            mp = _model_price_from_row(r, mk, run_id, built_at, now)
            if mp is not None:
                model_prices.append(mp)
            rec = _candidate_from_row(r, m, mk, run_id, slate)
            if rec is not None:
                recommendations.append(rec)

    # ---- human decisions (the assisted track): RECOMMENDED / PASS / WATCH, authority ASSISTED
    for d in inputs.get("decisions") or []:
        if d.get("decision") not in DECISION_STATUS or not d.get("ticker") or d.get("side") not in ("YES", "NO"):
            warnings.append(f"decision {d.get('decision_id')} is malformed; not exported")
            continue
        ticker = str(d["ticker"]).upper()
        mk = market_by_ticker.get(ticker)
        if mk is None:
            ev_id = event_by_kalshi.get(d.get("event_id"))
            if ev_id is None:
                ev = _event_from_decision(d, built_at)
                if ev is None:
                    warnings.append(f"decision {d.get('decision_id')} names no event/start; not exported")
                    continue
                if ev["event_id"] not in event_by_kalshi.values():
                    events.append(ev)
                    event_by_kalshi[d["event_id"]] = ev["event_id"]
                ev_id = ev["event_id"]
            mk = build.market_stub(sport=SPORT, kalshi_ticker=ticker, market_family=d.get("market_family"),
                                   yes_description=d.get("market_description"), event_id=ev_id, source="assisted_decision")
            markets.append(mk)
            market_by_ticker[ticker] = mk
        recommendations.append(_recommendation_from_decision(d, mk, run_id))

    # ---- wagers: routed (accounting ledger) and human-recorded (assisted track). Never linked by hand.
    wagers: list[dict] = []
    settlements: list[dict] = []
    clv_values: dict[str, float] = {}

    def _market_for(ticker: str, label: str) -> dict:
        t = str(ticker).strip().upper()
        mk = market_by_ticker.get(t)
        if mk is None:
            mk = build.market_stub(sport=SPORT, kalshi_ticker=t, source=label)
            markets.append(mk)
            market_by_ticker[t] = mk
        return mk

    routed_by_key = {}
    for w in inputs.get("routed_wagers") or []:
        mk = _market_for(w["market_ticker"], "ledger")
        wg = _routed_wager(w, mk["event_id"])
        routed_by_key[w["source_bet_key"]] = wg
        wagers.append(wg)
    for s in inputs.get("routed_settlements") or []:
        wg = routed_by_key.get(s.get("source_bet_key"))
        if wg is None:
            warnings.append("routed settlement without its wager on the ledger; not exported")
            continue
        st = _routed_settlement(s, wg)
        settlements.append(st)
        _settle(wg, st)
    assisted_by_id = {}
    for w in inputs.get("assisted_wagers") or []:
        mk = _market_for(w["ticker"], "assisted_wager")
        wg = _assisted_wager(w, mk["event_id"])
        assisted_by_id[w["wager_id"]] = wg
        wagers.append(wg)
    for wid, s in sorted(_latest_assisted_settlements(inputs.get("assisted_settlements") or []).items()):
        wg = assisted_by_id.get(wid)
        if wg is None:
            continue
        st = _assisted_settlement(s, wg)
        settlements.append(st)
        _settle(wg, st)
        if s.get("strict_executable_clv") is not None:
            clv_values[wg["wager_id"]] = float(s["strict_executable_clv"])
    wagers = [linkage.apply_links(w, model_prices, recommendations, markets) for w in wagers]

    # ---- run, health, board, performance, detail
    gates = inputs.get("gates") or []
    failing = [f"{g.get('gate')} {g.get('name')} {g.get('status')}" for g in gates if g.get("status") == "FAIL"]
    errors = [x for x in failing if str(x).startswith("TENNIS-16 ")]
    heartbeat = max((h for h in inputs.get("heartbeats") or [] if h.get("ran_at")), key=lambda h: timeutil.parse_ts(h["ran_at"]), default=None)
    pipeline = inputs.get("pipeline") or {}
    sha = commit_sha or (heartbeat or {}).get("code_sha") or pipeline.get("code_sha")
    last_capture = _latest([m.get("captured_at") for m in markets])
    src = slate.get("sources") or {}
    run = build.run(sport=SPORT, repo=SOURCE_REPO, completed_at=built_at, scope="assisted_slate", status="SUCCESS",
                    native_run_id=slate["slate_id"], commit_sha=sha, workflow_run_id=workflow_run_id,
                    model_version=slate.get("slate_version"), started_at=None,
                    events_requested=(slate.get("counts") or {}).get("matches"), events_processed=len(events),
                    markets_discovered=(slate.get("counts") or {}).get("markets") or len(markets), markets_priced=len(model_prices),
                    recommendations_created=len(recommendations),
                    data_sources=["kalshi_capture", "shadow_board_v1", "model4_board_v1", "gen1_ledger", "external_v1", "firstball_store"],
                    input_freshness={"kalshi": last_capture, "shadow_board": src.get("shadow_last"), "model4": src.get("model4_last"),
                                     "gen1_ledger": src.get("ledger_last"), "external": src.get("external_last")},
                    warnings=warnings + failing, errors=errors,
                    source_ids={"slate_id": slate["slate_id"], "content_sha256": slate.get("content_sha256"),
                                "discrepancy_version": (slate.get("discrepancy_sanity") or {}).get("version")})
    extra = {}
    if pipeline.get("last_run_at"):
        extra["assisted_pipeline"] = chealth.component(pipeline["last_run_at"], thresholds=MODEL_THRESHOLDS, now=now, required=False,
                                                       detail=pipeline.get("evidence_state"))
    if heartbeat is not None:
        extra["frozen_producers"] = chealth.component(heartbeat["ran_at"], thresholds=MODEL_THRESHOLDS, now=now, required=False,
                                                      detail=heartbeat.get("producer"))
    for g in gates:
        if g.get("gate") == "TENNIS-16":
            extra["assisted_pipeline_gate"] = {"status": "OK" if g.get("status") == "PASS" else "DEGRADED" if g.get("status") == "FAIL" else "UNKNOWN",
                                               "as_of": None, "age_seconds": None, "detail": f"{g.get('gate')} {g.get('status')}"}
    health = chealth.build_health(
        sport=SPORT, run_id=run_id, bet_authority=BET_AUTHORITY, last_market_capture=last_capture, last_model_generated=built_at,
        last_successful_run=now_iso, payload_run_id=run_id, payload_available=True, export_failed=False, commit_sha=sha,
        next_scheduled_run=slate.get("refresh_due_by"),
        router_as_of=_latest([w["placed_at"] for w in wagers if w["source"] == "KALSHI_ROUTER"]),
        settlement_as_of=_latest([s["settled_at"] for s in settlements]),
        thresholds=THRESHOLDS, warnings=warnings + failing, errors=errors, extra_components=extra, now=now, generated_at=now)
    board = cboard.build_board(sport=SPORT, run_id=run_id, generated_at=now, events=events, markets=markets, model_prices=model_prices,
                               recommendations=recommendations, wagers=wagers, health=health, thresholds=THRESHOLDS, now=now)
    perf = performance.build_performance(sport=SPORT, run_id=run_id, generated_at=now, wagers=wagers, settlements=settlements,
                                         markets=markets, recommendations=recommendations, clv_values=clv_values,
                                         notes=["routed wagers come from the accounting-data ledger; assisted-track wagers are human-recorded",
                                                "CLV only where the assisted settler established a strict pregame close"])
    freshness_of_row = {row["event_id"]: row["data_freshness"] for row in board["items"]}
    packets = {m.get("event_id"): m for m in slate["matches"]}
    documents = {
        "events": build.collection("events", SPORT, run_id, now, events),
        "markets": build.collection("markets", SPORT, run_id, now, markets),
        "model_prices": build.collection("model_prices", SPORT, run_id, now, model_prices),
        "recommendations": build.collection("recommendations", SPORT, run_id, now, recommendations),
        "theses": build.collection("theses", SPORT, run_id, now, []),
        "wagers": build.collection("wagers", SPORT, run_id, now, wagers),
        "settlements": build.collection("settlements", SPORT, run_id, now, settlements),
        "runs": build.collection("runs", SPORT, run_id, now, [run]),
        "board": board, "performance": perf,
    }
    for ev in events:
        packet = packets.get(ev["source_ids"].get(EVENT_SOURCE)) or {}
        mc = packet.get("model_context") or {}
        context = {"players": packet.get("players"), "start": {k: v for k, v in (packet.get("start") or {}).items() if k != "start_time_candidates"},
                   "first_ball": packet.get("first_ball"), "warnings": packet.get("warnings"),
                   "model_context": {"player_a_win": mc.get("player_a_win"), "model_uncertainty": mc.get("model_uncertainty"),
                                     "data_quality": mc.get("data_quality"), "selector_v1": mc.get("selector_v1"),
                                     "model_rows_predicted_at": mc.get("model_rows_predicted_at")},
                   "model_validity": packet.get("model_validity"), "external_context": packet.get("external_context"),
                   "identity_checks": packet.get("identity_checks"), "data_quality_check": packet.get("data_quality_check"),
                   "frozen_rule_context": packet.get("frozen_rule_context"), "available_expressions": packet.get("available_expressions")}
        documents[f"event_detail/{ev['event_id']}"] = cboard.build_event_detail(
            sport=SPORT, run_id=run_id, generated_at=now, event=ev, markets=markets, model_prices=model_prices,
            recommendations=recommendations, theses=[], wagers=wagers, settlements=settlements, context=context,
            data_freshness=freshness_of_row.get(ev["event_id"], "UNKNOWN"))
    freshness_doc = {
        "kalshi": {"as_of": last_capture, "status": freshness.status_for(last_capture, thresholds=MARKET_THRESHOLDS, now=now)},
        "model": {"as_of": built_at, "status": freshness.status_for(built_at, thresholds=MODEL_THRESHOLDS, now=now)},
    }
    return {"documents": documents, "health": health, "run_id": run_id, "generated_at": now_iso, "commit_sha": sha,
            "model_version": slate.get("slate_version"), "freshness": freshness_doc, "warnings": warnings + failing,
            "slate_id": slate["slate_id"]}


def export(data_root: str, out: str, *, now=None, accounting_dir: str | None = None, commit_sha=None, workflow_run_id=None) -> dict:
    """Build and publish atomically. Raises on any problem WITHOUT touching an existing payload."""
    now = now or timeutil.now_utc()
    inputs = load_inputs(data_root, accounting_dir)
    built = build_documents(inputs, now=now, commit_sha=commit_sha, workflow_run_id=workflow_run_id)
    manifest = publish.publish(root=Path(out), sport=SPORT, run_id=built["run_id"], generated_at=now, documents=built["documents"],
                               source_repo=SOURCE_REPO, source_branch=SOURCE_BRANCH, commit_sha=built["commit_sha"],
                               model_version=built["model_version"], status="SUCCESS", freshness=built["freshness"],
                               warnings=built["warnings"], health=built["health"])
    manifest["slate_id"] = built["slate_id"]
    return manifest


def failure_health(out: str, exc: BaseException, *, now, commit_sha=None) -> dict:
    """The health document for a failed attempt: export_failed, last-known-good payload (if any) left alone."""
    prev = publish.read_manifest(Path(out))
    fr = (prev or {}).get("freshness") or {}
    run_id = (prev or {}).get("run_id") or ids.run_id(SPORT, SOURCE_REPO, None, generated_at=timeutil.to_iso(now))
    return chealth.build_health(
        sport=SPORT, run_id=run_id, bet_authority=BET_AUTHORITY,
        last_market_capture=(fr.get("kalshi") or {}).get("as_of"), last_model_generated=(fr.get("model") or {}).get("as_of"),
        last_successful_run=(prev or {}).get("generated_at"), payload_run_id=(prev or {}).get("run_id"),
        payload_available=prev is not None, export_failed=True, commit_sha=commit_sha or (prev or {}).get("commit_sha"),
        thresholds=THRESHOLDS, errors=[f"{type(exc).__name__}: {exc}"], now=now, generated_at=now)


def run_cli(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Export the TENNIS assisted slate, decisions, wagers and health to the Edge Finder app contract")
    ap.add_argument("--out", default=os.path.join("data", "app", "latest"))
    ap.add_argument("--data-root", default="data", help="the data directory (<checkout>/tennis-edge-finder/data on tennis-data)")
    ap.add_argument("--accounting-dir", default=None, help="a checkout of the accounting-data branch (routed wagers)")
    ap.add_argument("--now", default=None, help="ISO timestamp with zone; default: the real clock")
    ap.add_argument("--commit-sha", default=None)
    ap.add_argument("--workflow-run-id", default=None)
    a = ap.parse_args(argv)
    now = timeutil.parse_ts(a.now) if a.now else timeutil.now_utc()
    try:
        manifest = export(a.data_root, a.out, now=now, accounting_dir=a.accounting_dir, commit_sha=a.commit_sha,
                          workflow_run_id=a.workflow_run_id)
    except Exception as exc:  # noqa: BLE001  -- the failure path is the point: health only, payload untouched, red job
        health = failure_health(a.out, exc, now=now, commit_sha=a.commit_sha)
        publish.write_health_only(Path(a.out), health)
        print(f"app export FAILED ({type(exc).__name__}): {exc}", file=sys.stderr)
        print(f"health.json written with export_failed=True (overall {health['overall_status']}); payload left as last-known-good",
              file=sys.stderr)
        return 1
    counts = manifest.get("counts") or {}
    print(f"app export OK: run {manifest['run_id']} slate {manifest.get('slate_id')} -> {a.out}")
    print("  " + " ".join(f"{k}={counts.get(k)}" for k in ("events", "markets", "model_prices", "recommendations", "wagers", "settlements")))
    return 0
