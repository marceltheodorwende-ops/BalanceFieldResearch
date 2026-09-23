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
- the mandatory Jordan-block and supercritical instability controls are rejected.

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
- GitHub mathematical integration audit: PASS
- finite reduced master closure profile: PASS
- checkpoint save/load/resume: PASS

The random noncommuting formation rate is not treated as a target to maximize.
Formation failure is an admissible BFG result; weakening the gate to make all
random seeds pass would invalidate the benchmark.

## Provenance

Each hardening report stores a source-tree SHA-256 fingerprint. Results from a
different code fingerprint are not silently treated as the same software state.

## External empirical validation

Hardening is necessary but not sufficient for natural realization.

The next empirical step requires one independently defined carrier under
`REAL_DOMAIN_VALIDATION_PROTOCOL.md`.


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


## BalanceFieldResearch mathematical-integration gate

Hardening now also requires the source-sensitive mathematical integration
audit to pass. It checks:

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
