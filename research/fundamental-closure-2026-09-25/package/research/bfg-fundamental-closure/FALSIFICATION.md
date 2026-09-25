# Falsification and Failure Criteria

This file defines ways the current **conditional finite BFG candidate** can fail.

## Exact mathematical failures

Any one of the following refutes the stated current finite candidate or one of its
theorems in the declared scope:

- a valid state for which the implemented exact neutral partition fails;
- a successful update that violates positivity/category conditions of
  \(\rho_F,\rho_W,Y\);
- a successful update that changes witness trace away from one;
- witness support outside the declared persistent projector;
- a successful cross-fed step with
  \[
  \dim\mathcal H_+>\dim\mathcal H;
  \]
- failure of unitary covariance in a theorem that claims it;
- failure of the full-persistent selected lock for exact \(P=I,\ 0<Y<I\);
- a counterexample to a stated branch-count/root-count theorem inside its assumptions;
- a current file that treats a declared completion as source-derived without proof.

## Numerical implementation failures

These are implementation failures, not automatically physical falsifications:

- test regression;
- inconsistent terminal reason labels;
- threshold-sensitive classification presented as exact;
- non-reproducible stress JSON;
- broken manifest or internal file reference;
- source code that does not compile.

The implementation must distinguish exact stops from numerical ambiguity.

Examples:

- exact: `dual_load_zero_terminal`;
- numerical only: `dual_load_numerical_ambiguity`,
  `numerical_rank_ambiguity`,
  `neutral_contrast_boundary_ambiguity`.

## Continuum-completion failures

A continuum rule is rejected in its stated scope if it:

- misses committed discrete endpoints;
- breaks positivity where positivity is claimed;
- breaks exact same-rank R4 endpoint transport;
- silently changes projector rank along a continuous exact-projector path;
- uses hidden history where a local-state theorem claims none is required.

## Physical-program falsification

Future physical claims require independent predictions.

A physical-sector claim fails if it only reproduces known equations by inserting their
structure, tuning sector-specific parameters, or choosing boundary data after seeing
the target.

The present package does not yet make a completed Theory-of-Everything claim.
