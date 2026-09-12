#!/usr/bin/env python3
"""Add the uncertainty-weighted fallback lane to an existing Gen-2 prediction frame.

Still MODEL 3: the rating is built from results, never from prices. Serve statistics exist for four
percent of ITF matches, so a structural model has nothing to say about most of the universe. Rather than
pretend, its point probabilities are shrunk toward the point probabilities IMPLIED by the rating, in
proportion to how much serve evidence the THINNER of the two players actually has.

Done as a separate pass over the saved frame because the inversion is the expensive part and doing it
here lets the cache be shared across every row at once.
"""
from __future__ import annotations

import argparse
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.rules.formats import MatchFormat, TOUR_SINGLES_BO3          # noqa: E402
from tennis_edge.sim.analytic import match_win_prob, point_probs_from_match_prob   # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_INV: dict = {}
_MWP: dict = {}
_BO5 = MatchFormat(**{**TOUR_SINGLES_BO3.__dict__, "best_of": 5})


def inv(p_match: float, lvl: float):
    key = (round(float(p_match), 3), round(float(lvl), 2))
    v = _INV.get(key)
    if v is None:
        v = point_probs_from_match_prob(min(max(key[0], 1e-4), 1 - 1e-4), key[1], TOUR_SINGLES_BO3)
        _INV[key] = v
    return v


def mwp(pa: float, pb: float, bo: int):
    key = (round(float(pa), 3), round(float(pb), 3), int(bo))
    v = _MWP.get(key)
    if v is None:
        v = match_win_prob(key[0], key[1], TOUR_SINGLES_BO3 if key[2] == 3 else _BO5)
        _MWP[key] = v
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tour", default="ATP")
    ap.add_argument("--blend-points", type=float, default=1500.0)
    ap.add_argument("--dir", default=os.path.join(PROJ, "research", "gen2"))
    a = ap.parse_args()
    path = os.path.join(a.dir, f"predictions_{a.tour}.parquet")
    d = pd.read_parquet(path)
    ev_min = np.minimum(d.ev_a.values, d.ev_b.values)
    w = ev_min / (ev_min + a.blend_points)
    lvl = d.gen2_pa.values + (1.0 - d.gen2_pb.values)
    out = np.empty(len(d))
    for i in range(len(d)):
        epa, epb = inv(d.p_elo.values[i], lvl[i])
        bpa = w[i] * d.gen2_pa.values[i] + (1 - w[i]) * epa
        bpb = w[i] * d.gen2_pb.values[i] + (1 - w[i]) * epb
        out[i] = mwp(bpa, bpb, d.best_of.values[i])
    d["p_gen2_blend"] = out
    d["blend_weight"] = w
    d.to_parquet(path, index=False)
    print(f"{a.tour}: blended {len(d)} rows; inversion cache {len(_INV)} keys, match cache {len(_MWP)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
