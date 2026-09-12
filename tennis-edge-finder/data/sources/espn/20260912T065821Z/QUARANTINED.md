# QUARANTINED — do not ingest

This snapshot carries a tour-labelling defect. A combined event is returned by BOTH ESPN league boards
carrying BOTH draws, and the parser that wrote these files took the tour from the league it fetched. The
men's draws of the combined events were therefore written into the WTA file.

* published here: 779 ATP / 4,692 WTA
* truth for the same raw payloads: 2,152 ATP / 3,319 WTA
* 1,373 men's singles matches are mislabelled

The `raw/` payloads in this directory are unaffected — they are what ESPN returned — and re-parsing them
with the fixed `tennis_edge/data/espn_results.py` reproduces the corrected split. Only the two derived
`espn_matches_*.csv.gz` files are wrong.

Fixed on `main` in "fix: ESPN filed a combined event's men's draw as WTA". A later snapshot in this
directory tree supersedes this one.

This branch is append-only evidence, so the bad files are marked rather than deleted.
