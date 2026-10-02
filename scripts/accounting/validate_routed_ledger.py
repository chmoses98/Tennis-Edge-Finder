#!/usr/bin/env python3
"""Validate the TENNIS routed-wager ledger. The destination's own verdict on its own data. COUNTS AND REASONS ONLY.

    python scripts/accounting/validate_routed_ledger.py --base-dir <accounting-data checkout> \
        [--base-ref origin/accounting-data] [--result-out result.json]

Checks: every line decodes; wager and settlement schemas (incl. no model/recommendation provenance field);
source_bet_key unique in each file; every settlement has its wager with the same ticker and side; with --base-ref
(a git ref resolvable in --base-dir), both files are APPEND-ONLY relative to that ref.

accounting-data carries no .github/, so a pull request into it gets no CI; kalshi-bet-router runs this after its
import and the exit status is the verdict (0 pass, 1 fail). Failures name a file and LINE NUMBER and a reason --
never a ticker, stake, price, contract count, P&L or source_bet_key.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

from tennis_edge.accounting.spec import SPEC  # noqa: E402
from edge_finder_contract.routed_ledger import run_validate_cli  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    return run_validate_cli(SPEC, argv)


if __name__ == "__main__":
    raise SystemExit(main())
