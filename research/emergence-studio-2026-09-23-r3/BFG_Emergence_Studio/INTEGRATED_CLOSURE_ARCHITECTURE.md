# Integrated Closure Architecture

The BFG Emergence Studio exposes one coherent closure stack.

## Core finite runtime

The reduced state is

\[
S=(\rho,K,Y,R)
\]

with rank-one positive \(\rho\), Hermitian \(K\), positive-definite \(Y\), and
power-bounded \(R\).

The active finite update uses neutral resolution, graph-metric persistence,
reciprocal dual loads, polar support transport, intrinsic Gram rebuilding,
simple-negative-mode formation, and unitary successor recursion.

Successful successors satisfy

\[
R_+=\exp(i\tau K_+),
\]

hence are power bounded by construction.

Failure decisions map to the absorbing terminal object \(\bot\).

## Stability layer

Finite power boundedness is audited through the closed-unit-disk spectrum plus
semisimple unit-circle criterion. Exact rational nonnormal certificates are
available for supplied invariant splittings and Lyapunov/isometry metrics.

Small perturbation norm alone is not considered a stability guarantee. The
perturbed operator must remain inside the admissible power-bounded class, while
the active successor law is unitary by construction.

## Reconstruction layer

The active finite profile uses

\[
Y_+=A^\dagger A,\qquad
B_{C,+}=Y_+^{1/2},\qquad
W_{N,+}=I,\qquad
L_{C,+}=I.
\]

Retained external channels are tracked through the exact tangent/external Gram
decomposition. Conditional G1 and finite connection-model machinery remain
available as specialized extensions.

## Runtime dispatch

Generic `simulate(...)` calls without an explicit carrier use the finite master
runtime. Explicit carrier adapters invoke the application/research lane.

This keeps the mathematical core and carrier-specific transition laws separate
without maintaining two competing generic runtimes.

## Bounded infinite-dimensional entry

The declared bounded entry class requires bounded self-adjoint \(K\), uniformly
positive bounded \(Y\), rank-one \(\rho\), power-bounded \(R\), isolated finite
peripheral Riesz range and a strictly stable complement. That class reduces to
the finite runtime after the admissible reduction step.

Arbitrary unbounded/infinite-rank transport is outside the executable category.

## Empirical separation

Mathematical/runtime closure and empirical natural realization remain distinct.
External carriers are evaluated through the sealed validation portfolio.


## Real-carrier master transport

Real-domain carrier states enter the finite master grammar through the common
adapter

\[
D\mapsto
\rho=\frac{|D\rangle\langle D|}{\langle D|D\rangle},
\]

while their frozen `K`, `Y` and `R_C` are transported into the reduced state.

After that adapter, Sunspots, CO2 and ENSO use the exact same finite master
successor law.

The current development/calibration audit processes `1,375/1,375` states
without an uncaught exception and yields `1,375/1,375` successful first
master transfers.

The architecture therefore distinguishes three layers:

\[
\text{carrier measurement map}
\to
\text{common BFG reduced state}
\to
\text{common master transformation}.
\]

Carrier-specific forecasting remains outside this common successor layer.

Repeated floating-point reclosure is monitored separately. `bottom` remains
an admissible terminal object, and numerical resolution boundaries are
committed to `bottom` rather than escaping the total runtime as exceptions.


## Recursive load-contraction regime

The reduced finite map has an exactly tractable scalar sector:

\[
K=-1,\quad \rho=1,\quad Y=y>0
\]

gives

\[
y_+
=
\frac{2y^2}{(1+y)^2(1+y^2)}.
\]

Hence

\[
y_+\sim2y^2
\qquad (y\to0^+).
\]

The real-carrier master trajectories empirically enter the corresponding
near-quadratic regime after their first closure step, with pooled
depth-specific exponents near 1.95 and 1.98 at depths 2 and 3.

Therefore the architecture distinguishes:

\[
\text{structural superlinear load contraction}
\]

from

\[
\text{finite numerical commitment to }\bot.
\]

Internal threshold crossings are transported to absorbing `bottom` so the
runtime remains total, but the audit labels them as numerical admissibility
boundaries rather than exact zero-load theorems.

Formation-depth coordinates are also treated as a family of declared
dimensionless observables. The original spectral normalization remains
non-overlapping across the three current real domains; RMS, gap, and
mean-absolute-eigenvalue normalizations presently share development
corridors.


## Quadratic contraction theorem layer

The neutral interface and reciprocal load geometry imply

\[
\lambda_{\rm up}
\le
\mu\|Y\|_2^2,
\qquad
\mu=\operatorname{tr}\rho.
\]

If

\[
\lambda_{\rm keep}\ge\eta>0,
\]

then

\[
\alpha
\le
\frac{\mu}{\eta}\|Y\|_2^2.
\]

With \(p=\|P\|_2\), the adopted packet and Gram successor satisfy

\[
\boxed{
\|Y_+\|_2
\le
p^2
\left(
1+\frac{\mu}{\eta}
\right)
\|Y\|_2^2.
}
\]

