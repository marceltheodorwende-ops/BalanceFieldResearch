# Canonical Two-Channel CP Suspension and Frozen Full-State Flow

## 1. Status

This document constructs a continuous **positive/CP path** through every frozen
two-channel BFG reclosure step.

It uses only:

- the canonical BFG neutral load eigenvalues \(y_i\);
- the two positive reciprocal weights \(\alpha,\beta\);
- the already-derived BFG correlation multiplier \(\Chi\);
- standard Gram-matrix / Schur-product mathematics.

The path construction is new to this package. It is not claimed to have appeared
explicitly in the earlier BFG corpus.

The main result is stronger than the previous infinite-divisibility test:

\[
\boxed{
\text{failure of a CP semigroup does not force a jump.}
}
\]

Every frozen BFG channel still has a canonical continuous CP interpolation generated
by its own two-channel geometry.

---

## 2. BFG channel-angle representation

For

\[
\alpha>0,\qquad \beta>0,\qquad \alpha+\beta=1,
\]

define

\[
\boxed{
\tan\theta_i
=
\sqrt{\frac{\beta}{\alpha}}\,y_i,
\qquad
0\le\theta_i<\frac{\pi}{2}.
}
\]

Then

\[
\cos\theta_i
=
\frac{\sqrt\alpha}
{\sqrt{\alpha+\beta y_i^2}},
\]

\[
\sin\theta_i
=
\frac{\sqrt\beta\,y_i}
{\sqrt{\alpha+\beta y_i^2}}.
\]

Define the normalized two-channel vector

\[
u_i=
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix}.
\]

Its Gram matrix is

\[
u_i^Tu_j
=
\cos(\theta_i-\theta_j).
\]

But

\[
\cos(\theta_i-\theta_j)
=
\frac{
\alpha+\beta y_i y_j
}{
\sqrt{
(\alpha+\beta y_i^2)
(\alpha+\beta y_j^2)
}
}.
\]

Therefore the canonical BFG Schur multiplier has the exact representation

\[
\boxed{
\chi_{ij}
=
\cos(\theta_i-\theta_j).
}
\]

This explains directly why \(\Chi\) is a rank-at-most-two correlation matrix.

---

## 3. Minimal two-channel dilation

In the neutral-load eigenbasis, define an isometry

\[
V|i\rangle
=
|i\rangle\otimes|u_i\rangle.
\]

Then for an operator \(M\),

\[
\operatorname{Tr}_{\rm ch}
\left(
VMV^\dagger
\right)
=
\Chi\circ M.
\]

Thus the frozen BFG Schur reclosure is exactly the reduced action of its own
two-dimensional neutral-channel Gram geometry.

This is a standard Gram/Stinespring-type mathematical realization applied to the
BFG-derived channel vectors. It does not add a new physical environment ontology.

---

## 4. Canonical within-step interpolation

The retained/complementary channel axes give a preferred first-quadrant angle chart.

For one step fraction

\[
0\le s\le1,
\]

move each channel vector along its shortest first-quadrant angular path:

\[
\boxed{
u_i(s)
=
\begin{pmatrix}
\cos(s\theta_i)\\
\sin(s\theta_i)
\end{pmatrix}.
}
\]

At \(s=0\),

\[
u_i(0)=
\begin{pmatrix}
1\\0
\end{pmatrix}
\]

for every mode, so the Gram matrix is the all-ones Schur identity multiplier.

At \(s=1\),

\[
u_i(1)=u_i.
\]

The intermediate correlation matrix is

\[
\boxed{
\chi_{ij}(s)
=
\cos\left(
s(\theta_i-\theta_j)
\right).
}
\]

Because this is a Gram matrix of unit vectors,

\[
\boxed{
\Chi(s)\succeq0,
\qquad
\chi_{ii}(s)=1
}
\]

for every \(s\in[0,1]\).

Therefore

