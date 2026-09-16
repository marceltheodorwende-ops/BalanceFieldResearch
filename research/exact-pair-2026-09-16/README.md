# Exact pair stage — 2026-09-16

This stage preserves the prior boundary results and adds a narrowly scoped
analytic fallback. [Protocol](protocol.md), [proof/API](method.md),
[audit](audit.md), [full machine-readable results](results.json).

| Same 39 cases | Boundary stage | Exact pair stage |
| --- | ---: | ---: |
| Common witness | 34 | 35 |
| Entire declared family excluded | 3 | 4 |
| Unresolved | 2 | 0 |

The exact observation (0.7,0.3) admits the symbolic edge weight
`-log(2/5)/2` for t=1 and initial state (1,0). Rational bounds certify that
it lies in [0,2]. The exact equilibrium observation at time 100 is excluded
because a nonzero initial difference remains nonzero at every finite time.

The original input hash is unchanged. All 37 previously resolved cases retain
their status. These 39 known synthetic regressions are now resolved; this is
not a complete solver or a 100% success rate on arbitrary or empirical data.

Verification: 89 software tests passed, including ten new tests for symbolic
certificates, finite-time equilibrium, sensor ordering, mass conservation,
out-of-box weights, log-budget limits, invalid budgets and scope restrictions.
The initial focused run failed because the new module did not yet exist.

Reproduce from the repository root:

```sh
python -m bfg_lab.exact_evaluation
python -m unittest discover -s tests
```

The evaluator writes this stage's results.json; historical stage files are not
its output targets. On the owner's working machine the unrelated unpublished
test_observation.py is excluded from the publication test count.

Previous stages: [boundary findings](../../docs/BOUNDARY_FINDINGS.md),
[earlier 39-case comparison](../../docs/CERTIFIED_COMPARISON.md).
Future stages should receive their own research subfolder. Existing papers,
historical result files and original solver APIs remain unchanged.
