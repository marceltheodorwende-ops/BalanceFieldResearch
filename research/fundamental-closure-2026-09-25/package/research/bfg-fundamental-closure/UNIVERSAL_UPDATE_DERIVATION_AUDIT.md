# Universal State Update — derivation audit

> **Historical-state note.**  
> This document analyzes an earlier vector-chart quotient using \(d\). That quotient is
> retained here only for the obstruction/derivation argument it established. The
> authoritative current finite state is the two-density state
> \[
> (\mathcal H,\mathfrak D,\mathfrak c,\aleph,\rho_F,\rho_W,Y,R_C),
> \]
> with \(d\) only a rank-one chart when \(\rho_F=dd^\dagger\). See `MASTER_STATE.md`.
>


## Result

The current BFG corpus determines a larger part of the universal update than the
previous package contract stated, but it still does **not** determine a unique full
successor state.

After quotienting representational factorizations, the genuine unresolved completion
reduces to exactly two successor objects:

\[
\boxed{Y_{n+1}}
\qquad\text{and}\qquad
\boxed{R_{C,n+1}}.
\]

Everything else in the finite reclosure step is fixed once these two objects are known.

This is a mathematical reduction of the open problem, not a new physical axiom.

---

## 1. Generator-level quotient state

The triples

\[
(B_C,W_N,L_C)
\]

enter the universal neutral/polar generator only through

\[
Y=L_C^\dagger B_C^\dagger W_N B_C L_C.
\]

Therefore define the Gram-gauge equivalence

