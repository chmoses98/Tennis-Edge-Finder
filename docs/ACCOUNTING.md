# TENNIS wager accounting (routed from kalshi-bet-router)

**Accounting only.** This records tennis bets the owner already placed by hand on Kalshi. It never decides, sizes,
recommends or places a bet. `AUTONOMOUS_REAL_MONEY_AUTHORITY` stays OFF, the frozen producers stay research-only,
and nothing here reads or writes a model, a slate or an assisted-track record.

## Two different wager paths (never merged)
| | routed ledger (this document) | ChatGPT-assisted track |
|---|---|---|
| what it records | fills the router observed on the exchange | a wager a PERSON says they placed, linked to the decision (`AD-...`) they recorded first |
| who writes | kalshi-bet-router, via a pull request into `accounting-data` | the owner, via `scripts/research/record_assisted_decision.py` -> `tennis_edge.assisted.record` |
| where | branch `accounting-data`: `data/accounting/wagers.jsonl`, `settlements.jsonl` | branch `tennis-data`: `research/assisted_decisions/records/wagers/**` (`AW-...`), compiled to `assisted_wagers.jsonl`, settled by `tennis_edge.assisted.settle` |
| identity | `tenw-<24 hex>` = sha256(`source_bet_key`) | `AW-<date>-<12 hex>` minted at recording time |
| economics | the exchange's own fills and fees (`fees_are_estimated` always false) | the person's stated entry price / contracts; fees default to the published taker formula |
| provenance | none; a row carrying any model/recommendation field is REFUSED | the decision record it implements (thesis, model context, discrepancy block) |
| app export | `wagers.json` `source=KALSHI_ROUTER` | `wagers.json` `source=MANUAL` |

The assisted track is untouched by this work (docs/ASSISTED_HANDICAPPING.md). A bet may legitimately appear on both
paths (the owner records it in the assisted track AND the router observes the fill); the app export keeps them as two
wagers with different sources and ids rather than guessing they are one.

## How a routed wager gets here
1. The owner places a tennis bet on Kalshi by hand.
2. kalshi-bet-router (read-only exchange access) classifies the market as TENNIS from Kalshi's own metadata, rebuilds
   the order from its fills and sends one row in its snake_case dialect.
3. The router opens a delivery pull request into this repository's `accounting-data` branch, running this repository's
   importer (`scripts/accounting/import_routed_wagers.py`, code taken from `main`) and validator
   (`scripts/accounting/validate_routed_ledger.py`).
4. After Kalshi settles the market, the router's settlement job delivers the settlement the same way
   (`scripts/accounting/import_routed_settlements.py`, `router-settlement-economics.v2`).

## Code
The three scripts are THIN stdlib-only wrappers over the vendored, byte-identical shared ledger
`contract/edge_finder_contract/routed_ledger.py` (`LedgerSpec`, `run_import_cli`, `run_validate_cli`). The tennis
parameters are defined ONCE in `tennis_edge/accounting/spec.py`:

```python
LedgerSpec(sport="TENNIS", id_prefix="ten", wager_schema="tennis_accounted_wager.v1",
           settlement_schema="tennis_wager_settlement.v1")      # -> data/accounting/{wagers,settlements}.jsonl
```

Importing `tennis_edge.accounting.spec` pulls nothing from numpy/pandas (tested): the router's runner checks out
`main` and installs nothing from this repository.

```
python scripts/accounting/import_routed_wagers.py      --payload TENNIS.json --base-dir <accounting-data> --receipts-out r.json
python scripts/accounting/import_routed_settlements.py --payload TENNIS-settlements.json --base-dir <accounting-data> --receipts-out r.json
python scripts/accounting/validate_routed_ledger.py    --base-dir <accounting-data> [--base-ref origin/accounting-data] --result-out v.json
```
Exit codes: 0 ok, 1 refused/conflict (the router's merge gate fails), 2 unreadable payload or ledger.

## Scalar settlements (tennis-specific)
Tennis contracts can settle SCALAR on the exchange: a walkover or retirement settles at a fair price strictly
between 0 and 1 rather than at YES/NO. The router sends such a row with `result` absent/None and `gross_return` /
`net_profit_loss` exactly as the exchange states them; the shared ledger accepts `result` None with established money
(and refuses a row with neither money nor a refusal reason). The app export maps it to `result=SCALAR`.

## Guarantees (tested in `tests/test_routed_accounting.py`)
- Identity is minted here and deterministic: `wager_id` = `tenw-` + sha256(`source_bet_key`)[:24]; `settlement_id`
  = `tens-` + the same digest. No wall clock and no economics feed into either.
- Same row twice: `DUPLICATE_NOOP`, zero bytes change (byte-identical file).
- Same key with different economics: `CONFLICT`, field NAMES reported (never values), nothing rewritten, exit 1.
- A settlement with no wager on the ledger: refused as `ORPHAN`. A second, different settlement: `CONFLICT`.
- Refused rows: model/recommendation provenance fields; unknown fields; estimated fees; a venue other than kalshi;
  non-positive contracts or stake; a price outside (0, 1); naive timestamps; stake != contracts x price + fees.
- The validator checks every line decodes, both schemas, unique keys, settlement <-> wager ticker/side agreement and,
  with `--base-ref`, that both files are append-only.
- Public Actions logs carry counts and reasons only: never a ticker, stake, price, contract count, P&L or key
  (the scripts' stdout is asserted against those strings).

## Status (2026-10-02)
- `accounting-data` exists with a README and two empty ledger files; no tennis wager has been routed yet.
- The settlement path is TESTED (incl. SCALAR), not OBSERVED.
- The app export (docs/APP_EXPORT.md) reads the ledger from a checkout passed as `--accounting-dir`; both production
  workflows fetch the branch when it exists.
