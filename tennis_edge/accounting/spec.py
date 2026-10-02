"""The ONE definition of the tennis routed-wager ledger (``LedgerSpec``) shared by the three importer scripts.

Stdlib only: importing this module must never pull numpy/pandas (the router's runner installs nothing from
this repository). The ledger implementation itself is the vendored, byte-identical
``contract/edge_finder_contract/routed_ledger.py``; this module only names the tennis parameters:

    sport               TENNIS
    id_prefix           ten      -> wager_id ``tenw-<24 hex>``, settlement_id ``tens-<24 hex>``
    wager_schema        tennis_accounted_wager.v1
    settlement_schema   tennis_wager_settlement.v1
    files               data/accounting/wagers.jsonl, data/accounting/settlements.jsonl (on ``accounting-data``)

ACCOUNTING ONLY. A row says the owner placed a tennis bet by hand on Kalshi; it carries no model provenance
and the shared ledger refuses a row that tries to. The ChatGPT-assisted track's human-recorded wagers
(``AW-...`` under ``data/research/assisted_decisions``) are a different, unrelated path (docs/ACCOUNTING.md).
"""

from __future__ import annotations

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CONTRACT_DIR = os.path.join(REPO_ROOT, "contract")
if CONTRACT_DIR not in sys.path:
    sys.path.insert(0, CONTRACT_DIR)

from edge_finder_contract.routed_ledger import LedgerSpec  # noqa: E402

SPORT = "TENNIS"
ID_PREFIX = "ten"
WAGER_SCHEMA = "tennis_accounted_wager.v1"
SETTLEMENT_SCHEMA = "tennis_wager_settlement.v1"

SPEC = LedgerSpec(sport=SPORT, id_prefix=ID_PREFIX, wager_schema=WAGER_SCHEMA, settlement_schema=SETTLEMENT_SCHEMA)

__all__ = ["SPEC", "SPORT", "ID_PREFIX", "WAGER_SCHEMA", "SETTLEMENT_SCHEMA", "LedgerSpec", "REPO_ROOT", "CONTRACT_DIR"]