\[
(B_C,W_N,L_C)\sim_G(B'_C,W'_N,L'_C)
\iff
Y=Y'.
\]

Likewise, the raw recursive factors

\[
R_C=MRM^\dagger,\qquad M=\sqrt{N_R}
\]

enter persistence selection through the realized operator \(R_C\).
For the generator-level update define

\[
(N_R,R)\sim_R(N'_R,R')
\iff
MRM^\dagger=M'R'M'^\dagger.
\]

The minimal operational state is therefore

\[
\boxed{
\Xi=
(\mathcal H,\mathfrak D,\mathfrak c,\aleph,d,Y,R_C).
}
\]

This quotient does not assert that the factors have no interpretation in a richer
carrier theory. It states only that the universal generator cannot distinguish two
factorizations producing the same \(Y\) and \(R_C\).

---

## 2. Maximal update already forced by BFG

Given admissible \(\Xi_n\):

### Formation

\[
K_n=\mathfrak c_n+\aleph_n-\mathfrak D_n.
\]

### Neutral pair

\[
C_n=(I+Y_n)^{-1},
\qquad
B_n=Y_n(I+Y_n)^{-1}.
\]

### Persistence

Use the repaired isolated peripheral Riesz space

\[
\mathcal W_n=\operatorname{Ran}P_{{\rm per},n}^{R}
\]

and its \(G_n\)-orthogonal projector

\[
P_n=P_{\mathcal W_n}^{(G_n)},
\qquad
G_n=I+Y_n.
\]

### Persistent branches

\[
d_n^{C}=P_n C_n d_n,
\qquad
d_n^{B}=P_n B_n d_n.
\]

### Loads

\[
\Lambda_n^C=\|d_n^C\|_{G_n}^2,
\qquad
\Lambda_n^B=\|d_n^B\|_{G_n}^2.
\]

If either load vanishes, the genuine dual reclosure terminates.

### Reciprocal weights

\[
\omega_{n+1}^{C}
=
\frac{\Lambda_n^B}{\Lambda_n^C+\Lambda_n^B},
\qquad
\omega_{n+1}^{B}
=
\frac{\Lambda_n^C}{\Lambda_n^C+\Lambda_n^B}.
\]

### Cross-fed analysis operator

\[
\mathcal A_n
=
\begin{bmatrix}
\sqrt{\omega_{n+1}^{C}}P_nC_n\\
\sqrt{\omega_{n+1}^{B}}P_nB_n
\end{bmatrix}.
\]

### Candidate packet

\[
\widetilde d_{n+1}
=
\mathcal A_n d_n.
\]

### Polar transport

\[
Q_n=(\mathcal A_n^\dagger\mathcal A_n)^{1/2},
\qquad
J_n=\mathcal A_nQ_n^+.
\]

\[
S_n=J_n^\dagger J_n,
\qquad
E_n=J_nJ_n^\dagger.
\]

### New carrier and capacities

\[
\mathcal H_{n+1}=\overline{\operatorname{Ran}J_n},
\]

and for

\[
\mathfrak A\in\{\mathfrak D,\mathfrak c,\aleph\}
\]

\[
\mathfrak A_{n+1}
=
E_n(\mathfrak A_n\oplus\mathfrak A_n)E_n
\big|_{\mathcal H_{n+1}}.
\]

Thus

\[
K_{n+1}
=
\mathfrak c_{n+1}
+
\aleph_{n+1}
-
\mathfrak D_{n+1}.
\]

The formation gate is now evaluable before any new carrier-specific physical law is
inserted.

This entire map is denoted

\[
\boxed{
\Pi_{\rm BFG}(\Xi_n)
}
\]

and will be called the **maximal forced preclosure update**.

---

## 3. Once \(Y_{n+1}\) is known, the active vector is not free

The existing universal reclosure equation already fixes the final neutral step:

\[
\boxed{
d_{n+1}
=
C_N(Y_{n+1})\widetilde d_{n+1}.
}
\]

Therefore \(d_{n+1}\) is not an independent completion function.

This removes one previously listed degree of freedom.

---

## 4. Gram non-uniqueness theorem

### Theorem

Suppose the target carrier has dimension at least one and the only declared successor
Gram requirement is

\[
Y_+
=
L_+^\dagger B_+^\dagger W_+B_+L_+
\succeq0.
\]

Then the current BFG equations do not determine \(Y_+\) uniquely.

### Proof

Let \(Y_\star\succeq0\) be arbitrary. Choose

\[
L_+=I,\qquad
W_+=I,\qquad
B_+=Y_\star^{1/2}.
\]

Then

\[
L_+^\dagger B_+^\dagger W_+B_+L_+
=
Y_\star.
\]

Thus every positive semidefinite \(Y_\star\) has an admissible Gram representation.

If the additional relation

\[
B_+=D_{{\rm cov},+}\mathfrak c_+
\]

is imposed and \(\mathfrak c_+\) is invertible, choose

\[
D_{{\rm cov},+}
=
Y_\star^{1/2}\mathfrak c_+^{-1}.
\]

Hence that relation alone also does not select a unique \(Y_\star\).

Therefore the successor load is underdetermined unless an additional BFG relation
links the new Gram operator to already generated preclosure data.

q.e.d.

### Explicit two-choice witness

For the same preclosure packet choose

\[
Y_+^{(1)}=I,
\qquad
Y_+^{(2)}=2I.
\]

Both satisfy the positive Gram rule, but

\[
C_N(Y_+^{(1)})=\frac12 I,
\qquad
C_N(Y_+^{(2)})=\frac13 I,
\]

so for nonzero \(\widetilde d_+\)

\[
d_+^{(1)}
\neq
d_+^{(2)}.
\]

The full successor state is therefore genuinely non-unique.

---

## 5. Recursive non-uniqueness theorem

### Theorem

Suppose a target carrier has a chosen one-dimensional persistent subspace
\(\mathcal W=\operatorname{Ran}P\) and nonzero complement. The current bounded-recursion
conditions do not determine \(R_C^+\) uniquely.

### Proof

For every

\[
0\le r<1
\]

define

\[
R_r=P+r(I-P).
\]

Then

\[
R_r^k=P+r^k(I-P),
\]

so

\[
\sup_k\|R_r^k\|<\infty.
\]

The peripheral Riesz space is exactly

\[
\operatorname{Ran}P,
\]

and the stable complement contracts with rate \(r\).

For distinct \(r_1,r_2\),

\[
R_{r_1}\neq R_{r_2},
\]

while both satisfy the same persistence/boundedness grammar.

Therefore the present BFG stability conditions do not choose one successor recursion
operator.

q.e.d.

---

## 6. Why the R4 cross-stratum theorem does not remove this freedom

The R4 continuation theorem constructs

\[
T=\operatorname{polar}(Q_+Q_-)
\]

from **already specified source and target support projectors** \(Q_-\) and \(Q_+\).

It canonically transports surviving witness structure and forbids invented amplitude,
but it does not construct the target persistent projector \(Q_+\) from the old state.

If \(Q_+\) is the persistent support of \(R_{C,+}\), then \(R_{C,+}\) must already be
known far enough to define \(Q_+\).

Therefore cross-stratum continuation solves the transport problem after the target
stratum is specified; it does not by itself solve the successor-recursion problem.

---

## 7. Two-law obstruction theorem

### Theorem

On the generator quotient state

\[
\Xi=(\mathcal H,\mathfrak D,\mathfrak c,\aleph,d,Y,R_C),
\]

the existing finite BFG architecture uniquely determines the preclosure map
\(\Pi_{\rm BFG}\) and, conditional on \(Y_+\), the final active vector

\[
d_+=C_N(Y_+)\widetilde d_+.
\]

A unique full universal state update exists if and only if BFG additionally determines
single-valued successor laws

\[
\boxed{
Y_+=\mathcal Y_{\rm BFG}(\Pi_{\rm BFG}(\Xi),\Xi)
}
\]

and

\[
\boxed{
R_{C,+}
=
\mathcal R_{\rm BFG}(\Pi_{\rm BFG}(\Xi),Y_+,\Xi)
}
\]

satisfying positivity, unitary covariance, recursive admissibility and the common
terminal/no-retuning rules.

Equivalently,

\[
\boxed{
\mathcal U_{\rm BFG}
=
\mathcal F_{\rm final}
\circ
(\mathcal Y_{\rm BFG},\mathcal R_{\rm BFG})
\circ
\Pi_{\rm BFG}.
}
\]

The current corpus does not yet supply unique \(\mathcal Y_{\rm BFG}\) and
\(\mathcal R_{\rm BFG}\).

---

## 8. Four-pass self-check

### Pass 1 — Type check

- \(Y_n,C_n,B_n,P_n\) act on \(\mathcal H_n\).
- \(\mathcal A_n:\mathcal H_n\to\mathcal H_n\oplus\mathcal H_n\).
- \(J_n\) has the same source/codomain.
- \(E_n\) acts on the doubled carrier.
- transported capacities act on \(\mathcal H_{n+1}=\operatorname{Ran}J_n\).
- \(Y_{n+1}\) and \(R_{C,n+1}\) must act on that same new carrier.
- only after \(Y_{n+1}\) exists is \(C_N(Y_{n+1})\widetilde d_{n+1}\) type-correct.

No type repair requires external physics.

### Pass 2 — Gauge check

Changing \((B_C,W_N,L_C)\) while keeping \(Y\) fixed leaves every downstream neutral,
metric, load, reciprocal-weight and polar quantity unchanged. Therefore factor-level
non-uniqueness is representational for the generator.

Changing \(Y\) changes the generator. Therefore \(Y_+\) itself is a genuine dynamical
freedom and cannot be quotiented away.

Likewise, raw factorizations of a fixed \(R_C\) can be quotiented, but changing \(R_C\)
changes persistence and is genuine dynamics.

### Pass 3 — Counterexample check

The explicit families

\[
Y_+=aI,\qquad a>0,
\]

and

\[
R_r=P+r(I-P),\qquad 0\le r<1,
\]

produce infinitely many mathematically admissible completions under the currently
stated positive-Gram and bounded-recursion conditions.

Therefore uniqueness cannot be recovered by algebraic rearrangement alone.

### Pass 4 — No-smuggling check

No Einstein, Yang–Mills, Schrödinger, Standard Model, thermodynamic, or external
physical equation was used.

The obstruction is internal to BFG's present mathematical specification.

---

## 9. Research consequence

The universal-update problem is now sharper:

> Do not search for seven arbitrary reconstruction functions.

Search for exactly two internally forced constitutive laws:

\[
\boxed{\mathcal Y_{\rm BFG}}
\qquad\text{and}\qquad
\boxed{\mathcal R_{\rm BFG}}.
\]

A proposed formula for either object must be rejected as "derived" unless it follows
from already declared BFG structure. If a new principle is required, it must be named
as a new BFG axiom rather than hidden inside the update.
