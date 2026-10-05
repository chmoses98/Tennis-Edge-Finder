"""Projection Engine V2: independent pre-match tennis probabilities (no market input anywhere in this package).

See docs/PROJECTION_ENGINE_V2.md. Modules:
  elo        configurable Elo family (level prior / level K / surface pooling / margin of victory / layoff)
  form       opponent-adjusted current form: decayed rating residuals at several horizons
  context    pre-match context: rest, workload, retirements, surface switches
  replay     one chronological pass that records every model's PRE-match prediction and features
  stacker    evidence-aware logistic ensemble, fitted walk-forward, no intercept (A/B symmetric)
  inference  live: the same feature builder over persisted end states
"""
