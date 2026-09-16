# Numerical proposals with exact acceptance

API: `bfg_lab.certified_interior.assess_interior`, taking the physical arguments
of `assess_exact_pair` and its options, plus `fit_evaluations=256` and
`fit_terms=64`. Existing functions are unchanged. CLI:

```sh
python -m bfg_lab.certified_interior --input your_input.json
```

First run the existing solver. Preserve every resolved result. For unresolved
histories, optimize independent edge weights and uncertain initial coordinates
inside their original intervals. Fixed coordinates are omitted. Each free
coordinate is normalized to [0,1] with a midpoint start. A numerical symmetric
Laplacian eigendecomposition predicts the WHOLE observed history for each
candidate. No generating graph, case identifier or expected result is an input.

Finite differences use normalized step 1e-5, clipped at boundaries. NumPy
least squares proposes a Gauss–Newton step. Up to 12 projected backtracking
trials use successive factors of 1/2, accepting only lower squared residual.
Movement below 1e-12 stalls. Stop at maximum residual <= half the sensor bound,
stagnation, numerical failure or the forward-evaluation budget. Each complete
trajectory prediction counts once, including Jacobian and rejected trials.
No claim of convergence or global optimization is made.

The last accepted candidate is rounded to 12 decimal places in normalized
coordinates, converted to exact fractions and clamped to [0,1]. Mapping with
the ORIGINAL rational lower bounds and widths gives an admissible candidate,
regardless of floating-point rounding in the optimizer. Symmetric edges are
mirrored. The fixed candidate is then passed to `assess_family` with zero
candidate initial uncertainty, original sensor error and 64 terms by default.
Only its rigorous `compatible_witness` result can change the family outcome.

This acceptance rule is sound under the existing certifier's assumptions:
the candidate belongs to the original family, and the same candidate's entire
trajectory enclosure fits all observations. Optimization need not be accurate
for this implication. A rejected singleton candidate does not exclude other
family members. `fit_certificate_status=healthy_family_excluded` refers ONLY
to the singleton check; the outer status remains unresolved in that case.

Zero fitting budget disables the fallback. Numerical problems can retain an
unresolved result, never produce a new family exclusion. A small floating
residual alone cannot pass; this is explicitly regression-tested by withholding
sufficient exact certification terms. This method uses only the existing NumPy
dependency, ordinary least squares and the previous rational certifier.

Limitations: ill-conditioning, non-identifiable directions, local stagnation,
finite-difference artifacts, finite precision and the single midpoint start.
Work scales with both graph size and free-coordinate count. Numerical and
rational evaluation counts are different units of work, not matched runtime.
