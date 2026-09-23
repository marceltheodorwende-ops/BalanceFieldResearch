# BFG Real Relational Carrier Audit

Carrier: **Zachary weighted karate-club interaction network**

Status: **EXPLORATORY**

No club/fission label is used by the BFG mapping.

State contract: `34/34`

First-step formation/master success: `13/34` (`38.235%`)

## First-step failures

- `formation gate failed: no simple negative lowest eigenvalue`: 21

## Small-load theorem

Successful recursive certificates: `41`

Explicit quadratic bounds satisfied: `41/41`

## Permutation equivariance

Equivariant: `True`

- D: `2.317e-16`
- K: `6.685e-16`
- Y: `2.077e-15`
- R_C: `1.527e-14`

## Four-domain transformation-corridor check

| Metric | Shared across Sunspots + CO2 + ENSO + network |
|---|---:|
| alpha | False |
| formation_depth_normalized | False |
| formation_gap_normalized | False |
| neutral_load_density_ratio | False |
| k_rms_ratio | False |

## Four-domain formation-normalization check

| Metric | Shared across all four domains |
|---|---:|
| depth_over_spectral_norm | False |
| depth_over_rms_norm | False |
| depth_over_gap | False |
| depth_over_mean_abs_eigenvalue | False |

## Interpretation

The carrier deliberately tests relational structure rather than another time-series recurrence graph.

The existing three-domain transformation corridors are not promoted to universal invariants if they fail to include this network carrier.

The small-load theorem is evaluated separately because it is a mathematical master-runtime statement rather than an empirical corridor claim.

This carrier is not moved to READY_FOR_VALIDATION until an independent confirmatory network target and sealed split are specified prospectively.
