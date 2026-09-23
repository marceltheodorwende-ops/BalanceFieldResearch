# Finite persistence and formation repair

Date: 23 September 2026. BFG sources: Marcel Theodor Wende. This is an AI-assisted mathematical amendment and verification record, separate from the author's unchanged PDFs.

## Outcome

- [REPAIR.md](REPAIR.md) replaces the invalid witness-span definition by a uniquely characterized finite persistent subspace, including power-bounded nonnormal operators.
- It proves the real-polarity and complex-phase alternatives and states the real-structure compatibility needed for polar transport.
- [RECONSTRUCTION.md](RECONSTRUCTION.md) identifies the remaining selection problem and the exact input contract for a complete update. It does not invent a uniquely forced Gram law.
- [verify.py](verify.py) checks exact rational counterexamples and identities, plus numerical formation and polar-transport cases. [RESULTS.json](RESULTS.json) records the run.

Run from the repository root: `python research/finite-repair-2026-09-23/verify.py` (Python and NumPy).

## Audit ledger

| Claim | Status after this amendment |
| --- | --- |
| Printed architecture Eq. (23) defines persistence | Rejected as printed; original counterexample retained |
| Corrected finite persistent space | Proved under finite dimension and power boundedness |
| Spectral and metric projectors coincide generally | False; exact nonnormal counterexample retained |
| Exactly two complex quartic minima | False; corrected to a phase orbit |
| Exactly two real quartic minima | Proved with simple negative ground eigenvalue and a specified real sector |
| Real structure survives polar transport | Proved under the intertwining hypotheses in REPAIR.md |
| These repairs uniquely determine the next Gram or full update | Not established; explicit ambiguity remains |
| Full general nonnormal or infinite-dimensional closure | Open; no claim of closure here |

Method: the three supplied audit documents require source/claim separation, preservation of failures and a recoverable stage record. Their identities and hashes are in the [canonical source manifest](../../papers/canonical-2026-09-22/manifest.json); the prior [review](../canonical-consolidation-2026-09-22/REVIEW.md) remains intact. This amendment changes the proposed specification, not historical source bytes. The emergence CSV supplies simulation summaries, not a proof of the amended laws or empirical validation.
