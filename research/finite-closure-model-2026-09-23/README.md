# Finite conditional BFG closure model

Author of the BFG framework: **Marcel Theodor Wende**. This stage contains an AI-assisted model completion, proofs and executable checks, dated 23 September 2026. Repository copyright terms apply.

## Result

[THEOREM.md](THEOREM.md) specifies a complete update for a reduced finite BFG state, proves preservation of its category and unitary-coordinate independence, and gives a restricted bounded infinite-dimensional entry theorem. It explicitly identifies two chosen laws: the active intrinsic-Gram rebuild and the unitary successor recursion. They are **additional model rules**, not a proof of uniquely forced universal BFG closure.

[finite_closure.py](finite_closure.py) implements this model as a separate corrected engine. It rejects growing recursion, distinguishes spectral and metric projectors, reports unresolved peripheral/formation decisions and represents formation by a phase-independent rank-one operator. It does not overwrite the [original Studio snapshot](../emergence-studio-2026-09-23/README.md) or its historical outputs.

Run with Python, NumPy and SciPy:

```sh
cd research/finite-closure-model-2026-09-23
python test_finite_closure.py
```

Fifteen focused regression tests pass; [RESULTS.json](RESULTS.json) records the result. This includes an analytically known scalar step, a nonnormal successful step and 24 random unitary coordinate changes over three steps. A 20-step floating-point success claim was rejected during development because channel loads became numerically unresolved; the retained test checks explicit ambiguity handling instead. See [AUDIT.md](AUDIT.md).

The [seven-obligation table](THEOREM.md#6-disposition-of-the-seven-obligations) distinguishes what is closed in this model from what remains open for the general original architecture. Test success is not empirical confirmation.
