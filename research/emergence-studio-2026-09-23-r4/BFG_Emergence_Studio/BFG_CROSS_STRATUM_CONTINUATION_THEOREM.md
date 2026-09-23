# BFG Cross-Stratum Continuation Theorem

## 1. Purpose

The finite runtime already knows when a declared stratum ends. The remaining
question is how a persistent witness is transported when the active or
persistent support changes.

The continuation law must satisfy four requirements:

1. no basis matching by hand;
2. no semantic reset of surviving witness structure;
3. no invented amplitude in newly appearing directions;
4. no arbitrary branch choice when a new sector is degenerate.

The construction below closes that finite-runtime transport problem.

---

## 2. Support projectors

Let

\[
Q_-
\]

be the source support projector and

\[
Q_+
\]

the target support projector in one common ambient Hilbert space.

For the active runtime stratum,

\[
Q_A
=
\mathbf 1_{(\tau_A^2,\infty)}
(A^\dagger A),
\]

where

\[
\tau_A
=
\max(
\mathrm{rank\_tol},
\mathrm{rtol}\,\sigma_1(A)
).
\]

For the persistent runtime stratum of a normal contraction,

\[
Q_P
=
\mathbf 1_{[\tau_P^2,\infty)}
(R^\dagger R),
\qquad
\tau_P=1-\mathrm{peripheral\_tol}.
\]

These projectors are spectral objects. They do not depend on a choice or
ordering of eigenvectors inside a degenerate support block.

---

## 3. Canonical polar transport

Define

\[
X=Q_+Q_-.
\]

Let

\[
X=T|X|
\]

be the polar decomposition on the support of \(|X|\).

Equivalently,

\[
\boxed{
T
=
X(X^\dagger X)^{\dagger 1/2},
}
\]

where the inverse square root is taken only on the positive support.

Then \(T\) is the unique polar partial isometry associated with
\(Q_+Q_-\).

Its initial and final supports are

\[
S_-=T^\dagger T,
\qquad
S_+=TT^\dagger.
\]

They satisfy

\[
S_-\le Q_-,
\qquad
S_+\le Q_+.
\]

The lost and emergent projectors are

\[
\boxed{
L=Q_- - S_-,
}
\]

\[
\boxed{
E=Q_+ - S_+.
}
\]

No basis pairing is used anywhere in the construction.

---

## 4. Unitary equivariance

Let \(U\) be any ambient unitary transformation.

Under

\[
Q_\pm\mapsto UQ_\pm U^\dagger,
\]

one has

\[
X\mapsto UXU^\dagger.
\]

Uniqueness of the polar decomposition implies

\[
\boxed{
T\mapsto UTU^\dagger.
}
\]

Likewise,

\[
S_\pm\mapsto US_\pm U^\dagger,
\]

\[
E\mapsto UEU^\dagger,
\qquad
L\mapsto ULU^\dagger.
\]

Therefore the continuation rule is coordinate-free.

The current numerical equivariance control has maximum residual of order

\[
10^{-15}.
\]

---

## 5. Witness transport

Let

\[
\rho_-\succeq0,
\qquad
\operatorname{tr}\rho_-=1,
\qquad
Q_-\rho_-Q_-=\rho_-.
\]

The transportable witness mass is

\[
\boxed{
m_{\rm keep}
=
\operatorname{tr}(S_-\rho_-).
}
\]

The lost witness mass is

\[
\boxed{
m_{\rm lost}=1-m_{\rm keep}.
}
\]

If

\[
m_{\rm keep}>0,
\]

the normalized inherited witness in the target stratum is

\[
\boxed{
\rho_+^{\rm inh}
=
\frac{
T\rho_-T^\dagger
}{
m_{\rm keep}
}.
}
\]

This state is positive, normalized and supported on \(S_+\).

The emergent complement satisfies

\[
E\rho_+^{\rm inh}=0.
\]

Thus inherited witness continuity never invents amplitude in a new sector.

If

\[
m_{\rm keep}=0,
\]

there is no surviving semantic/witness corridor into the target stratum. The
finite no-reset rule therefore commits the continuation to

\[
\boxed{\bot}.
\]

---

