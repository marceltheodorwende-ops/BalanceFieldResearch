# BFG Finite-Dimensional Recursive Stability Theorem

## Status and scope

This document adds a theorem-level stability layer to the BFG Emergence Studio
without changing the frozen theory-facing stack above Level 30.

It formalizes the finite-dimensional recursive stability condition already used
by the canonical BFG persistence architecture:

\[
R_C e_T=e_T,\qquad
\|R_C|_{E_s}\|_L\le r<1,
\]

together with the broader finite-dimensional power-boundedness criterion.

The result is **not** a theorem that every conceivable BFG carrier is stable.
It is an exact theorem under explicit finite-dimensional operator assumptions,
plus a conditional BFG corollary.

The infinite-dimensional extension remains a separate proof obligation.

---

## 1. Definitions

Let \(H\) be a finite-dimensional real or complex Hilbert space and let

\[
R_C:H\to H
\]

be the recursive closure operator.

### Definition 1 — Power-bounded recursive closure

\(R_C\) is power bounded if

\[
\sup_{n\ge0}\|R_C^n\|<\infty.
\]

Consequently, every recursive trajectory satisfies

\[
\sup_{n\ge0}\|R_C^n s\|<\infty.
\]

This is stronger than the scalar condition \(\rho(R_C)\le1\).

### Definition 2 — Peripheral spectrum

\[
\sigma_{\rm per}(R_C)
=
\{\lambda\in\sigma(R_C):|\lambda|=1\}.
\]

An eigenvalue is **semisimple** if its algebraic and geometric multiplicities are
equal. Equivalently, it has no nontrivial Jordan block.

### Definition 3 — Stable complement

For an invariant decomposition

\[
H=W\oplus E_s,
\]

\(W\) is the persistent/peripheral sector and \(E_s\) is a strictly stable
complement if

\[
\rho(R_C|_{E_s})<1.
\]

The associated spectral gap is

\[
\gamma
=
1-\rho(R_C|_{E_s})
>0.
\]

---

## 2. Exact finite-dimensional power-boundedness theorem

### Theorem 1 — Recursive Stability Criterion

For a finite-dimensional operator \(R_C\), the following are equivalent:

1. \(R_C\) is power bounded:
   \[
   \sup_{n\ge0}\|R_C^n\|<\infty.
   \]

2. Both conditions hold:
   \[
   \sigma(R_C)\subseteq\{z:|z|\le1\},
   \]
   and every eigenvalue satisfying \(|\lambda|=1\) is semisimple.

Therefore

\[
\boxed{
R_C\ \text{power bounded}
\iff
\rho(R_C)\le1
\ \text{and all unit-circle eigenvalues are semisimple}.
}
\]

### Proof

Put \(R_C\) into Jordan normal form over \(\mathbb C\):

\[
R_C=SJS^{-1}.
\]

For a Jordan block

\[
J_\lambda=\lambda I+N,
\qquad N^m=0,
\]

the binomial formula gives

\[
J_\lambda^n
=
\sum_{k=0}^{m-1}
\binom{n}{k}\lambda^{\,n-k}N^k.
\]

If \(|\lambda|>1\), the term \(|\lambda|^n\) grows exponentially, so the powers
cannot be bounded.

If \(|\lambda|=1\) and \(m>1\), at least one term contains a nonzero polynomial
factor \(\binom nk\), so the block grows polynomially. Hence a unit-circle
eigenvalue must have only size-one Jordan blocks.

Conversely, if every eigenvalue lies in the closed unit disk and every
unit-circle block has size one, then the unit-circle part is bounded and every
block with \(|\lambda|<1\) decays despite any finite Jordan polynomial factor.
Thus \(J^n\) is uniformly bounded, and so is

\[
R_C^n=SJ^nS^{-1}.
\]

This proves the equivalence. \(\square\)

---

## 3. BFG protected-witness corollary

### Corollary 1 — Persistent sector plus stable complement

Assume an invariant direct sum

\[
H=W\oplus E_s
\]

such that

\[
R_C(W)\subseteq W,
\qquad
R_C(E_s)\subseteq E_s,
\]

the persistent restriction \(R_C|_W\) is diagonalizable with spectrum on the unit
circle, and

\[
\rho(R_C|_{E_s})<1.
\]

Then \(R_C\) is power bounded.

If in the strongest protected-witness case

\[
R_C|_W=I_W,
\]

then for

\[
s=w+s_s
\]

one has

\[
R_C^n s
=
w+(R_C|_{E_s})^n s_s,
\]

and therefore

\[
(R_C|_{E_s})^n s_s\to0.
\]

