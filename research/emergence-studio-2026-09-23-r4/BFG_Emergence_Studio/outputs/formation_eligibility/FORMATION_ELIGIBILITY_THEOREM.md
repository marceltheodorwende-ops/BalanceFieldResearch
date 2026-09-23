# BFG Formation Eligibility Theorem

**No held-out target is opened.**

Let

\[
H=K\oplus K,\qquad A=U_r\Sigma_rV_r^\dagger.
\]

The active formation operator is

\[
K_+=U_r^\dagger H U_r.
\]

Define on the active right support

\[
M=V_r^\dagger A^\dagger H A V_r,\qquad
N=V_r^\dagger A^\dagger A V_r.
\]

Because

\[
M=\Sigma_rK_+\Sigma_r,\qquad N=\Sigma_r^2,
\]

the generalized eigenvalues of `(M,N)` are exactly the eigenvalues of `K_+`.

Therefore formation is admissible exactly when the smallest generalized eigenvalue is negative and simple under the declared gate tolerances.

## Parent-ground witness

For a normalized ground vector `u_-` of the parent `K`, let

\[
\chi_-=
\frac{\langle Au_-,(K\oplus K)Au_-\rangle}
{\langle Au_-,Au_-\rangle}.
\]

By the min-max principle,

\[
\chi_-<0\quad\Longrightarrow\quad\lambda_{\min}(K_+)<0.
\]

This is a sufficient carrier-independent witness, not a general necessity theorem.

## Current audit

States audited: `1409`

Maximum direct/generalized eigenvalue mismatch: `3.553e-15`

| Carrier | Gate states | Successes | Parent K negative | Exact criterion | Ground witness sign | Min gap |
|---|---:|---:|---:|---:|---:|---:|
| annual-sunspots | 297 | 297 | 297 | 297/297 | 297/297 | 1.45508 |
| mauna-loa-co2 | 370 | 370 | 370 | 370/370 | 370/370 | 1.55709 |
| enso-pacific-sst | 708 | 708 | 708 | 708/708 | 708/708 | 1.40954 |
| zachary-karate-network | 34 | 13 | 34 | 34/34 | 34/34 | 0.0838803 |

## Why 13/34 in the relational network?

All 34 parent `K` operators already have a negative ground mode.

All 34 active formation gaps exceed the simplicity threshold.

The differentiating quantity is the transported ground-mode witness:

- all 13 successful probes have `chi_- < 0`;
- all 21 formation terminals have `chi_- > 0`.

Thus the observed split is a transport/capture effect of the persistent neutral packet, not absence of a negative parent mode.
