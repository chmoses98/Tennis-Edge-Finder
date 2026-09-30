#!/usr/bin/env python3
"""Build the assisted handicapping slate (data/research/assisted_slates/latest.{json,md}).

A read-only join of what the frozen producers, the Gen-1 ledger, the external scan, the Kalshi capture and
the first-ball store already wrote. It selects no bet. Run by RUN TENNIS after the frozen producers, and
on demand by the `TENNIS assisted slate` workflow when someone says RUN TENNIS.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.assisted.slate import build_slate, write_slate   # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "research", "assisted_slates"))
    a = ap.parse_args(argv)
    slate = build_slate(a.data_root)
    run = write_slate(slate, a.out)
    print(json.dumps(run, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
