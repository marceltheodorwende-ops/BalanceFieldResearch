# BFG Emergence Studio — Hardening and Validation

The theory-facing implementation is frozen through Identity Closure.

The current engineering phase asks a different question:

> Does the same implementation remain stable, reproducible, auditable, and
> no-retuning compatible under fixed benchmarks, randomized algebraic tests,
> parameter perturbations, persistence, and external-carrier constraints?

## Current hardening gates

The master hardening command requires all of the following:

- all frozen cross-layer reference benchmarks pass,
- randomized algebraic property tests pass,
- commuting inheritance controls stay non-novel,
- a substantial fraction of random noncommuting seeds remain formation-admissible,
- every successful noncommuting trial in the current audit exhibits the declared
  spectral novelty witness,
- numerical classification is stable under implementation-tolerance sweeps,
- a local carrier perturbation grid remains operational,
- invalid negative neutral geometry is rejected,
- checkpoint save/load hash verification succeeds,
- a loaded core BFG state can continue its trajectory,
- the finite-dimensional recursive stability theorem hypotheses pass for all current development/calibration carrier operators,
- the mandatory Jordan-block and supercritical instability controls are rejected,
- master runtime transfer audit passes on all allowed real development/calibration states.

Run:

```bash
python -m bfg_studio hardening --trials 200 --workers 4
```

## Current reference hardening result

The included master run reports:

- 9/9 cross-layer benchmarks: PASS
- 200 randomized algebraic trials: 0 failures
- 40 commuting controls: 0 failures
- noncommuting formation success fraction: 0.825
- novelty fraction among successful noncommuting trials: 1.0
- tolerance classification stable: yes
- ±5% carrier-grid survival fraction: 1.0
- recursive stability theorem audit: PASS
- integrated mathematical closure audit: PASS
- finite reduced master closure profile: PASS
- master runtime transfer audit: PASS
- formation-dynamics smoke gate: PASS
- relational network audit: PASS
- formation-robustness audit: PASS
- parent-formation-radius audit: PASS
- stratum-transition audit: PASS
- small-load contraction theorem smoke gate: PASS
- checkpoint save/load/resume: PASS

The random noncommuting formation rate is not treated as a target to maximize.
Formation failure is an admissible BFG result; weakening the gate to make all
random seeds pass would invalidate the benchmark.

## Provenance

Each hardening report stores a source-tree SHA-256 fingerprint. Results from a
different code fingerprint are not silently treated as the same software state.

## External empirical validation

Hardening is necessary but not sufficient for natural realization.

The active portfolio already contains three independently frozen real-domain
carriers under `REAL_DOMAIN_VALIDATION_PROTOCOL.md`. They remain separated from
confirmatory claims until an explicit one-time held-out permit is used.


## Recursive stability gate

Hardening now includes `run_master_stability_audit`.

The audit checks the finite-dimensional theorem criterion

`closed-unit-disk spectrum + semisimple unit-circle spectrum`

and reports stable complement gaps and finite-horizon power norms.

Mandatory controls ensure that the checker rejects both:

- a unit-circle Jordan block with spectral radius exactly one;
- an operator with an eigenvalue outside the unit disk.

This is a numerical audit of theorem hypotheses, not a replacement for the
proof in `BFG_RECURSIVE_STABILITY_THEOREM.md`.


Current recursive-stability hardening result:

- `1,375/1,375` recursive operators from the active development/calibration
  real-carrier states satisfy the finite-dimensional spectral criterion;
- semisimple peripheral spectrum: `1,375/1,375`;
- minimum stable gap across those carrier families: approximately `0.24`;
- unit-circle Jordan defect control: correctly rejected;
- supercritical control: correctly rejected.


## Integrated mathematical-closure gate

Hardening now also requires the integrated mathematical closure audit to pass. It checks:

- exact supplied rational nonnormal persistence certificates;
- rejection of a defective unit-circle control;
- supplied-factor Gram rebuilding;
- retained-channel Gram-energy identity;
- positive and negative G1 intertwining controls;
- M3 Cayley-unitarity under its declared skew-Hermitian connection
  assumptions.

The gate now also exercises the adopted 23-September finite master closure
profile. Runtime closure is accepted only if its scalar analytic identity,
finite-iteration category preservation, factor reconstruction and successor
unitarity controls pass.

G1 and M3 retain their own declared roles; they are not required to make the
finite master closure total.


## Runtime-dispatch and perturbation controls

Hardening now checks that:

