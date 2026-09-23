# BFG Parent-State Formation Robustness Theorem

## 1. Purpose

The active formation margin gives an exact distance in the successor formation
operator \(K_+\). This document transports that margin backward to the parent
state

\[
S=(\rho,K,Y,R).
\]

A crucial limitation appears immediately: there is **no positive unrestricted
ambient-matrix radius** that can preserve the exact BFG persistence/active-rank
structure.

Two elementary counterexamples show why.

For active rank,

\[
A_0=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
A_\varepsilon=
\begin{pmatrix}
1&0\\
0&\varepsilon
\end{pmatrix},
\]

satisfy

\[
\|A_\varepsilon-A_0\|_2=\varepsilon
\]

for arbitrarily small \(\varepsilon>0\), but

\[
\operatorname{rank}A_0=1,
\qquad
\operatorname{rank}A_\varepsilon=2.
\]

For exact persistence,

\[
R_0=\operatorname{diag}(1,1/2),
\qquad
R_\varepsilon=\operatorname{diag}(1-\varepsilon,1/2)
\]

are arbitrarily close, but the exact unit-circle persistent dimension drops from
one to zero.

Therefore the correct theorem is a **stratified admissible perturbation theorem**:
the parent radius is certified inside a fixed persistent-rank / fixed-active-rank
BFG stratum.

---

## 2. Parent product norm

For an admissible perturbation

\[
\widetilde S
=
(\widetilde\rho,\widetilde K,\widetilde Y,\widetilde R),
\]

define

\[
\Delta K=\widetilde K-K,
\quad
\Delta Y=\widetilde Y-Y,
\quad
\Delta R=\widetilde R-R,
\quad
\Delta\rho=\widetilde\rho-\rho,
\]

and the componentwise product norm

\[
\boxed{
\|\Delta S\|_\oplus
=
\max\left\{
\|\Delta K\|_2,\,
\|\Delta Y\|_2,\,
\|\Delta R\|_2,\,
\|\Delta\rho\|_1
\right\}.
}
\]

The theorem assumes

\[
\|\Delta S\|_\oplus\le\delta.
\]

The admissible perturbation class additionally requires:

1. \(Y,\widetilde Y\succ0\);
2. \(\rho,\widetilde\rho\) are nonzero rank-one PSD;
3. \(R,\widetilde R\) are normal contractions;
4. the peripheral dimension is unchanged;
5. the packet active rank is unchanged;
6. the persistent and active singular gaps remain open.

---

## 3. Persistent-subspace transport

For a normal contraction define

\[
H_R=I-R^\dagger R.
\]

Its kernel is the unit-singular persistent sector. Let

\[
g_R
=
\lambda_{\min}^{+}(H_R)
\]

be the first positive eigenvalue after the persistent kernel.

For

\[
\|\Delta R\|_2\le\delta,
\]

one has

\[
\|\widetilde H_R-H_R\|_2
\le
2\|R\|_2\delta+\delta^2
=:h_R(\delta).
\]

If

\[
h_R(\delta)<\frac{g_R}{2},
\]

the persistent cluster remains spectrally separated. A conservative
Davis--Kahan estimate gives

\[
\boxed{
q_R
:=
\|\widetilde Q-Q\|_2
\le
\frac{2h_R(\delta)}{g_R},
}
\]

where \(Q,\widetilde Q\) are the Euclidean persistent projectors.

---

## 4. Weighted persistent projector

Let

\[
G=I+Y,
\qquad
\widetilde G=I+\widetilde Y,
\]

and let \(P,\widetilde P\) be the corresponding \(G\)- and
\(\widetilde G\)-orthogonal projectors onto the persistent subspaces.

Write

\[
g=\|G\|_2,
\qquad
\widetilde g\le g+\delta.
\]

The fixed-subspace metric perturbation and the persistent-subspace rotation give
the conservative bound

\[
\boxed{
\|\widetilde P-P\|_2
\le
\delta(g+1)
+
2\sqrt2\,
\widetilde g(1+\widetilde g)\,q_R
=:d_P.
}
\]

This step is where the \(R\)- and \(Y\)-perturbations first couple.

---

## 5. Neutral resolvent transport

The neutral pair is

\[
C=(I+Y)^{-1},
\qquad
B=I-C.
\]

Because \(Y,\widetilde Y\succeq0\),

\[
\|C\|_2,\|\widetilde C\|_2\le1.
\]

The resolvent identity gives

\[
\widetilde C-C
=
-\widetilde C\,\Delta Y\,C,
\]

hence

\[
\boxed{
\|\widetilde C-C\|_2\le\delta.
}
\]

Since \(B=I-C\),

\[
\boxed{
\|\widetilde B-B\|_2\le\delta.
}
\]

Let

\[
p=\|P\|_2,
\qquad
\widetilde p\le p+d_P.
\]

For either retained channel \(X=PC\) or \(PB\),

\[
\boxed{
\|\widetilde X-X\|_2
\le
d_P+p\delta
=:d_X.
}
\]

---

## 6. Reciprocal-load transport

Let

