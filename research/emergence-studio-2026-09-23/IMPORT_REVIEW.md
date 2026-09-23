# Intake review — 23 September 2026

## Disposition

Publish as an unchanged experimental source snapshot with independent intake notes. This is a bounded intake review, not a security certification, full mathematical audit or independent empirical replication. Instructions inside the archive were treated as source material, not commands to the importing agent.

## Fresh evidence

- Archive: 293 files, 6,509,518 uncompressed bytes; ZIP SHA-256 `ffde5a303db12aba996a75d45f69c74f475f5348624893dea5833df9434b88e9`.
- Archive paths were checked to remain inside the extraction directory; symbolic-link entries were rejected.
- All 60 Python files parsed successfully with Python's AST parser.
- A bounded textual scan for private-key headers, GitHub tokens, AWS access identifiers and quoted secret assignments found no matches. This does not establish absence of every kind of sensitive data.
- No separate LICENSE, copyright file or AGENTS.md was found in the supplied archive. Existing repository rights rules remain in effect subject to third-party rights.
- Attempted `python -m pytest tests/test_core.py -q -p no:cacheprovider`: could not start because pytest was absent. A direct core import also failed because SciPy was absent. No tests are counted as passed by this intake.
- The supplied `PROJECT_STATUS.md` reports 84/84 tests, nine reference benchmarks and randomized audits. These remain supplied historical claims, not a fresh run here.

## Mathematical integration findings

1. **Persistence admission is incomplete for arbitrary inputs.** `bfg_studio/core.py:persistent_basis` selects eigenvectors whose eigenvalue modulus is within a tolerance of one. It does not establish power boundedness, reject growing modes, or certify semisimplicity of peripheral eigenvalues. `canonical_reclosure` does not add those checks. This is a source-inspection finding; the attempted runtime probe could not run without SciPy. Do not equate its numerical persistent sector with the amended exact definition for every input.
2. **The next load and recursion are carrier choices.** `ReferenceGramCarrier.advance` chooses the next load from `analysis* analysis`, and sets recursion using formation-eigenvalue phases plus a contraction on the complement. Its contraction and phase-scale parameters are explicit modeling choices. The class itself correctly calls this a demonstration carrier. It does not close the previously identified uniqueness problem.
3. **The complex formation vector is a representative.** The code selects one `eigh` eigenvector and a sign adjustment based on the previous profile. That is not a proof of exactly two minima over a complex space. The real-sector or phase-orbit distinction from the finite amendment remains necessary.
4. **Empirical status must preserve the historical failure.** The archive includes a sunspot held-out result marked FAIL: about 0.658% improvement against a required 1% margin; AR(12) has a lower RMSE. These values are supplied results, not independently recomputed here. The newer READY_FOR_VALIDATION entries do not erase that failed earlier hypothesis or establish success on their new held-out targets.

## Acceptance and next work

Archival acceptance: suitable. Runtime verification: incomplete due to missing dependencies. General mathematical closure: not established. Empirical confirmation: not established by this intake. No held-out confirmation permit was issued or consumed, no carrier was retuned and no original result was overwritten.

Next engineering work should use an isolated environment to run the existing test suite, then add explicit admissibility regression cases for growing and defective peripheral operators before claiming compatibility with the finite repair. A full held-out empirical run is a separate research decision, not part of importing the archive.

The three BFG audit documents guide this separation of source claims, fresh evidence and failures. Their identities are recorded in the [canonical manifest](../../papers/canonical-2026-09-22/manifest.json).
