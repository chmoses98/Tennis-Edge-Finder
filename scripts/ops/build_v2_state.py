#!/usr/bin/env python3
"""RUN TENNIS step: rebuild the Projection V2 end states (data/processed/v2/state_<tour>.json.gz) from the
canonical table with the committed, frozen coefficients' lanes. Both tours in parallel. No prices."""
from __future__ import annotations

import argparse, hashlib, json, os, sys, time
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _one(args):
    tour, matches_path, out, sha = args
    import pandas as pd
    from tennis_edge.v2.production import build_state, load_coefficients, save_state
    from tennis_edge.v2.replay import COLUMNS
    t0 = time.time()
    m = pd.read_parquet(matches_path, columns=COLUMNS)
    m = m[m.tour == tour]
    st = build_state(m, tour, load_coefficients(), matches_sha256=sha)
    path = os.path.join(out, f"state_{tour}.json.gz")
    save_state(st, path)
    return tour, len(st["players"]), st["last_date"], round(time.time() - t0, 1), st["data_horizon_by_level_group"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--matches", default=os.path.join(PROJ, "data", "processed", "matches.parquet"))
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "processed", "v2"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    sha = hashlib.sha256(open(a.matches, "rb").read()).hexdigest()
    with ProcessPoolExecutor(max_workers=2) as ex:
        for tour, n, last, secs, hz in ex.map(_one, [(t, a.matches, a.out, sha) for t in ("ATP", "WTA")]):
            print(json.dumps({"tour": tour, "players": n, "last_date": last, "seconds": secs, "data_horizon": hz}))


if __name__ == "__main__":
    main()
