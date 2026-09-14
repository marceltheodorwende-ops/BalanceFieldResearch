# Verification record — 13 September 2026

Environment: Windows, Python 3.12.14, NumPy 2.3.5.

- `python -m unittest discover -s tests -v`: 8 tests passed.
- Complex invariant checks: 105 cases, seed 20260913, dimensions 2–8.
- `python -m bfg_lab --output results`: JSON and standalone HTML generated.
- Three synthetic scenarios, each with 81 recorded states; conserved total state,
  neutral partition and expected edge-failure timing checked.
- Dashboard JavaScript executed in Node with a minimal DOM stub: all 18
  scenario/measurement selector combinations produced data without NaN.
  This is a logic smoke test, not a browser rendering or accessibility audit.
- Original PDF SHA-256 recorded in `papers/README.md`; no PDF edits.

Not run: empirical benchmarks, full-paper simulation reproduction, full universal
reclosure, browser visual inspection, cross-platform or Python-version matrix.
No CI run is claimed. Run the documented commands after cloning.

## Candidate verification: 14 September 2026

The new tests initially failed because the formation module was absent. After implementation, `python -m unittest discover -s tests -v` passed all 15 tests, including 7 new formation tests and the existing 105 complex matrix cases. `python -m bfg_lab.formation` reports an admitted candidate with minimum -1 and a rejected candidate with minimum approximately +1. Tests cover support reduction, unitary-coordinate invariance, zero load, missing gap, degeneracy, near-zero minima and invalid inputs. No full universal iteration or empirical validation is claimed.
# Minimal recursion verification, 2026-09-14

`python -m unittest discover -s tests -v`: 20 tests passed (exit 0).
Five new tests cover the analytic stop at candidate 2, the finite step budget,
next-state invariants and input preservation, +/-1e-6 perturbations, and invalid
parameters. Before implementation the focused suite failed with missing
`bfg_lab.minimal`, establishing the absent feature. `python -m bfg_lab.minimal`
also executed successfully for both examples. Fixed absolute tolerance is not
swept; tolerance-independent or physical robustness is not established.
