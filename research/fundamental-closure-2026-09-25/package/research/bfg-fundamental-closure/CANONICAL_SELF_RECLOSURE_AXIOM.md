# Canonical Self-Reclosure Axiom and finite closure theorem

## 0. Status

This document records two **declared finite BFG completion rules** used by the living
candidate. They are BFG-internal and use no external physical equation, but neither is
claimed to be uniquely forced by the historical corpus.

### Intrinsic-Gram successor load — declared completion

The source BFG neutral architecture supplies positive Gram constructions and the
cross-fed analysis map. It does not uniquely force the next master load to equal the
Gram of that particular analysis map.

The living package therefore **declares**

\[
\boxed{
Y_{n+1}
=
\mathcal A_n^{DO}\mathcal A_n^{DO\dagger}
\big|_{\mathcal H_{n+1}}
}
\]

in range coordinates, equivalently

\[
\boxed{
Y_{n+1}^{\rm supp}
=
\mathcal A_n^{DO\dagger}\mathcal A_n^{DO}
\big|_{\mathcal H_{a,n}}
}
\]

in active source-support coordinates.

The two are unitarily equivalent through the polar partial isometry.

### Neutral transverse recursion — declared completion

The historical BFG corpus requires protected persistence plus bounded transverse
recursion but does not supply a unique successor \(R_C\).

The living package therefore declares:

> The next protected persistent sector is the canonically inherited/seeded persistent
> support selected by the finite update. On its complement, recursive maintenance is
> exactly the retained neutral response \(C_N(Y_+)\), with no fitted scalar or
> sector-specific response law.

These rules are explicitly **completion principles**, not retroactive source theorems.

---

## 1. Active coordinates

Let

\[
\mathcal A:\mathcal H\to\mathcal H\oplus\mathcal H
\]

be the BFG cross-fed analysis operator.

Take its reduced singular-value decomposition

\[
\mathcal A=U\Sigma V^\dagger,
\qquad
\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_r),
\qquad
\sigma_j>0.
\]

Then

\[
\mathcal H_a=\operatorname{Ran}V,
\qquad
\mathcal H_+=\operatorname{Ran}U,
\]

and the polar partial isometry is

\[
J=UV^\dagger.
\]

In these matched active coordinates the transport is the identity between the two
\(r\)-dimensional coordinate copies.

---

## 2. Intrinsic next load

The source-side Gram is

\[
V^\dagger\mathcal A^\dagger\mathcal A V
=
\Sigma^2.
\]

The target-side Gram is

\[
U^\dagger\mathcal A\mathcal A^\dagger U
=
\Sigma^2.
\]

Therefore define

\[
\boxed{
Y_+=\Sigma^2.
}
\]

This is positive definite on the active target carrier because all retained singular
values are strictly positive.

Consequently

\[
G_+=I+Y_+>0
\]

and

\[
C_+:=C_N(Y_+)=(I+Y_+)^{-1}
\]

satisfies

\[
0<C_+<I.
\]

In finite dimension there is therefore a strict number

\[
q_+:=\|C_+\|_2
=
\frac{1}{1+\lambda_{\min}(Y_+)}
<1.
\]

---

## 3. Canonical transport of persistence

Let \(\mathcal W\) be the repaired peripheral Riesz space of the source recursive
operator and let \(W\) be an ordinary orthonormal basis matrix for that subspace.

Only the part of \(\mathcal W\) visible to the active source support can survive:

\[
W_{\rm surv}:=V^\dagger W.
\]

Let \(V_{\rm per,+}\) be the polar partial isometry / orthonormal range basis of
\(W_{\rm surv}\).

If

\[
\operatorname{rank}W_{\rm surv}=0,
\]

the persistence corridor is lost and the branch returns

\[
\bot.
\]

Otherwise define the target persistent projector

\[
\boxed{
P_+
=
V_{\rm per,+}V_{\rm per,+}^\dagger.
}
\]

This construction cannot increase persistent rank:

\[
\operatorname{rank}P_+
\le
\dim\mathcal W.
\]

