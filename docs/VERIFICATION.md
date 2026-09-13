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
