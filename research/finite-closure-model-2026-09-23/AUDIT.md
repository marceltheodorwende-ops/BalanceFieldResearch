# Fresh evidence and failure ledger

## Source continuity

Baseline: the unchanged 293-file Studio archive, the canonical papers, and the finite repair amendment. The three BFG audit documents identified in the [canonical manifest](../../papers/canonical-2026-09-22/manifest.json) require explicit assumptions, source/evidence separation, and retention of negative results. This stage follows those rules; it adds a conditional model rather than changing historical findings.

## Reproduced original defect

Using the installed Python 3.12 environment with SciPy, the four zero-argument tests in the original `tests/test_core.py` were executed directly and passed. The same process evaluated an original Studio state with D=(1,1), K=diag(-2,1), Y=I, R=diag(1,2). Original `canonical_reclosure` returned success even though R is not power bounded. The corrected engine's growing-recursion regression rejects the corresponding density state.

The earlier intake environment lacked SciPy; the present check used a different installed environment. This is fresh evidence, not a reinterpretation of the earlier failed import. The complete original 84-test suite has still not been rerun; no such claim is made.

## Focused verification

Command: `python test_finite_closure.py` under the stage directory, using the installed Python 3.12 interpreter. Final exit status 0: 15 tests passed. Cases cover growing recursion, a peripheral Jordan block, a stable Jordan block, the exact nonnormal projector distinction, near-unit ambiguity, terminal absorption, invalid non-Hermitian input, degenerate formation, positive formation, phase invariance, repeated-step ambiguity, explicit Gram factor reconstruction, an analytically known scalar update, a successful nonnormal step and unitary-coordinate invariance.

The first run had 11 passes and one error: a test expecting 20 successful steps encountered `NumericalAmbiguity: dual load near zero`. The model and numerical thresholds were retained. The test was corrected to reflect the distinction between exact category closure and finite-precision resolvability; this is not a claim that the original expectation was satisfied. The final run includes three subsequently added factor-gauge and exact-example checks.

## Numerical and mathematical boundaries

- Floating eigenvalue classification cannot prove exact equality to the unit circle. Clear growth is rejected; a near-unit band is inconclusive; sufficiently roundoff-close values are treated as numerically consistent only.
- A badly conditioned peripheral eigenbasis is rejected as defective or unresolved, even though some exact admissible matrices may also be ill-conditioned. This conservative numerical implementation does not cover every exact theorem input.
- Very small singular values are truncated under a declared rank threshold; numerical active support is not an exact rank certificate.
- Degenerate or unresolved ground modes raise numerical ambiguity. The exact mathematical specification terminates when a genuinely multiple ground mode is known. The numerical engine does not claim to decide exact multiplicity from a tolerance.
- Exact matrix identities and theorem proofs are distinct from numerical residual tests.
- The selected successor recursion is unitary, so every nonterminal successor has full persistent support. This is an explicit restriction of the chosen completion.
- Real two-minimum formation, full historical capacity-factor semantics and arbitrary unbounded infinite-dimensional transport are not inferred from this complex reduced model.

No supplied empirical benchmark was rerun, no validation permit was issued and no dataset or historical output was changed. Internal-uniqueness and general-realization claims remain open as documented in THEOREM.md.
