# CSR Stress Audit

## Scope

This audit stress-tests the current **conditional BFG-only completion candidate**:

1. intrinsic-Gram successor load
   \[
   Y_+=A^\dagger A|_{H_a},
   \]
2. canonical self-reclosure recursion
   \[
   R_{C,+}=P_++(I-P_+)C_N(Y_+)(I-P_+).
   \]

Both use only BFG-defined objects and standard mathematics. The first is already
present in the repository as an explicitly selected model law; the second is the new
BFG-internal recursion axiom of this package. Neither is claimed to have been uniquely
forced by the older BFG axioms.

## 1. Multi-step finding

The finite CSR map is single-valued on every successful step. The transported
persistent rank is nonincreasing when the exact/cached persistent projector is used.

A numerical implementation must not rediscover persistence solely from a tolerance
test `abs(abs(lambda)-1)<eps`, because the stable CSR eigenvalues can approach 1 from
below as the load becomes small. Such a tolerance can falsely convert stable modes
into persistent modes.

The runtime therefore now stores `P_per` as a **derived numerical certificate/cache**.
It is not an additional fundamental state variable in exact mathematics.

## 2. Exact scalar boundary theorem

For a one-dimensional full-persistence state with scalar load \(y>0\),

\[
C=\frac1{1+y},
\qquad
B=\frac{y}{1+y}.
\]

The two \(G=1+y\) loads are

\[
\Lambda_C=\frac{|d|^2}{1+y},
\qquad
\Lambda_B=\frac{y^2|d|^2}{1+y}.
\]

Reciprocal balance gives

\[
\omega_C=\frac{y^2}{1+y^2},
\qquad
\omega_B=\frac1{1+y^2}.
\]

Both weighted branches have the same scalar amplitude,

\[
\sqrt{\omega_C}C
=
\sqrt{\omega_B}B
=
\frac{y}{(1+y)\sqrt{1+y^2}}.
\]

Hence

\[
\boxed{
y_+
=
\frac{2y^2}{(1+y)^2(1+y^2)}.
}
\]

Moreover

\[
y_+-y
=
-\frac{
y(y^4+2y^3+2y^2+1)
}{
(1+y)^2(1+y^2)
}
<0
\]

for every \(y>0\). Therefore

\[
\boxed{0<y_+<y}
\]

and the exact scalar orbit satisfies

\[
y_n\downarrow0.
\]

For small \(y\),

\[
y_+=2y^2+O(y^3),
\]

so convergence to the neutral boundary is superlinear.

This is not a floating-point bug; it is an exact consequence of the selected
intrinsic-Gram completion rule.

The existing repository's finite closure theorem independently records the same scalar
formula and warns that floating-point loads become unresolved rapidly.

## 3. Interpretation boundary

The scalar load collapse does **not** imply finite-step mathematical termination:
for exact \(y_n>0\), every finite successor remains positive.

It does imply that the current completion candidate has a strong neutralizing
attractor on this stratum. A future BFG TOE must decide, before empirical tuning,
whether this is:

- the intended vacuum/closure attractor;
- a restricted-stratum effect;
- or evidence that the intrinsic-Gram completion law is not the universal law.

No external physical interpretation is assumed here.

## 4. Unitary covariance

For a simultaneous source coordinate change \(U\), the doubled target carrier changes
by \(U\oplus U\). Reduced SVD target frames can differ by an internal unitary gauge
\(Q\).

The stress tests verify

\[
A'_+=Q A_+Q^\dagger,
\quad
Y'_+=QY_+Q^\dagger,
\quad
R'_{C,+}=QR_{C,+}Q^\dagger,
\quad
d'_+=Qd_+
\]

for the tested capacity/load/recursion objects to floating-point precision.

Thus the candidate passes coordinate covariance modulo the unavoidable active-carrier
basis gauge.

## 5. Rank bounds

If the source persistent rank is \(p\), each branch of the analysis operator contains
a rank-\(p\) persistent projection. Therefore

\[
\operatorname{rank}A\le2p.
\]