Thus the recursive trajectory remains bounded and asymptotically approaches the
persistent witness sector.

This formalizes the canonical BFG source line

\[
R_C e_T=e_T,
\qquad
\|R_C|_{E_s}\|_L\le r<1.
\]

---

## 4. Lyapunov-metric corollary

### Corollary 2 — Adapted positive metric

Under the hypotheses of Corollary 1 there exists a positive-definite Hermitian
metric \(L\succ0\) in which

\[
\|R_C w\|_L=\|w\|_L
\quad (w\in W)
\]

and

\[
\|R_C s\|_L\le r\|s\|_L
\quad (s\in E_s)
\]

for some \(r<1\).

Equivalently,

\[
R_C^\dagger L R_C\preceq L
\]

on the full space, with strict contraction on \(E_s\).

### Construction argument

Because the peripheral restriction is diagonalizable with unit-modulus
eigenvalues, one may choose a positive metric on \(W\) that makes its eigenbasis
orthonormal; in that metric the peripheral block is isometric.

Because \(\rho(R_C|_{E_s})<1\), discrete Lyapunov theory gives a positive-definite
metric on \(E_s\) in which the stable block is strictly contractive.

Taking the direct-sum metric yields the claimed \(L\).

This is the precise finite-dimensional meaning of a bounded Lyapunov recursion
for the protected persistent/stable split.

---

## 5. Why \(\rho(R_C)\approx1\) is not sufficient

The scalar spectral-radius statement alone does not exclude defective
unit-circle recursion.

For example,

\[
J=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
\]

has

\[
\rho(J)=1,
\]

but

\[
J^n=
\begin{pmatrix}
1&n\\
0&1
\end{pmatrix},
\]

so

\[
\|J^n\|\to\infty.
\]

Therefore the BFG stability grammar must be read as

\[
\boxed{
\rho(R_C)\le1
\quad+\quad
\text{semisimple peripheral spectrum}
\quad+\quad
\text{strictly stable complement}
}
\]

rather than as spectral radius alone.

The software contains this Jordan-block counterexample as a mandatory rejection
control.

---

## 6. Neutral-interface stability lemma

Let

\[
Y\succeq0,
\]

and define

\[
C_N=(I+Y)^{-1},
\qquad
B_N=Y(I+Y)^{-1}=I-C_N.
\]

Then

\[
C_N+B_N=I,
\]

and spectral calculus gives

\[
0<C_N\le I,
\qquad
0\le B_N<I.
\]

Hence neutral resolution itself is non-amplifying in the operator-order sense.

This exact local boundedness result is logically distinct from recursive
power-boundedness of \(R_C\). Both are required for the stronger stability
architecture.

---

## 7. Feedback-criticality lemma

For the scalar recursive feedback relation

\[
IB=A+B\,IB,
\]

one obtains

\[
IB=\frac{A}{1-B}.
\]

If

\[
|1-B|\ge\varepsilon>0,
\]

then

\[
|IB|
\le
\frac{|A|}{\varepsilon}.
\]

Thus the feedback amplitude is bounded away from the critical denominator.

Again, this does **not** by itself imply power-boundedness of \(R_C\). It closes a
different failure surface: scalar recursive criticality.

---

## 8. Combined finite-dimensional BFG stability certificate

For a finite-dimensional implemented BFG recursion, the following package is a
sufficient stability certificate:

\[
Y\succeq0,
\]

\[
C_N=(I+Y)^{-1},\qquad B_N=I-C_N,
\]

\[
|1-B|\ge\varepsilon,
\]

\[
\sigma(R_C)\subseteq\overline{\mathbb D},
\]

every \(|\lambda|=1\) eigenvalue of \(R_C\) is semisimple, and the nonperipheral
spectrum satisfies

\[
\sup_{\lambda\notin\sigma_{\rm per}}
|\lambda|
\le1-\gamma
\]

for some \(\gamma>0\).

Then

\[
\sup_{n\ge0}\|R_C^n\|<\infty.
\]

If the peripheral sector is the protected witness sector, witness continuity is
preserved while the transverse sector decays.

---


## 9. Perturbation statement

A positive spectral separation between the peripheral cluster and the stable
cluster is robust under sufficiently small perturbations in the usual spectral
sense: the clusters remain separated when the perturbation is smaller than the
relevant conditioning/gap scale.

That statement is **not** the same as saying that arbitrary sufficiently small
perturbations preserve exact unit-circle persistence or power boundedness.

For example,

\[
R=
\operatorname{diag}(1,1/2)
\]

is power bounded, while

\[
R_\varepsilon=
\operatorname{diag}(1+\varepsilon,1/2)
\]

can be arbitrarily close to \(R\) and nevertheless has