Thus the architecture now has the chain

\[
\text{neutral mediation}
\to
\text{quadratic small-load contraction}
\to
\text{conditional double-exponential corridor bound}
\to
\text{finite numerical }\bot\text{ crossing}.
\]

The final threshold crossing remains an implementation/admissibility statement,
not an exact physical extinction statement.



## Relational carrier extension

A real weighted interaction graph now enters the architecture through the
same carrier/state boundary:

\[
\text{weighted graph}
\to
\text{node-centered diffusion probe}
\to
(D,K,Y,R_C)
\to
\text{finite master runtime}.
\]

The mapping is permutation equivariant to numerical precision.

Only `13/34` node probes satisfy the first simple-negative formation gate.
The remaining probes map to the terminal object rather than triggering
network-specific retuning.

Successful network trajectories still satisfy the same quadratic
small-load theorem (`41/41` current certificates).

Architecturally this creates a useful separation:

\[
\text{formation eligibility}
\quad\text{is carrier/state dependent,}
\]

while

\[
\text{small-load successor bound}
\quad\text{is a master-runtime theorem once the step is admissible.}
\]

The earlier three time-series transformation corridors are not treated as
universal after failing the four-domain relational extension.


## Formation eligibility transport layer

Formation now has an explicit pre-commit transport certificate.

Starting from

\[
A=
\begin{bmatrix}
\sqrt{\alpha}PC\\
\sqrt{\beta}PB
\end{bmatrix},
\qquad
H=K\oplus K,
\]

take

\[
A=U_r\Sigma_rV_r^\dagger.
\]

The active formation operator is

\[
K_+=U_r^\dagger H U_r.
\]

Equivalently, on the active right support its spectrum is the generalized
spectrum of

\[
\left(
V_r^\dagger A^\dagger H A V_r,\,
V_r^\dagger A^\dagger A V_r
\right).
\]

The formation branch can therefore be viewed as

\[
\boxed{
(K,Y,R,\rho)
\to
A
\to
\text{active generalized spectrum}
\to
\text{formation or }\bot.
}
\]

This explains the relational carrier without adding a network-specific
response law: parent negativity exists for every probe, but only 13 probes
transport that negative geometry into the active packet.


## Formation bifurcation geometry

The active formation layer now transports not only a yes/no gate but an
exact signed distance to the gate boundary.

With

\[
s=-\varepsilon_{\rm sign}-\lambda_0,
\qquad
g=(\lambda_1-\lambda_0)-\varepsilon_{\rm simple},
\]

the eligible-side distance is

\[
d_+=\min(s,g/2),
\]

while the terminal-side infimum is

\[
d_-=\max((-s)_+,(-g)_+/2).
\]

The architecture can therefore be read as

\[
(K,Y,R,\rho)
\to A
\to K_+
\to
\bigl(\text{eligibility},\mathfrak m_F\bigr)
\to
\text{successor or }\bot.
\]

The next unresolved transport layer is to push this active-space margin
backward through the state-to-packet map and obtain a certified radius in
the parent state geometry.


## Parent-to-active robustness transport

The formation branch now contains a perturbation transport layer:

\[
(\Delta K,\Delta Y,\Delta R,\Delta\rho)
\to
\Delta P
\to
\Delta A
\to
\Delta U_r
\to
\Delta K_+.
\]

On a fixed persistent-rank / fixed-active-rank admissible stratum,

\[
\|\Delta R\|
\]

is converted to a persistent-subspace rotation through the positive gap of

\[
I-R^\dagger R.
\]

The neutral resolvent gives

\[
\|\Delta C\|_2\le\|\Delta Y\|_2,
\qquad
\Delta B=-\Delta C.
\]

Reciprocal-load perturbations control the packet \(A\), Wedin controls the
active subspace \(U_r\), and compression stability yields an explicit
\(E_F(\delta)\) for the active formation operator.

The commit condition is

\[
E_F(\delta)<|\mathfrak m_F(K_+)|.
\]

The architecture therefore now distinguishes continuity **within** a
recursive stratum from **stratum transitions** where persistent or active
rank changes.


## Unified bifurcation ledger

Formation commitment now carries the ledger

\[
\mathcal L_{\rm bif}
=
(
m_{\rm sign},
m_{\rm simple},
r_P,
r_A
).
\]

The first two coordinates belong to the active formation operator \(K_+\).
The persistent coordinate belongs to \(R\), and the active-rank coordinate
belongs to the packet \(A\).

They are not naively minimized in native coordinates.

Instead, the parent transport maps them into the common product norm:

\[
\delta<r_P,
\]

\[
E_A(\delta)<r_A,
\]

\[
E_F(\delta)<|\mathfrak m_F|.
\]

The resulting strict runtime-stratum radius guarantees simultaneously:

\[
\boxed{
\text{persistent runtime rank unchanged},
}
\]

\[
\boxed{
\text{active runtime rank unchanged},
}
\]

and

\[
\boxed{
\text{formation status unchanged}.
}
\]

Exact algebraic rank remains outside this positive-radius claim.
