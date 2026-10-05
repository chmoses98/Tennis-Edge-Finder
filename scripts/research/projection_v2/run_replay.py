#!/usr/bin/env python3
"""Projection V2 step 1: walk-forward replay of every candidate lane over the canonical table.

Writes <out>/replay_<tour>.parquet (one row per match from --record-from, every lane's PRE-match view) and
<out>/replay_<tour>.meta.json (input hash, configs, timings). No prices are read.
"""
from __future__ import annotations

import argparse, hashlib, json, os, sys, time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import pandas as pd  # noqa: E402

from tennis_edge.v2.replay import ELO_VARIANTS, GEN2_VARIANTS, finalise, replay  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--matches", required=True)
    ap.add_argument("--tour", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--record-from", type=int, default=2005)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    t0 = time.time()
    sha = hashlib.sha256(open(a.matches, "rb").read()).hexdigest()
    from tennis_edge.v2.replay import COLUMNS
    m = pd.read_parquet(a.matches, columns=COLUMNS)
    m = m[m.tour == a.tour]
    df, states = replay(m, a.tour, record_from=a.record_from, progress=True)
    del m
    t1 = time.time()
    df = finalise(df)
    t2 = time.time()
    df.to_parquet(os.path.join(a.out, f"replay_{a.tour}.parquet"), index=False)
    meta = {"tour": a.tour, "matches_sha256": sha, "matches_path": a.matches, "record_from": a.record_from,
            "n_rows": int(len(df)), "n_replayed": states["n_matches"], "last_date": states["last_date"],
            "elo_variants": [c.to_dict() for c in ELO_VARIANTS],
            "gen2_variants": {k: c.to_dict() for k, c in GEN2_VARIANTS.items()},
            "seconds_replay": round(t1 - t0, 1), "seconds_finalise": round(t2 - t1, 1)}
    json.dump(meta, open(os.path.join(a.out, f"replay_{a.tour}.meta.json"), "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in meta.items() if k not in ("elo_variants", "gen2_variants")}, default=str))


if __name__ == "__main__":
    main()
