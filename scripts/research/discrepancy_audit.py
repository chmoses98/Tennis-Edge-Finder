#!/usr/bin/env python3
"""Historical model-vs-market discrepancy audit -> AUDIT.{json,md} (descriptive research; changes no model).

    python scripts/research/discrepancy_audit.py --data-root data --out research/model_market_discrepancy

Reads the frozen producers' rows, the Gen-1 ledger, settlements, the external scan and first-ball truth; see
tennis_edge/research/discrepancy_audit.py for the rules (no reconstruction, hindsight used only to diagnose).
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.research.discrepancy_audit import run_audit, write_audit   # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "research", "model_market_discrepancy"))
    a = ap.parse_args(argv)
    audit = run_audit(a.data_root)
    write_audit(audit, a.out)
    summary = {"out": a.out, "observations": audit.get("total_observations"),
               "ge_25pp_primary_causes": (audit.get("root_causes_ge_25pp") or {}).get("primary_cause"),
               "MODEL_CHANGE_RECOMMENDED": (audit.get("model_change_recommendation") or {}).get("MODEL_CHANGE_RECOMMENDED")}
    print(json.dumps(summary, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
