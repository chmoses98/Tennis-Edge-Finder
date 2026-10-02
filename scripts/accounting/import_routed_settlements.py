#!/usr/bin/env python3
"""Import a kalshi-bet-router TENNIS settlement payload into data/accounting/settlements.jsonl. COUNTS ONLY.

    python scripts/accounting/import_routed_settlements.py --payload TENNIS-settlements.json \
        --base-dir <accounting-data checkout> --receipts-out receipts.json

Payload: ``{"settlements": [...]}`` rows under router-settlement-economics.v2 (the only version accepted). A
settlement whose ``source_bet_key`` is not on the tennis wager ledger is refused as ORPHAN. An identical repeat is
DUPLICATE_NOOP (zero bytes change); a different settlement for an already-settled wager is CONFLICT; either refusal
exits 1. stdout never carries a ticker, payout, P&L or key.

Tennis settles SCALAR on the exchange sometimes (a walkover settles at a fair price strictly between 0 and 1): the
router sends such a row with ``result`` absent/None and the money fields as the exchange states them, and the
shared ledger accepts ``result`` None with established money.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

from tennis_edge.accounting.spec import SPEC  # noqa: E402
from edge_finder_contract.routed_ledger import run_import_cli  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    return run_import_cli(SPEC, "settlements", argv)


if __name__ == "__main__":
    raise SystemExit(main())