\[
\boxed{
\mathcal E_s(M)
=
\Chi(s)\circ M
}
\]

is a unital trace-preserving completely positive Schur map throughout the step.

No infinite-divisibility assumption is needed.

---

## 5. Relation to the discrete BFG reclosure

At the endpoints,

\[
\Chi(0)=\mathbf1\mathbf1^T,
\]

so

\[
\mathcal E_0(M)=M.
\]

At

\[
s=1,
\]

\[
\Chi(1)=\Chi,
\]

hence

\[
\boxed{
\mathcal E_1(M)
=
\Chi\circ M
=
M_+.
}
\]

Thus the path reproduces the exact frozen BFG one-step reclosure.

---

## 6. Repeated-step CP suspension

Let recursive time be scaled so that one discrete step is

\[
\Delta\tau=\log2.
\]

Write

\[
\frac{\tau}{\log2}
=
n+s,
\qquad
n\in\mathbb N,
\quad
0\le s<1.
\]

Define

\[
\boxed{
\mathcal M_\tau
=
\Chi^{\circ n}
\circ
\Chi(s).
}
\]

Then

\[
\mathcal M_{n\log2}
=
\Chi^{\circ n}.
\]

Therefore

\[
\boxed{
\mathcal E_\tau(M)
=
\mathcal M_\tau\circ M
}
\]

passes exactly through every repeated frozen BFG iterate.

It is continuous at the integer step boundaries because

\[
\Chi^{\circ n}\circ\Chi(1)
=
\Chi^{\circ(n+1)}\circ\Chi(0)
=
\Chi^{\circ(n+1)}.
\]

Each \(\mathcal M_\tau\) is a correlation matrix: powers and products here are
Hadamard products of correlation matrices, hence remain positive semidefinite with
unit diagonal.

Thus

\[
\boxed{
\mathcal E_\tau
\text{ is CP and trace preserving for every }\tau\ge0.
}
\]

---

## 7. Why this is not generally a semigroup

Inside one step,

\[
\chi_{ij}(s)
=
\cos(s\Delta\theta_{ij}).
\]

In general,

\[
\cos((s+t)\Delta\theta)
\ne
\cos(s\Delta\theta)
\cos(t\Delta\theta).
\]

Therefore

\[
\boxed{
\mathcal E_{s+t}
\ne
\mathcal E_s\mathcal E_t
}
\]

in general.

The path is a continuous CP **suspension** of the discrete BFG map, not necessarily a
time-homogeneous Markov semigroup.

This resolves the earlier apparent dichotomy:

\[
\boxed{
\text{not CP-divisible}
\not\Rightarrow
\text{discontinuous jump}.
}
\]

Instead the intermediate path can be positive but history/step-phase dependent.

---

## 8. Time-local within-step generator

For

\[
K_{ij}(s)
=
\cos(s\Delta\theta_{ij})
K_{ij}(0),
\]

differentiate:

\[
\frac{dK_{ij}}{ds}
=
-
\Delta\theta_{ij}
\sin(s\Delta\theta_{ij})
K_{ij}(0).
\]

Since all BFG angles lie in the first quadrant,

\[
|\Delta\theta_{ij}|<\frac{\pi}{2},
\]

so the denominator never vanishes for \(0\le s\le1\). Hence

\[
\boxed{
\frac{dK_{ij}}{ds}
=
-
\Delta\theta_{ij}
\tan(s\Delta\theta_{ij})
K_{ij}(s).
}
\]

This is an exact time-local generator for one frozen step.

It resets its step phase at each discrete BFG reclosure boundary, so it is not an
autonomous global semigroup generator in the non-infinitely-divisible case.

---

## 9. Frozen full-state path

The current rank-aware BFG state is

\[
\Xi=
(
\mathcal H,
\mathfrak D,
\mathfrak c,
\aleph,
\rho_F,
\rho_W,
Y,
R_C
).
\]

Consider a **frozen same-support stratum**:

