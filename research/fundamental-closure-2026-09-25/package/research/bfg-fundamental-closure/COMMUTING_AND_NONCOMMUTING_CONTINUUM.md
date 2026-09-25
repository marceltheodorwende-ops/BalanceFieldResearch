# Commuting-Stratum Invariance and First Noncommuting Continuum

## 1. Correction to the naive multi-mode spectral lift

The scalar selected completion

\[
f(y)=\frac{2y^2}{(1+y)^2(1+y^2)}
\]

does **not** automatically lift to the full commuting multi-mode master law as

\[
Y_+=f(Y)
\]

mode by mode.

The reason is BFG-specific: reciprocal balance produces one pair of **global** branch
weights from all active formation modes.

Let the current selected commuting state be diagonal in one common basis:

\[
Y=\operatorname{diag}(y_1,\ldots,y_m),
\qquad
0<y_i<1,
\]

and let the diagonal formation density have weights

\[
r_i\ge0,
\qquad
\sum_i r_i>0.
\]

Then

\[
\Lambda_C
=
\sum_i \frac{r_i}{1+y_i},
\]

\[
\Lambda_B
=
\sum_i \frac{r_i y_i^2}{1+y_i}.
\]

Reciprocal balance gives the common scalars

\[
\alpha
=
\frac{\Lambda_B}{\Lambda_C+\Lambda_B},
\qquad
\beta
=
\frac{\Lambda_C}{\Lambda_C+\Lambda_B}.
\]

The exact intrinsic-Gram successor eigenvalues are therefore

\[
\boxed{
y_i^+
=
\frac{\alpha+\beta y_i^2}{(1+y_i)^2}.
}
\]

This is a coupled diagonal map because \(\alpha,\beta\) depend on all modes.

---

## 2. Commuting-stratum invariance theorem

Assume:

1. all current Hermitian state objects are diagonal in one common basis;
2. Selection retains the current modes under consideration;
3. the persistent projector is diagonal in that basis;
4. the formation and witness densities are diagonal;
5. no cross-stratum formation seed is required inside the selected carrier.

Then the BFG reclosure preserves the diagonal algebra.

### Reason

The exact neutral operators \(C_N(Y)\), \(B_N(Y)\), and \(G=I+Y\) are diagonal.

The \(G\)-orthogonal persistent projector equals the ordinary coordinate projector on
a coordinate spectral subspace.

The two-channel analysis map has orthogonal columns, one per spectral mode. Its right
singular frame can therefore be chosen in the same spectral basis.

For every diagonal capacity operator \(A\),

\[
U^\dagger(A\oplus A)U
\]

remains diagonal because each target column has support only in the two copies of the
same mode.

Hence

\[
\boxed{
\text{the common diagonal algebra is invariant under the successful selected reclosure.}
}
\]

This establishes a genuine commuting invariant stratum of the finite master law under
the stated conditions.

---

## 3. Selected-stratum retention

For

\[
0<y_i<1,
\qquad
0<\alpha,\beta<1,
\]

\[
0<\alpha+\beta y_i^2<1
\]

and

\[
(1+y_i)^2>1.
\]

Therefore

\[
\boxed{
0<y_i^+<1.
}
\]

Thus once a successful diagonal mode lies strictly in the retained neutral-contrast
sector, the coupled intrinsic-Gram step does not push it across the \(Y=I\) export
boundary.

The selected commuting stratum is therefore forward invariant under the coupled
load update, barring another exact gate.

---

## 4. Isotropic ray

If all active eigenvalues coincide,

\[
Y=yI,
\]

then

\[
\Lambda_C
=
\frac{R}{1+y},
\qquad
\Lambda_B
=
\frac{Ry^2}{1+y},
\qquad
R=\sum_i r_i.
\]

Hence

\[
\alpha=\frac{y^2}{1+y^2},
\qquad
\beta=\frac1{1+y^2}.
\]

Substitution gives

\[
\boxed{
y^+
=
\frac{2y^2}{(1+y)^2(1+y^2)}
=
f(y).
}
\]

Therefore the scalar Böttcher semigroup is an **exact full-master reduction on the
isotropic commuting ray**, not on an arbitrary commuting multi-mode state.

This sharpens the scope of the previous fixed-stratum operator continuum theorem.

---

## 5. Neutral-boundary quadratic tangent

Let

\[
y_i=sx_i,
\qquad
s\downarrow0,
\]

with fixed positive profile \(x\).

Set

\[
\langle x^2\rangle_r
=
\frac{\sum_j r_jx_j^2}{\sum_jr_j}.
\]

Then

\[
\alpha
=
s^2\langle x^2\rangle_r+O(s^3),
\qquad
\beta=1+O(s^2),
\]

and

\[
\boxed{
\frac{y_i^+}{s^2}
\longrightarrow
Q_i(x)
=
x_i^2+\langle x^2\rangle_r.
}
\]

Thus the multi-mode neutral boundary is governed by a coupled homogeneous quadratic
map rather than independent copies of the scalar map.

---

## 6. Two-cluster projective fixed-profile theorem

Normalize a positive projective profile by weighted mean

\[
\sum_i \bar r_i x_i=1,
\qquad
\bar r_i=\frac{r_i}{\sum_jr_j}.
\]

Suppose a positive fixed profile of the quadratic tangent has two distinct values

\[
a\ne b.
\]

Let total normalized formation weight \(p\) sit on the \(a\)-cluster and
\(q=1-p\) on the \(b\)-cluster.

Projective fixedness means

\[
x_i^2+\langle x^2\rangle_r
=
\lambda x_i.
\]

Therefore every component is a root of one quadratic equation, so there can be at most
two distinct positive values.

For the two-value case,

\[
ab=\langle x^2\rangle_r.
\]

But

