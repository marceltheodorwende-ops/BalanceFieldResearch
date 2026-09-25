# Neutral-Contrast Closure Gain and Exact Stratum Selection

## 0. Epistemic status

The canonical September BFG reclosure preprint already defines

\[
C_N(Y)=(I+Y)^{-1},
\qquad
B_N(Y)=Y(I+Y)^{-1},
\]

calls \(C_N\) the retained response and \(B_N\) the complementary response, and defines

\[
\boxed{
Z(Y)=C_N(Y)-B_N(Y)
=
(I-Y)(I+Y)^{-1}
}
\]

as the **exact neutral contrast**.

Pure BFG separately states the Selection axiom

\[
S_A(x)=\mathrm{retain}
\iff
\Delta C_A(x)>0.
\]

The historical corpus does not explicitly identify \(\Delta C_A\) with \(Z\).

This document introduces one explicit **NEW BFG-INTERNAL IDENTIFICATION PRINCIPLE**:

> A mode is closure-positive exactly when the exact retained neutral response exceeds
> its complementary neutral response.

Equivalently,

\[
\boxed{
\operatorname{sign}\Delta\mathcal C_A
=
\operatorname{sign}Z.
}
\]

The simplest normalized representative is

\[
\boxed{
\Delta\mathcal C_A:=Z.
}
\]

No external physical law or fitted coefficient is introduced.

---

## 1. Sign-uniqueness theorem

Suppose closure gain satisfies the following BFG-minimality requirements:

1. it depends on the exact neutral pair only through its contrast;
2. swapping retained and complementary responses reverses the gain sign;
3. exact balance \(C_N=B_N\) has zero gain;
4. increasing retained-over-complementary contrast cannot decrease closure gain;
5. no new state-dependent coefficient is introduced.

Then every admissible scalar spectral representation has the form

\[
\Delta c=g(z)
\]

with \(g\) odd and strictly increasing on the realized contrast spectrum.

Therefore

\[
\operatorname{sign}\Delta c
=
\operatorname{sign}z.
\]

Hence the BFG Selection projector is independent of the particular monotone
reparameterization \(g\):

\[
\boxed{
Q_{\rm retain}
=
\mathbf1_{(0,\infty)}(Z).
}
\]

Thus selection is unique even if the numerical scale of "gain" is changed monotonically.

---

## 2. Load-threshold representation

For every spectral value \(y\ge0\),

\[
z=\frac{1-y}{1+y}.
\]

Therefore

\[
z>0
\iff
y<1,
\]

\[
z=0
\iff
y=1,
\]

\[
z<0
\iff
y>1.
\]

The exact selector is consequently

\[
\boxed{
Q_{\rm retain}
=
\mathbf1_{[0,1)}(Y)
}
\]

and

\[
\boxed{
Q_{\rm export}
=
\mathbf1_{[1,\infty)}(Y).
}
\]

The threshold \(1\) is not a fitted tolerance. It is the exact equality point

\[
C_N=B_N=\frac12 I
\]

in the dimensionless master load.

---

## 3. Why this is more canonical than weighted closure scores

Earlier biological BFG models used domain-level closure scores containing weighted
balance, information, coupling, recursive-stability, energetic-cost and drift terms.

Those are useful carrier models but cannot be the universal TOE selector without
retuning.

The neutral contrast instead:

- already exists in the canonical universal reclosure;
- is dimensionless;
- is basis independent;
- contains no carrier-specific weight;
- is bounded in \((-1,1]\);
- encodes the exact retained/complementary split losslessly;
- has an intrinsic zero at neutral balance.

For the universal stratum law this makes its **sign** the minimal no-retuning closure
gain candidate.

---

## 4. Target-stage selection

Let the cross-fed BFG analysis operator have reduced SVD

\[
A=U\Sigma V^\dagger.
\]

Under the already-declared intrinsic-Gram completion rule,

\[
Y_+^{\rm pre}=\Sigma^2.
\]

Define the target neutral contrast

\[
Z_+^{\rm pre}
=
(I-Y_+^{\rm pre})
(I+Y_+^{\rm pre})^{-1}.
\]

Then

\[
\boxed{
Q_+
=
\mathbf1_{(0,\infty)}
(Z_+^{\rm pre})
=
\mathbf1_{[0,1)}
(Y_+^{\rm pre}).
}
\]

This places Selection after candidate reclosure geometry has been generated but before
identity and formation are committed to the next persistent stratum.

