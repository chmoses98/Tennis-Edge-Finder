#!/usr/bin/env python3
"""Render research/projection_v2/ALIAS_REVIEW_DECISION.json as the readable ALIAS_REVIEW_RESULTS.md.

The live-coverage section is read from research/projection_v2/alias_review/coverage_before_after.json when present
(written after the production run); until then the report says the live comparison is pending."""
from __future__ import annotations

import json
import os
import sys

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
R = os.path.join(PROJ, "research", "projection_v2")


def main():
    d = json.load(open(os.path.join(R, "ALIAS_REVIEW_DECISION.json")))
    cov_p = os.path.join(R, "alias_review", "coverage_before_after.json")
    cov = json.load(open(cov_p)) if os.path.exists(cov_p) else None
    dec = d["decisions"]
    per = {}
    for x in dec:
        per.setdefault((x["foreign_system"], x["foreign_id"]), []).append(x)
    out = {}
    for k, xs in per.items():
        ds = [x["decision"] for x in xs]
        out[k] = ("ACCEPTED" if "ACCEPTED" in ds else "AMBIGUOUS" if "AMBIGUOUS" in ds
                  else "INSUFFICIENT_EVIDENCE" if "INSUFFICIENT_EVIDENCE" in ds else "REJECTED")
    n = {s: sum(1 for v in out.values() if v == s) for s in ("ACCEPTED", "REJECTED", "AMBIGUOUS", "INSUFFICIENT_EVIDENCE")}
    L = ["# Alias review results (2026-10-06)", "",
         "Machine-readable record: `ALIAS_REVIEW_DECISION.json`. Raw external evidence: `alias_review/evidence_raw/` "
         "(fetched on a GitHub runner by `.github/workflows/tennis-identity-evidence.yml`; the research sandbox cannot reach "
         "ESPN, Wikidata or the tours). Data-derived evidence: `alias_review/local_evidence.json`. Flattened per pair: "
         "`alias_review/evidence_summary.json`.", "",
         f"Reviewer: {d['reviewer']}. Nothing was accepted from name similarity; no automated threshold was changed. Accepted "
         "pairs are the only new entries in `data/identity/reviewed_aliases.json` (`crosswalk_aliases`, bound by source-specific id "
         "and tour).", "",
         "## Summary", "",
         "| | foreign ids |", "|---|---|",
         f"| reviewed (mint-twin list) | {len(out)} |"] + [f"| {k} | {v} |" for k, v in n.items()] + [""]
    L += ["## Acceptance criteria", "", "```", d["criteria"], "```", ""]
    L += ["## Not accepted (still fail-closed)", "", "| foreign id | name | candidate | decision | why |", "|---|---|---|---|---|"]
    for x in dec:
        if x["decision"] != "ACCEPTED":
            L.append(f"| {x['foreign_system']}/{x['foreign_id']} | {x['foreign_name']} | {x['tour']} {x['proposed_canonical_id']} "
                     f"{x['proposed_canonical_name']} | {x['decision']} | {x['rationale']} |")
    L += ["", "Unresolved foreign ids: " + ", ".join(f"{k[0]}/{k[1]} ({per[k][0]['foreign_name']})" for k, v in out.items()
                                                  if v != "ACCEPTED"), ""]
    L += ["## Accepted", "", "| foreign id | name | -> canonical | DOB check | nationality | ATP id link | shared matches | live tickers | basis |",
          "|---|---|---|---|---|---|---|---|---|"]
    for x in dec:
        if x["decision"] == "ACCEPTED":
            e = x["evidence"]
            L.append(f"| {x['foreign_system']}/{x['foreign_id']} | {x['foreign_name']} | {x['tour']} {x['proposed_canonical_id']} "
                     f"{x['proposed_canonical_name']} | {e['dob_check']} ({e.get('foreign_dob') or '-'} / {e.get('canonical_dob') or '-'}) | "
                     f"{e['nationality_check']} | {e['governing_body_id_check']} | {e['shared_matches']} | "
                     f"{x['live_tickers_naming_this_player']} | {x['rationale'][:160]} |")
    L += ["", "## Kalshi-name queue (prior 9-entry `alias_review_queue`) and Mimi Xu", "",
          "| Kalshi name | tour | decision | why |", "|---|---|---|---|"]
    for k in d["kalshi_name_decisions"]:
        L.append(f"| {k['kalshi_name']} | {k['tour']} | {k['decision']} | {k['rationale']} |")
    L += ["", "## Live coverage", ""]
    if cov:
        L += [cov.get("markdown", "")]
    else:
        L += ["Pending: measured on the first production RUN TENNIS after merge."]
    open(os.path.join(R, "ALIAS_REVIEW_RESULTS.md"), "w").write("\n".join(L) + "\n")
    print(n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
