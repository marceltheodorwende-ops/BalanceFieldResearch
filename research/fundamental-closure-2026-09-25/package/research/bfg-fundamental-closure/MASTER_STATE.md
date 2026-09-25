# Master state contract

## Current rank-aware finite state

The vector-only quotient state is superseded for the universal rank-changing program.

The current candidate is

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

Here:

- \(\rho_F\succeq0\), \(\operatorname{tr}\rho_F>0\): phase-free formation/load density;
- \(\rho_W\succeq0\), \(\operatorname{tr}\rho_W=1\): inherited identity witness;
- \(Y\succeq0\): realized positive master load;
- \(R_C\): realized recursive closure operator.

An ordinary projector \(P_{\rm per}\) onto the persistent range may be cached
numerically, but is derived rather than fundamental.

## Why two positive operators are required

R4 demands zero inherited witness in a genuinely emergent sector while independently
allowing a nonzero endogenous formation density there. One untagged positive operator
cannot satisfy both roles.

See `TWO_DENSITY_UNIVERSAL_STATE.md`.

## Formation and neutral geometry

\[
K=\mathfrak c+\aleph-\mathfrak D,
\]

\[
C=(I+Y)^{-1},
\qquad
B=Y(I+Y)^{-1},
\qquad
G=I+Y.
\]

## Density-form reciprocal loads

With the \(G\)-orthogonal persistent projector \(P\),

\[
\ell_C=\operatorname{tr}(GPC\rho_FCP^\dagger),
\]

\[
\ell_B=\operatorname{tr}(GPB\rho_FBP^\dagger).
\]

For positive dual loads,

\[
\alpha=\frac{\ell_B}{\ell_C+\ell_B},
\qquad
\beta=\frac{\ell_C}{\ell_C+\ell_B}.
\]

## Cross-fed analysis

\[
A=
\begin{bmatrix}
\sqrt{\alpha}PC\\
\sqrt{\beta}PB
\end{bmatrix}.
\]

Reduced SVD:

\[
A=U\Sigma V^\dagger.
\]

The active target carrier is represented by the columns of \(U\), with

\[
Y_+=\Sigma^2
\]

under the selected intrinsic-Gram completion rule.

## Capacity transport

\[
\mathfrak A_+
=
U^\dagger(\mathfrak A\oplus\mathfrak A)U,
\qquad
\mathfrak A\in\{\mathfrak D,\mathfrak c,\aleph\}.
\]

## Witness transport

Let \(P_-\) be the ordinary source persistent projector and

\[
T=\operatorname{polar}(V^\dagger P_-).
\]

Then

\[
S_-=T^\dagger T,
\qquad
S_+=TT^\dagger,
\qquad
E=I-S_+.
\]

\[
m_{\rm keep}=\operatorname{tr}(S_-\rho_W).
\]

If \(m_{\rm keep}=0\), return \(\bot\). Otherwise

\[
\rho_{W,+}
=
\frac{T\rho_WT^\dagger}{m_{\rm keep}}.
\]

## Formation update

\[
\rho_F^{\rm inh}=T\rho_FT^\dagger.
\]

When \(E\ne0\), the R4 no-choice rule supplies a new formation seed only for a simple
negative ground mode of

\[
K_E=EK_+E|_{\operatorname{Ran}E}.
\]

Then

\[
\rho_E=(-\lambda_0^E)\Pi_E,
\]

and

\[
\rho_{F,+}=\rho_F^{\rm inh}+\rho_E.
\]

## Persistent successor and recursion

The current rank-aware completion candidate sets

\[
P_+=S_++\Pi_E
\]

and

\[
R_{C,+}
=
P_+
+
(I-P_+)C_N(Y_+)(I-P_+).
\]

This is the current living state contract. Its completion rules remain explicitly
conditional until independently derived or falsified.


## Exact Selection / Export object

Pure BFG additionally requires closure-positive retention:

\[
S_A(x)=\mathrm{retain}\iff\Delta C_A(x)>0.
\]

For a finite self-adjoint closure-gain operator \(\Delta\mathcal C_A\), the exact
selector is

\[
Q_{\rm retain}
=
\mathbf1_{(0,\infty)}(\Delta\mathcal C_A).
\]

This produces exact target strata with no runtime tolerance.

However, the current universal state does not yet contain a uniquely derived law

\[
\Delta\mathcal C_A=\mathcal G_{\rm BFG}(\Xi).
\]

Accordingly, `DeltaC_A` is a required derived constitutive object, not silently added as
a free fitted parameter.


## Finite committed state versus continuum extension

The committed finite master state remains

\[
\Xi=
(\mathcal H,\mathfrak D,\mathfrak c,\aleph,\rho_F,\rho_W,Y,R_C).
\]

The continuum research layer may extend a no-event chart by

\[
(\Omega,M_b),
\]

where \(\Omega\) is normalized recursive phase and \(M_b\) is a continuation-branch
label only when the phase readout is non-injective.

These are **continuum bookkeeping/state variables**, not additional coordinates of the
committed finite update.

On injective charts, \(M_b\) is redundant. Rank-changing events remain exact finite
event maps rather than continuous projector-rank motion.
