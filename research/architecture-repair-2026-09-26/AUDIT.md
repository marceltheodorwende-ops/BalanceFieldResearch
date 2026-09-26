# Audit and source ledger
Date: 26 September 2026. Review object: REPAIR.md in this folder.
Status: finite persistence corrected; Gram completion conditional; universal closure and physical realization unproved.

The three BFG audit documents previously supplied are applied through the source register in outputs/BFG_Mathematischer_Audit_2026-09-15.md: BFG_Audit_Complete_Edition.docx (claim-state, distinguishability, redescription, counterchecking), BFG_Audit_Workflow_Master.docx (stage boundaries, interpretation, provenance), and BFG_X_Context_Recovery_Protocol_Master finish.docx (source hierarchy and continuity). This note is not a new independent audit of those documents.

## Evidence
Primary source is the author's supplied September 22 FINAL architecture PDF. Existing repository notes were read directly on main before the change. The source tree was main at commit 1edeb8bf95e46ab2cc30257df99d1a62c1e6419b.
- FUNDAMENTAL_CLOSURE_LAW.md blob: 2938df47c019da532712262f3bbfe4d7b55cc22d.
- UNIVERSAL_UPDATE_DERIVATION_AUDIT.md blob: 1776128df21c0281fdd4765667f93a9c8d2f643b.
Both reside under research/fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/.

## Claim audit
| Claim | Status | Qualification |
|---|---|---|
| Original non-decay span equals peripheral space | Refuted | Exact 2D counterexample |
| Riesz-range replacement isolates finite persistence | Proved | Power boundedness, finite carrier, semisimple peripheral sector |
| Riesz projector is the metric orthogonal projector | False in general | Exact nonnormal 2D counterexample |
| Original positive Gram factorization uniquely fixes Y+ | Refuted | I versus 2I |
| Induced quadratic-form principle uniquely fixes Y+ | Conditional theorem | Principle and metric explicitly added |
| Individual BC/WN/LC roles reconstructed | Not established | A Gram factorization is not unique role semantics |
| General infinite-dimensional case repaired | Not established | Only a restricted spectral-split extension stated |
| Natural laws derived | Not established | No physical observable or realization bridge |

## Verification scope
Counterexamples and proofs were checked algebraically. A short exact-rational calculation confirmed 1/16 versus 1/8 for the two metric choices and 1/2 versus 1/3 for neutral responses; printed symbolic examples are not counted as automated tests. No regression suite or empirical experiment was run, and no test-pass count is claimed.

The finite proofs do not assert nonnormal orthogonality, closed range for arbitrary infinite-dimensional operators, or uniqueness of a factorization. Rank-zero and singular-coherence cases are explicitly separated. Historical negative findings remain visible.

Recommendation: use the corrected finite persistence definition. Treat induced-Gram closure as a declared candidate unless a stronger BFG source derivation is established. Do not present this note as author-approved replacement text for the original PDF or as full implementation certification.
