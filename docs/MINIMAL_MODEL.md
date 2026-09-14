# Experimental closure M1

For a separate rule that preserves multiple directions, see [M2](MULTIMODE_MODEL.md).
M1 remains the default Python API behavior; the module CLI now prints both models.

This is a fully specified finite-dimensional toy recursion, not a derivation or
implementation of the universal BFG map. It reuses the candidate formation code
and proposed peripheral persistence interpretation. The five source documents
remain unchanged. No microscopic Gram construction or empirical claim follows.

## State and extra assumptions

State: `(Y, d, R, D, C, N)`, with PSD load Y, nonzero state vector d, normal
power-bounded R, and PSD capacities D, C, N. Here C denotes a capacity; it is
distinct from the neutral response `(I+Y)^-1` used inside the split.
All variables are dimensionless. Parameters are retention `a in [0,1]` and
stable contraction `0 <= rho < 1-TOL`.

1. Run the existing split, capacity compression and formation gate.
   A rejected candidate ends the run with the reported reasons.
2. In orthonormal coordinates of the transported support, take packet z and
   define `d_next = z / ||z||`. Normalization is an added rule that discards
   amplitude; no conservation of the original metric norm is claimed.
3. For compressed capacities, choose `D_next = a D_hat`, `C_next = C_hat`,
   `N_next = N_hat`. Retention is an imposed depletion law.
4. Choose `Y_next = (C_next + N_next)/(1 + ||D_next||_2)` and metric
   `G_next = I + Y_next`. This is an added PSD Gram closure. Roundoff-sized
   negative load eigenvalues are clamped to zero.
5. Choose `R_next = rho I + (1-rho) d_next d_next*`.
   This deliberately gives one persistent direction and contracting orthogonal
   directions. It is an imposed transport law, not emergent persistence.

The next carrier is the compressed support space. These choices define every
input of the next iteration. They preserve PSD capacities and load, positive
definite metric, unit Euclidean state norm and normal power-bounded transport
in exact arithmetic. Dimension cannot increase. Rank-one transport has one
persistent direction, but its two split branches can jointly span up to two
directions when the load does not preserve that space. Only the diagonal
reference example below reduces to one dimension. This model therefore cannot
demonstrate growing complexity, a unique canonical closure or universal dynamics.
Invalid inputs raise errors; hitting the step limit does not prove infinite survival.

## Analytic reference and experiments

Run `python -m bfg_lab.minimal` from the repository root. It emits JSON histories.
The seed uses Y=I, d=(1,1), R=diag(1,0.5), D=3I and C=N=I.
The first compression has dimension one. At candidate step k the scalar
formation value is `2 - 3 a^k`.

- `a=1`: the gate remains admitted through the chosen 12-step budget.
- `a=0.8`: values are -1, -0.4 and +0.08, so two transitions occur and the
  third candidate is rejected. This behavior is built into the depletion law.
- Relative D and state perturbations of +/-1e-6 leave that stop index unchanged.

All gate decisions retain the lab's fixed absolute TOL=1e-10. This experiment
does not establish tolerance independence: near zero eigenvalues, nearly
degenerate minima or nearly peripheral modes remain sensitive. A separate
scale-aware numerical policy and nontrivial higher-rank closure are future work.
