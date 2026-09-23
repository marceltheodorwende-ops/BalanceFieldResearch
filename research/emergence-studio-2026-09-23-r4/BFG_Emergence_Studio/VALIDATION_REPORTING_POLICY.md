# BFG Emergence Studio — Validation Reporting Policy

The software distinguishes exploration from confirmatory validation.

## Exploratory work

Exploratory carrier variants may be iterated, rejected, simplified, or replaced
using calibration / training data.

They do not need to appear as separate headline "FAIL" results in the public
summary. Their role is engineering and model development.

However:

- they are not relabeled as confirmatory tests,
- they may not inspect the sealed held-out target metric,
- material design changes are retained in the audit/design log.

## Readiness

A carrier may receive `READY_FOR_VALIDATION` only after a prospective preflight
gate passes on calibration-only temporal folds and the final mapping + validation
plan have been fingerprinted.

`READY_FOR_VALIDATION` is **not** an empirical pass.

## Confirmatory evaluation

Once a held-out target metric is opened, the result is immutable for that frozen
plan.

A negative confirmatory result:

- remains in the empirical benchmark registry,
- is not deleted or converted to "exploratory",
- cannot be fixed by retuning on the same held-out block.

A new hypothesis may later be tested only with a newly frozen plan and genuinely
new held-out data.

## Reporting

The main project status may emphasize current validated / ready systems rather
than list every exploratory dead end.

It must nevertheless distinguish:

- `EXPLORATORY`
- `NOT_YET_VALIDATED`
- `READY_FOR_VALIDATION`
- `CONFIRMED`
- `REJECTED`

This keeps reports readable without turning omission into cherry-picking.


## Blind-heldout opening control

`READY_FOR_VALIDATION` does not grant automatic access to held-out targets.

Before confirmation, the portfolio manager seals the carrier's mapping,
validation plan, readiness artifact, frozen model, and current source tree.

A confirmatory opening then requires the exact acknowledgement:

`CONFIRM HELDOUT OPENING`

which creates a one-time permit. Using that permit consumes it before held-out
targets are transformed or scored.

This separates three distinct commitments:

1. readiness was established,
2. the implementation was frozen,
3. a human explicitly chose to spend the held-out block.

No permit is generated automatically by the master build.
