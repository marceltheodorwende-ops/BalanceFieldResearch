# BFG Stratum Transition Geometry and Runtime Bifurcation Ledger

## 1. Scope

The finite BFG formation runtime contains four distinct local transition
families:

\[
\boxed{
\text{formation sign},
\quad
\text{formation simplicity},
\quad
\text{persistent runtime rank},
\quad
\text{active runtime rank}.
}
\]

The first two are spectral surfaces of the active formation operator \(K_+\).
The latter two are runtime stratum surfaces defined by the declared numerical
admissibility policy.

The distinction between exact algebraic strata and runtime strata is essential.

Exact matrix rank and exact unit-circle persistence are not open properties in
ambient matrix space. Therefore a positive ambient radius preserving them
cannot be claimed in general.

The finite runtime instead uses explicit nonzero tolerances. Those declared
thresholds create locally certifiable **operational strata**.

---

## 2. Formation-sign surface

Let

\[
\lambda_0(K_+)
\]

be the lowest active formation eigenvalue.

The finite formation sign gate is

\[
\lambda_0<-\varepsilon_{\rm sign},
\]

with

\[
\varepsilon_{\rm sign}=\texttt{atol}.
\]

The transition surface is

\[
\boxed{
\lambda_0=-\varepsilon_{\rm sign}.
}
\]

The native sign clearance is

\[
s_F
=
-\varepsilon_{\rm sign}-\lambda_0.
\]

---

## 3. Formation-simplicity surface

Let

\[
g_F=\lambda_1-\lambda_0.
\]

The simple-ground-state gate is

\[
g_F>\varepsilon_{\rm simple},
\]

where

\[
\varepsilon_{\rm simple}
=
\texttt{simple\_gap\_tol}.
\]

The transition surface is

\[
\boxed{
\lambda_1-\lambda_0=\varepsilon_{\rm simple}.
}
\]

Because a Hermitian perturbation of operator norm \(\eta\) can move the two
lowest eigenvalues in opposite directions by at most \(\eta\) each, the native
operator-distance contribution is

\[
\frac{
g_F-\varepsilon_{\rm simple}
}{2}.
\]

Together with the sign clearance this yields the exact active formation margin
already used by the master runtime.

---

## 4. Persistent runtime-rank surface

Assume \(R\) is a normal contraction.

The runtime declares an eigenvalue persistent when

\[
\bigl||\lambda|-1\bigr|
\le
\varepsilon_P,
\]

with

\[
\varepsilon_P=\texttt{peripheral\_tol}.
\]

For a normal contraction, eigenvalue moduli and singular values coincide as
multisets. Therefore the runtime persistent rank is the number of singular
values satisfying

\[
\sigma_i(R)
\ge
\tau_P,
\qquad
\tau_P=1-\varepsilon_P.
\]

Let the persistent runtime rank be \(p\). Define

\[
d_P^-=
\sigma_p(R)-\tau_P,
\]

and, when a stable singular value exists,

\[
d_P^+=
\tau_P-\sigma_{p+1}(R).
\]

Then Weyl's singular-value inequality gives

\[
|\sigma_i(\widetilde R)-\sigma_i(R)|
\le
\|\widetilde R-R\|_2.
\]

Hence

\[
\boxed{
r_P
=
\min(d_P^-,d_P^+)
}
\]

is a certified native operator radius preserving the runtime persistent count,
provided the perturbed operator remains inside the normal-contraction category.

The two persistent-rank transition directions are therefore

\[
\boxed{
\sigma_p(R)=\tau_P
}
\]

for loss of persistence and

\[
\boxed{
\sigma_{p+1}(R)=\tau_P
}
\]

for acquisition of an additional persistent runtime mode.

For exact unit-circle persistence, \(\varepsilon_P=0\), the loss-side radius
collapses to zero whenever \(\sigma_p=1\). This reproduces the exact
non-openness result rather than hiding it.

---

## 5. Active runtime-rank surface

For the packet

\[
A
=
\begin{bmatrix}
\sqrt\alpha\,PC\\
\sqrt\beta\,PB
\end{bmatrix},
\]

the finite runtime defines the active threshold

