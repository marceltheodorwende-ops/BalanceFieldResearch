# New small-network evaluation — 2026-09-16

[Protocol](protocol.md) · [Inputs and results](results.json) · [Audit](audit.md)

The solver is unchanged. Twenty newly constructed cases test paths with three
nodes and complete graphs with four nodes, intact versus an isolated input node,
full versus single-node sensing, interior weights and constant-state controls.

| Condition | Cases | Compatible | Family excluded | Unresolved |
| --- | ---: | ---: | ---: | ---: |
| Intact, impulse | 8 | 0 | 0 | 8 |
| Isolated node 0, impulse | 8 | 0 | 8 | 0 |
| Isolated node 0, constant state | 4 | 4 | 0 | 0 |

The original midpoint assessor produces the SAME classification in all 20
cases. Thus the additional search has **no classification gain in this run**.
There are zero exclusions of known compatible histories. That finite safety
observation does not prove a universal absence of false exclusions.

All eight intact cases remain unresolved under the fixed budget. Their true
weights lie inside the declared intervals, but a blind search does not find
and certify a fitting common witness here. A missing witness is not an alarm.
The four constant histories cannot reveal the topology change: a compatible
healthy graph exists despite the changed generating graph. This is expected
non-identifiability, not proof that the cut was absent.

The earlier 39/39 result therefore does not transfer as complete resolution to
these new cases. Full and partial sensing give identical statuses here, which
does not establish that additional sensors are generally useless.

## Reproduction and evidence

```sh
python -m bfg_lab.network_transfer
python -m unittest discover -s tests -p test_network_transfer.py -v
```

Results include the complete input catalogue, protocol/data hashes, status per
case, effort and available witnesses/certificates. Original solver modules,
physical uncertainty bounds and earlier results are not changed.
92 publication tests pass. New tests check catalogue coverage, initial readings,
mass conservation and closed-form trajectories against independent numerical
matrix evolution. Decimal rounding is far below the declared measurement error;
the floating comparison is a cross-check, not an exact arithmetic proof.

Next research question: why the search misses interior healthy parameters as
the number of uncertain edges grows. Candidate proposals based on measured
trajectories could be explored, but must still pass the existing rigorous
certifier and be compared with matched compute budgets. No such repair or
improvement is claimed in this stage.
