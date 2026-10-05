#!/usr/bin/env python3
"""Fit the production stacker coefficients for a live season from the walk-forward replay records.

For live season Y the frozen specification is fitted on seasons Y-window .. Y-1 -- exactly the walk-forward
rule every research number used, so the 2026 coefficients ARE the ones the 2026 holdout was scored with
(asserted below against predictions_holdout.parquet). Envelope variants (alternative rating, no context,
no structural blocks, weaker regularisation, shorter window) are fitted the same way.
"""
from __future__ import annotations

import argparse, hashlib, json, os, sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tennis_edge.v2.production import ALT_ELO, COEF_PATH, MODEL_VERSION  # noqa: E402
from tennis_edge.v2.stacker import StackerSpec, fit  # noqa: E402

RESEARCH = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2")


def variants(spec: StackerSpec) -> dict:
    drop = lambda *b: tuple(x for x in spec.blocks if x not in b)
    mk = lambda **kw: StackerSpec(**{**dict(elo=spec.elo, blocks=spec.blocks, form_horizon=spec.form_horizon,
                                             C=spec.C, window=spec.window), **kw})
    return {"base": spec, "alt_elo": mk(elo=ALT_ELO), "no_context": mk(blocks=drop("context")),
            "no_structural": mk(blocks=drop("g2", "g2s")), "weak_l2": mk(C=1.0), "window4": mk(window=4)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, required=True, help="live season the coefficients serve")
    ap.add_argument("--replay", default="/home/user/work/v2/replay")
    ap.add_argument("--out", default=COEF_PATH)
    a = ap.parse_args()
    fz = json.load(open(os.path.join(RESEARCH, "FROZEN_CHALLENGER.json")))
    s = fz["spec"]
    spec = StackerSpec(elo=s["elo"], blocks=tuple(s["blocks"]), form_horizon=s["form_horizon"], C=s["C"], window=s["window"])
    assert spec.fingerprint() == fz["spec_fingerprint"]
    out = {"model_version": MODEL_VERSION, "live_season": a.season, "frozen_spec": fz["spec"],
           "frozen_spec_fingerprint": fz["spec_fingerprint"], "fitted_at": datetime.now(timezone.utc).isoformat(),
           "tours": {}}
    hold = os.path.join(RESEARCH, "predictions_holdout.parquet")
    hold = pd.read_parquet(hold) if os.path.exists(hold) else None
    for t in ("ATP", "WTA"):
        meta = json.load(open(os.path.join(a.replay, f"replay_{t}.meta.json")))
        df = pd.read_parquet(os.path.join(a.replay, f"replay_{t}.parquet"))
        vs = {}
        for name, sp in variants(spec).items():
            tr = df[(df.season >= max(a.season - sp.window, 2008)) & (df.season < a.season)]
            f = fit(tr, sp)
            vs[name] = f.to_dict()
            if name == "base" and hold is not None and a.season == 2026:
                te = df[df.season == 2026]
                h = hold[hold.tour == t].set_index("uid").loc[te.uid, "CHALLENGER"].to_numpy()
                diff = float(np.max(np.abs(f.predict(te) - h)))
                assert diff < 1e-12, f"{t}: coefficients do not reproduce the holdout ({diff})"
                vs[name]["reproduces_holdout_max_abs_diff"] = diff
        out["tours"][t] = {"variants": vs, "replay_matches_sha256": meta["matches_sha256"]}
    out["fingerprint"] = hashlib.sha256(json.dumps(out["tours"], sort_keys=True).encode()).hexdigest()[:16]
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(out, open(a.out, "w"), indent=1)
    print("wrote", a.out, "fingerprint", out["fingerprint"])
    for t in out["tours"]:
        b = out["tours"][t]["variants"]["base"]
        print(t, "train seasons", b["train_seasons"], "n", b["n_train"], {n: round(c / s, 4) for n, c, s in zip(b["names"], b["coef"], b["scale"])})


if __name__ == "__main__":
    main()