- \(Y\) is fixed;
- the persistent support is fixed;
- reciprocal \(\alpha,\beta\) are fixed;
- no Selection/Export event occurs;
- no new formation seed is required;
- \(R_C\) is fixed by the frozen persistence geometry.

R4 same-support self-continuation has retained witness mass \(1\); in a fixed carrier
gauge its polar support transport is the identity. Hence the inherited witness and
formation/load density do not need a new amplitude assignment in this frozen
continuation. The existing cross-stratum theorem preserves witness by polar transport
and does not invent amplitude in new sectors. fileciteturn104file2 The living
two-density state likewise transports inherited formation density by the same polar
support map. fileciteturn105file1

Therefore define

\[
\rho_F(\tau)=\rho_F(0),
\]

\[
\rho_W(\tau)=\rho_W(0),
\]

\[
Y(\tau)=Y(0),
\]

\[
R_C(\tau)=R_C(0),
\]

while applying the CP suspension to all three capacity operators:

\[
\boxed{
\mathfrak D(\tau)
=
\mathcal E_\tau(\mathfrak D_0),
}
\]

\[
\boxed{
\mathfrak c(\tau)
=
\mathcal E_\tau(\mathfrak c_0),
}
\]

\[
\boxed{
\aleph(\tau)
=
\mathcal E_\tau(\aleph_0).
}
\]

By linearity,

\[
K(\tau)
=
\mathfrak c(\tau)
+
\aleph(\tau)
-
\mathfrak D(\tau)
=
\mathcal E_\tau(K_0).
\]

Thus the formation operator and its three generating capacities evolve consistently.

If any capacity is positive semidefinite initially, CP guarantees it remains positive
semidefinite throughout the frozen path.

The witness remains positive and normalized, the formation density remains positive,
and the frozen \(Y,R_C\) retain their admissibility properties.

This gives the first complete positive continuous **frozen BFG state path**.

---

## 10. Markovian versus non-Markovian frozen strata

There are now two nested classes.

### Class M — CP-semigroup embeddable

If

\[
D_{ij}=-\log\chi_{ij}
\]

is conditionally negative semidefinite, then

\[
\Chi^{\circ t}
\]

is positive for all \(t\ge0\).

The frozen path can be chosen as the time-homogeneous CP semigroup

\[
\mathcal T_\tau(M)
=
\Chi^{\circ\tau/\log2}\circ M.
\]

### Class S — CP-suspension only

If the Schoenberg condition fails, the time-homogeneous entrywise-power semigroup is
not positive at all intermediate times.

Nevertheless the two-channel angle path above supplies a continuous CP suspension
through every discrete BFG iterate.

Therefore these strata need not be treated as jumps.

They are continuous but non-semigroup/non-Markovian at the reduced frozen-state level.

---

## 11. What still causes genuine BFG events

The angle suspension does **not** remove the exact event architecture of the full
master law.

A genuine event remains when:

- Neutral-Contrast Selection changes support;
- persistent rank changes;
- inherited witness mass is lost;
- an emergent formation seed is created;
- the no-choice gate terminates;
- the carrier dimension changes.

Those are changes of stratum, not merely missing interpolation inside one frozen
reclosure.

Thus the current continuum architecture becomes

\[
\boxed{
\text{positive continuous frozen-stratum paths}
+
\text{exact BFG cross-stratum events}.
}
\]

Within a frozen stratum, even non-CP-divisible one-step channels need not jump.

---

## 12. Remaining full-state problem

The major unresolved continuum problem is now narrower.

The continuous frozen-state path keeps

\[
Y,\rho_F,\rho_W,R_C
\]

fixed.

The true master law evolves \(Y\), reciprocal weights, support, densities and recursion
between steps.

A global state-level conjugacy must therefore derive their simultaneous continuous
evolution rather than freezing them by assumption.

The present theorem proves that the noncommuting capacity/formation sector itself no
longer blocks continuous positive interpolation.
