# Fixed-Stratum Operator Continuum Theorem

## 1. Scope

The scalar selected BFG reclosure admits the exact continuous embedding

\[
\theta(f(y))=2\theta(y),
\qquad
\partial_\tau\theta=\theta.
\]

This document gives the largest operator lift currently justified without inventing a
new noncommutative continuum law.

The lift is **conditional** on a fixed spectral stratum in which the discrete load
update is genuinely modewise:

\[
\boxed{
Y_+=f(Y)
}
\]

by standard spectral functional calculus, with

\[
0<Y\le I.
\]

No rank change, Selection jump, support change, or eigenvector rotation is allowed
inside this stratum.

## 2. Spectral functional calculus

Let

\[
Y=\sum_j y_jP_j,
\qquad
0<y_j\le1.
\]

For every scalar BFG function \(g\), define

\[
g(Y)=\sum_jg(y_j)P_j.
\]

In particular,

\[
\boxed{
\Theta(Y)=\theta(Y)=\sum_j\theta(y_j)P_j.
}
\]

Since

\[
\theta(f(y_j))=2\theta(y_j),
\]

we obtain the exact operator identity

\[
\boxed{
\Theta(f(Y))=2\Theta(Y).
}
\]

No matrix approximation is involved.

## 3. Exact fixed-stratum semigroup

Define

\[
\boxed{
\Theta(Y(\tau))=e^\tau\Theta(Y_0).
}
\]

Because the scalar coordinate is invertible on the retained branch, this defines

\[
Y(\tau)=F_\tau(Y_0)
\]

mode by mode.

The family obeys

\[
\boxed{
F_{\tau+\sigma}=F_\tau\circ F_\sigma.
}
\]

At

\[
\tau=\log2,
\]

\[
\Theta(F_{\log2}(Y))=2\Theta(Y)=\Theta(f(Y)),
\]

hence

\[
\boxed{
F_{\log2}(Y)=f(Y).
}
\]

Thus one finite BFG scalar-mode reclosure is exactly one fixed amount of recursive
time in this operator stratum.

## 4. Operator generator

Let

\[
v(y)=\frac{\theta(y)}{\theta'(y)}.
\]

Then spectral functional calculus gives

\[
\boxed{
\frac{dY}{d\tau}
=
\mathcal V(Y)
=
v(Y).
}
\]

Equivalently,

\[
\boxed{
\frac{d\Theta}{d\tau}=\Theta.
}
\]

Because \(v(y)<0\) on \(0<y<1\), every selected eigenvalue moves monotonically toward
zero while its spectral projector is fixed.

## 5. Unitary covariance

For a unitary coordinate change

\[
Y'=UYU^\dagger,
\]

functional calculus gives

\[
\Theta(Y')=U\Theta(Y)U^\dagger,
\]

\[
F_\tau(Y')=UF_\tau(Y)U^\dagger,
\]

and

\[
\mathcal V(Y')=U\mathcal V(Y)U^\dagger.
\]

Therefore the fixed-stratum continuum is basis independent.

## 6. Commuting BFG subalgebra

A strong sufficient condition for a complete fixed operator stratum is that the
relevant Hermitian BFG state objects commute pairwise, for example

\[
[Y,\mathfrak D]
=
[Y,\mathfrak c]
=
[Y,\aleph]
=
[Y,\rho_F]
=
[Y,\rho_W]
=
[Y,R_C]
=0,
\]

with corresponding pairwise commutation where simultaneous diagonalization of the
whole tuple is required.

Then there is a common spectral basis and the finite BFG equations reduce to coupled
scalar mode equations **provided the reclosure law preserves that algebra**.

This last preservation condition must be checked; commutation at one instant alone
does not prove it for the full master update.

## 7. Why the general master law is different

The living finite master update uses more than a scalar function of \(Y\). It also
contains:

- the persistent Riesz sector;
- the \(G\)-orthogonal projector;
- formation density;
- reciprocal weights;
- a rectangular cross-fed analysis map;
- reduced SVD/polar transport;
- Selection/Export;
- rank-changing R4 continuation;
- emergent formation seeding.

Therefore, in general,

\[
Y_+\ne f(Y)
\]

as an operator functional-calculus identity.

The eigenvectors can rotate and the carrier dimension can change.

Consequently the fixed-stratum Böttcher semigroup must not be silently applied to the
full noncommutative runtime.

## 8. Rank-change obstruction to one fixed-manifold smooth flow

Suppose the state space were one fixed finite-dimensional smooth manifold and the full
BFG evolution were generated everywhere by one ordinary smooth vector field.

A smooth trajectory remains in that same manifold dimension. But the exact BFG event
maps can change active carrier and persistent ranks.

Therefore a rank-changing transition cannot be represented merely as an ordinary
smooth flow on one fixed-rank matrix manifold.

It requires either:

1. a larger ambient stratified state space; or
2. an explicit jump/event map between fixed-rank strata.

The current BFG mathematics already supplies the second structure through Selection
and R4 polar continuation.

Thus

\[
\boxed{
\text{fixed-stratum continuous flow}
+
\text{exact cross-stratum jump maps}
}
\]

is the natural present architecture.

## 9. Noncommutativity is an obstruction to the spectral lift, not a global no-go

If

\[
[Y,A]\ne0
\]

for other state operators, the update may rotate eigenvectors and couple spectral
modes. Then the scalar functional calculus alone cannot reconstruct the full next
state.

This proves only

\[
\boxed{
\text{the modewise Böttcher lift is insufficient in the noncommuting sector.}
}
\]

It does **not** prove that no noncommutative continuous embedding exists.

A future full operator generator would need a conjugacy on the complete typed state
bundle, for example a map \(\boldsymbol\Theta\) satisfying a state-level Schröder or
Koenigs equation such as

\[
\boldsymbol\Theta(\mathcal U(X))
=
e^{\mathcal L}\boldsymbol\Theta(X),
\]

with the correct treatment of event surfaces and changing carrier types.

No such global conjugacy has yet been derived.

## 10. Current result

The continuum program now has three rigorously separated levels.

### Level C0 — scalar retained stratum

Exact Böttcher semigroup: established conditionally on the selected scalar completion.

### Level C1 — fixed commuting/operator stratum

Exact spectral Böttcher semigroup whenever the discrete BFG load update is modewise
\(Y_+=f(Y)\) and the stratum is preserved.

### Level C2 — full noncommuting/rank-changing master law

No global smooth generator established. Current mathematically justified architecture:
stratified continuous flows plus exact BFG event maps.


## Scope correction: full commuting master versus conditional spectral lift

The spectral theorem in this document remains correct **conditional on**
\(Y_+=f(Y)\) modewise.

The later commuting-stratum audit shows that the full multi-mode BFG master law does
not generally satisfy this premise, because reciprocal balance uses global branch
loads and therefore global weights \(\alpha,\beta\).

For the actual selected commuting master state,

\[
y_i^+
=
\frac{\alpha+\beta y_i^2}{(1+y_i)^2},
\]

with \(\alpha,\beta\) depending on all active modes.

Thus the exact Böttcher operator lift here applies directly to the isotropic ray
\(Y=yI\), the one-dimensional sector, or any separately proved modewise submodel. It
is not the generic full commuting multi-mode continuum.

See `COMMUTING_AND_NONCOMMUTING_CONTINUUM.md`.
