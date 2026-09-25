# Frozen Schur CP-Embeddability Theorem

## 1. Problem

For frozen neutral geometry, canonical BFG formation reclosure is

\[
K_+=\Chi\circ K,
\]

with \(\Chi\) a positive-entry correlation matrix.

The exact Hermiticity-preserving interpolation

\[
K(\tau)=\Chi^{\circ\tau/\log2}\circ K_0
\]

always exists because every \(\chi_{ij}>0\).

But positivity of the intermediate Schur maps is a stronger question.

---

## 2. Schoenberg criterion

Define

\[
D_{ij}=-\log\chi_{ij}.
\]

Standard Schoenberg theory states that

\[
\Chi^{\circ t}\succeq0
\quad\text{for every }t\ge0
\]

if and only if \(D\) is conditionally negative semidefinite:

\[
\sum_i x_i=0
\quad\Longrightarrow\quad
x^TDx\le0.
\]

Equivalently, with

\[
J=I-\frac1n\mathbf1\mathbf1^T,
\]

\[
\boxed{
-\frac12 JDJ\succeq0.
}
\]

Therefore the frozen BFG Schur reclosure is continuously positive/CP-embeddable by
entrywise powers exactly when this centered Gram condition holds.

This criterion is standard mathematics; its role here is to classify the specific
BFG-generated correlation multipliers.

---

## 3. Two-mode theorem

For two modes,

\[
\Chi=
\begin{pmatrix}
1&c\\
c&1
\end{pmatrix},
\qquad
0<c\le1.
\]

Then

\[
D=
\begin{pmatrix}
0&d\\
d&0
\end{pmatrix},
\qquad
d=-\log c\ge0.
\]

For every zero-sum vector \((a,-a)\),

\[
(a,-a)D(a,-a)^T=-2da^2\le0.
\]

Hence every two-mode frozen BFG Schur reclosure is infinitely divisible and admits the
positive/CP semigroup

\[
\boxed{
T_\tau(M)
=
\Chi^{\circ\tau/\log2}\circ M.
}
\]

Thus the first genuinely noncommuting **two-mode** frozen sector has a complete
continuous positive embedding.

---

## 4. Three-mode obstruction

The property fails in general from three modes onward.

Choose

\[
\alpha=\beta=\frac12,
\qquad
(y_1,y_2,y_3)=\left(\frac1{10},1,10\right).
\]

The canonical BFG multiplier is

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

The discrete matrix \(\Chi\) is positive semidefinite as required by the canonical
reclosure theorem.

But the half-step entrywise square root has determinant

\[
\det \Chi^{\circ1/2}
=
1-2a-b+2a\sqrt b
<0.
\]

Therefore

\[
\boxed{
\Chi^{\circ1/2}\not\succeq0.
}
\]

So the corresponding frozen BFG Schur channel is not infinitely divisible by this
entrywise-power interpolation.

---

## 5. Stratification of the first noncommuting continuum

The frozen noncommuting formation sector therefore splits into two classes.

### CP-embeddable frozen strata

\[
-\frac12J(-\log\Chi)J\succeq0.
\]

Then

\[
T_\tau(M)=\Chi^{\circ\tau/\log2}\circ M
\]

is a positive/CP Schur semigroup for all \(\tau\ge0\).

### Hermiticity-only frozen strata

The centered Gram criterion fails.

Then the same formula is still an exact linear semigroup on the Hermitian formation
vector space, but it cannot be used as a positive density-state semigroup at all
intermediate times.

---

## 6. Consequence for the BFG continuum program

Noncommutativity itself is not the decisive obstruction.

The sharper distinction is

\[
\boxed{
\text{noncommuting + infinitely divisible }\Chi
\quad\text{versus}\quad
\text{noncommuting + non-infinitely-divisible }\Chi.
}
\]

The first class already has a mathematically admissible positive continuous frozen
reclosure.

The second class requires a different state-level interpolation, a larger conjugacy,
or an event-based description if positivity of densities must hold continuously.

This gives an exact algebraic test for where the next noncommutative continuum
construction can proceed without adding new physics.
