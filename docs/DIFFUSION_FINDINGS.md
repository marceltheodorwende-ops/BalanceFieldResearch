# Diffusion reference and identifiability check

## Outcome

72 fixed cases pass the [D1 protocol](DIFFUSION_PROTOCOL.md). The maximal
absolute error between the modal prediction and repeated heat-operator steps
is 6.25e-15. The largest numerical upper-bound excess is 5.70e-15; mass error
is 3.01e-14 and projected-load error is 4.92e-15. All are below 1e-10.
These results validate a known mathematical process, not empirical BFG physics.

Reproduce with `python -m bfg_lab.diffusion`. The generated
`results/diffusion.json` contains all 72 rows and the SHA-256 of the fixed
protocol. No parameters were fitted; this is not a held-out machine-learning
evaluation. The transport and the modal prediction both use eigendecomposition,
so their agreement is not an independent confirmation of the flux law.
A two-node analytic heat-kernel test separately checks the implementation.

## Independently specified dynamics

For symmetric weights w_ij >= 0, specify edge flux w_ij(x_j-x_i). Summing
edge contributions yields dx/dt=-Lx. Solving this linear equation gives
R=exp(-dt L). This is a derivation from the flux assumption, not from BFG.
On a connected graph, L has one zero mode proportional to the constant vector;
the other eigenvalues are positive. Hence the sampled process has one persistent
direction and decaying transient modes. Mass is conserved.

For initial disagreement z=x-mean(x), Laplacian eigenpairs (lambda_j,v_j), and
T=horizon*dt, the predicted ratio is

`sqrt(sum_{j>0} exp(-2*T*lambda_j) |v_j* z|^2) / ||z||`.

It is bounded above by `exp(-T*lambda_2)`. This bound is not generally an
equality. The baseline has full graph and state information; no claim of a
fair learned-predictor feature comparison is made.

## What the selected BFG readouts retain

Use the explicit observation choice Y=dt L+alpha I, alpha=0.2. With P the
constant-mode projector, P commutes with Y and equals the metric projector.
Consequently `P C x = mean(x)/(1+alpha) * 1` and
`P B x = alpha*mean(x)/(1+alpha) * 1` for the neutral responses C and B.
The projected loads are therefore

`lk = n mean(x)^2/(1+alpha)`, `lu = alpha^2 lk`.

The reciprocal weights are `[alpha^2,1]/(1+alpha^2)`. Moreover,

`gain^2 = 2 alpha^2 lk / ((1+alpha^2) x*[(1+alpha)I+dt L]x)`.

Thus these loads and weights discard the nonzero Laplacian spectrum; gain
additionally sees only the initial quadratic energy. A zero load offset would
remove the upper projected branch, showing that the observation choice matters.

## Concrete counterexample

Both graphs have four nodes, unit weights, initial x=e_0, and degree(0)=1.
Star center is vertex 1. Thus mean, norm and initial Laplacian energy coincide.
The table uses dt=0.2 and horizon=20 (T=4).

| Quantity | Path | Star |
| --- | ---: | ---: |
| Initial keep load | 0.2083333333 | 0.2083333333 |
| Initial upper load | 0.0083333333 | 0.0083333333 |
| Initial dual gain | 0.1069901231 | 0.1069901231 |
| Remaining disagreement ratio | 0.0724362567 | 0.0172681499 |
| Laplacian gap | 0.5857864376 | 1 |

The same selected readouts produce different targets. No deterministic function
of these readouts alone can exactly predict both outcomes. This is an
identifiability limitation for this mapping and these initial readouts, not
a refutation of all BFG representations, other measurements or time-series use.

## Self-check and next obligation

The implementation rejects sampling intervals where the absolute persistence
tolerance incorrectly merges transient modes into the persistent space.
Disconnected graphs and initially constant states are outside this target's
domain. The existing numerical and experimental modules remain unchanged.

The five-paper gap in upstream construction remains: the flux law and the load
offset are extra assumptions. This experiment supplies a reference process, not
a universal reclosure. Before any application claim, choose a real observation
budget and test a proposed additional measurement on independently reserved
systems. Simply adding the full spectrum recovers standard diffusion analysis
and would not by itself establish new BFG predictive content.
