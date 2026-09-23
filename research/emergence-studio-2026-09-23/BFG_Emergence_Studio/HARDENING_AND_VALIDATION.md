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
- a loaded core BFG state can continue its trajectory.

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
