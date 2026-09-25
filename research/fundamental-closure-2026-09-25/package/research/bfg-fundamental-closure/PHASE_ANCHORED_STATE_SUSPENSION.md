# Phase-Anchored State Suspension and Exact Same-Rank R4 Continuum

## 1. Purpose and epistemic status

The finite BFG master candidate fixes discrete successors

\[
\Xi_{n+1}=\mathcal U_{\rm BFG}(\Xi_n).
\]

The remaining continuum question is not whether one can draw an arbitrary smooth curve
between two matrices. It is whether BFG itself determines a unique admissible
within-step state evolution.

The source BFG state already contains a recursive phase coordinate \(\Omega\), temporal
continuity \(T\), and memory persistence \(M\). Separate BFG work also introduces
phase-sensitive Closure Phase Operators and continuous persistent phase propagation.

Those sources justify treating recursive phase and persistence memory as legitimate BFG
state roles.

They do **not** already prove the specific normalized anchor-phase suspension introduced
below.

Accordingly:

- using a recursive phase coordinate is source-aligned BFG structure;
- using a committed source state as a within-step anchor is a new continuum
  realization of the memory/persistence role;
- the particular load interpolation chosen below is a **NEW BFG CONTINUUM COMPLETION
  RULE**, not a theorem forced by the discrete corpus.

---

## 2. Full-persistent no-event endpoint

Consider the same-carrier stratum

\[
P=I,
\qquad
R_C=I,
\qquad
0<Y<I.
\]

Let

\[
Y=U\,\mathrm{diag}(y_1,\ldots,y_m)U^\dagger
\]

and write the diagonal formation weights in this basis as

\[
r_i=(U^\dagger\rho_FU)_{ii}.
\]

The exact dual loads are

\[
\Lambda_C
=
\sum_i\frac{r_i}{1+y_i},
\]

\[
\Lambda_B
=
\sum_i\frac{r_i y_i^2}{1+y_i}.
\]

Hence

\[
\alpha
=
\frac{\Lambda_B}{\Lambda_C+\Lambda_B},
\qquad
\beta
=
\frac{\Lambda_C}{\Lambda_C+\Lambda_B}.
\]

The exact gauge-aligned successor load is

\[
\boxed{
y_i^+
=
\frac{\alpha+\beta y_i^2}{(1+y_i)^2}.
}
\]

The canonical capacity multiplier is

\[
\boxed{
\chi_{ij}
=
\frac{\alpha+\beta y_i y_j}
{\sqrt{(\alpha+\beta y_i^2)(\alpha+\beta y_j^2)}}.
}
\]

Thus for each capacity operator

\[
\mathfrak A\in
\{\mathfrak D,\mathfrak c,\aleph\},
\]

the gauge-aligned endpoint is

\[
\boxed{
\mathfrak A_+
=
U
\left[
\Chi\circ
(U^\dagger\mathfrak A U)
\right]
U^\dagger.
}
\]

In this full-persistent stratum the R4 support transport is identity in the aligned
carrier gauge, so

\[
\rho_{F,+}=\rho_F,
\]

\[
\rho_{W,+}=\rho_W,
\]

\[
R_{C,+}=I.
\]

The implementation verifies that these closed formulas agree with the generic finite
master update up to the target-unitary gauge introduced by its SVD coordinates.

---

## 3. Continuum underdetermination theorem

Suppose only the following conditions are required of a within-step load path \(Y(s)\):

1. exact endpoints:
   \[
   Y(0)=Y_0,\qquad Y(1)=Y_1;
   \]
2. strict positivity;
3. unitary covariance;
4. preservation of the selected order interval
   \[
   0<Y(s)<I
   \]
   when both endpoints lie there;
5. continuity in \(s\in[0,1]\).

These conditions do **not** determine a unique path.

### Affine positive bridge

\[
\boxed{
Y_{\rm aff}(s)
=
(1-s)Y_0+sY_1.
}
\]

The positive cone and the order interval \(0<Y<I\) are convex, so this bridge remains
admissible.

### Closure-depth / log-Euclidean bridge

Using

\[
H=-\log Y,
\]

define

\[
H(s)
=
(1-s)H_0+sH_1
\]

and

\[
\boxed{
Y_{\log}(s)
=
\exp[-H(s)].
}
\]

In the current full-persistent endpoint, \(Y_0\) and \(Y_1\) commute, so spectrally

\[
y_i(s)
=
y_{i,0}^{\,1-s}
y_{i,1}^{\,s}.
\]

This is also positive, selected, continuous and unitary covariant.

For a generic nontrivial eigenvalue pair

