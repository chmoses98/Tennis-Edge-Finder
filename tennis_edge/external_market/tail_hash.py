"""Constant-cost hash-chain appends for the external-market day files (2026-10-07).

`ExternalStore.append_many` and the FROZEN `DislocationLedger.append` (tennis_edge/external_market/dislocation.py,
hash-pinned) found each row's `prev_hash` by reading and JSON-parsing the WHOLE day file -- once per appended row.
Within one capture-conductor run the day file grows by a few thousand rows a pass, so the external scan took 124 s
on pass 0 and 1,466 s by pass 15 (2026-10-06, conductor #198): the 10-minute cadence stretched to 31 minutes and
TENNIS-5 failed. The same defect was fixed for the prediction ledger in #21.

`last_row_hash` reads only the last non-empty line (seeking back from the end of the file), and `TailHashLedger`
keeps it per day in memory after its own appends. Rows, hashes and the chain are byte-for-byte what the original
classes write; only the cost of finding the previous hash changes. The frozen module is not edited.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone

from tennis_edge.external_market.dislocation import DislocationLedger

GENESIS = "GENESIS"


def last_row_hash(path: str, block: int = 65536) -> str:
    """`row_hash` of the last non-empty line of a JSONL file; GENESIS when the file is absent or empty.

    Same answer as scanning the whole file the way the stores did, as long as the last line carries a row_hash
    (every row these stores write does). A last line that is not valid JSON falls back to the full scan, so a
    torn write is never silently skipped."""
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return GENESIS
    with open(path, "rb") as f:
        f.seek(0, os.SEEK_END)
        end = f.tell()
        buf = b""
        pos = end
        while pos > 0:
            step = min(block, pos)
            pos -= step
            f.seek(pos)
            buf = f.read(step) + buf
            lines = [ln for ln in buf.split(b"\n") if ln.strip()]
            if len(lines) >= 2 or (lines and pos == 0):
                try:
                    return json.loads(lines[-1]).get("row_hash", GENESIS) if lines else GENESIS
                except ValueError:
                    return full_scan_hash(path)
        return GENESIS


def full_scan_hash(path: str) -> str:
    prev = GENESIS
    with open(path) as f:
        for line in f:
            if line.strip():
                prev = json.loads(line).get("row_hash", prev)
    return prev


class TailHashLedger(DislocationLedger):
    """`DislocationLedger` with an O(1) previous-hash lookup. Writes exactly what the parent writes."""

    def __init__(self, root: str):
        super().__init__(root)
        self._tail: dict = {}

    def _last_hash(self, path: str) -> str:
        if path not in self._tail:
            self._tail[path] = last_row_hash(path)
        return self._tail[path]

    def append(self, row) -> dict:
        d = super().append(row)
        day = (row.generated_at or datetime.now(timezone.utc).isoformat())[:10]
        self._tail[self._path(day)] = d["row_hash"]
        return d