\[
\boxed{
\tau_A(A)
=
\max\left(
\varepsilon_{\rm rank},
r_{\rm tol}\,\sigma_1(A)
\right),
}
\]

with

\[
\varepsilon_{\rm rank}=\texttt{rank\_tol},
\qquad
r_{\rm tol}=\texttt{rtol}.
\]

The runtime active rank is

\[
r
=
\#\{
i:\sigma_i(A)>\tau_A(A)
\}.
\]

Define

\[
d_A^-=
\sigma_r(A)-\tau_A(A),
\]

and, if a latent singular value exists,

\[
d_A^+=
\tau_A(A)-\sigma_{r+1}(A).
\]

Singular values are \(1\)-Lipschitz in operator norm, while

\[
\tau_A(A)
\]

is \(r_{\rm tol}\)-Lipschitz because \(\sigma_1\) is \(1\)-Lipschitz and the
maximum with a constant preserves that Lipschitz factor.

Therefore

\[
\boxed{
r_A
=
\frac{
\min(d_A^-,d_A^+)
}{
1+r_{\rm tol}
}
}
\]

is a sufficient native packet-operator radius preserving the declared active
runtime rank.

The two active-rank transition surfaces are

\[
\boxed{
\sigma_r(A)=\tau_A(A)
}
\]

and

\[
\boxed{
\sigma_{r+1}(A)=\tau_A(A).
}
\]

This is an operational runtime statement. It does not convert exact algebraic
rank into an open property.

---

## 6. Why the native margins are kept separate

The quantities

\[
|\mathfrak m_F(K_+)|,
\qquad
r_P(R),
\qquad
r_A(A)
\]

live in different operator coordinates.

Therefore the master does **not** take their raw numerical minimum and call that
a universal scalar bifurcation distance.

Instead it records a bifurcation ledger

\[
\boxed{
\mathcal L_{\rm bif}
=
(
m_{\rm sign},
m_{\rm simple},
r_P,
r_A
).
}
\]

Only after each native surface is transported back into the common parent
product norm can a single parent continuity radius be formed.

---

## 7. Parent-norm transport of the rank surfaces

The parent product norm is

\[
\|\Delta S\|_\oplus
=
\max\left\{
\|\Delta K\|_2,
\|\Delta Y\|_2,
\|\Delta R\|_2,
\|\Delta\rho\|_1
\right\}.
\]

The Parent-State Formation Robustness Theorem already supplies a monotone packet
bound

\[
\|\Delta A\|_2
\le
E_A(\delta)
\]

and an active formation bound

\[
\|\Delta K_+\|_2
\le
E_F(\delta).
\]

The operational runtime stratum is guaranteed to remain unchanged whenever

\[
\boxed{
\delta<r_P
}
\]

and

\[
\boxed{
E_A(\delta)<r_A.
}
\]

Formation status is simultaneously preserved whenever

\[
\boxed{
E_F(\delta)<|\mathfrak m_F|.
}
\]

Thus a full runtime-stratum parent certificate requires all three conditions:

\[
\boxed{
\delta<r_P,
\qquad
E_A(\delta)<r_A,
\qquad
E_F(\delta)<|\mathfrak m_F|.
}
\]

The resulting parent radius is stricter than the earlier conditional
fixed-stratum radius because runtime rank preservation is now a consequence of
the bound rather than an assumption.

---

## 8. Two parent radii must be distinguished

The architecture now records two different objects.

### Conditional formation radius

\[
r_{\rm parent}^{\rm cond}
\]

assumes the perturbation remains on the declared persistent-rank /
active-rank stratum and certifies formation-status preservation.

### Full runtime-stratum radius

\[
r_{\rm parent}^{\rm runtime}
\]

additionally guarantees that the finite runtime's own persistent- and
active-rank decisions remain unchanged.

Therefore

\[
\boxed{
r_{\rm parent}^{\rm runtime}
\le
r_{\rm parent}^{\rm cond}.
}
\]

The difference between them is not a contradiction. It measures the cost of
protecting the runtime stratum itself.

---

## 9. Current four-carrier native ledger

The complete current first-step audit contains

