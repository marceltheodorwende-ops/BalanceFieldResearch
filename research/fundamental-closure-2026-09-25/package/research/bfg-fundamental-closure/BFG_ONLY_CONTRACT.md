# BFG-Only Contract

## Purpose

This file is the methodological contract for the living fundamental-closure package.

The package may use standard mathematics freely, but it may not import an external
physical law as a fundamental BFG equation.

## Epistemic labels

Every nontrivial statement belongs to one of these classes:

- **SOURCE BFG / BFG PRIMITIVE** — explicitly present in the BFG source corpus.
- **BFG DERIVED** — follows from source BFG plus stated mathematics.
- **KNOWN MATHEMATICS APPLIED TO BFG** — standard mathematical theorem/classification.
- **DECLARED FINITE BFG COMPLETION RULE** — BFG-internal choice needed to make the
  discrete finite candidate single-valued, not uniquely forced by the historical source.
- **DECLARED CONTINUUM COMPLETION RULE** — interpolation rule between committed finite
  states; not part of the discrete finite law.
- **NUMERICAL INTERNAL WITNESS** — reproducible finite computation, not empirical
  evidence.
- **OPEN** — not established.
- **REFUTED** — disproved in the stated scope.

## Current committed finite state

\[
\Xi=
(\mathcal H,\mathfrak D,\mathfrak c,\aleph,\rho_F,\rho_W,Y,R_C).
\]

The cached persistent projector is derived from \(R_C\).

A vector \(d\) is not fundamental; it is only a rank-one chart when
\(\rho_F=dd^\dagger\).

## Current declared finite completions

The living finite candidate uses exactly these three declared completions:

1. **Intrinsic-Gram successor load**
   \[
   Y_+=\Sigma^2
   \]
   in reduced active coordinates.

2. **Neutral-Contrast Selection**
   \[
   Q_{\rm retain}
   =
   \mathbf1_{(0,\infty)}
   \left[(I-Y)(I+Y)^{-1}\right].
   \]

3. **Neutral transverse recursion**
   \[
   R_{C,+}
   =
   P_+
   +(I-P_+)C_N(Y_+)(I-P_+).
   \]

They are BFG-internal and no-retuning, but they are not retroactively relabelled as
historical source theorems.

## Current continuum completions

The continuum research layer additionally uses:

- affine interpolation in closure depth \(H=-\log Y\) between committed endpoints;
- recursive phase \(\Omega\);
- branch-continuity memory \(M_b\) where the phase readout is non-injective;
- exact same-rank R4 principal-angle support interpolation;
- exact finite event maps for rank change.

These continuum rules do not modify the discrete committed update.

## Prohibited shortcuts

Do not:

- insert Einstein, Schrödinger, Yang–Mills, Standard Model, QFT, thermodynamic, or
  domain-specific physical equations into the fundamental BFG law;
- call a completion rule `DERIVED` merely because it is simple or canonical-looking;
- turn floating tolerances into physical constants;
- identify numerical ambiguity with exact terminality;
- claim a Theory of Everything before independently testable physical sectors are
  derived from the frozen universal law;
- relabel known mathematics as new BFG mathematics.

## Update policy

Files are updated in place. No `v1`, `v2`, date-suffixed, or parallel “latest” trees are
created. Git history is the chronology.
