# Mathematical Closure Ledger

## Active master status

The BFG Emergence Studio now adopts the 23 September reduced finite closure laws
as its **binding finite runtime profile**.

Within that declared category:

- finite next-state reconstruction is **closed**;
- Gram reconstruction is **closed** by the selected intrinsic-Gram law and
  square-root factor gauge;
- recursive successor transport is **closed** by the fixed unitary law
  \(R_+=\exp(i\tau K_+)\);
- the update is a single-valued total map after adjoining absorbing \(\bot\);
- every exact finite iterate is defined;
- a restricted bounded infinite-dimensional input class with finite peripheral
  rank reduces to the finite profile.

These are no longer listed as open runtime obligations.

## Supporting exact mathematics

The runtime profile is supported by:

- the finite power-boundedness criterion;
- the exact supplied rational nonnormal persistence certificate;
- exact neutral-resolvent identities;
- the retained-channel Gram-energy identity;
- the simple-negative-mode formation gate;
- unitary successor recursion after successful finite closure.

## Scope

The runtime architecture makes an explicit mathematical **law selection**. It
does not need a separate proof that older source axioms uniquely force this
selection.

That historical/internal-uniqueness question is therefore not an operational
closure gap in the master.

The current executable master category does not attempt arbitrary unbounded
infinite-rank operator transport. Empirical natural realization is also a
separate question from mathematical/runtime closure.


## Recursive load contraction

The one-dimensional reduced master map has the exact recurrence

\[
y_+
=
\frac{2y^2}{(1+y)^2(1+y^2)}.
\]

Thus the small-load sector contracts quadratically.

Cross-domain real-carrier trajectories show depth-2 and depth-3 fitted
exponents close to this quadratic regime. This is recorded as a structural
contraction result.

The finite numerical depth at which a trajectory is committed to absorbing
`bottom` is not an exact zero-load theorem; it depends on the declared
numerical admissibility floors.


## Multidimensional quadratic contraction

Closed under the declared finite master assumptions:

\[
\lambda_{\rm up}\le\mu\|Y\|_2^2,
\]

\[
\alpha
\le
\frac{\mu}{\lambda_{\rm keep}}\|Y\|_2^2,
\]

and

\[
\boxed{
\|Y_+\|_2
\le
\|P\|_2^2
\left(
1+\frac{\mu}{\lambda_{\rm keep}}
\right)
\|Y\|_2^2.
}
\]

If one uniform contraction coefficient \(C\) persists and \(C\|Y_0\|<1\),

\[
\|Y_n\|_2
\le
C^{-1}(C\|Y_0\|_2)^{2^n}.
\]

The one-step theorem is independent of empirical carrier performance. The
current carrier audits only verify that implemented successful states satisfy
its explicit inequalities.





## Formation eligibility generalized-spectrum closure

For the finite master packet

\[
A=U_r\Sigma_rV_r^\dagger,
\qquad
H=K\oplus K,
\]

the active successor formation operator is

\[
K_+=U_r^\dagger H U_r.
\]

On the active right support,

\[
M=V_r^\dagger A^\dagger H A V_r
=\Sigma_rK_+\Sigma_r,
\]

\[
N=V_r^\dagger A^\dagger A V_r
=\Sigma_r^2.
\]

Hence

\[
\boxed{
\sigma_{\rm gen}(M,N)=\sigma(K_+).
}
\]

The simple-negative formation gate is therefore exactly representable as a
finite generalized-eigenvalue criterion.

For a parent ground vector \(u_-\),

\[
\chi_-=
\frac{\langle Au_-,(K\oplus K)Au_-\rangle}
{\|Au_-\|^2}<0
\]

is a sufficient active-negativity witness by the min-max principle.

The current `1,409`-state audit verifies the direct/generalized spectral
identity to a maximum residual of approximately `3.55e-15`.


## Formation bifurcation margin

Closed for the active finite Hermitian formation operator.

Eligible distance to the complementary gate set:

\[
\boxed{
d_+
=
\min\left(
-\varepsilon_{\rm sign}-\lambda_0,\,
\frac{
\lambda_1-\lambda_0-\varepsilon_{\rm simple}
}{2}
\right).
}
\]

Terminal-state infimum distance to the eligible set:

\[
\boxed{
d_-
=
\max\left(
(\lambda_0+\varepsilon_{\rm sign})_+,\,
\frac{
(\varepsilon_{\rm simple}-(\lambda_1-\lambda_0))_+
}{2}
\right).
}
\]

Exactness follows from Weyl bounds plus extremal perturbations aligned with
the lowest two eigenspaces.

A parent-state norm radius remains a separate theorem because the active
packet subspace itself varies under perturbations of \(K,Y,R,\rho\).


## Conditional parent-state formation robustness

Closed as a sufficient perturbation theorem on a fixed admissible
persistent-rank / active-rank stratum.

With the componentwise product norm

\[
\|\Delta S\|_\oplus
=
\max\{
\|\Delta K\|_2,\|\Delta Y\|_2,
\|\Delta R\|_2,\|\Delta\rho\|_1
\},
\]

the implemented bound transports \(\delta\) through persistent-subspace,
weighted-projector, neutral-resolvent, reciprocal-load, packet and
active-subspace perturbations to obtain

\[
\|\Delta K_+\|_2\le E_F(\delta).
\]

If

\[
E_F(\delta)<|\mathfrak m_F|,
\]

formation status is preserved.

No unrestricted ambient radius exists in general because exact persistence
and exact active rank are not open properties. This non-openness is now
explicitly represented in the mathematical audit rather than hidden behind
a numerical tolerance.


## Runtime stratum-transition closure

Closed for the declared finite numerical runtime under the stated
normal-contraction and admissibility assumptions.

Persistent runtime rank:

\[
r_P
=
\min\{
\sigma_p(R)-(1-\varepsilon_P),\,
(1-\varepsilon_P)-\sigma_{p+1}(R)
\}
\]

is a native sufficient operator radius.

Active runtime rank:

\[
r_A
=
\frac{
\min\{
\sigma_r(A)-\tau_A,\,
\tau_A-\sigma_{r+1}(A)
\}
}{
1+\mathrm{rtol}
}
\]

with

\[
\tau_A=\max(\mathrm{rank\_tol},\mathrm{rtol}\,\sigma_1(A))
\]

is a native sufficient packet radius.

Combined parent guarantee:

\[
\boxed{
\delta<r_P,\quad
E_A(\delta)<r_A,\quad
E_F(\delta)<|\mathfrak m_F|
}
\]

implies preservation of runtime persistent rank, runtime active rank and
formation status.

Exact algebraic rank and exact unit-circle persistence remain explicitly
non-open; no contradictory ambient exact-rank theorem is claimed.
