#!/usr/bin/env python3
"""Build the walk-forward rating artifacts the Wave 3 opportunity dataset scores against.

One artifact per tour: the full rating state at a base date, plus a checkpoint for each player after
every match they play from then on. A market on day D is scored with the last checkpoint strictly before
D, so no result from D or later can reach a prediction made on D.
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import date

import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.models.asof import build_asof, save_asof, AsOfStates   # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-date", default="2026-06-01", help="first day covered by checkpoints")
    ap.add_argument("--matches", default=os.path.join(PROJ, "data", "processed", "matches.parquet"))
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "processed", "asof"))
    a = ap.parse_args()
    m = pd.read_parquet(a.matches)
    for tour in ("ATP", "WTA"):
        obj = build_asof(m, tour, date.fromisoformat(a.base_date))
        path = os.path.join(a.out, f"asof_{tour}.json.gz")
        save_asof(obj, path)
        st = AsOfStates.load(path)
        print(f"{tour}: {obj['n_matches']} matches, {st.known_players()} players at base, "
              f"{sum(len(v) for v in obj['checkpoints'].values())} checkpoints, {os.path.getsize(path)/1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
