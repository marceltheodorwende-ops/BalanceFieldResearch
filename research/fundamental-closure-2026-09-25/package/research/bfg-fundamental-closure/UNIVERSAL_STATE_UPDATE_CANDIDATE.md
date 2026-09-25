# Finite BFG Universal State Update Candidate

## Selection-order correction

The official living candidate uses **current-state Selection before next-state reclosure**, matching the BFG spine \(K\to C\to A\to S_A\to T_A\). Any later section that discusses target-stage contrast should be read as a diagnostic/comparison, not the committed order.

## 1. Status

This is the current **living finite master-law candidate** of the package.

It is BFG-only in the sense that no GR, QFT, Standard Model, biological, cognitive,
thermodynamic, or other external sector equation appears in the update.

It is **not** claimed that the historical BFG corpus already forces every completion
principle uniquely.

The current law contains three explicitly declared BFG-internal completion principles:

1. intrinsic-Gram successor load;
2. Neutral-Contrast Selection Principle;
3. neutral transverse recursive rebuild.

Everything else in the finite step is source BFG mathematics or a proved finite
consequence of those declared rules.

---

## 2. State

\[
\boxed{
\Xi_n=
(
\mathcal H_n,
\mathfrak D_n,
\mathfrak c_n,
\aleph_n,
\rho_{F,n},
\rho_{W,n},
Y_n,
R_{C,n}
).
}
\]

Conditions:

\[
\rho_{F,n}\succeq0,\quad
\operatorname{tr}\rho_{F,n}>0,
\]

\[
\rho_{W,n}\succeq0,\quad
\operatorname{tr}\rho_{W,n}=1,
\]

\[
Y_n\succeq0.
\]

The persistent projector is derived from \(R_{C,n}\) in exact mathematics and may be
cached numerically.

---

## 3. Formation

\[
K_n
=
\mathfrak c_n+\aleph_n-\mathfrak D_n.
\]

---

## 4. Exact neutral pair

\[
C_n=(I+Y_n)^{-1},
\]

\[
B_n=Y_n(I+Y_n)^{-1},
\]

\[
C_n+B_n=I.
\]

The exact neutral contrast is

\[
\boxed{
Z_n=C_n-B_n=(I-Y_n)(I+Y_n)^{-1}.
}
\]

---

## 5. Persistent geometry and density loads

Let \(P_n^{(G)}\) be the \(G_n=I+Y_n\)-orthogonal projector onto the current repaired
persistent Riesz space.

The density loads are

\[
\Lambda_n^C
=
\operatorname{tr}
\left(
G_nP_n^{(G)}C_n
\rho_{F,n}
C_nP_n^{(G)\dagger}
\right),
\]

\[
\Lambda_n^B
=
\operatorname{tr}
\left(
G_nP_n^{(G)}B_n
\rho_{F,n}
B_nP_n^{(G)\dagger}
\right).
\]

For two positive loads,

\[
\omega_n^C
=
\frac{\Lambda_n^B}
{\Lambda_n^C+\Lambda_n^B},
\]

\[
\omega_n^B
=
\frac{\Lambda_n^C}
{\Lambda_n^C+\Lambda_n^B}.
\]

---

## 6. Selection before reclosure

The source architecture orders the universal closure spine as

\[
K	o C	o A	o S_A	o T_A.
\]

Accordingly, Selection acts on the **current** neutral load before the next packet is
generated:

\[
Z_n=(I-Y_n)(I+Y_n)^{-1},
\]

\[
Q_n^{m sel}=\mathbf1_{(0,\infty)}(Z_n).
\]

R4 polar transport from the current persistent projector \(P_n\) to
\(Q_n^{m sel}\) records any exact inherited witness/formation loss. The surviving
projector is then used to build the next graph-metric packet.

This ordering is what permits genuine demotion without a numerical target window.

## 7. Cross-fed analysis

\[
\mathcal A_n
=
\begin{bmatrix}
\sqrt{\omega_n^C}\,P_n^{(G)}C_n\\
\sqrt{\omega_n^B}\,P_n^{(G)}B_n
\end{bmatrix}.
\]

Take the reduced SVD

\[
\mathcal A_n
=
U_n\Sigma_nV_n^\dagger.
\]

The active successor carrier is represented by \(U_n\).

Capacities transport as

\[
\mathfrak A_{n+1}^{\rm pre}
=
U_n^\dagger
(\mathfrak A_n\oplus\mathfrak A_n)
U_n,
\qquad
\mathfrak A\in
\{\mathfrak D,\mathfrak c,\aleph\}.
\]

Thus

\[
K_{n+1}^{\rm pre}
=
\mathfrak c_{n+1}^{\rm pre}
+
\aleph_{n+1}^{\rm pre}
-
\mathfrak D_{n+1}^{\rm pre}.
\]

---

## 7. Intrinsic-Gram completion

The declared BFG-internal Gram rule is

\[
\boxed{
Y_{n+1}^{\rm pre}
=
\Sigma_n^2.
}
\]