\[
\langle x^2\rangle_r-ab
=
(b-a)(qb-pa).
\]

Since \(a\ne b\),

\[
qb=pa.
\]

Together with

\[
pa+qb=1,
\]

this gives

\[
\boxed{
a=\frac1{2p},
\qquad
b=\frac1{2q}.
}
\]

These are exact projective fixed-profile candidates of the neutral-boundary tangent
map. Stability of every such profile is **not** asserted by this theorem.

For equal formation weights and one distinguished mode among \(m\) modes,

\[
p=\frac{m-1}{m},
\qquad
q=\frac1m,
\]

so

\[
a=\frac{m}{2(m-1)},
\qquad
b=\frac m2.
\]

This explains the two-cluster profiles seen in finite internal audits without treating
them as empirical physics.

---

## 7. First genuinely noncommuting continuous sector

The canonical reclosure preprint already proves that for frozen

\[
Y_P,\ P,\ \alpha,\ \beta
\]

the formation operator obeys, in the eigenbasis of \(Y_P\),

\[
\boxed{
K_+=\Chi\circ K,
}
\]

with

\[
\chi_{ij}
=
\frac{\alpha+\beta y_i y_j}
{\sqrt{(\alpha+\beta y_i^2)(\alpha+\beta y_j^2)}}.
\]

When

\[
[Y,K]\ne0,
\]

cross-eigenspace matrix elements are nonzero and the sector is genuinely
noncommutative.

Because every \(\chi_{ij}>0\) for positive weights, the formation map has the exact
continuous vector-space embedding

\[
\boxed{
K(\tau)
=
\Chi^{\circ\,\tau/\log2}\circ K_0,
}
\]

where the exponent is entrywise.

At

\[
\tau=\log2,
\]

\[
K(\log2)=\Chi\circ K_0=K_+.
\]

The semigroup law follows entrywise:

\[
\boxed{
\mathcal T_{\tau+\sigma}
=
\mathcal T_\tau\mathcal T_\sigma.
}
\]

The generator is

\[
\boxed{
\frac{dK}{d\tau}
=
\mathcal L_\Chi K
=
\frac{\log\Chi}{\log2}\circ K.
}
\]

This is the first exact continuous embedding in a genuinely noncommuting BFG formation
sector.

It is a **formation-sector** result with frozen neutral geometry, not yet the complete
state-level master generator.

---

## 8. Continuous dephasing identity

For Hermitian \(K\),

\[
K_{ij}(\tau)
=
\chi_{ij}^{\tau/\log2}K_{ij}(0).
\]

Therefore

\[
\operatorname{tr}K(\tau)
=
\operatorname{tr}K(0),
\]

while

\[
\|K(\tau)\|_F^2
=
\sum_{ij}
\chi_{ij}^{2\tau/\log2}
|K_{ij}(0)|^2.
\]

Differentiating,

\[
\boxed{
\frac d{d\tau}\|K(\tau)\|_F^2
=
\frac2{\log2}
\sum_{ij}
(\log\chi_{ij})
\chi_{ij}^{2\tau/\log2}
|K_{ij}(0)|^2
\le0.
}
\]

The inequality is strict whenever \(K\) contains matrix elements between distinct
\(Y\)-eigenspaces.

Thus the discrete inheritance/novelty theorem acquires an exact continuous frozen-
geometry counterpart.

---

## 9. Positivity obstruction for fractional Schur times

The discrete multiplier \(\Chi\) is a correlation matrix and therefore its one-step
Schur map is completely positive.

However, the entrywise fractional powers

\[
\Chi^{\circ s},
\qquad
0<s<1,
\]

need not remain positive semidefinite.

Hence the exact vector-space interpolation above need not be a positive or completely
positive map on arbitrary positive matrices at intermediate times.

A simple deterministic counterexample uses

\[
\alpha=\beta=\frac12,
\qquad
(y_1,y_2,y_3)=\left(\frac1{10},1,10\right).
\]

Then

\[
\Chi=
\begin{pmatrix}
1&a&b\\
a&1&a\\
b&a&1
\end{pmatrix},
\]

with

\[
a=\frac{11}{\sqrt{202}},
\qquad
b=\frac{20}{101}.
\]

For the half-step \(s=\frac12\),

\[
\Chi^{\circ1/2}
=
\begin{pmatrix}
1&\sqrt a&\sqrt b\\
\sqrt a&1&\sqrt a\\
\sqrt b&\sqrt a&1
\end{pmatrix}.
\]

Its determinant is

\[
\boxed{
1-2a-b+2a\sqrt b<0.
}
\]

Therefore

\[
\Chi^{\circ1/2}\not\succeq0.
\]

So the frozen noncommuting formation sector has an exact Hermiticity-preserving
continuous embedding, but **not in general a positive/CP Schur semigroup**.

This blocks the naive promotion of that interpolation to a universal density-state
continuum.

---

## 10. Consequence for the full state-level conjugacy

The current continuum structure is now sharper.

### Commuting full-master sector

The full selected commuting algebra is invariant, but its load dynamics is globally
coupled through reciprocal weights.

Only the isotropic ray reduces exactly to the scalar Böttcher map.

### Frozen noncommuting formation sector

An exact continuous linear semigroup exists:

\[
\partial_\tau K
=
(\log\Chi/\log2)\circ K.
\]

It is generally not a positive semigroup on the full matrix cone.

### Full noncommuting master state

Still open.

A genuine state-level continuous conjugacy must simultaneously preserve:

- positive formation density;
- positive normalized witness;
- admissibility;
- Selection/Export;
- rank-changing event structure;
- BFG recursion.

The frozen formation semigroup proves that noncommutativity itself does not forbid
continuous interpolation. The fractional-positivity counterexample proves that
formation interpolation alone is insufficient for a universal positive state flow.