\[
\mu=\operatorname{tr}\rho,
\qquad
\widetilde\mu\le\mu+\delta,
\]

and

\[
\lambda_{\rm keep}
=
\operatorname{tr}
\left(
G X_{\rm keep}\rho X_{\rm keep}^\dagger
\right),
\]

\[
\lambda_{\rm up}
=
\operatorname{tr}
\left(
G X_{\rm up}\rho X_{\rm up}^\dagger
\right).
\]

A common sufficient load bound is

\[
\boxed{
L(\delta)
=
\delta\,\widetilde p^2\widetilde\mu
+
g\,\widetilde\mu(\widetilde p+p)d_X
+
g\,p^2\delta.
}
\]

Thus

\[
|\Delta\lambda_{\rm keep}|
\le L(\delta),
\qquad
|\Delta\lambda_{\rm up}|
\le L(\delta).
\]

Let

\[
S_\lambda
=
\lambda_{\rm keep}+\lambda_{\rm up},
\qquad
\alpha
=
\frac{\lambda_{\rm up}}{S_\lambda},
\qquad
\beta=1-\alpha.
\]

If

\[
L(\delta)
<
\min(\lambda_{\rm keep},\lambda_{\rm up})
\]

and

\[
2L(\delta)<S_\lambda,
\]

then

\[
\boxed{
|\widetilde\alpha-\alpha|
\le
\frac{L(\delta)}
{S_\lambda-2L(\delta)}
=:d_\alpha.
}
\]

The same bound holds for \(\beta\).

If

\[
d_\alpha<\min(\alpha,\beta),
\]

then the square-root weights obey

\[
|\sqrt{\widetilde\alpha}-\sqrt\alpha|
\le
\frac{d_\alpha}
{\sqrt\alpha+\sqrt{\alpha-d_\alpha}},
\]

and analogously for \(\beta\).

---

## 7. Packet perturbation

The master packet is

\[
A=
\begin{bmatrix}
\sqrt\alpha\,PC\\
\sqrt\beta\,PB
\end{bmatrix}.
\]

Let

\[
s_\alpha
=
\frac{d_\alpha}
{\sqrt\alpha+\sqrt{\alpha-d_\alpha}},
\]

\[
s_\beta
=
\frac{d_\alpha}
{\sqrt\beta+\sqrt{\beta-d_\alpha}}.
\]

Then

\[
E_{\rm keep}
=
s_\alpha\,\widetilde p
+
\sqrt\alpha\,d_X,
\]

\[
E_{\rm up}
=
s_\beta\,\widetilde p
+
\sqrt\beta\,d_X,
\]

and therefore

\[
\boxed{
\|\widetilde A-A\|_2
\le
E_A
:=
\sqrt{
E_{\rm keep}^2+E_{\rm up}^2
}.
}
\]

---

## 8. Active-subspace transport

Let

\[
\sigma_r(A)>0
\]

be the smallest singular value on the fixed active rank-\(r\) stratum.

If

\[
E_A<\frac{\sigma_r(A)}{2},
\]

a Wedin-type subspace bound gives

\[
\boxed{
\sin\Theta_U
\le
\frac{2E_A}{\sigma_r(A)}.
}
\]

There exists an aligned pair of active orthonormal bases \(U,\widetilde U\)
satisfying

\[
\|\widetilde U-UQ\|_2
\le
\sqrt2\,\sin\Theta_U
\]

for a suitable unitary \(Q\).

---

## 9. Parent-to-active formation bound

Let

\[
H=K\oplus K,
\qquad
K_+=U^\dagger H U.
\]

For the perturbed parent,

\[
\widetilde K_+
=
\widetilde U^\dagger
(\widetilde K\oplus\widetilde K)
\widetilde U.
\]

After unitary alignment of the active coordinates,

\[
\|\Delta K_+\|_2
\le
\|\Delta K\|_2
+
2\|K\|_2
\|\widetilde U-UQ\|_2.
\]

Hence

\[
\boxed{
\|\Delta K_+\|_2
\le
\delta
+
2\sqrt2\,\|K\|_2\sin\Theta_U
=:E_F(\delta).
}
\]

Let

\[
m_F
=
|\mathfrak m_F(K_+)|
\]

be the exact active formation margin from the Formation Robustness Theorem.

If

\[
\boxed{
E_F(\delta)<m_F,
}
\]

then the formation status of the perturbed parent is unchanged.

---

## 10. Conditional Parent-State Formation Theorem

### Theorem

Let \(S=(\rho,K,Y,R)\) satisfy the finite master assumptions and lie in a stratum
with fixed persistent rank and fixed active packet rank.

Assume the perturbation
\(\widetilde S\) remains in the same admissible stratum and satisfies

\[
\|\widetilde S-S\|_\oplus\le\delta.
\]

If all intermediate positivity, persistent-gap, load, reciprocal-weight and
active-singular-gap conditions above hold, and

\[
E_F(\delta)<m_F,
\]

then

\[
\boxed{
\operatorname{FormationStatus}(\widetilde S)
=
\operatorname{FormationStatus}(S).
}
\]