\[
y_{i,0}\ne y_{i,1}
\]

and

\[
0<s<1,
\]

the arithmetic and geometric interpolants differ.

Therefore

\[
\boxed{
\text{discrete endpoints + positivity + covariance do not uniquely fix the continuum.}
}
\]

A state-level continuous law needs one additional continuum principle.

---

## 4. Declared closure-depth interpolation principle

The living package selects, for investigation, the following explicit continuum
completion rule:

> Within a no-event same-carrier step, interpolate the positive master load affinely in
> closure depth \(H=-\log Y\).

Thus

\[
\boxed{
H(s)
=
(1-s)H_n+sH_{n+1},
}
\]

\[
\boxed{
Y(s)=e^{-H(s)}.
}
\]

Why this candidate is structurally economical:

- \(H=-\log Y\) was already derived as an invertible coordinate on generated
  \(Y>0\);
- Neutral-Contrast Selection is simply the positive spectral projector of \(H\);
- the terminal dual-load boundary \(Y\to0\) becomes \(H\to+\infty\);
- no carrier-specific coefficient is introduced.

These observations motivate the rule but do **not** prove uniqueness.

Its status is therefore:

\[
\boxed{\text{NEW BFG CONTINUUM COMPLETION PRINCIPLE}.}
\]

---

## 5. Capacity interpolation from the two-channel geometry

For the source reciprocal weights define

\[
\tan\theta_i
=
\sqrt{\beta/\alpha}\,y_i.
\]

The within-step CP correlation path is

\[
\chi_{ij}(s)
=
\cos[s(\theta_i-\theta_j)].
\]

For each capacity,

\[
\boxed{
\mathfrak A(s)
=
U
\left[
\Chi(s)\circ
(U^\dagger\mathfrak A_0U)
\right]
U^\dagger.
}
\]

At \(s=0\),

\[
\mathfrak A(0)=\mathfrak A_0.
\]

At \(s=1\),

\[
\mathfrak A(1)=\mathfrak A_+.
\]

Every positive capacity remains positive because each \(\Chi(s)\) is a correlation
matrix.

The formation operator remains exactly

\[
K(s)
=
\mathfrak c(s)+\aleph(s)-\mathfrak D(s).
\]

---

## 6. Phase-anchored full-state readout

For the full-persistent no-event stratum define a normalized recursive phase

\[
\omega\in[0,1].
\]

The phase-anchored readout is

\[
\boxed{
\mathcal I_\omega(\Xi_n)
=
\left(
\mathfrak D(\omega),
\mathfrak c(\omega),
\aleph(\omega),
\rho_{F,n},
\rho_{W,n},
Y(\omega),
I
\right).
}
\]

It has exact endpoints

\[
\mathcal I_0(\Xi_n)=\Xi_n,
\]

\[
\mathcal I_1(\Xi_n)=\mathcal U_{\rm BFG}(\Xi_n)
\]

in the gauge-aligned full-persistent representation.

Thus the continuous path is not a replacement for the discrete master law. The
discrete law fixes the endpoint; the phase rule supplies an admissible interpolation
between committed closures.

---

## 7. Why the reduced readout is not Markovian

In a non-CP-divisible frozen sector, the intermediate angle generator depends on the
phase within the current step and on the source-step neutral geometry.

Likewise, the selected closure-depth bridge depends on both

\[
Y_n
\]

and the already determined endpoint

\[
Y_{n+1}.
\]

Therefore the reduced instantaneous readout alone does not generally determine the
rest of the path.

This is not a defect in the discrete BFG map. It shows that the continuum description
has hidden step-phase information if one insists on using only the reduced finite
state.

---

## 8. Extended anchor-phase state

Introduce the continuum bookkeeping state

\[
\boxed{
\widehat\Xi
=
(\Xi_\star,\omega),
}
\]

where

- \(\Xi_\star\) is the last committed discrete closure;
- \(\omega\in[0,1)\) is the normalized recursive phase.

The next committed target is not an independent future input:

\[
\Xi_+
=
\mathcal U_{\rm BFG}(\Xi_\star)
\]

is computed from the anchor.

Choose dimensionless recursive time \(\tau\) so one full reclosure has length

\[
\Delta\tau=\log2.
\]

Then

\[
\frac{d\omega}{d\tau}
=
\frac1{\log2}
\]

between commits.

When

\[
\omega\to1,
\]

commit

\[
\Xi_\star
\leftarrow
\mathcal U_{\rm BFG}(\Xi_\star)
\]

and reset

\[
\omega\leftarrow0.
\]

The physical/readout state is

