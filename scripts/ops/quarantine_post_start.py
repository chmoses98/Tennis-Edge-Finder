#!/usr/bin/env python3
"""Register legacy post-start ledger rows in the append-only quarantine register (idempotent).

Only rows generated BEFORE the in-play guard (tennis_edge/ledger/quarantine.py:GUARD_DEPLOYED_AT) can be
registered; an active leak raises instead of being hidden. The ledger is read, never written.
"""
from __future__ import annotations

import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import tennis_edge.health.gates as g  # noqa: E402
from tennis_edge.ledger import quarantine  # noqa: E402


def main():
    root = os.path.join(g.PROJ, "data", "research", "quarantine")
    extra = g._auto_extra()
    rows, starts = extra.get("ledger_rows", []), extra.get("starts", {})
    n = quarantine.append(root, quarantine.legacy_violations(rows, starts, extra.get("settled_at")))
    have, problems = quarantine.load(root)
    print(f"quarantine register: +{n} new, {len(have)} total, problems={problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