---

## 8. Neutral-Contrast Selection

The target neutral contrast is

\[
Z_{n+1}^{\rm pre}
=
(I-Y_{n+1}^{\rm pre})
(I+Y_{n+1}^{\rm pre})^{-1}.
\]

The new BFG-internal identification principle states that closure-positive means
positive exact neutral contrast.

Hence

\[
\boxed{
Q_{n+1}
=
\mathbf1_{(0,\infty)}
(Z_{n+1}^{\rm pre})
=
\mathbf1_{[0,1)}
(Y_{n+1}^{\rm pre}).
}
\]

and

\[
Q_{n+1}^{\rm exp}
=
I-Q_{n+1}.
\]

No carrier-specific closure weights or fitted threshold occur.

---

## 9. R4 identity transport

Let \(P_n\) denote the ordinary source persistent projector.

The source-to-selected-target overlap is

\[
X_n
=
Q_{n+1}V_n^\dagger P_n.
\]

Define

\[
T_n
=
\operatorname{polar}(X_n).
\]

Then

\[
S_n^-=T_n^\dagger T_n,
\qquad
S_n^+=T_nT_n^\dagger.
\]

Witness retention is

\[
m_n
=
\operatorname{tr}
(S_n^-\rho_{W,n}).
\]

If

\[
m_n=0,
\]

the transition returns

\[
\boxed{\bot}.
\]

Otherwise

\[
\boxed{
\rho_{W,n+1}
=
\frac{
T_n\rho_{W,n}T_n^\dagger
}{
m_n
}.
}
\]

---

## 10. Formation transport and new seed

Inherited formation density is

\[
\rho_{F,n+1}^{\rm inh}
=
T_n\rho_{F,n}T_n^\dagger.
\]

The closure-positive target part with no inherited witness is

\[
E_{n+1}
=
Q_{n+1}-S_n^+.
\]

If \(E_{n+1}\ne0\), compress

\[
K_E
=
E_{n+1}
K_{n+1}^{\rm pre}
E_{n+1}
\big|_{\operatorname{Ran}E_{n+1}}.
\]

Only a simple negative lowest eigenmode receives a canonical seed:

\[
\boxed{
\rho_E=(-\lambda_0^E)\Pi_E.
}
\]

If the requested emergent sector has no negative simple ground mode, the no-choice gate
returns \(\bot\).

Then

\[
\boxed{
\rho_{F,n+1}
=
\rho_{F,n+1}^{\rm inh}
+
\rho_E.
}
\]

---

## 11. Persistent successor and bounded recursion

The persistently justified next sector is

\[
\boxed{
P_{n+1}
=
S_n^+
+
\Pi_E.
}
\]

The declared neutral self-reclosure rule is

\[
\boxed{
R_{C,n+1}
=
P_{n+1}
+
(I-P_{n+1})
C_N(Y_{n+1}^{\rm pre})
(I-P_{n+1}).
}
\]

The persistent block has eigenvalue \(1\).

On its orthogonal complement,

\[
\left\|
(I-P_{n+1})
C_N(Y_{n+1}^{\rm pre})
(I-P_{n+1})
\right\|
<1
\]

on the active positive-Gram carrier.

Therefore

\[
\sup_k
\|R_{C,n+1}^k\|
\le1
\]

in the finite declared class.

---

## 12. Master equation

Collecting the stages,

\[
\boxed{
\Xi_{n+1}
=
\mathcal U_{\rm BFG}^{NC}(\Xi_n)
}
\]

where

\[
\mathcal U_{\rm BFG}^{NC}
=
\mathcal R_{\rm rec}
\circ
\mathcal F_{\rm form}
\circ
\mathcal T_{\rm R4}
\circ
\mathcal S_Z
\circ
\mathcal G_{\rm Gram}
\circ
\mathcal P_{\rm polar}
\circ
\mathcal N_{\rm exact}.
\]

This is the current finite BFG-only master-law candidate.

---

## 13. Failure / terminal states

A step is terminal or unresolved if, among other declared gates,

- no persistent source sector exists;
- one reciprocal load is zero;
- active rank is exactly zero;
- the neutral-contrast sign is numerically uncertifiable at the exact boundary \(Y=I\);
- all target modes are closure-nonpositive;
- inherited witness mass is zero;
- a required emergent selected sector lacks a unique negative formation seed.

Floating boundary ambiguity is not identified with exact physical terminality.

---

## 14. What remains before a TOE claim

This finite map is not yet a Theory of Everything.

The next obligations are:

1. prove or falsify the three BFG-internal completion principles rather than merely
   adopt them;
2. establish indefinite exact iteration or a mathematically characterized terminal
   stratification;
3. construct an infinite-dimensional/continuum limit;
4. derive locality, causal geometry, gravity, internal symmetry, matter and
   quantum-statistical behavior from the same frozen law;
5. confront those derived sectors with observation without retuning.

The package therefore calls this object a **finite universal-state-update candidate**,
not an established TOE.
