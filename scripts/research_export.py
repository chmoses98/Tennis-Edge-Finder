#!/usr/bin/env python3
"""Publish the TENNIS research graph (app/latest/explorer) beside the v1 app export.

    python scripts/research_export.py --out data/app/latest [--data-root data] [--now <iso>] [--top-n 200]
                                      [--capture-days 3] [--commit-sha X]

Run it AFTER scripts/app_export.py with the same --data-root/--out. Thin CLI over ``tennis_edge.research_export``
(the pure adapter). On success the explorer/ tree is replaced atomically (index.json last); on ANY failure the
previous explorer/ tree and the whole v1 payload stay byte-for-byte and the exit status is 1 (the workflow records
RESEARCH_EXPORT_FAILED and fails the job after publishing). Reads no credential of any kind. See docs/APP_EXPORT.md.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from tennis_edge.research_export import run_cli  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(run_cli())
