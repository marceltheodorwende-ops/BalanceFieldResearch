# BFG Emergence Studio — Real-Domain Validation Protocol

The software is ready for an external carrier, but the first real-domain result
must not be produced by inventing a convenient mapping after inspecting the
outcomes.

A real-domain benchmark therefore follows this order.

## 1. Declare the domain and target

Write a prospective statement that can fail.

Example structure:

> With one fixed measurement-to-BFG mapping, the BFG carrier will distinguish
> condition X from matched null condition Y on held-out observations without
> changing the mapping or generator parameters.

Do not use a vague target such as "show interesting emergence."

## 2. Freeze the carrier mapping

Implement a `ValidatedCarrierAdapter` and declare:

- how measurements produce `D`,
- how measurements produce `K`,
- how measurements produce positive `Y`,
- how measurements produce `R_C`,
- which parameters are invariant across the full dataset,
- physical / empirical units where applicable.

The SDK generates a SHA-256 mapping fingerprint.

After this point, changing the mapping invalidates the preregistered comparison.

## 3. Freeze calibration and held-out indices

The indices must be disjoint and written into a `HeldoutValidationPlan` before
held-out results are inspected.

Calibration data may be used only for domain-justified calibration explicitly
allowed by the plan. It may not be used to repeatedly redesign the universal BFG
generator.

## 4. Freeze the null model

The null model must receive the same observations and must be evaluated on the
same held-out indices.

A useful null should match trivial explanatory capacity so the comparison does
not reward BFG merely for having more structure.

## 5. Freeze the primary metric and success criterion

The metric and criterion are part of the plan. Secondary exploratory metrics may
be reported but must remain labeled exploratory.

## 6. Run no-retuning validation

`run_heldout_carrier_validation` checks the mapping fingerprint for every
measurement and records the core BFG reclosure diagnostics.

The held-out result is written together with:

- mapping fingerprint,
- plan fingerprint,
- source-code fingerprint,
- calibration / held-out metrics,
- null-model metrics,
- full state-level diagnostics,
- interpretation guard.

## 7. Interpretation boundary

A successful benchmark supports only the preregistered domain statement.

It does not by itself establish:

- universal empirical validity of BFG,
- consciousness,
- biological realization of all closure levels,
- a new physical law,
- superiority in unrelated domains.

Repeated no-retuning success across independently chosen domains would be stronger
evidence than tuning a separate carrier until each dataset fits.

## Current status

The protocol and software infrastructure are implemented.

No external empirical dataset is bundled as a "validated BFG carrier" yet. This
is deliberate: the first such carrier should use an independently justified
domain mapping and a genuinely held-out dataset rather than a post-hoc software
demonstration.


## Blind opening gate

A carrier that reaches `READY_FOR_VALIDATION` enters the central validation
portfolio.

Before held-out evaluation:

- run the portfolio audit,
- build a cryptographic carrier seal,
- verify the seal after all source changes,
- issue a one-time confirmation permit only when the held-out block is
  intentionally being opened.

A source-tree change invalidates the old seal. Re-sealing is permitted only
while held-out metrics remain unevaluated and the mapping / validation plan /
readiness artifacts themselves remain unchanged.

The permit is consumed at the start of confirmatory target access.
