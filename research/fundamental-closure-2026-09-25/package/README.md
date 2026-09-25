# BFG Fundamental Closure

Living research package for deriving a BFG-only fundamental closure law.

## Update policy

This package is deliberately **unversioned**. There will be no `v1`, `v2`, `v3`,
date-stamped successor folder, or parallel "latest" copy. New mathematical results
update these files in place. Git history is the chronology.

## Scientific objective

Derive a single-valued universal state update

\[
\Xi^+ = \mathcal U_{\mathrm{BFG}}(\Xi)
\]

from BFG primitives alone.

"From BFG alone" means:

- standard mathematics may be used freely;
- known mathematical results must be identified as known mathematics;
- no GR, QFT, Standard Model, thermodynamic, or other external physical law may be
  inserted as a fundamental BFG equation;
- external physical theories may appear later only as derived limits, comparison
  models, or falsification targets;
- any new law not derived from existing BFG primitives must be labelled
  `NEW BFG AXIOM / HYPOTHESIS`, not `DERIVED`.

## Current status

The historical/source BFG corpus alone does not uniquely force a complete successor
map. The living package now defines one deterministic finite master-law **candidate**
conditional on three explicitly declared BFG-internal completion rules: intrinsic-Gram
successor load, Neutral-Contrast Selection, and neutral transverse recursion.

Those rules are not retroactively labelled source-derived. The continuum layer adds
separately labelled interpolation rules and does not modify the committed finite step.

## Mandatory claim classes

Every claim is labelled as one of:

1. `BFG PRIMITIVE`
2. `BFG DERIVED`
3. `KNOWN MATHEMATICS`
4. `NEW BFG AXIOM / HYPOTHESIS`
5. `NUMERICAL FINDING`
6. `EMPIRICAL FINDING`
7. `OPEN`
8. `REFUTED`

A BFG construction may land in a known mathematical class. That does not make the
construction "non-BFG", but known consequences of the class are not relabelled as
new BFG mathematics.

## Package map

- `research/bfg-fundamental-closure/BFG_ONLY_CONTRACT.md`
- `research/bfg-fundamental-closure/MASTER_STATE.md`
- `research/bfg-fundamental-closure/UNIVERSAL_STATE_UPDATE_CANDIDATE.md`
- `research/bfg-fundamental-closure/FUNDAMENTAL_CLOSURE_LAW.md`
- `research/bfg-fundamental-closure/CLAIMS.md`
- `research/bfg-fundamental-closure/RESEARCH_PLAN.md`
- `research/bfg-fundamental-closure/FALSIFICATION.md`
- `research/bfg-fundamental-closure/PRIOR_ART_BOUNDARY.md`
- `bfg_lab/fundamental_closure.py`
- `tests/test_fundamental_closure.py`

This package is a research program plus executable theorem-level kernel. It is
**not yet a Theory of Everything**.

## Fixed-stratum operator continuum

See `research/bfg-fundamental-closure/FIXED_STRATUM_OPERATOR_CONTINUUM.md`. The scalar Böttcher flow lifts exactly by spectral calculus whenever a selected operator stratum is genuinely modewise and carrier-preserving. Rank-changing/noncommuting evolution remains stratified.

## Commuting and first noncommuting continuum

See `research/bfg-fundamental-closure/COMMUTING_AND_NONCOMMUTING_CONTINUUM.md`. It derives the actual globally coupled commuting load map and an exact frozen noncommuting formation semigroup, together with a fractional-positivity obstruction.

## Frozen Schur CP embeddability

See `research/bfg-fundamental-closure/FROZEN_SCHUR_CP_EMBEDDABILITY.md`. It classifies frozen noncommuting BFG reclosure into CP-embeddable and Hermiticity-only continuous strata using the Schoenberg condition.

## Canonical two-channel CP suspension

See `research/bfg-fundamental-closure/CANONICAL_TWO_CHANNEL_CP_SUSPENSION.md`. Every frozen two-channel BFG Schur reclosure has a continuous CP angle interpolation, even when no CP semigroup exists.

## Phase-anchored state suspension

See `research/bfg-fundamental-closure/PHASE_ANCHORED_STATE_SUSPENSION.md`. The reduced discrete state does not uniquely determine its continuum interpolation; the current package uses a closure-depth bridge plus recursive phase/anchor suspension and a same-rank R4 principal-angle path.

## Local anchor elimination

See `research/bfg-fundamental-closure/LOCAL_ANCHOR_ELIMINATION_THEOREM.md`. The anchor is locally reconstructible from current state plus recursive phase whenever the suspension chart is invertible; memory is only required to distinguish dynamically different non-injective continuation branches.

## Simple-fold memory geometry

See `research/bfg-fundamental-closure/SIMPLE_FOLD_MEMORY_THEOREM.md`. The first coupled two-mode inverse singularity is a generic simple fold: one bit suffices locally, but the global three-branch example requires a branch/chart identifier rather than one universal bit.

## Global memory graph

See `research/bfg-fundamental-closure/GLOBAL_MEMORY_GRAPH_THEOREM.md`. The current continuum completion admits a constructive `3^(n-1)` continuation-branch lower bound in n-mode commuting strata, ruling out one universal fixed finite-state memory bound across unbounded dimension.

## Carrier-dimension monotonicity

See `research/bfg-fundamental-closure/CARRIER_DIMENSION_MONOTONICITY_THEOREM.md`. The cross-fed successor carrier never exceeds the source carrier dimension; repeated persistence growth can occur inside a fixed carrier, and full selected persistence is forward locked.

## Fixed-dimension memory tameness

See `research/bfg-fundamental-closure/FIXED_DIMENSION_MEMORY_TAMENESS.md`. O-minimal uniform finiteness gives a finite branch-count bound at each fixed carrier dimension on finite inverse fibers; only positive-dimensional dynamically inequivalent fibers remain as a route to non-finite memory.

## Reciprocal-alpha fiber reduction

See `research/bfg-fundamental-closure/RECIPROCAL_ALPHA_FIBER_REDUCTION.md`. At fixed reciprocal alpha, each selected mode has at most three inverse roots; any positive-dimensional full-persistent load fiber is at most one-dimensional and can be parameterized by alpha plus a finite sheet label.

## Consistency gate

See `research/bfg-fundamental-closure/CONSISTENCY_AUDIT.md` and `PACKAGE_STATUS.json`. The current audited package passes compile, 174 regression tests, both deterministic stress generators, manifest/reference checks, and the static consistency audit.