---

## 5. R4 continuation

Let \(P_-\) be the old persistent projector in source coordinates.

The active source frame is \(V\), so the exact source-to-selected-target overlap is

\[
X=Q_+V^\dagger P_-.
\]

Define

\[
T=\operatorname{polar}(X).
\]

Then R4 gives

\[
S_-=T^\dagger T,
\qquad
S_+=TT^\dagger,
\]

and for the normalized identity witness

\[
m_{\rm keep}
=
\operatorname{tr}(S_-\rho_W).
\]

If \(m_{\rm keep}=0\), the identity corridor ends at

\[
\bot.
\]

Otherwise

\[
\boxed{
\rho_{W,+}
=
\frac{T\rho_WT^\dagger}{m_{\rm keep}}.
}
\]

Thus a load mode crossing from \(y<1\) to \(y>1\) produces an exact structural export
sector without any numerical spectral window. Witness loss occurs precisely when the
selected target support loses overlap rank with the inherited witness support; whether
the full endogenous BFG generator realizes such crossings generically is a separate
dynamical question and is not assumed here.

---

## 6. Emergent selected sector

The selected target sector not inherited from the old persistent space is

\[
E_+
=
Q_+-S_+.
\]

It receives no inherited witness.

If a new formation seed is required, apply the existing R4 no-choice rule to

\[
K_E=E_+K_+E_+|_{\operatorname{Ran}E_+}.
\]

Only a simple negative lowest mode is seeded:

\[
\rho_E=(-\lambda_0^E)\Pi_E.
\]

Then

\[
\rho_{F,+}
=
T\rho_FT^\dagger+\rho_E.
\]

This keeps "new formation" distinct from "old identity".

---

## 7. Persistent recursion

The current BFG-internal completion retains

\[
P_+=S_++\Pi_E
\]

and uses

\[
\boxed{
R_{C,+}
=
P_+
+
(I-P_+)C_N(Y_+^{\rm pre})(I-P_+).
}
\]

The inherited/seeded persistent space has eigenvalue \(1\); every other active target
mode is strictly contracted.

An exported neutral-contrast mode can therefore remain in the active carrier as a
transient stable direction without being classified as persistent.

---

## 8. Deterministic current-kernel stress audit

The current official Selection-first candidate is exercised by

`stress_neutral_contrast.py`

with seed `20260925`, 1,000 synthetic finite complex states, and at most eight
successful-step attempts per state.

The current machine-readable result is
`NEUTRAL_CONTRAST_STRESS_RESULTS.json`.

The reproduced run reports:

- `export_events = 812`;
- `persistent_rank_decreases = 1150`;
- `persistent_rank_increases = 781`;
- `witness_loss_events = 166`;
- `dual_load_numerical_ambiguity = 984`;
- `no_closure_positive_source_sector = 16`;
- maximum observed recursive power norm approximately
  \(1.0000000000000182\).

These counts are **internal numerical stress data**, not empirical evidence and not
probabilities for a physical ensemble.

In particular,

`dual_load_numerical_ambiguity`

is not exact BFG terminality. It records finite-precision loss of a strict-positive-load
certificate near the asymptotic boundary.

The stress audit demonstrates that the implemented Selection/Export rule is nontrivial
on the declared synthetic ensemble; it does not establish physical prevalence of rank
gain, rank loss, export, or any terminal class.

---

## 9. Boundary discipline

Exact mathematics assigns \(y=1\) to export because the Selection axiom requires
strictly positive gain.

Floating arithmetic cannot certify exact equality from a near-one eigenvalue.

Therefore the implementation reports

`neutral_contrast_boundary_ambiguity`

for numerically unresolved values rather than converting a floating tolerance into a
fundamental physical parameter.

---

## 10. Current status of the universal law

The previous generic unknown

\[
\Delta\mathcal C_A
=
\mathcal G_{\rm BFG}(\Xi)
\]

is replaced, under the explicit Neutral-Contrast Selection Principle, by the existing
canonical BFG operator

\[
\boxed{
\Delta\mathcal C_A
\equiv
Z(Y)
=
(I-Y)(I+Y)^{-1}.
}
\]

This is the first threshold-free, no-retuning, carrier-independent closure-gain
candidate constructed entirely from canonical BFG neutral mathematics.

It remains a **new BFG identification principle** until independently justified,
falsified, or shown to follow from a deeper BFG axiom.
