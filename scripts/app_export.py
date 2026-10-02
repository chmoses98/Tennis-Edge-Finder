#!/usr/bin/env python3
"""Export the TENNIS assisted slate, human decisions, wagers and health to the Edge Finder app contract.

    python scripts/app_export.py --out data/app/latest [--data-root data] [--accounting-dir <accounting-data checkout>]
                                 [--now <iso>] [--commit-sha X] [--workflow-run-id Y]

Thin CLI over ``tennis_edge.app_export`` (the pure adapter). On success the whole ``app/latest`` tree is replaced
atomically (manifest last). On ANY failure only ``health.json`` is rewritten (export_failed=True), the previous
payload stays byte-for-byte as last-known-good, and the exit status is 1 so the workflow goes red AFTER the
production outputs have been published (see docs/APP_EXPORT.md). Reads no credential of any kind.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from tennis_edge.app_export import run_cli  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(run_cli())
