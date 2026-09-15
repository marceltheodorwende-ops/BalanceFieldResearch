# Boundary evaluation results

2026-09-15. Exploratory engineering result under [the frozen protocol](BOUNDARY_PROTOCOL.md).
All 39 input cases have the same SHA-256 as the previous comparison. The
previous comparison and its negative findings are preserved unchanged.

| Ablation | Compatible witness | Family excluded | Unresolved |
| --- | ---: | ---: | ---: |
| Original search, original terms | 13 | 3 | 23 |
| Original search, 64 terms | 13 | 3 | 23 |
| Boundary candidates, original terms | 16 | 3 | 20 |
| Boundary candidates, 64 candidate terms | 34 | 3 | 2 |

All runs retain 255 boxes and depth 20. Boundary runs add up to 81 candidate
checks. Original terms are 24 except the existing two-term series-limit case.
No measurement, calibration or graph interval was widened. No generating
parameters or case identifiers enter the new decision function.

The combined change resolves 21 formerly open cases: the 20 remaining
calibration/measurement corners and the weight-2 boundary case. The
original-term boundary ablation resolves only three additional cases; raising
the old search's series budget alone resolves none. These ablations support the
combined candidate-selection/certification change on this known catalogue.
They do not demonstrate equal-runtime superiority or held-out generalization.

Two negative results remain: exact observation (0.7,0.3) and exact equilibrium
at finite time 100. Their analytic diagnoses remain as recorded in
CERTIFIED_COMPARISON.md. Neither is silently converted into a machine certificate.
Existing certificates are not reversed; no constructed healthy case is excluded.

## Reproduce

```sh
python -m bfg_lab.boundary_evaluation old24
python -m bfg_lab.boundary_evaluation old64
python -m bfg_lab.boundary_evaluation boundary24
python -m bfg_lab.boundary_evaluation boundary64
```

Each command creates its own `results/boundary_<mode>.json` with case/protocol
hashes, per-case results, witness parameters and candidate counts. Inputs remain
in `results/certified_comparison.json`. The evaluator checks returned witness
membership against the original bounds. The publication suite passes 79 tests.

The next unresolved implementation question is symbolic or tighter numerical
handling of the exact two-node cases. Larger graphs and new held-out cases still
require separate evaluation; the 144 earlier network stress cases are not part
of this run. This result does not establish empirical BFG validity.
