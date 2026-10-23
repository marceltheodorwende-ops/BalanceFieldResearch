# BFG spacetime and conservation investigation

This is the BFG-only research packet authorized by Marcel Theodor Wende on 23 October 2026. Start with the [binding German mandate](MANDATE.de.md) and [checked status](STATUS.md).

**Result:** finite conservation identities and counterexamples are established in stated sectors. A standard Hermitian-two-mode determinant construction supplies an algebraic Lorentz carrier, but physical dimensional selection, transport, clock, stress, action and Einstein dynamics remain OPEN.

## Contents
- [MANDATE.de.md](MANDATE.de.md): binding scope, source hierarchy and completion rules; committed first.
- [PROTOCOL.md](PROTOCOL.md): predeclared candidates, bounds and transparent amendments.
- [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json): pinned manuscript and original kernel.
- [DERIVATION.md](DERIVATION.md): proofs, exact witnesses and their limits.
- [STATUS.md](STATUS.md): German claim/evidence ledger and next dependency.
- [audit.py](audit.py), [test_audit.py](test_audit.py), [results.json](results.json): executable finite controls.
- [REVIEW.md](REVIEW.md): verification scope and retained failures.

## Two-mode/environment continuation

[Exact pair-selection limits and environment-assisted factor](PAIR_DERIVATION.md), with [preregistered checks](PAIR_PROTOCOL.md) and [new source controls](pair_results.json). A pure pair and pair-plus-alpha fail autonomous closure; a complementary formation-weighted spectral measure supplies a sufficient closed factor on the full-persistence history domain. No physical clock/current or Einstein completion is claimed.

Run the additional controls with:
    python research/spacetime-conservation/pair_audit.py

## Stable current-state pair selection

[Invariant spectral class and derivative correction](STABLE_PAIR_DERIVATION.md), [protocol](STABLE_PAIR_PROTOCOL.md), [fresh results](stable_pair_results.json). On the stated full-persistence class, the two-smallest selector is retained and the environment-assisted factor needs no extra pair-history label. Complementary mass and first moment still do not close it. Physical selection/clock/current remain open.

Additional controls:
    python research/spacetime-conservation/stable_pair_audit.py

## Reproduce
Use Python 3.12 and the adjacent requirements.txt. From the repository root:
    python -m pip install -r research/spacetime-conservation/requirements.txt
    python research/spacetime-conservation/audit.py
    cd research/spacetime-conservation
    python -m unittest -v test_audit

The audit imports the unchanged source update, checks its exact Git blob, and never calls the empirical data evaluator. It writes only this packet's results.json. On Windows, use a checkout retaining the source's LF bytes (for example git -c core.autocrlf=false clone ...); a byte mismatch intentionally stops rather than silently changing the pin. Upstream source changes require an explicit new source review.

The six-event trajectory reaches a recorded numerical rank cutoff at event six; only five completed events are claimed. Other bounded controls pass. Numerical controls do not replace the proofs and do not establish physical emergence.

This research branch starts from the active manuscript branch, not the older main. Original manuscripts, kernel, licenses and empirical artifacts remain unchanged.