The largest \(\delta\) certified by these sufficient inequalities is a
**conditional parent-state formation radius**.

The bound is intentionally conservative; it is not claimed to be the exact
parent-state distance to the bifurcation surface.

---

## 11. Why the stratum restriction is necessary

The restriction is not cosmetic.

Exact unit-circle persistence and exact matrix rank are not open properties in
ambient matrix space. Therefore no theorem can assign a positive unconstrained
ambient radius around a generic boundary-sensitive state while simultaneously
guaranteeing unchanged persistent dimension and active rank.

The BFG-admissible statement is instead:

\[
\boxed{
\text{within a fixed admissible recursive stratum,}
\quad
\|\Delta S\|_\oplus<r_{\rm parent}
\Rightarrow
\text{formation status is preserved}.
}
\]

This is the correct continuity corridor for the finite runtime.

---

## 12. Current real-carrier audit

The certificate was evaluated on all current first-step states:

\[
\boxed{1409/1409}
\]

receive a positive conditional parent radius.

Median certified radii are approximately:

\[
3.7351\times10^{-6}
\]

for annual Sunspots,

\[
2.4781\times10^{-6}
\]

for Mauna Loa CO2,

\[
2.0443\times10^{-6}
\]

for ENSO Pacific SST,

and

\[
1.4095\times10^{-7}
\]

for the relational network.

For the network:

\[
r_{\rm parent}^{\min}
\approx
5.19\times10^{-8},
\]

\[
r_{\rm parent}^{\max}
\approx
4.89\times10^{-6}.
\]

The 13 eligible network probes have median radius approximately

\[
7.05\times10^{-7},
\]

while the 21 terminal probes have median radius approximately

\[
1.41\times10^{-7}.
\]

A set of 43 deterministic structured admissible controls was also run: all
34 network probes plus three representative states from each time-series
carrier.

For all

\[
\boxed{43/43}
\]

controls:

- the perturbation stayed inside the certified product-norm radius;
- persistent and active rank remained on the declared stratum;
- formation status was preserved;
- the observed active spectral shift stayed below the theorem bound.

These controls are regression evidence for the implementation, not the source
of the theorem.

---

## 13. Claim boundary

The following is now supported as a conditional mathematical theorem:

\[
\boxed{
\text{fixed admissible rank stratum}
+
\text{explicit gap/load inequalities}
+
E_F(\delta)<m_F
\Rightarrow
\text{formation-status preservation}.
}
\]

The following is explicitly **not** claimed:

\[
\boxed{
\text{one positive unconstrained ambient radius for arbitrary}
\ (\Delta K,\Delta Y,\Delta R,\Delta\rho).
}
\]

The counterexamples above show why such an unrestricted statement would be
false.

The next natural extension is to characterize the **stratum-transition
geometry** itself: when and how persistent rank or active packet rank changes,
and whether those rank-changing surfaces can be integrated into the same
bifurcation ledger as the sign and simplicity surfaces.


## 14. Operational runtime-stratum refinement

The conditional radius above assumes a fixed persistent-rank / active-rank
stratum. The runtime now also carries a stricter certificate that protects
those **numerical runtime rank decisions themselves**.

For normal-contraction \(R\), the persistent runtime threshold is

\[
\tau_P=1-\varepsilon_P.
\]

With persistent runtime rank \(p\),

\[
r_P
=
\min\{
\sigma_p(R)-\tau_P,\,
\tau_P-\sigma_{p+1}(R)
\}.
\]

Thus

\[
\|\Delta R\|_2<r_P
\]

preserves the declared persistent runtime count.

For the packet \(A\), the active runtime threshold is

\[
\tau_A(A)
=
\max(
\varepsilon_{\rm rank},
r_{\rm tol}\sigma_1(A)
).
\]

If \(r\) is the current active runtime rank, then the sufficient packet
radius

\[
r_A
=
\frac{
\min\{
\sigma_r(A)-\tau_A,\,
\tau_A-\sigma_{r+1}(A)
\}
}{
1+r_{\rm tol}
}
\]

preserves that rank decision.

The stricter parent radius is therefore defined by the simultaneous
conditions

\[
\boxed{
\delta<r_P,
\qquad
E_A(\delta)<r_A,
\qquad
E_F(\delta)<|\mathfrak m_F|.
}
\]

On this stricter corridor, equal runtime persistent rank and equal runtime
active rank are consequences of the bound rather than assumptions.

Across the current 1,409 first-step states, every state receives a positive
strict runtime-stratum parent radius. The limiting surface is the active
runtime-rank surface in all 1,409 current real-carrier states.

The resulting medians are approximately:

\[
6.1454\times10^{-14}
\]

for annual Sunspots,

\[
3.2465\times10^{-14}
\]

for Mauna Loa CO2,

\[
2.9252\times10^{-14}
\]

for ENSO Pacific SST, and

\[
1.8099\times10^{-14}
\]

for the relational network.

These values are runtime numerical continuity scales dominated by the
declared active-rank threshold. They are not interpreted as physical
critical constants.
