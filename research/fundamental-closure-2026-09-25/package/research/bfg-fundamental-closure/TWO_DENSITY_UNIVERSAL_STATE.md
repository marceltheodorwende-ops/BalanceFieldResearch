# Two-Density Universal State and Rank-Aware Reclosure

## Status

This document integrates two already-present BFG finite structures:

1. the finite reduced model's positive formation density
   \[
   \rho_F=dd^\dagger
   \]
   used in reciprocal load traces;
2. R4's normalized inherited witness, which is transported without fabricated
   amplitude in a genuinely emergent sector.

The conclusion is a **state-structure theorem**: one untagged positive operator cannot
simultaneously represent both roles across a seeded rank increase.

The rank-aware **reclosure portion** remains conditional on two declared BFG-internal
completion rules:

- intrinsic-Gram rebuild for \(Y_+\);
- neutral transverse self-reclosure rebuild for \(R_{C,+}\).

The official living master update additionally applies the declared
Neutral-Contrast Selection principle **before** next-state reclosure.

All three are BFG-only completion rules; none is claimed to have been uniquely forced
by the older source corpus.

---

## 1. Two-density separation theorem

R4 requires, for an inherited normalized witness,

\[
E\rho_W^{\rm inh}=0
\]

on every genuinely emergent sector \(E\).

The same R4 transition may independently create a nonzero endogenous formation seed

\[
\rho_E=(-\lambda_0^E)\Pi_E,
\qquad
E\rho_E=\rho_E\ne0.
\]

Suppose one untagged operator \(\rho_+\) were required to mean both "inherited
identity witness" and "total formation density".

If \(\rho_E\) is included in \(\rho_+\), then

\[
E\rho_+\ne0,
\]

contradicting the no-fabrication condition for the inherited witness.

If \(\rho_E\) is excluded, then the state fails to carry the canonical emergent
formation seed.

Therefore the universal state must carry either two positive operators or an
equivalent tagged direct decomposition.

\[
\boxed{
\rho_F\ \text{(formation/load density)}
\quad\text{and}\quad
\rho_W\ \text{(normalized identity witness)}
}
\]

are the minimal explicit choice.

---

## 2. Updated finite state

The current rank-aware candidate state is

\[
\boxed{
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
}
\]

Conditions:

\[
\rho_F\succeq0,
\qquad
\operatorname{tr}\rho_F>0,
\]

\[
\rho_W\succeq0,
\qquad
\operatorname{tr}\rho_W=1,
\]

\[
Y\succeq0,
\qquad
K=\mathfrak c+\aleph-\mathfrak D.
\]

A vector \(d\) is no longer fundamental. When \(\rho_F\) is rank one it may be written

\[
\rho_F=dd^\dagger,
\]

but \(d\) is only a phase-dependent chart for the phase-free operator.

---

## 3. Reciprocal loads without a vector

With

\[
G=I+Y,
\quad
C=(I+Y)^{-1},
\quad
B=Y(I+Y)^{-1},
\]

and the \(G\)-orthogonal persistent projector \(P\),

\[
\boxed{
\ell_C
=
\operatorname{tr}(GPC\rho_FCP^\dagger)
}
\]

and

\[
\boxed{
\ell_B
=
\operatorname{tr}(GPB\rho_FBP^\dagger).
}
\]

For \(\rho_F=dd^\dagger\), these reduce exactly to the previous squared \(G\)-norm
loads.

Reciprocal balance remains

\[
\alpha=\frac{\ell_B}{\ell_C+\ell_B},
\qquad
\beta=\frac{\ell_C}{\ell_C+\ell_B}.
\]

Then

\[
A=
\begin{bmatrix}
\sqrt{\alpha}PC\\
\sqrt{\beta}PB
\end{bmatrix}.
\]

---

## 4. Active carrier and intrinsic Gram

Take the reduced SVD

\[
A=U\Sigma V^\dagger
\]

with positive singular values.

The next active carrier is \(\operatorname{Ran}U\), represented in its \(r\)-dimensional
active coordinates.

The selected BFG-internal Gram completion is

\[
\boxed{
Y_+=\Sigma^2.
}
\]

Capacities are transported by the polar active frame:

