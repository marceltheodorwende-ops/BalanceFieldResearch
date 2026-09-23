# Formation Geometry → Dual-Load Decay → Termination Surface

**Development/calibration data only. No held-out target is opened.**

States: `1375`

First-step master success: `1375/1375`

## Formation-depth normalization candidates

| Candidate | Shared q10-q90 corridor | Lower | Upper | Overlap ratio |
|---|---:|---:|---:|---:|
| depth_over_spectral_norm | False |  |  | 0.0000 |
| depth_over_rms_norm | True | 1.32728 | 1.34201 | 0.0715 |
| depth_over_gap | True | 0.760588 | 0.790084 | 0.2235 |
| depth_over_mean_abs_eigenvalue | True | 1.36563 | 1.41587 | 0.2015 |

All candidates are retained; none is selected merely because it overlaps.

A zero-spread normalization is flagged as degenerate rather than counted as independent invariant evidence.

Degenerate candidates: `none`

Shared nontrivial candidates: `depth_over_rms_norm, depth_over_gap, depth_over_mean_abs_eigenvalue`

## Neutral-load contraction

Pooled log-log fit:

\[
\log_{10} y_+ = a+p\log_{10} y,
\]

with `p = 1.638869` over `3816` successful transitions.

Depth-specific fitted exponents:

- depth 1: `p=5.685902` over `1375` transitions
- depth 2: `p=1.952120` over `1375` transitions
- depth 3: `p=1.979730` over `1066` transitions

The exact scalar recurrence is

\[
y_+ = \frac{2y^2}{(1+y)^2(1+y^2)},
\]

so for small load

\[
y_+\sim2y^2.
\]

## Domain summaries

### annual-sunspots

- states: `297`
- maximum successful depth: `3`
- median successful depth: `3.000`
- fitted Y-decay exponent: `1.697014`

Median log10 dual-load margin over the numerical gate:

- depth 1: `7.675822`
- depth 2: `6.000650`
- depth 3: `2.513368`
- depth 4: `-4.062838`

Terminal reasons:

- `dual persistent load below admissibility threshold`: 274
- `numerical successor admissibility boundary: reduced closure requires Y positive definite`: 23

### mauna-loa-co2

- states: `370`
- maximum successful depth: `3`
- median successful depth: `3.000`
- fitted Y-decay exponent: `1.573320`

Median log10 dual-load margin over the numerical gate:

- depth 1: `7.474723`
- depth 2: `5.827022`
- depth 3: `2.154946`
- depth 4: `-3.603539`

Terminal reasons:

- `dual persistent load below admissibility threshold`: 358
- `numerical successor admissibility boundary: reduced closure requires Y positive definite`: 12

### enso-pacific-sst

- states: `708`
- maximum successful depth: `3`
- median successful depth: `3.000`
- fitted Y-decay exponent: `1.640140`

Median log10 dual-load margin over the numerical gate:

- depth 1: `7.396755`
- depth 2: `5.706489`
- depth 3: `1.922563`
- depth 4: `-5.132612`

Terminal reasons:

- `dual persistent load below admissibility threshold`: 644
- `numerical successor admissibility boundary: reduced closure requires Y positive definite`: 64

## Tolerance sensitivity

Only `atol` and `psd_tol` are scaled; spectral/rank/gap tolerances stay fixed.

| Scale | Median successful depth | q10 | q90 | Max depth |
|---:|---:|---:|---:|---:|
| 0.1 | 3.000 | 2.000 | 3.000 | 4 |
| 1 | 3.000 | 2.000 | 3.000 | 3 |
| 10 | 3.000 | 2.000 | 3.000 | 3 |

If the terminal depth shifts when only the numerical floors move, the location of `bottom` is partly numerical even when the underlying load contraction is structural.

## Interpretation

The analysis separates two questions:

1. whether a different dimensionless formation-depth coordinate has a three-domain corridor;
2. whether repeated closure contracts the neutral/dual load toward the terminal surface.

The exact scalar map already exhibits quadratic small-load contraction. The real-carrier log-log exponent tests whether the multidimensional master transport shows a related contraction regime.

A numerical bottom caused by the declared tolerance is reported as such. It is not silently reinterpreted as an exact mathematical extinction.
