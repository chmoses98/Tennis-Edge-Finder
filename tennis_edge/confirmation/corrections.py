"""Evidence-accounting corrections: what a corrected harvester changed relative to the evidence already stored.

A correction is never a rewrite. The store is append-only and versioned; when a corrected harvest finds that
an observation previously recorded as INCLUDED must now be EXCLUDED, the store appends a NEWER version of
that observation (same observation_id, same decision-time fields) and readers take the latest version.
The earlier line stays in the file forever. This module only COUNTS what changed so a report can show it.
"""
from __future__ import annotations

from collections import Counter

from tennis_edge.confirmation import evidence as ev


def _level(ticker) -> str:
    from tennis_edge.assisted.schema import level_bucket
    return level_bucket((ticker or "").split("-")[0])


def post_settlement_correction(prior_latest: dict, rows) -> dict:
    """prior_latest: observation_id -> the authoritative stored version BEFORE this harvest;
    rows: this harvest's EvidenceRow list. Counts MARKET_SETTLED_BEFORE_OBSERVATION by prior state."""
    hit = [r for r in rows if ev.R_SETTLED_BEFORE_OBSERVATION in r.exclusion_reasons]
    corrected, other, marked, fresh = [], [], [], []
    for r in hit:
        p = prior_latest.get(r.observation_id)
        if p is None:
            fresh.append(r)
        elif ev.R_SETTLED_BEFORE_OBSERVATION in (p.get("exclusion_reasons") or []):
            marked.append(r)
        elif p.get("inclusion_result") == ev.INCLUDED:
            corrected.append(r)
        else:
            other.append(r)
    return {
        "rule": ("an observation timestamped at or after the exchange's recorded settlement_ts of its contract "
                 "cannot be prospective pregame evidence (evidence-accounting correction, not a frozen-rule change)"),
        "observations_settled_before_observation": len(hit),
        "by_level": dict(sorted(Counter(_level(r.ticker) for r in hit).items())),
        "corrected_included_to_excluded": len(corrected),
        "corrected_by_level": dict(sorted(Counter(_level(r.ticker) for r in corrected).items())),
        "corrected_settled_rows": sum(1 for r in corrected if r.settlement_result in ("yes", "no")),
        "corrected_strict_clv_rows": sum(1 for r in corrected if r.strict_clv_executable is not None),
        "previously_excluded_for_other_reasons": len(other),
        "already_marked_by_an_earlier_corrected_harvest": len(marked),
        "first_harvested_this_run": len(fresh),
        "corrected_observations": [{"observation_id": r.observation_id, "ticker": r.ticker, "captured_at": r.captured_at,
                                    "settled_at": r.settled_at, "level": _level(r.ticker)} for r in corrected][:100],
        "history": ("the earlier INCLUDED version of every corrected observation remains in the evidence file; the "
                    "newer EXCLUDED version (same observation_id) is authoritative for scoring"),
    }