Thus no new direction is falsely labelled inherited persistence.

Set

\[
P_s^+=I-P_+.
\]

---

## 4. Canonical recursive rebuild

The new BFG recursion axiom gives

\[
\boxed{
R_{C,+}
=
P_+
+
P_s^+\,C_N(Y_+)\,P_s^+.
}
\]

No free decay coefficient appears.

No external evolution law appears.

No phase parameter appears; pure internal holonomy is already quotiented at this
generator level.

---

## 5. Recursive stability theorem

### Theorem

For finite-dimensional active carrier \(\mathcal H_+\), with \(Y_+>0\) and
\(P_+\neq0\), the operator

\[
R_{C,+}
=
P_+
+
P_s^+C_+P_s^+
\]

is self-adjoint, power bounded, has peripheral eigenspace exactly
\(\operatorname{Ran}P_+\), and has a strictly contracting complementary block.

### Proof

Since \(P_+\) and \(P_s^+\) are complementary orthogonal projectors,

\[
P_+P_s^+=0.
\]

The operator \(C_+\) is positive self-adjoint with

\[
0<C_+\le q_+I,
\qquad
q_+<1.
\]

Therefore

\[
T_s:=P_s^+C_+P_s^+
\]

is positive self-adjoint on \(\operatorname{Ran}P_s^+\) and

\[
\|T_s\|\le q_+<1.
\]

The two blocks are orthogonal, so

\[
R_{C,+}^k
=
P_+
+
T_s^k.
\]

Hence

\[
\sup_{k\ge0}\|R_{C,+}^k\|
\le1
\]

and

\[
\|T_s^k\|
\le q_+^k\to0.
\]

On \(\operatorname{Ran}P_+\),

\[
R_{C,+}=I.
\]

On the complementary block the spectral radius is strictly below one. Therefore the
only unit-modulus spectrum is the eigenvalue \(1\) on \(\operatorname{Ran}P_+\).

Thus the repaired persistent Riesz space of the successor is exactly

\[
\operatorname{Ran}P_+.
\]

q.e.d.

---

## 6. Final active state

The existing neutral reclosure now contains no remaining freedom:

\[
\widetilde d_+
=
\mathcal A d,
\]

written in active target coordinates as

\[
\widetilde d_+^{\rm act}=U^\dagger\mathcal A d.
\]

Then

\[
\boxed{
d_+
=
C_N(Y_+)\widetilde d_+^{\rm act}.
}
\]

Because \(C_N(Y_+)\) is invertible and a nonterminal packet is nonzero,

\[
d_+\neq0.
\]

---

## 7. Complete candidate universal update

With the new BFG recursion axiom, the finite generator is now single-valued:

\[
\boxed{
\Xi_+
=
\mathcal U_{\rm BFG}^{\rm CSR}(\Xi)
}
\]

where the step consists only of

1. exact BFG neutral resolution;
2. repaired spectral persistence;
3. graph-metric projection;
4. reciprocal endogenous weights;
5. cross-fed BFG analysis;
6. polar active-support transport;
7. common capacity compression;
8. intrinsic Gram rebuild \(Y_+=A A^\dagger|_{\mathcal H_+}\);
9. transported persistence \(P_+\);
10. neutral transverse recursive rebuild;
11. final neutral active-state update;
12. common formation / admissibility gates;
13. otherwise \(\bot\).

No GR, QFT, Standard Model, thermodynamic, or carrier-specific law appears.

---

## 8. What is and is not solved

### Closed conditionally

Under the Canonical Self-Reclosure Axiom, the finite quotient generator has no free
successor load and no free successor recursion operator.

### Not claimed

This does not prove that the recursion clause was already forced by the historical BFG
documents.

It is a new BFG law proposed because the earlier corpus provably leaves the successor
recursion underdetermined.

The axiom is falsifiable at the mathematical level: if it breaks category closure,
unitary covariance, recursive boundedness, or later no-retuning recovery tests, it is
rejected rather than repaired sector by sector.
