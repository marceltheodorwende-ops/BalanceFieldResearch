# BFG Master Runtime Transfer Audit

Audit: **PASS**

**No active held-out target metric is opened by this audit.**

States processed: `1375/1375`

First-step nonterminal transfers: `1375/1375` (`100.000%`)

Recursive diagnostic horizon: `4`

| Carrier | States | First-step success | Median successful depth | Max depth | Max unitarity residual | Max Gram residual |
|---|---:|---:|---:|---:|---:|---:|
| annual-sunspots | 297 | 100.000% | 3.000 | 3 | 5.808e-16 | 0.000e+00 |
| mauna-loa-co2 | 370 | 100.000% | 3.000 | 3 | 5.629e-16 | 0.000e+00 |
| enso-pacific-sst | 708 | 100.000% | 3.000 | 3 | 7.031e-16 | 0.000e+00 |

## Terminal reasons within the recursive diagnostic horizon

### annual-sunspots
- `dual persistent load below admissibility threshold`: 274
- `numerical successor admissibility boundary: reduced closure requires Y positive definite`: 23

### mauna-loa-co2
- `dual persistent load below admissibility threshold`: 358
- `numerical successor admissibility boundary: reduced closure requires Y positive definite`: 12

### enso-pacific-sst
- `dual persistent load below admissibility threshold`: 644
- `numerical successor admissibility boundary: reduced closure requires Y positive definite`: 64

## Cross-domain transformation corridors

| Metric | Shared q10-q90 corridor | Lower | Upper | Overlap ratio |
|---|---:|---:|---:|---:|
| alpha | True | 0.00217992 | 0.00856743 | 0.3239 |
| formation_depth_normalized | False |  |  | 0.0000 |
| formation_gap_normalized | True | 1.26485 | 1.30354 | 0.1851 |
| neutral_load_density_ratio | True | 0.0245657 | 0.0572644 | 0.3321 |
| k_rms_ratio | True | 0.795695 | 0.811047 | 0.1438 |

## Interpretation

The first-step result asks whether heterogeneous real-domain states can enter the same finite BFG master transformation without a domain-specific successor law.

The recursive-depth diagnostic is deliberately separate. A later bottom state is a legitimate total-map outcome; it is not reclassified as a software failure.

Shared corridors are exploratory transformation coordinates, not confirmatory evidence of a universal natural law.
