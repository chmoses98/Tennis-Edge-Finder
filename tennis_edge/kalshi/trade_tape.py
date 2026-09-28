"""Bounded, gap-tracking scan of Kalshi's GLOBAL trade tape.

The tape is served newest-first and is far busier than tennis: roughly nine thousand trades a minute
across the exchange in September 2026. The capture conductor reads it every ten minutes with a fixed page
budget, and every one of 1,689 passes between 2026-09-11 and 2026-09-27 hit that budget.

What the previous cursor did on truncation
------------------------------------------
It set the next pass's lower bound to the OLDEST trade the truncated pass had scanned. A newest-first scan
that stops early leaves the OLDER end of its window unscanned, so that choice (a) skipped the unscanned
older end for good and (b) made the next window start inside the region already scanned, spending most of
the next budget re-reading it. Measured on the captured files: a median of ~28 minutes of tape read per
pass against a ~16 minute cadence, and 54 windows (~2.75 hours of tape) that no pass ever read.

What this module does instead
-----------------------------
* The NEW window of a pass is always (end of the last new window, now]: no re-scan of covered ground.
* If the new window truncates, the unscanned OLDER remainder [lo, oldest_seen] is queued as a backlog gap
  -- nothing is skipped silently.
* Whatever page budget the new window did not use goes to the backlog, newest gap first.
* The total pages per pass never exceed the budget, so runtime per pass stays bounded exactly as before.
* A gap older than `max_gap_age_s` is ABANDONED explicitly and reported, so a tape that out-runs the
  budget for a long time fails the health gate instead of quietly falling behind.

Boundary seconds are included on both sides of a split (Kalshi's min_ts/max_ts are whole seconds), so a
trade on a boundary may be read twice; readers deduplicate on trade_id. Reading one twice is harmless,
never reading one is not.
"""
from __future__ import annotations

from dataclasses import dataclass, field

DEFAULT_PAGE_BUDGET = 250          # the pre-existing per-pass bound; unchanged
DEFAULT_NEW_WINDOW_PAGES = 200     # reserve the rest for the backlog
DEFAULT_MAX_GAP_AGE_S = 24 * 3600
DEFAULT_FIRST_WINDOW_S = 3600      # a cold start reads the last hour, as before


@dataclass
class TradeTape:
    cursor_ts: int | None = None                     # end of the last NEW window scanned
    backlog: list = field(default_factory=list)      # [[lo, hi], ...] unscanned, oldest first

    @classmethod
    def from_state(cls, state: dict) -> "TradeTape":
        """Read the tape state; a legacy state (only `trades_cursor_ts`) starts with an empty backlog."""
        bl = [[int(a), int(b)] for a, b in (state.get("trades_backlog") or []) if int(a) <= int(b)]
        cur = state.get("trades_tape_cursor_ts")
        if cur is None:
            cur = state.get("trades_cursor_ts")
        return cls(int(cur) if cur is not None else None, sorted(bl))

    def to_state(self, state: dict) -> dict:
        state["trades_tape_cursor_ts"] = self.cursor_ts
        state["trades_cursor_ts"] = self.cursor_ts          # kept for older readers
        state["trades_backlog"] = [list(g) for g in self.backlog]
        return state

    def new_window(self, t_now: int) -> tuple[int, int]:
        lo = self.cursor_ts if self.cursor_ts is not None else t_now - DEFAULT_FIRST_WINDOW_S
        return min(lo, t_now), t_now

    def record_new(self, lo: int, hi: int, complete: bool, oldest_seen: int | None) -> None:
        """The new window [lo, hi] was scanned newest-first; queue whatever older part was not reached."""
        if not complete:
            gap_hi = oldest_seen if oldest_seen is not None else hi
            if gap_hi >= lo:
                self._add_gap(lo, gap_hi)
        self.cursor_ts = hi

    def backlog_newest_first(self) -> list[tuple[int, int]]:
        return [tuple(g) for g in sorted(self.backlog, key=lambda g: -g[1])]

    def record_backlog(self, lo: int, hi: int, complete: bool, oldest_seen: int | None) -> None:
        """A backlog gap [lo, hi] was scanned newest-first; keep only what is still unread."""
        self.backlog = [g for g in self.backlog if not (g[0] == lo and g[1] == hi)]
        if not complete:
            gap_hi = oldest_seen if oldest_seen is not None else hi
            if gap_hi >= lo:
                self._add_gap(lo, gap_hi)

    def abandon_older_than(self, cutoff_ts: int) -> list[list[int]]:
        """Drop (and return) every gap whose NEWEST second is older than `cutoff_ts`; clip straddlers."""
        dropped, keep = [], []
        for lo, hi in self.backlog:
            if hi < cutoff_ts:
                dropped.append([lo, hi])
            elif lo < cutoff_ts:
                dropped.append([lo, cutoff_ts - 1])
                keep.append([cutoff_ts, hi])
            else:
                keep.append([lo, hi])
        self.backlog = sorted(keep)
        return dropped

    def pending_seconds(self) -> int:
        return sum(hi - lo + 1 for lo, hi in self.backlog)

    def oldest_gap_age_s(self, t_now: int) -> int | None:
        return (t_now - min(lo for lo, _ in self.backlog)) if self.backlog else None

    def _add_gap(self, lo: int, hi: int) -> None:
        gaps = sorted(self.backlog + [[lo, hi]])
        merged = []
        for g in gaps:
            if merged and g[0] <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], g[1])
            else:
                merged.append(list(g))
        self.backlog = merged


