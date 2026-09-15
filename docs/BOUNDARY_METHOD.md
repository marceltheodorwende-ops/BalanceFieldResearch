# Certified boundary candidates

`assess_boundary` in `bfg_lab.certified_boundary` retains the previous
`refine_family` result unless it certifies a new common witness. It does not
change the historical APIs or their results. Use the same JSON input as before:

```sh
python -m bfg_lab.certified_boundary --input examples/certified_search.json
```

Defaults: 255 search boxes, depth 20, 81 extra candidate checks, 64 candidate
series terms. `terms` remains the original subdivision budget (default 24).
`max_candidates=0` disables the extra stage. Exhaustion remains unresolved.

## Why the certificates remain valid

At time zero the heat propagator is identity. For measured coordinate i,
every feasible initial state therefore satisfies both calibration bounds
`xhat_i-ex <= x_i <= xhat_i+ex` and measurement bounds
`y_i(0)-ey <= x_i <= y_i(0)+ey`. Their intersection cannot remove a feasible
state. Unmeasured coordinates retain their calibration intervals.

For each independent edge interval and intersected initial interval, enumerate
lower endpoint, midpoint and upper endpoint, removing duplicate values.
Coordinates use upper-triangle row order followed by initial-state order.
Cartesian products are traversed lazily and stopped at the candidate budget.
This deterministic ordering can disadvantage later coordinates; it is a
bounded heuristic, not a complete search or an optimal allocation of work.

Every candidate lies inside the ORIGINAL declared family. Its weights are
mirrored to preserve symmetry. Pass the fixed weights and fixed initial state
to the existing rational trajectory certifier. Accept only if its entire
trajectory enclosure lies within every measurement interval at every time.
Thus one common candidate, rather than different candidates at different
times, is a valid existential witness. A failed singleton candidate says
nothing about other members of the family and never produces family exclusion.

The method sees no case names, generating parameters or expected outcomes.
It adds standard interval intersection and finite candidate enumeration, not
a new physical law or a BFG-specific mathematical mechanism.

## Limits

There is no guaranteed reduction of unresolved cases. The Cartesian space grows
exponentially, but the configured cap limits evaluated candidates. Large graphs
can still be expensive per check. Interior non-dyadic or exactly specified
transcendental solutions can be missed; finite interval widths may prevent
equality certificates. Invalid budgets raise ValueError. Budget exhaustion and
candidate failure must not be presented as a physical fault.