\[
\rho(R_\varepsilon)>1.
\]

Therefore exact recursive stability is perturbatively preserved only inside an
admissible perturbation class that independently retains the finite
power-boundedness criterion, or inside a stronger constrained class such as a
unitary/tangential perturbation of the peripheral block.

The active finite master runtime has such a stronger successor guarantee after
successful closure:

\[
R_+=\exp(i\tau K_+),
\qquad
K_+=K_+^\dagger,
\]

so \(R_+\) remains unitary by construction.

The software audit now includes both controls:

- a small outward perturbation of a unit-circle eigenvalue is rejected;
- a small tangential perturbation along the unit circle remains admissible.


---

## 10. What is now mathematically secured

Within the finite-dimensional class satisfying the theorem hypotheses, recursive
boundedness is no longer merely a heuristic or a finite-run observation.

It follows exactly from the spectral/Jordan structure.

In particular, the theorem formally excludes:

- supercritical eigenvalues \(|\lambda|>1\),
- defective Jordan blocks on the unit circle,
- loss of the strict stable gap,
- conflation of scalar feedback margin with operator stability.

---


## 11. Relation to the closed finite master runtime

The power-boundedness theorem remains a conditional operator theorem: an
arbitrary externally supplied \(R_C\) must satisfy its hypotheses.

The active master runtime now resolves the successor side differently. Under the
adopted reduced finite closure profile,

\[
R_+=\exp(i\tau K_+),
\]

with \(K_+=K_+^\dagger\). Hence \(R_+\) is unitary and

\[
\|R_+^n\|=1
\qquad\text{for all }n\ge0.
\]

Thus after every successful finite master step, recursive power boundedness is
satisfied by construction.

The initial state is still admitted through the repaired power-boundedness
criterion. Once admitted and successfully reclosed, the master successor no
longer requires a separate stability guess.

A restricted bounded infinite-dimensional entry class with finite peripheral
rank reduces to the finite profile. Arbitrary unbounded/infinite-rank transport
is outside the executable category.

Empirical realization remains logically separate from this mathematical runtime
closure.

---

## 12. Software realization

`bfg_studio.stability` implements:

- the finite-dimensional spectral power-boundedness criterion;
- peripheral semisimplicity / Jordan-defect detection;
- stable-gap reporting;
- finite-horizon power diagnostics;
- neutral-resolvent boundedness auditing;
- feedback-margin auditing;
- an explicit unit-circle Jordan counterexample;
- a master stability audit over the current finite-dimensional real carriers.

The software checks theorem hypotheses numerically. The proof above does not
depend on those numerical runs.


---

## 13. Exact rational certificate for supplied nonnormal splittings

The nonnormal persistence extension strengthens the numerical
semisimplicity audit with an exact finite certificate.

Let \(R,S,M,N\) have rational entries, \(S\) invertible, and suppose

\[
S^{-1}RS=\operatorname{diag}(A,T).
\]

If

\[
A^TMA=M,\qquad M\succ0,
\]

and

\[
N-T^TNT\succ0,\qquad N\succ0,
\]

then \(A\) is isometric in the \(M\)-metric and \(T\) is strictly
contractive in the \(N\)-metric. Therefore \(R\) is power bounded even when
it is nonnormal in the original Euclidean coordinates.

The exact spectral projector supplied by this certificate is

\[
P_{\rm spec}
=
S\operatorname{diag}(I_p,0)S^{-1}.
\]

It is generally oblique and is **not** identified with the BFG graph-metric
projector.

`bfg_studio.closure_math.verify_exact_recursive_certificate` checks this
certificate using exact rational arithmetic. It accepts a supplied
certificate; it does not automatically discover the invariant split.

---

## 14. Retained-channel and reconstruction boundary

For \(P=UU^\dagger\),

\[
B_{\rm tan}=U^\dagger B_2U,
\qquad
E=(I-P)B_2U
\]

gives the exact decomposition

\[
U^\dagger B_2^\dagger B_2U
=
B_{\rm tan}^\dagger B_{\rm tan}+E^\dagger E.
\]

Thus retained external channels close the missing **Gram-energy accounting**
on the active support.

However \(E^\dagger E\) does not in general determine the direction of the
external channel, future derivatives, future couplings, or a unique
\(R_{\rm next}\). This is a reconstruction boundary rather than an
instability of the finite theorem.

The master therefore separates:

\[
\text{recursive stability once }R_C\text{ is specified}
\]

from

\[
\text{universal autonomous reconstruction of the next }R_C.
\]

The first has an exact finite-dimensional theorem and exact supplied
certificates. The second remains a distinct closure obligation.
