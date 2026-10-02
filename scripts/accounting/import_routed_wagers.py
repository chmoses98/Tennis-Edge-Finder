#!/usr/bin/env python3
"""Import a kalshi-bet-router TENNIS wager payload into data/accounting/wagers.jsonl. COUNTS ONLY.

    python scripts/accounting/import_routed_wagers.py --payload TENNIS.json --base-dir <accounting-data checkout> \
        --receipts-out receipts.json

The payload is the router's envelope ``{"importBatchId": ..., "rows": [...]}``. Identity (``wager_id``,
``tenw-<24 hex>``) is minted from ``source_bet_key``; an identical re-delivery is DUPLICATE_NOOP and changes zero
bytes; a re-delivery with different economics is CONFLICT and exits 1 so the router's merge gate fails.

This repository's Actions logs are public: stdout carries counts and refusal REASONS by row position, never a
ticker, price, stake, contract count or key. Per-row receipts go only to the --receipts-out file.

Recording is not endorsing: a row says the owner placed a tennis bet by hand. No model, slate or assisted-track
record is read or written here (stdlib only; nothing from this repository's numpy/pandas stack is imported).
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

from tennis_edge.accounting.spec import SPEC  # noqa: E402  (also puts contract/ on sys.path)
from edge_finder_contract.routed_ledger import run_import_cli  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    return run_import_cli(SPEC, "wagers", argv)


if __name__ == "__main__":
    raise SystemExit(main())