## 6. Rank increase

Suppose

\[
\operatorname{rank}Q_+
>
\operatorname{rank}Q_-.
\]

The polar transport carries the entire overlapping source witness into the
target support.

The orthogonal complement

\[
E=Q_+-TT^\dagger
\]

is the genuinely emergent sector.

The inherited witness has zero support there:

\[
\operatorname{tr}(E\rho_+^{\rm inh})=0.
\]

Hence a rank increase means

\[
\boxed{
\text{old witness persists}
+
\text{new sector appears without inherited content}.
}
\]

No ad hoc initialization is allowed.

---

## 7. Rank decrease

Suppose

\[
\operatorname{rank}Q_+
<
\operatorname{rank}Q_-.
\]

Then

\[
L=Q_- - T^\dagger T
\]

is the lost source sector.

The exact lost witness mass is

\[
\boxed{
m_{\rm lost}
=
\operatorname{tr}(L\rho_-).
}
\]

If the witness lies entirely in the retained source support,

\[
m_{\rm keep}=1,
\]

continuity is exact.

If only part survives,

\[
0<m_{\rm keep}<1,
\]

the runtime records the loss explicitly and normalizes only the surviving
witness.

If

\[
m_{\rm keep}=0,
\]

continuity terminates at \(\bot\).

---

## 8. Same-rank transport

Equal source and target ranks do not imply identical supports.

For rotating support planes the same polar law applies.

If the two supports have full mutual overlap, then

\[
T^\dagger T=Q_-,
\qquad
TT^\dagger=Q_+,
\]

so \(T\) is a unitary isomorphism from the source support to the target support.

This gives a canonical continuation through smooth support rotation without
eigenvector matching.

---

## 9. Emergent-sector no-choice rule

A genuinely new sector \(E\) has no inherited witness.

If the architecture requires that new sector to obtain an endogenous formation
seed, use the formation operator \(H\) compressed to the emergent support:

\[
H_E
=
EHE
\big|_{\operatorname{ran}E}.
\]

Let

\[
\lambda_0^E
\]

be its lowest eigenvalue.

A canonical seed exists only if

\[
\boxed{
\lambda_0^E<-\varepsilon_{\rm sign}
}
\]

and the lowest eigenvalue is simple:

\[
\boxed{
\lambda_1^E-\lambda_0^E
>
\varepsilon_{\rm simple}.
}
\]

Then the ambient ground projector

\[
\Pi_E
\]

is unique and basis-independent, and the new formation density is

\[
\boxed{
\rho_E=(-\lambda_0^E)\Pi_E.
}
\]

If the lowest mode is nonnegative or degenerate, the runtime does **not** pick
one vector from the block.

It commits the requested seeded transition to

\[
\boxed{\bot}.
\]

This is the cross-stratum form of the BFG no-choice rule.

---

## 10. Cross-stratum chain stability

Each polar transport \(T_j\) is a partial isometry. Therefore

\[
\boxed{
\|T_j\|_2\le1.
}
\]

For any finite sequence of strata,

\[
Q_0\to Q_1\to\cdots\to Q_n,
\]

define

\[
\mathcal T_n
=
T_{n-1}\cdots T_1T_0.
\]

Submultiplicativity gives

\[
\boxed{
\|\mathcal T_n\|_2\le1.
}
\]

Thus the cross-stratum transport layer is nonamplifying.

For the unnormalized inherited witness,

\[
\widetilde\rho_{j+1}
=
T_j\widetilde\rho_jT_j^\dagger,
\]

one has

\[
\operatorname{tr}\widetilde\rho_{j+1}
\le
\operatorname{tr}\widetilde\rho_j.
\]

Therefore cumulative inherited witness mass is monotone nonincreasing.

Cross-stratum continuation by itself cannot create recursive witness blow-up.

---

## 11. Transition taxonomy

The finite runtime distinguishes:

\[
\boxed{
\text{rank increase}
}
\]

when

\[
\operatorname{rank}Q_+>\operatorname{rank}Q_-,
\]

\[
\boxed{
\text{rank decrease}
}
\]

when

\[
\operatorname{rank}Q_+<\operatorname{rank}Q_-,
\]