- the generic simulation API enters the finite master runtime when no carrier
  adapter is supplied;
- explicit carrier mode remains backward compatible;
- an arbitrarily small outward perturbation of a unit-circle eigenvalue is
  not accepted merely because the perturbation norm is small;
- tangential unit-circle perturbations can remain admissible;
- successful finite successors remain unitary by construction.


## Master runtime transfer gate

Hardening now executes the full real-carrier transfer audit over all currently
allowed development/calibration states.

A PASS requires:

- every state is processed by the common finite master runtime;
- no uncaught transfer exception occurs;
- every successful successor satisfies the declared unitarity tolerance;
- every successful successor satisfies the Gram-rebuild tolerance;
- no active held-out target metric is evaluated.

A legitimate transition to absorbing `bottom` does not fail this gate.

Current result:

- `1,375/1,375` states processed;
- `1,375/1,375` successful first master transfers;
- `0` uncaught exceptions;
- maximum unitarity residual `~7.03e-16`;
- maximum Gram-rebuild residual `0`.


## Formation-dynamics gate

Hardening includes a bounded formation-dynamics smoke audit. It verifies
that:

- the real-carrier adapter enters the common master runtime;
- all smoke states complete the first master reclosure;
- no held-out target is opened;
- the pooled load-contraction fit is finite;
- the scalar recurrence approaches `2 y^2` at small load.

The full 1,375-state formation/tolerance analysis is retained as a separate
research artifact so hardening remains fast and deterministic.


## Small-load contraction theorem gate

Hardening now includes a bounded smoke audit of the exact multidimensional
successor-load theorem.

The gate verifies on real development/calibration smoke states that:

- `lambda_up <= mu ||Y||^2`;
- `alpha <= (mu / eta) ||Y||^2`;
- `||Y_+|| <= C ||Y||^2`;
- no held-out target is opened.

The full `3,816`-transition audit is retained separately under
`outputs/small_load`.

Current test suite: `142/142` pass.

Current source fingerprint: `9ed33c1e22e743dd88004ed147b447dfe7a0c832f25779196805b137726843b8`.


## Relational-network gate

Hardening now includes the exploratory real weighted interaction carrier.

A PASS requires:

- all 34 node-probe mappings satisfy the BFG state contract;
- permutation-equivariance residuals remain within numerical tolerance;
- successful recursive transitions satisfy the small-load theorem;
- no club/fission target labels are used by the BFG mapping;
- no held-out/confirmatory status is claimed.

Hardening does **not** require all node probes to pass the formation gate.
The current `13/34` first-step formation success is a scientific result, not
a software failure.


## Formation-eligibility gate

Hardening now checks the exact generalized-spectrum formation certificate.

The bounded smoke gate requires:

- direct active spectrum and generalized packet spectrum agree numerically;
- generalized criterion agrees with the runtime formation decision;
- all 34 relational parent operators are confirmed negative at ground level;
- all 34 relational simplicity gaps pass;
- the parent-ground witness sign reproduces the observed relational
  `13/21` split without retuning;
- no held-out target is opened.

The full `1,409`-state theorem audit is retained separately under
`outputs/formation_eligibility`.


## Formation-robustness gate

Hardening now includes an exact active-operator bifurcation control.

For the bounded smoke set it requires:

- every computed signed margin is finite away from the boundary;
- a `0.99 ×` nearest-boundary perturbation preserves formation status;
- a matched perturbation just beyond the exact nearest boundary changes
  formation status;
- no held-out target is accessed.

The full four-carrier audit verifies both controls on `1409/1409` active
first-step states.


## Parent-formation-radius gate

Hardening now includes a bounded parent-state formation-radius audit.

A PASS requires:

- every smoke state receives a positive conditional radius;
- the declared fixed persistent/active rank stratum remains explicit;
- structured admissible controls stay inside the radius;
- those controls preserve formation status;
- their observed active spectral shifts remain below the theorem bound;
- no held-out target is accessed.

The full research artifact contains `1409/1409` positive first-step
certificates and `43/43` structured controls passing.


## Stratum-transition hardening gate

Hardening now includes a bounded stratum-geometry audit.

A PASS requires:

- all smoke states expose the declared four surface families;
- persistent and active runtime ranks remain the expected rank 4;
- the nearest persistent transition is the loss surface;
- the nearest active transition is latent-mode activation;
- every strict runtime parent control preserves formation status and active
  runtime rank;
- no held-out target is opened.

The full retained audit covers all `1,409` current first-step states.