def oldest_created_ts(trades: list, parse) -> int | None:
    seen = [parse(t.get("created_time")) for t in trades if t.get("created_time")]
    seen = [s for s in seen if s is not None]
    return min(seen) if seen else None


def scan(client, tape: TradeTape, t_now: int, *, page_budget: int = DEFAULT_PAGE_BUDGET,
         new_window_pages: int = DEFAULT_NEW_WINDOW_PAGES, max_gap_age_s: int = DEFAULT_MAX_GAP_AGE_S,
         parse=None) -> tuple[list, dict]:
    """One pass over the tape: the new window, then the backlog, within `page_budget` pages in total.

    Returns (trades, report). `report["errors"]` lists fetch failures (not truncation) and
    `report["abandoned"]` lists gaps given up on; both are real incompleteness. A truncated window whose
    remainder is queued is NOT incompleteness -- it is recorded under `report["backlog"]`."""
    parse = parse or (lambda s: None)
    report = {"new_window": None, "backlog_scans": [], "errors": [], "abandoned": [], "pages": 0}
    report["abandoned"] = tape.abandon_older_than(t_now - max_gap_age_s)
    lo, hi = tape.new_window(t_now)
    pages = min(new_window_pages, page_budget)
    trades, ok, info = client.trades(min_ts=lo, max_ts=hi, limit=1000, max_pages=pages)
    used = int(info.get("pages") or 0)
    if not ok and info.get("error"):
        report["errors"].append({"window": [lo, hi], "error": info.get("error")})
    tape.record_new(lo, hi, ok, oldest_created_ts(trades, parse))
    report["new_window"] = {"lo": lo, "hi": hi, "complete": bool(ok), "pages": used, "trades": len(trades)}
    remaining = page_budget - used
    for glo, ghi in tape.backlog_newest_first():
        if remaining <= 0:
            break
        tr, ok2, info2 = client.trades(min_ts=glo, max_ts=ghi, limit=1000, max_pages=remaining)
        u = int(info2.get("pages") or 0)
        remaining -= u
        if not ok2 and info2.get("error"):
            report["errors"].append({"window": [glo, ghi], "error": info2.get("error")})
        tape.record_backlog(glo, ghi, ok2, oldest_created_ts(tr, parse))
        report["backlog_scans"].append({"lo": glo, "hi": ghi, "complete": bool(ok2), "pages": u, "trades": len(tr)})
        trades = trades + tr
    report["pages"] = page_budget - remaining
    report["backlog"] = {"gaps": len(tape.backlog), "pending_seconds": tape.pending_seconds(),
                         "oldest_gap_age_s": tape.oldest_gap_age_s(t_now)}
    return trades, report
