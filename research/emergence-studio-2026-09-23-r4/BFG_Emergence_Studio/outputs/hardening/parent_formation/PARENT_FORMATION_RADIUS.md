# BFG Parent-State Formation Radius

**Conditional theorem; no held-out target is opened.**

The declared parent product norm is

\[
\|\Delta S\|_\oplus=
\max\{\|\Delta K\|_2,\|\Delta Y\|_2,\|\Delta R\|_2,
\|\Delta\rho\|_1\}.
\]

The conditional theorem applies to admissible perturbations inside the normal-contraction BFG category. A stricter runtime-stratum certificate additionally proves preservation of the declared persistent and active numerical ranks.

States audited: `40`

Positive parent-radius certificates: `40/40`

Structured admissible perturbation controls preserving status: `40/40`

Structured controls satisfying the predicted active spectral bound: `40/40`

Strict runtime-stratum controls preserving status and active rank: `40/40`

| Carrier | Certified | Median conditional radius | Median full runtime-stratum radius |
|---|---:|---:|---:|
| annual-sunspots | 2/2 | 1.31177e-05 | 1.64318e-13 |
| mauna-loa-co2 | 2/2 | 9.303e-06 | 1.13678e-13 |
| enso-pacific-sst | 2/2 | 2.54868e-06 | 3.4622e-14 |
| zachary-karate-network | 34/34 | 1.40955e-07 | 1.80986e-14 |

## The transport chain

1. `Delta R` is converted to a persistent-subspace rotation bound through the Hermitian gap of `I-R*R`.
2. `Delta Y` controls the exact neutral resolvent through the resolvent identity.
3. Persistent-projector, load and reciprocal-weight perturbations give an explicit `Delta A` bound.
4. Wedin subspace perturbation controls the active left support.
5. Compression of `K xor K` converts that support rotation into an explicit `Delta K_+` bound.
6. If the resulting bound is smaller than the exact active formation margin, formation status is preserved.

## Full runtime-stratum radius

The stricter runtime-stratum radius additionally guarantees that the declared persistent and active numerical ranks themselves do not cross their runtime thresholds. In the current carriers this stricter radius is controlled overwhelmingly by the latent active-rank surface near the `rank_tol` threshold.

This stricter radius is operational: it protects the declared finite runtime decision. It is not a positive radius for exact algebraic rank.

## Essential restriction

The theorem is not an unconstrained exact-rank ambient-matrix ball. An arbitrarily small radial inward perturbation can destroy exact unit-circle persistence, and exact matrix rank can increase under arbitrarily small perturbations. The stricter runtime-stratum radius instead protects the finite runtime's thresholded rank decisions inside the admissible positivity / normal-contraction category.