The active successor carrier obeys

\[
\dim H_+=\operatorname{rank}\mathcal A\le\dim H.  The older bound \(\dim H_+\le2p\) is only a weaker packet-rank estimate.
\]

The CSR persistence transport gives

\[
\operatorname{rank}P_+\le p.
\]

Hence inherited persistence cannot be fabricated or rank-increased by an exact step.

## 6. R4 cross-stratum compatibility

Let \(P_-\) be the ordinary projector onto the old persistent subspace and let
\(S=VV^\dagger\) be the source active support of the cross-fed analysis map.

The R4-style polar continuation on the common source ambient space is

\[
T=\operatorname{polar}(SP_-).
\]

Its final projector is

\[
TT^\dagger
=
P_{\operatorname{Ran}(SP_-)}.
\]

The CSR transported persistence, pulled back from active coordinates, is exactly the
same range projector:

\[
V P_+V^\dagger
=
P_{\operatorname{Ran}(SP_-)}.
\]

Therefore CSR persistence selection is compatible with R4's no-fabrication polar
continuation at the **subspace level**.

The full R4 witness-density transport remains a separate layer and should not be
identified with this projector equality.

## 7. Current verdict

The stress audit supports:

- single-valued finite CSR steps;
- unitary covariance up to target gauge;
- strict recursion power boundedness;
- nonincreasing inherited persistent rank;
- R4-compatible persistent-subspace continuation.

It also exposes the principal structural warning:

\[
\boxed{\text{intrinsic-Gram CSR has an exact neutral-load attractor in the scalar/full-persistence sector.}}
\]

This warning must remain in the claim register and cannot be hidden by retuning
numerical thresholds.


## 8. Deterministic 1,000-state batch

A deterministic batch with seed `20260925` samples 1,000 finite complex states of
dimension 3--6 with certified persistent rank 1--3 and iterates the legacy CSR
structural step for at most 10 steps, with the formation gate disabled so the
recursion/load mechanism itself is isolated.

The machine-readable output is `CSR_STRESS_RESULTS.json`, generated by
`stress_csr.py`.

The current reproducible run reports:

- `persistent_rank_increases = 0`;
- `dual_load_numerical_ambiguity = 1000`;
- mean successful steps `3.777`;
- minimum successful steps `2`;
- maximum successful steps `5`;
- maximum observed recursive power norm approximately
  \(1.0000000000000193\).

The eventual stop is a **numerical dual-load ambiguity**, not exact \(\bot\).
This replaces older wording that described the same near-boundary floating failure as
rank ambiguity.

The audit remains a numerical/category stress test of the legacy inherited-only CSR,
not empirical evidence.

## 9. Universal-state gap exposed by R4

**Historical resolution:** the gap described in this section motivated the current
two-density state and is no longer an unresolved state-contract problem. The
authoritative finite state now carries separate \(\rho_F\) and \(\rho_W\). The vector
\(d\) below is retained only as the historical quotient chart used by this CSR audit.



R4 permits a genuinely emergent target sector

\[
E=Q_+-TT^\dagger
\]

and, when required, defines a phase-independent formation seed

\[
\rho_E=(-\lambda_0^E)\Pi_E
\]

when the compressed emergent formation operator has a simple negative ground mode.

The present quotient state

\[
(\mathcal H,\mathfrak D,\mathfrak c,\aleph,d,Y,R_C)
\]

contains only a vector \(d\), not an independent positive formation/witness density.
Therefore an R4 emergent seed cannot in general be inserted into `d` canonically:
choosing an eigenvector of \(\Pi_E\) would reintroduce a forbidden phase/basis choice.

This proves that the current quotient state is **too small for universal R4-compatible
rank-increasing closure**.

The next state-contract audit must decide whether the universal state carries an
additional positive operator \(\rho\) (or an equivalent phase-free formation object)
and derive how that object participates in loads, neutral reclosure, and persistence.

Until that is closed, inherited-only CSR remains a restricted finite completion, not
the final universal BFG state law.