\[
\boxed{
\text{same-rank transport}
}
\]

when the ranks agree and the overlap support is complete,

and

\[
\boxed{
\text{same-rank discontinuous overlap}
}
\]

when equal-rank supports lose an entire transportable direction.

The last case is not silently identified with smooth continuation.

---

## 12. Controlled crossing audit

Seven explicit crossing/control cases are retained in the master runtime.

### Active rank increase

\[
1\to2
\]

with full inherited witness retention.

Result:

\[
\boxed{\text{PASS}}.
\]

### Active rank decrease with retained witness

\[
2\to1
\]

while the witness lies in the surviving support.

Result:

\[
\boxed{\text{PASS}}.
\]

### Active rank decrease with witness annihilation

The witness lies entirely in the lost sector.

Result:

\[
\boxed{\bot}
\]

as required.

### Persistent rank increase

\[
1\to2
\]

through the declared persistent runtime threshold.

Result:

\[
\boxed{\text{PASS}}.
\]

### Same-rank rotating support

The support rotates continuously in the ambient space.

Result:

\[
\boxed{\text{PASS}},
\]

with target alignment equal to numerical unity.

### Degenerate emergent sector

The new sector has a twofold degenerate negative lowest mode.

Result:

\[
\boxed{\bot}
\]

under the no-choice rule.

### Unique emergent seed

The new sector has one simple negative lowest mode.

Result:

\[
\boxed{\text{PASS}},
\]

with the unique formation seed constructed.

---

## 13. Current real-carrier audit

All current first-step real-carrier states remain on the runtime stratum

\[
(p,r)=(4,4).
\]

Therefore the present natural carrier snapshots contain

\[
\boxed{0}
\]

observed first-step rank crossings.

This is important: the cross-stratum theorem is not being presented as if a
natural transition had already been empirically observed.

What can be audited on the current real states is the canonical support
construction and identity continuation.

Across

\[
\boxed{1409/1409}
\]

current real-carrier states:

- the active and persistent support projectors are well-defined;
- self-continuation retains witness mass \(1\);
- no spurious terminal transition occurs;
- the support transport residual remains within numerical tolerance.

---

## 14. Architectural integration

The finite BFG transition grammar is now

\[
\boxed{
S
\to
\mathcal L_{\rm bif}
\to
(Q_-,Q_+)
\to
T_{\rm polar}
\to
\begin{cases}
\text{inherited witness},\\
\text{emergent sector},\\
\text{lost sector}
\end{cases}
\to
\text{formation/no-choice gate}
\to
S_+\ \text{or}\ \bot.
}
\]

The stratum boundary is therefore no longer only detected.

The runtime now has a canonical rule for crossing it.

---

## 15. Claim boundary

The following are theorem-level finite-dimensional statements:

\[
\boxed{
T=\operatorname{polar}(Q_+Q_-)
}
\]

is the canonical support transport;

\[
\boxed{
\|T\|_2\le1
}
\]

and finite products of such transports are nonamplifying;

\[
\boxed{
m_{\rm keep}
=
\operatorname{tr}(T^\dagger T\,\rho_-)
}
\]

is the exact retained witness mass;

and a required emergent one-dimensional seed is admitted only by a simple
negative compressed formation ground mode.

The following is **not** claimed:

\[
\boxed{
\text{a real natural carrier rank crossing has already been observed}.
}
\]

The current real-carrier data provide support/self-continuation checks only.
Actual crossing behavior is presently theorem-level runtime machinery plus
controlled structural tests.

---

## 16. Closure consequence

Within the declared finite runtime, the formation architecture now contains:

1. exact formation eligibility;
2. exact active formation margin;
3. conditional parent-state formation robustness;
4. operational persistent- and active-rank transition surfaces;
5. a strict runtime-stratum parent corridor;
6. canonical basis-free cross-stratum witness continuation;
7. a no-choice rule for genuinely new sectors;
8. nonamplifying cross-stratum recursion.

Accordingly, the previously open finite **cross-stratum continuation block** is
closed for the declared runtime category.

This does not by itself establish empirical universal natural realization, nor
does it prove an unrestricted infinite-dimensional continuation theorem.
