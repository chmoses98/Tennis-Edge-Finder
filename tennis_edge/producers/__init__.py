"""Live producers for the FROZEN research lanes, and the records that say when each experiment began.

A producer here runs an existing frozen model on the live board and writes what it said, at the moment
it said it, to an append-only, hash-chained store. It never fits, tunes or re-specifies a model. The
experiment-start record is written ONCE, by the first production run of a producer, and is never
rewritten: everything before it is permanently unscorable for the candidates it serves.
"""