\[
\Xi_{\rm read}
=
\mathcal I_\omega(\Xi_\star).
\]

The code verifies the semigroup law on this **extended** anchor-phase state and exact
agreement with every discrete iterate at

\[
\tau=n\log2.
\]

The BFG source already contains both recursive phase \(\Omega\) and memory persistence
\(M\). Interpreting the normalized \(\omega\) and committed anchor as concrete
continuum realizations of those roles is source-aligned but remains a new realization,
not an old source theorem.

---

## 9. Exact same-rank R4 support continuum

The full-persistent case has fixed support. R4 also supplies a canonical route when the
persistent support rotates without changing rank.

Let

\[
P_0,\ P_1
\]

be orthogonal projectors of equal finite rank \(r\), with full overlap:

\[
\operatorname{rank}(P_1P_0)=r.
\]

Equivalently, every principal angle satisfies

\[
0\le\vartheta_j<\frac\pi2.
\]

Choose aligned principal vectors \(a_j\in\operatorname{Ran}P_0\) and
\(b_j\in\operatorname{Ran}P_1\) such that

\[
\langle a_i,b_j\rangle
=
\delta_{ij}\cos\vartheta_j.
\]

For \(\vartheta_j>0\), define

\[
n_j
=
\frac{
b_j-\cos\vartheta_j\,a_j
}{
\sin\vartheta_j
}.
\]

Then the principal-angle path is

\[
w_j(s)
=
\cos(s\vartheta_j)a_j
+
\sin(s\vartheta_j)n_j.
\]

Set

\[
\boxed{
P(s)
=
\sum_j
|w_j(s)\rangle\langle w_j(s)|.
}
\]

This is an exact rank-\(r\) orthogonal projector for every \(s\).

Define the partial isometry

\[
T(s)
\]

that maps \(a_j\mapsto w_j(s)\).

Then

\[
T(s)^\dagger T(s)=P_0,
\]

\[
T(s)T(s)^\dagger=P(s).
\]

At the endpoint,

\[
\boxed{
T(1)=\operatorname{polar}(P_1P_0),
}
\]

which is exactly the R4 cross-stratum polar transport.

Therefore a positive density supported in \(P_0\) has the continuous path

\[
\boxed{
\rho(s)
=
T(s)\rho_0T(s)^\dagger.
}
\]

Positivity and trace are preserved.

This supplies a canonical same-rank continuous interpolation for both inherited
identity witness and inherited formation density.

---

## 10. Rank-change obstruction theorem

Let

\[
P(s)
\]

be a norm-continuous finite-dimensional path of exact orthogonal projectors.

Because

\[
\operatorname{rank}P(s)
=
\operatorname{tr}P(s)
\]

and trace is continuous, while rank is integer-valued,

\[
\boxed{
\operatorname{rank}P(s)
\text{ is constant on every connected continuous projector path.}
}
\]

Therefore an exact persistent-rank change cannot be represented by a continuous path
that remains inside the manifold of exact persistence projectors.

A rank-changing BFG transition must therefore be represented as one of:

1. an exact stratum event/jump;
2. a path in a larger state space where the intermediate persistence object is no
   longer an exact projector.

The second option changes the current semantics of persistence and would require new
BFG axioms.

Under the current exact-projector semantics,

\[
\boxed{
\text{rank change remains a genuine BFG event.}
}
\]

---

## 11. Current continuum architecture

The present mathematically justified architecture is now:

### Inside a no-event same-rank stratum

- recursive phase \(\omega\);
- closure-depth interpolation of \(Y\) under the declared continuum completion rule;
- two-channel CP capacity path;
- principal-angle R4 support transport when the support rotates;
- positive transport of \(\rho_F,\rho_W\);
- bounded recursive closure rebuilt from the current persistent sector and neutral
  response.

### At a rank-changing or no-choice surface

- exact BFG event;
- update carrier/support;
- commit new anchor;
- reset recursive phase.

So the continuum is not one smooth ODE on one matrix manifold.

It is a phase-anchored stratified suspension of the discrete BFG master law.

---

## 12. What remains open

The full non-frozen same-rank state still requires one further derivation:

\[
Y(s),\ \alpha(s),\beta(s),\
P(s),\
\rho_F(s),\
\rho_W(s),\
R_C(s)
\]

must be coupled locally so that the within-step law can be evaluated from the
extended BFG state without separately invoking an arbitrary interpolation choice.

The anchor-phase construction proves existence and exact endpoint compatibility.

The continuum-underdetermination theorem proves that uniqueness cannot be claimed
without an explicit additional BFG continuum principle.