\[
\mathfrak A_+
=
U^\dagger
(\mathfrak A\oplus\mathfrak A)
U,
\qquad
\mathfrak A\in\{\mathfrak D,\mathfrak c,\aleph\}.
\]

Thus

\[
K_+=\mathfrak c_++\aleph_+-\mathfrak D_+.
\]

---

## 5. R4 inherited witness in active coordinates

Let \(P_-\) be the ordinary projector onto the old persistent space.

Define the rectangular overlap map

\[
M=V^\dagger P_-:
\mathcal H_-\to\mathcal H_+^{\rm act}.
\]

Let

\[
T=\operatorname{polar}(M).
\]

Then

\[
S_-=T^\dagger T,
\qquad
S_+=TT^\dagger,
\qquad
E=I-S_+.
\]

The retained identity-witness mass is

\[
\boxed{
m_{\rm keep}
=
\operatorname{tr}(S_-\rho_W).
}
\]

If \(m_{\rm keep}=0\),

\[
\boxed{\bot}.
\]

Otherwise

\[
\boxed{
\rho_{W,+}
=
\frac{T\rho_WT^\dagger}{m_{\rm keep}}.
}
\]

Therefore

\[
E\rho_{W,+}=0.
\]

No emergent formation is ever relabelled as inherited identity.

---

## 6. Formation density

Inherited formation is transported without normalization:

\[
\rho_F^{\rm inh}
=
T\rho_FT^\dagger.
\]

If \(E=0\), there is no emergent formation term.

If \(E\ne0\), compress the new formation operator:

\[
K_E=EK_+E|_{\operatorname{Ran}E}.
\]

A canonical new seed exists only when its lowest eigenvalue is negative and simple.

Then

\[
\boxed{
\rho_E=(-\lambda_0^E)\Pi_E.
}
\]

The total next formation density is

\[
\boxed{
\rho_{F,+}
=
\rho_F^{\rm inh}+\rho_E.
}
\]

This is positive and phase independent.

---

## 7. Rank-aware persistence

The surviving inherited persistent projector is

\[
S_+=TT^\dagger.
\]

The unique emergent seed projector is \(\Pi_E\).

The rank-aware completion rule promotes exactly these canonically justified sectors:

\[
\boxed{
P_+=S_++\Pi_E.
}
\]

Since \(\Pi_E\le E=I-S_+\),

\[
S_+\Pi_E=0
\]

and \(P_+\) is an orthogonal projector.

Thus a persistent rank increase can occur only through a canonical emergent formation
seed, never through arbitrary vector initialization.

---

## 8. Recursive rebuild

The BFG-internal self-reclosure rule remains

\[
\boxed{
R_{C,+}
=
P_+
+
(I-P_+)C_N(Y_+)(I-P_+).
}
\]

Because \(Y_+>0\) on the active carrier,

\[
\|C_N(Y_+)\|<1.
\]

Therefore the complementary block is strictly stable and the peripheral space is
exactly \(\operatorname{Ran}P_+\).

A seeded emergent mode can therefore increase persistent rank while the inherited
identity witness remains confined to \(S_+\).

---

## 9. What this resolves

The updated state can represent simultaneously:

- phase-free formation magnitude;
- reciprocal loads;
- inherited witness continuity;
- rank decrease and witness loss;
- active rank increase;
- a canonical emergent formation seed;
- persistent rank increase without fabricated inherited identity;
- bounded successor recursion.

The old vector-only quotient state could not do all of these at once.

---

## 10. Remaining claim boundary

The following are source-supported finite ingredients:

- density-form reciprocal loads in the reduced finite model;
- polar support/witness continuation;
- zero inherited witness on the emergent complement;
- canonical simple-negative emergent formation seed.

The following remain BFG-internal completion rules of this research package:

- \(Y_+=A^\dagger A\) on active support;
- promotion of a unique emergent seed into \(P_+\);
- neutral transverse recursion
  \[
  R_{C,+}=P_++(I-P_+)C_N(Y_+)(I-P_+).
  \]

Therefore this is a **rank-aware finite BFG-only completion candidate**, not yet a
proof that historical BFG axioms force the unique universal law.