\[
\boxed{1409}
\]

states.

Every state has

\[
\boxed{
p=4
}
\]

persistent runtime modes and

\[
\boxed{
r=4
}
\]

active runtime modes.

For all

\[
\boxed{1409/1409}
\]

states, the nearest persistent-rank transition is **loss of persistence**.

For all

\[
\boxed{1409/1409}
\]

states, the nearest active-rank transition is **activation of a latent packet
mode**.

Median native persistent-runtime radii are approximately

\[
1.0\times10^{-8}
\]

in every carrier family.

Median active-runtime packet radii are approximately

\[
1.673\times10^{-10}
\]

for Sunspots,

\[
1.205\times10^{-10}
\]

for CO2,

\[
1.132\times10^{-10}
\]

for ENSO,

and

\[
2.059\times10^{-10}
\]

for the relational network.

The active packet surface is therefore much closer in its native coordinate
than the persistent runtime surface.

---

## 10. Current full runtime-stratum parent radii

Transporting all four surface families back into the parent product norm yields
positive strict runtime-stratum radii on

\[
\boxed{1409/1409}
\]

audited states.

Median values are approximately

\[
\boxed{
6.1454\times10^{-14}
}
\]

for Sunspots,

\[
\boxed{
3.2465\times10^{-14}
}
\]

for Mauna Loa CO2,

\[
\boxed{
2.9252\times10^{-14}
}
\]

for ENSO Pacific SST,

and

\[
\boxed{
1.8099\times10^{-14}
}
\]

for the relational network.

For all

\[
\boxed{1409/1409}
\]

current real-carrier states, the limiting parent-level runtime surface is the
**active runtime-rank surface**.

That does **not** imply that natural BFG formation is physically fragile at
\(10^{-14}\). The number is dominated by the declared finite numerical
rank threshold

\[
\texttt{rank\_tol}=10^{-10}
\]

and the conservative parent-to-packet transport bound.

It is therefore a runtime numerical-continuity scale, not an empirical physical
constant.

---

## 11. Structured controls

The master runs 43 deterministic admissible controls:

- all 34 relational network probes;
- three representative states from each of the three time-series carriers.

At half of the strict runtime-stratum radius,

\[
\boxed{43/43}
\]

controls preserve formation status and

\[
\boxed{43/43}
\]

retain the declared active runtime rank.

The larger conditional-radius controls also continue to pass the previously
declared formation-status and active spectral-shift checks.

These controls validate the implementation path; they are not substitutes for
the analytic perturbation bounds.

---

## 12. Unified finite-runtime bifurcation grammar

The current finite formation grammar can now be represented as

\[
\boxed{
S
\longrightarrow
(P,C,B,\alpha,\beta,A)
\longrightarrow
\left[
\begin{array}{c}
\text{persistent-rank surface}\\
\text{active-rank surface}\\
\text{formation-sign surface}\\
\text{formation-simplicity surface}
\end{array}
\right]
\longrightarrow
\text{admissible successor or }\bot.
}
\]

This is the first master ledger in which rank-changing and
formation-changing transitions are represented inside one declared runtime
geometry.

---

## 13. Claim boundary

The following are theorem-level finite-runtime statements under the stated
assumptions:

\[
\boxed{
\|\Delta R\|_2<r_P
\Rightarrow
\text{persistent runtime count unchanged}
}
\]

for normal contractions,

and

\[
\boxed{
\|\Delta A\|_2<r_A
\Rightarrow
\text{active runtime rank unchanged}.
}
\]

Combined with the existing parent transport bounds,

\[
\boxed{
\|\Delta S\|_\oplus
<
r_{\rm parent}^{\rm runtime}
\Rightarrow
\begin{cases}
\text{persistent runtime rank unchanged},\\
\text{active runtime rank unchanged},\\
\text{formation status unchanged},
\end{cases}
}
\]

inside the declared admissible positivity / normal-contraction category.

The following is explicitly not claimed:

\[
\boxed{
\text{exact algebraic rank or exact unit-circle persistence has a positive
ambient-matrix stability radius}.
}
\]

The earlier counterexamples prove that such a claim would be false.
