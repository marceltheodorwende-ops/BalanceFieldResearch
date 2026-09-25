# Exact Selection–Export Formalization and Closure-Gain Obstruction

## 1. Source basis

Pure BFG already contains an explicit selection axiom:

\[
\boxed{
S_A(x)=
\begin{cases}
\mathrm{retain},&\Delta C_A(x)>0,\\
\mathrm{export},&\Delta C_A(x)\le0.
\end{cases}
}
\]

The monograph also states the corresponding failure criterion: if retention/export
cannot be operationally separated from arbitrary choice, the selection operator is
underdefined.

This document formalizes that existing BFG rule without importing an external
physical theory.

---

## 2. Operator form

Let

\[
\Delta\mathcal C_A=\Delta\mathcal C_A^\dagger
\]

be a self-adjoint closure-gain operator on a finite candidate target carrier and define

\[
\Delta C_A(x)
=
\langle x,\Delta\mathcal C_A x\rangle
\]

on its spectral modes.

Then the exact basis-free retention projector is

\[
\boxed{
Q_{\rm retain}
=
\mathbf 1_{(0,\infty)}
(\Delta\mathcal C_A).
}
\]

The export projector is

\[
\boxed{
Q_{\rm export}
=
I-Q_{\rm retain}
=
\mathbf 1_{(-\infty,0]}
(\Delta\mathcal C_A).
}
\]

Thus the source rule "retain iff positive; export otherwise" becomes a spectral
projector law.

No eigenvector ordering, arbitrary rank target, or floating threshold is part of the
exact definition.

---

## 3. Exact stratum transition

Let \(Q_-\) be the source persistent/support projector and let

\[
Q_+=Q_{\rm retain}.
\]

R4 then supplies the canonical transition

\[
X=Q_+Q_-,
\]

\[
\boxed{
T=X(X^\dagger X)^{\dagger1/2}.
}
\]

For normalized witness \(\rho_-\),

\[
m_{\rm keep}
=
\operatorname{tr}(T^\dagger T\rho_-),
\]

\[
m_{\rm lost}=1-m_{\rm keep}.
\]

If \(m_{\rm keep}>0\),

\[
\rho_+^{\rm inh}
=
\frac{T\rho_-T^\dagger}{m_{\rm keep}}.
\]

If \(m_{\rm keep}=0\),

\[
\bot.
\]

Therefore, **once the closure-gain operator is known**, BFG selection plus R4 gives an
exact, coordinate-free, threshold-free rank-decrease/rank-increase/same-rank
continuation law.

---

## 4. Unitary covariance theorem

If

\[
\Delta\mathcal C_A\mapsto
U\Delta\mathcal C_AU^\dagger,
\]

functional calculus gives

\[
Q_{\rm retain}
\mapsto
UQ_{\rm retain}U^\dagger.
\]

R4 polar transport is likewise unitarily equivariant. Hence the complete
selection/continuation stage is coordinate independent.

---

## 5. Closure-gain obstruction theorem

### Statement

The current universal BFG corpus does not uniquely determine
\(\Delta\mathcal C_A\) as a function of the finite master state.

### Reason

The source gives the **sign rule** for a quantity named closure gain, but no universal
operator formula for that gain.

The biological BFG model supplies domain-level closure functionals, for example a
weighted sum of balance, information, coupling and recursive-stability gains minus
energetic and drift costs. Those weights are domain/model inputs; they are not a
universal no-retuning operator law.

Therefore the selection axiom determines the projector only **conditional on a supplied
closure-gain operator**.

---

## 6. Explicit non-uniqueness witness

Consider one admissible finite state with

\[
K=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix},
\qquad
Y=I.
\]

Two BFG-internal, Hermitian and unitary-covariant candidate gain assignments are

\[
\Delta\mathcal C_A^{(1)}=-K
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\]

and

\[
\Delta\mathcal C_A^{(2)}=Y=I.
\]

The source-level sign axiom gives

\[
Q_{\rm retain}^{(1)}
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
\]

but

\[
Q_{\rm retain}^{(2)}=I.
\]

Both assignments are built only from BFG state operators and standard functional
calculus. The generic requirements "Hermitian, basis independent, BFG-internal" do not
choose between them.

Hence

\[
\boxed{
\text{the existing selection axiom does not by itself close the universal stratum law.}
}
\]

A universal TOE requires a unique law

\[
\boxed{
\Delta\mathcal C_A
=
\mathcal G_{\rm BFG}(\Xi)
}
\]

or an equivalent internally derived closure-gain functional.

---

## 7. Relation to the current packet architecture

The current cross-fed packet projects both branches into the already persistent
subspace before polar reclosure.

Consequently its exact active-support geometry is structurally biased toward retaining
already-selected persistent content. This is why rank loss cannot be manufactured by
numerical support tolerance in a fundamental theory.

The logical order required by pure BFG is therefore

\[
\boxed{
\text{candidate closure}
\to
\Delta\mathcal C_A
\to
S_A
\to
(Q_-,Q_+)
\to
T_{\rm polar}
\to
\text{retained / exported / emergent structure}.
}
\]

Selection/export must precede the final persistence projection when genuine demotion is
to occur.

---

## 8. Numerical rule

The exact boundary is zero.

A floating implementation must not replace this with a physical constant.

If an eigenvalue of \(\Delta\mathcal C_A\) is numerically too close to zero to certify
its sign, the implementation reports

`closure_gain_sign_ambiguity`

rather than silently retaining or exporting it.

---

## 9. Current status

We have now closed the **form** of the exact stratum selector:

\[
\boxed{
Q_+
=
\mathbf1_{(0,\infty)}
(\Delta\mathcal C_A)
}
\]

conditional on the BFG closure-gain operator.

The remaining pure-BFG derivation problem is correspondingly sharper:

\[
\boxed{
\text{derive }\mathcal G_{\rm BFG}:\Xi\mapsto\Delta\mathcal C_A.
}
\]

That operator is now the central unresolved constitutive object for a truly universal,
threshold-free Selection/Export law.
