# Network robustness monitor prototype

This command-line prototype checks necessary conditions of fixed symmetric
heat diffusion. It does not certify that a network is healthy, diagnose the
cause of a fault, or derive a new physical law from BFG.

## Use

Run `python -m bfg_lab.monitor` to generate eight scenario/coverage results in
`results/monitor.json`. All experiments are synthetic exploratory stress cases.

For your own samples:

```sh
python -m bfg_lab.monitor --input examples/two_node_samples.json --nodes 2 --assume-fixed-heat --target-step 20 --sample-error 0.00001
```

Input is a JSON matrix: equally spaced time samples in rows, fixed distinct
node sensors in columns, starting at time zero. `--nodes` declares total network
size; the software cannot verify sensor identities or completeness. Sample error
is a known absolute bound per scalar reading, not an estimated standard deviation.
Without `--assume-fixed-heat`, full observations produce no forecast. The flag
is a caller assumption about the process through the target time, not a check
that the software has established. Output is JSON; this is not a background
monitor or an installed live data integration.

## Status meanings

| Status | Meaning and action |
| --- | --- |
| insufficient_coverage | Some nodes are unobserved. Report local step changes only; no global forecast. |
| assumption_violation | Conservation, nonincreasing disagreement or log-convex decay conflicts with the stated error allowance. No forecast. |
| model_unverified | No detected conflict, but the fixed-heat assumption was not asserted. No forecast. |
| unresolved_initial_signal | Initial disagreement is zero or too small relative to measurement error. Ratio unavailable. |
| conditional_forecast | A future interval is provided only conditional on fixed symmetric heat dynamics without forcing through the target. |

For partial data, increases at observed nodes need not violate global diffusion.
The monitor therefore does not label local variation a physical anomaly. Even
constant partial observations cannot certify what unobserved nodes are doing.

## Checks and conservative errors

With n fully observed nodes and scalar error e, the centered Euclidean norm
has error at most sqrt(n)e, because centering is an orthogonal projection.
Two measured total sums may differ by up to 2ne without disproving conservation.
The monitor checks monotonicity using norm intervals. It checks log convexity
using `lower(norm_t)^2 <= upper(norm_{t-1}) upper(norm_{t+1})`.
These are necessary conditions, not a sufficient model identification test.
An additional absolute 1e-10 arithmetic tolerance is used for diagnostics.

From norm intervals [l0,u0] and [lm,um], the early ratio is conservatively
enclosed by [lm/u0,um/l0] intersected with [0,1]. The E1 result gives
`[(lm/u0)^(H/m), um/l0]` after that intersection. A zero initial lower bound
blocks the forecast. No graph or hidden node state enters `assess`.

## Self-check outcomes

Eight-node path, initial impulse, dt=0.2. At step 5 issue a conditional interval
for step 20; apply changes at step 7. Then assess the full observed history.
Every scenario is repeated with all nodes and with only nodes 0 and 1 observed.

| Scenario | Full-observation outcome | Original interval at step 20 |
| --- | --- | --- |
| Unchanged diffusion | Conditional forecast | Contains target |
| Remove middle edge | No diagnostic conflict: change goes undetected | Contains target |
| Add 0.5 to last node | Assumption violation; forecast withdrawn | Contains target despite violation |
| Multiply edge weights by 8 | Assumption violation; forecast withdrawn | Does not contain target |

All partial-observation cases abstain from a global forecast. Synthetic truth
is computed separately for evaluation and is never passed into the partial
monitor. The speedup illustrates actual interval failure outside the fixed-law
assumption. The cut illustrates a false negative: an undetected change is
possible even with full observation. No sensitivity/specificity rates or reliable
fault-detection claim can be inferred from these four constructed scenarios.

Six focused tests cover abstention, explicit assumptions, error allowance,
forcing, acceleration, undefined signals and the scenario outcomes. Test-first
execution failed on the absent monitor module before implementation.

Final verification: all 45 tests in the publication set passed. Both the
eight-case scenario CLI and the documented JSON-input command completed with
exit 0. The separate pre-existing local observation experiment is not part of
this publication and is preserved.
