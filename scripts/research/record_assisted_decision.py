#!/usr/bin/env python3
"""Record a ChatGPT-assisted handicapping decision (or its wager, postmortem or later evidence).

Structured JSON in, one immutable record out. The recorder validates the identifiers and the market,
refuses a decision made after an observed first ball, preserves the market price at decision time,
generates the id, and writes a write-once record file; it never edits or overwrites anything.

  # a decision (BET / PASS / WATCH)
  python scripts/research/record_assisted_decision.py --input decision.json
  echo '{...}' | python scripts/research/record_assisted_decision.py
  # the wager the person actually placed, linked to its decision
  python scripts/research/record_assisted_decision.py --kind wager --json '{"decision_id": "AD-...", ...}'
  # print an input template
  python scripts/research/record_assisted_decision.py --template decision

In production the same CLI runs inside the `TENNIS assisted record` workflow (workflow_dispatch), which
publishes the new record to the `tennis-data` branch. No order is ever placed by anything here.
Exit status: 0 recorded (or valid, with --dry-run), 2 refused, 1 unexpected error.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.assisted import record as R                       # noqa: E402
from tennis_edge.assisted.schema import AssistedValidationError     # noqa: E402
from tennis_edge.assisted.store import RecordStore                  # noqa: E402
from tennis_edge.producers.records import code_sha                  # noqa: E402

TEMPLATES = {
    "decision": {
        "ticker": "KXATPMATCH-26OCT01AAABBB-AAA", "side": "YES", "decision": "BET",
        "created_at": "2026-10-01T09:15:00+00:00",
        "kalshi_bid": 0.47, "kalshi_ask": 0.48,
        "chatgpt_fair_probability": 0.55, "chatgpt_confidence": "MEDIUM",
        "chatgpt_thesis": "why this price is wrong, in a few sentences",
        "key_supporting_factors": ["..."], "key_opposing_factors": ["..."],
        "factor_tags": ["SERVE_EDGE", "PRICE_VALUE"],
        "market_disagreement_reason": "...", "why_market_may_be_wrong": "...", "why_model_may_be_wrong": "...",
        "primary_match_thesis": "the match-level view the chosen market expresses",
        "why_chosen_expression_best_matches_thesis": "...",
        "bet_up_to_price": 0.51, "stake_units_if_bet": 1.0, "actual_wagered": False,
    },
    "wager": {"decision_id": "AD-20261001-0123456789ab", "placed_at": "2026-10-01T09:17:00+00:00",
              "entry_price": 0.48, "contracts": 20, "fees": 0.35, "source": "MANUAL_KALSHI_UI", "status": "FILLED"},
    "postmortem": {"decision_id": "AD-20261001-0123456789ab", "result": "LOSS", "what_thesis_got_right": "...",
                   "what_thesis_got_wrong": "...", "whether_loss_was_process_or_variance": "VARIANCE",
                   "data_that_would_have_helped": "...", "potential_research_question": "..."},
    "evidence": {"decision_id": "AD-20261001-0123456789ab", "evidence": "late withdrawal reported after the decision",
                 "source": "...", "bears_on": ["INJURY"]},
}
KIND_ID = {"decision": "decision_id", "wager": "wager_id", "postmortem": "postmortem_id", "evidence": "evidence_id"}


def _load(a) -> object:
    if a.json:
        return json.loads(a.json)
    if a.input and a.input != "-":
        return json.load(open(a.input))
    return json.loads(sys.stdin.read())


def run(payload: dict, a) -> dict:
    kind = a.kind
    common = {"store_root": a.store}
    if kind == "decision":
        rec = R.build_decision(payload, **common, data_root=a.data_root, slate_dir=a.slate_dir, code_sha=code_sha(PROJ))
    elif kind == "wager":
        rec = R.build_wager(payload, **common, data_root=a.data_root)
    elif kind == "postmortem":
        rec = R.build_postmortem(payload, **common)
    else:
        rec = R.build_evidence(payload, **common)
    out = {"status": "VALID" if a.dry_run else "RECORDED", "kind": kind, "id": rec[KIND_ID[kind]],
           "warnings": rec.get("warnings") or []}
    if kind == "decision":
        out.update({k: rec[k] for k in ("ticker", "side", "decision", "model_agreement_state", "side_entry_price",
                                        "market_quote_source", "first_ball_status_at_decision")})
    if not a.dry_run:
        store_kind = {"decision": "decisions", "wager": "wagers", "postmortem": "postmortems", "evidence": "evidence"}[kind]
        out["path"] = os.path.relpath(RecordStore(a.store).write(store_kind, rec), PROJ)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--kind", choices=sorted(KIND_ID), default="decision")
    ap.add_argument("--input", help="JSON file ('-' or omitted: stdin)")
    ap.add_argument("--json", help="the JSON payload inline")
    ap.add_argument("--store", default=os.path.join(PROJ, "data", "research", "assisted_decisions"))
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--slate-dir", default=os.path.join(PROJ, "data", "research", "assisted_slates"))
    ap.add_argument("--dry-run", action="store_true", help="validate and print, write nothing")
    ap.add_argument("--template", choices=sorted(TEMPLATES), help="print an input template and exit")
    a = ap.parse_args(argv)
    if a.template:
        print(json.dumps(TEMPLATES[a.template], indent=1))
        return 0
    try:
        payload = _load(a)
    except (OSError, ValueError) as e:
        print(json.dumps({"status": "REFUSED", "code": "INVALID_PAYLOAD", "message": str(e)}))
        return 2
    items = payload if isinstance(payload, list) else [payload]
    rc = 0
    for p in items:
        try:
            print(json.dumps(run(p, a), default=str))
        except AssistedValidationError as e:
            print(json.dumps({"status": "REFUSED", "code": e.code, "message": str(e)}))
            rc = 2
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
