# Interior search — 2026-09-16

[Protocol](protocol.md) · [Method and soundness argument](method.md) ·
[Results](results.json) · [BFG audit](audit.md)

On the unchanged 20 network-transfer cases:

| Procedure | Compatible | Family excluded | Unresolved |
| --- | ---: | ---: | ---: |
| Previous solver, 31 boxes | 4 | 8 | 8 |
| Previous solver, 256 boxes | 4 | 8 | 8 |
| 31 boxes plus numerical proposals/exact checks | 8 | 8 | 4 |

All four intact path3 histories now have exact rational certificates, with full
or single-node sensing at either weight. They use 16, 16, 16 and 21 numerical
trajectory evaluations. The four intact complete4 histories remain unresolved:
the optimizer stalls after 118, 53, 25 and 38 evaluations respectively and the
final singleton candidate is rejected. These are not family exclusions.

No existing certificate is reversed. The earlier 39-case exact-pair catalogue
also retains all 39 statuses. Original uncertainty bounds and inputs are
unchanged; both input hashes are recorded. The improvement is four certified
cases, not a general solution to parameter inference. No additional healthy
case is excluded, and no detection benefit is inferred from unresolved outputs.

The comparison is not equal-runtime: extra floating evaluations differ in cost
from extra rational box checks. This known-case result cannot establish general
superiority or out-of-sample performance. Solver settings were not retuned to
remove the remaining negative findings.

## Verification

```sh
python -m bfg_lab.interior_evaluation
python -m unittest discover -s tests -p test_certified_interior.py -v
```

The publication suite passes 98 tests. Six new tests cover an interior witness,
original bounds, zero and exhausted budgets, failed fits, invalid budgets,
joint state/weight fitting and rejection of a small floating residual when the
rigorous enclosure is insufficient. The initial focused run failed because the
new module did not yet exist. Inputs remain in prior stage files; this stage
stores new results without replacing previous records.

Next investigation: diagnose the complete-graph optimizer's stagnation,
particularly Jacobian conditioning and poorly identifiable directions. This
is a hypothesis about the numerical method, not a proven cause or a reason to
relax certification. No empirical BFG claim is established.
