# Conservative reference-family decision procedure

This implements the next mathematical repair as a separate API; the historical
single-reference detector and its negative results remain unchanged. The new
procedure covers every fixed symmetric nonnegative edge-weight matrix in a
declared box. It uses exact rational arithmetic and an analytic series remainder.
It is not a complete feasibility solver or a physical fault classifier.

## Run

```sh
python -m bfg_lab.certified --input examples/certified_family.json
```

Output: `results/certified.json`. The supplied example returns
`compatible_witness`. API: `assess_family(weight_lower, weight_upper, initial,
samples, times, sensors, initial_error=0, sensor_error=0, terms=24)`.
Times start at zero and increase. Use decimal strings for exact interpretation;
JSON numeric decimals are also parsed as strings by the CLI. Python float
arguments are interpreted via their decimal `str`, not as the exact binary
floating-point value. Input measurement and model uncertainty must cover any
upstream conversion error. All weights have units reciprocal to supplied time.

The nominal initial state is a full-network calibration with uniform absolute
componentwise error `initial_error`. Ongoing observations may cover a subset
of distinct nodes. `sensor_error` bounds each supplied reading. The true graph
and initial state must be fixed over the entire history; no unknown forcing.
The declared family must be independently justified, not chosen to fit outcomes.

## Three outcomes

| Status | Certificate and meaning |
| --- | --- |
| compatible_witness | Midpoint weights and nominal initial state are one common witness; rigorous trajectory enclosures lie inside every observation-error interval. |
| healthy_family_excluded | An observation is strictly outside a rigorous outer enclosure of ALL declared healthy trajectories. Exact rational bounds are included. |
| unresolved | Neither certificate is established: for example outer overlap without a verified witness, or insufficient series budget. |

No claim is made that `unresolved` histories are compatible. Only one witness
candidate is attempted. Compatible families whose feasible points differ from
that candidate may remain unresolved. Pointwise outer overlap never becomes a
common-witness certificate. Malformed input raises ValueError; caller software
must not turn exceptions or resource failures into fault alarms.

## Family enclosure in the infinity norm

Let A0 be the midpoint edge weights, radii b_ij=(upper-lower)/2, and
`eta=2 max_i sum_j b_ij`. Every admissible L obeys ||L-L0||_infinity<=eta.
Nonnegative undirected graph heat operators are stochastic and contractions
in the infinity norm. Duhamel's identity therefore gives
`||exp(-tL)-exp(-tL0)||_infinity <= t eta`.

Both operators preserve constants. Center xhat at the midpoint of its extrema,
giving contrast c=(max(xhat)-min(xhat))/2. Each true component at time t is
within `initial_error + t eta c` of the nominal heat trajectory. Add sensor
error for a healthy observation envelope. This is the infinity-norm counterpart
of the audited 2-norm bound, avoiding square-root rounding. Disconnected graphs
and zero edge weights are allowed. The envelope is conservative and widens in
time, so sensitive detection is not guaranteed.

## Certified nominal trajectory

Choose q=max degree(A0) and B=I-L0/q. For q>0, B is a nonnegative stochastic
matrix and `exp(-tL0)=exp(-u) sum_k u^k B^k/k!`, u=qt.
Subtract min(xhat) from the state so every component lies in [0,W]. For N terms
let s=sum_(k=0..N) u^k/k! and z_N=sum_(k=0..N) u^k B^k z/k!.
If u<N+2, the remaining scalar series is bounded by
`T=(u^(N+1)/(N+1)!)/(1-u/(N+2))`.

The exponential factor is in [1/(s+T),1/s]; the missing vector terms are in
[0,W T]. Thus each shifted nominal component lies in
`[z_N/(s+T), min(W,(z_N+W T)/s)]`. Restore the subtracted constant.
Every operation uses Python Fraction; there is no arbitrary floating tolerance
in the decision. At zero time, zero rate or constant initial state the exact
trajectory is returned. If the remainder condition fails, return unresolved.
Terms are limited to 0..128; this method favors small networks and modest qt.

## Verification and interpretation boundary

Ten new tests cover all three states, an interior healthy parameter missed by
an endpoint grid, timewise compatibility without a common midpoint witness,
partial observation, malformed boxes and insufficient computational budget.
The error-corner test checks 24 healthy two-node cases with independent
90-digit Decimal exponential evaluation: weights at both ends and midpoint,
all initial error sign combinations and both sensor error signs, at four times.
Its sensor allowance includes a conservative margin above oracle rounding.
A three-node path is also compared with its independently written analytic
modal solution at 80-digit precision.

The targeted suite failed on the absent module before implementation, then
passed. This supports the implementation of the stated proof, not the truth
of supplied uncertainty bounds. It is still possible for healthy and faulty
families to overlap, or for an excluded healthy family to reflect unmodeled
forcing instead of an edge failure. No BFG-specific novelty or field guarantee
is inferred from this reference-model repair.

Final verification: 63 tests in the publication set passed (exit 0), including
10 new certified-family tests. The documented CLI completed with a compatible
witness. The separate pre-existing local observation module is preserved outside
this publication set. The implementation and proof remain subject to external
review; exact arithmetic does not establish that the chosen physical family is correct.
