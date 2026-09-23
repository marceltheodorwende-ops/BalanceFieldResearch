# BFG Formation Robustness and Bifurcation Surface

**No held-out target is opened.**

The finite formation gate is

\[
\lambda_0<-\varepsilon_{\rm sign},
\qquad
\lambda_1-\lambda_0>\varepsilon_{\rm simple}.
\]

Define

\[
s=-\varepsilon_{\rm sign}-\lambda_0,
\qquad
g=(\lambda_1-\lambda_0)-\varepsilon_{\rm simple}.
\]

For an eligible active operator the exact operator-norm distance to loss of formation is

\[
\boxed{
r_+=\min\left(s,\frac{g}{2}\right).
}
\]

For an ineligible operator the infimum distance to the eligible set is

\[
\boxed{
r_-=\max\left((-s)_+,\frac{(-g)_+}{2}\right).
}
\]

The signed formation margin is `+r_+` for eligible states and `-r_-` for terminal states.

These formulas are exact in Hermitian operator 2-norm by Weyl's inequalities, and the bounds are attained by perturbations aligned with the two lowest eigenspaces.

## Audit

Gate states: `1409`

Sub-boundary adversarial controls preserving status: `1409/1409`

Just-beyond-boundary controls crossing status: `1409/1409`

| Carrier | Eligible | Terminal | Median |margin| | Sign-limited | Gap-limited |
|---|---:|---:|---:|---:|---:|
| annual-sunspots | 297 | 0 | 0.793453 | 0 | 297 |
| mauna-loa-co2 | 370 | 0 | 0.809676 | 0 | 370 |
| enso-pacific-sst | 708 | 0 | 0.758325 | 0 | 708 |
| zachary-karate-network | 13 | 21 | 0.0967446 | 31 | 3 |

## Relational network

Eligible probes: `13`

Terminal probes: `21`

Nearest eligible state to the bifurcation surface: `0.0166927689`

Nearest terminal state to the bifurcation surface: `-0.0183398303`

The signed margin therefore resolves not only the `13/21` classification but also how much active-operator perturbation is required to change that classification.

## Claim boundary

The radius is exact for perturbations of the active Hermitian formation operator `K_+`. It is not yet a theorem giving the same radius directly in the parent `(K,Y,R,rho)` state norm, because parent perturbations can also rotate the active packet subspace.
