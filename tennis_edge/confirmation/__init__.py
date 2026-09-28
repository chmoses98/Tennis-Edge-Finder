"""Prospective confirmation: score already-frozen edge candidates on observations captured after the freeze.

Nothing in this package fits, tunes or re-specifies anything. It reads a frozen candidate definition,
reads immutable prospective observations, applies the frozen inclusion rule, attaches settlement and
first-ball truth that arrived later, and writes a DERIVED, append-only evidence layer beside the
original evidence. The candidate definition files are never written.
"""
