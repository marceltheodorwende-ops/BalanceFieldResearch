# Real Relational Network Carrier

## Purpose

The fourth real-domain carrier is deliberately not another scalar time series.
It is the weighted Zachary karate-club interaction network: 34 observed members,
78 weighted undirected interaction ties.

The source dataset contains later club/fission labels. The BFG mapping does not
use those labels.

The carrier is currently **EXPLORATORY**. It is not a member of the sealed
confirmatory portfolio because no independent prospective network target/split
has yet been defined.

## Mapping

Each observed node defines one node-centered probe. With normalized weighted
graph Laplacian \(L_n\),

\[
D_i
=
\frac{\exp(-tL_n)e_i}
{\|\exp(-tL_n)e_i\|},
\]

with fixed \(t=1\).

The graph-aligned BFG state uses

\[
K
=
L_n+0.20I-1.45\,uu^\dagger,
\]

\[
Y
=
0.42L_n^2
+
0.18\,sI,
\]

where \(u=D_i\) and \(s\) is the fixed probe-complement stress.

The recursive operator uses the observed graph-Laplacian eigenbasis, four
persistent low modes, contraction \(0.76\) on the complement, and fixed phase
scale \(0.40\).

These are the same graph-aligned coefficients already used by the three real
time-series carriers. No network outcome was fitted.

## Current audit

All

\[
\boxed{34/34}
\]

node-probe mappings satisfy the BFG state contract.

The simple-negative formation gate accepts

\[
\boxed{13/34}
\]

first master transfers. The other 21 probes terminate at

`formation gate failed: no simple negative lowest eigenvalue`.

That result is retained. The formation drive is not increased merely to make all
nodes pass.

For the successful recursive transitions, the multidimensional small-load
theorem is satisfied in

\[
\boxed{41/41}
\]

certificates.

At depth 1 none of the successful network probes is yet inside the strict local
condition \(C\|Y\|<1\). At depth 2 and depth 3 all successful probes are inside
it.

## Permutation-equivariance control

The node labels were deterministically permuted and the entire graph was
reconstructed under that permutation.

Maximum residuals were approximately:

- \(D\): \(2.32\times10^{-16}\)
- \(K\): \(6.69\times10^{-16}\)
- \(Y\): \(2.08\times10^{-15}\)
- \(R_C\): \(1.53\times10^{-14}\)

Therefore the carrier mapping is permutation equivariant to numerical precision.

## Four-domain result

Adding the relational network changes the interpretation of the earlier
three-domain corridors.

The q10-q90 transformation corridors shared by Sunspots, CO2 and ENSO do **not**
extend to the network carrier for:

- reciprocal weight \(\alpha\),
- spectral-normalized formation depth,
- formation gap,
- neutral-load density ratio,
- normalized \(K\)-RMS transport.

Likewise, none of the four tested formation-depth normalizations has a common
q10-q90 intersection across all four domains.

Therefore those earlier overlaps are now classified as

\[
\boxed{\text{time-series-family shared corridors}}
\]

rather than universal cross-structure invariants.

The small-load theorem is different: it is an operator theorem of the master
runtime, and its explicit inequalities continue to hold on every successful
network transition audited here.

## Current interpretation

The fourth carrier therefore provides both a negative and a positive result.

Negative:

\[
\text{three time-series corridors}
\not\Rightarrow
\text{four-domain universal corridor}.
\]

Positive:

\[
\text{successful relational master transitions}
\Rightarrow
\text{same small-load theorem certificate}.
\]

This is a stronger separation between carrier-family empirical regularities and
master-runtime mathematical structure.


## Exact explanation of the 13/21 formation split

The split is no longer merely descriptive.

All 34 parent formation operators possess a negative ground eigenvalue, and
all 34 active formation gaps exceed the simplicity tolerance.

Let \(u_-\) be the parent ground mode and define

\[
\chi_-=
\frac{\langle Au_-,(K\oplus K)Au_-\rangle}
{\langle Au_-,Au_-\rangle}.
\]

For the 13 formation-success probes,

\[
-0.55412\le\chi_-\le-0.01602.
\]

For the 21 formation-terminal probes,

\[
0.01983\le\chi_-\le0.13599.
\]

The exact generalized active-spectrum criterion agrees with the runtime on
`34/34` probes.

Thus the current relational split is a **negative-mode transport effect**:
the parent negative direction exists everywhere, but the persistent neutral
packet preserves it as an active negative direction only for 13 probes.


## Formation robustness margin

Each of the 34 relational probes now carries an exact signed distance to the
active formation bifurcation surface.

Eligible probe margins range from

\[
+0.0166927689
\]

to approximately

\[
+0.378602068.
\]

Terminal probe margins range from approximately

\[
-0.134876951
\]

to

\[
-0.0183398303.
\]

Thus the closest successful and terminal probes lie on opposite sides of
zero with finite separation.

Of the 34 probes, 31 are limited by the sign surface and 3 by the simplicity
surface. This makes the relational carrier a useful concrete realization of
the two distinct formation bifurcation mechanisms.


## Parent-state formation robustness

The relational carrier now also has a conditional radius in the parent
product norm

\[
\|\Delta S\|_\oplus
=
\max\{
\|\Delta K\|_2,\|\Delta Y\|_2,
\|\Delta R\|_2,\|\Delta\rho\|_1
\}.
\]

All `34/34` relational probes receive a positive certificate on the fixed
persistent-rank / fixed-active-rank admissible stratum.

Network parent-radius statistics:

- median: `1.40955e-7`
- q10: `1.05032e-7`
- q90: `1.17932e-6`
- minimum: `5.19460e-8`
- maximum: `4.88643e-6`

All `34/34` structured network controls inside half of the certified radius
preserve formation status, retain active rank, and satisfy the predicted
active spectral-shift bound.

The radius is deliberately conditional: exact persistent dimension and
exact packet rank are not open under arbitrary ambient perturbations.


## Relational stratum-transition geometry

All 34 node probes have:

\[
p_{\rm runtime}=4,
\qquad
r_{\rm active}=4.
\]

Their median native persistent-runtime radius is approximately

\[
1.0\times10^{-8},
\]

while the median native active-runtime packet radius is approximately

\[
2.059\times10^{-10}.
\]

The stricter parent-level runtime-stratum radius has median

\[
1.8099\times10^{-14},
\]

with all 34 relational states limited by the active runtime-rank surface.

This very small scale is controlled by the declared numerical rank threshold
and is not interpreted as a physical network critical constant.
