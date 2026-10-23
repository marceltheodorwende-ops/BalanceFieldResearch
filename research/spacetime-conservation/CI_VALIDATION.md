# GitHub verification of published research code

Verified 23 October 2026.

- Tested commit: [5855349d1e4a6bb058911f66010a2e6e16ed64a2](https://github.com/marceltheodorwende-ops/BalanceFieldResearch/commit/5855349d1e4a6bb058911f66010a2e6e16ed64a2).
- [GitHub Actions run 40002079626](https://github.com/marceltheodorwende-ops/BalanceFieldResearch/actions/runs/40002079626): completed, success.
- All job steps succeeded: dependency installation, original manuscript SHA256 validation, source-pinned finite audit, seven unittest boundary tests and result-artifact upload.
- All 13 changed repository files were read back from the published commit; text contents matched the prepared files (trailing-newline normalization only).
- [Draft PR #1](https://github.com/marceltheodorwende-ops/BalanceFieldResearch/pull/1) targets the active manuscript branch.

A successful CI run means these checks passed. The audit intentionally reports the six-event numerical trajectory limitation and OPEN physical gates; success does not turn either into a completed physical theorem. This documentation-only verification record is later than the tested code commit and makes no claim that a future code change is covered.

## Two-mode spectral-environment continuation

Verified 23 October 2026 for code commit [73c4035e4e8da390e99f65463596f286a3b8a8b8](https://github.com/marceltheodorwende-ops/BalanceFieldResearch/commit/73c4035e4e8da390e99f65463596f286a3b8a8b8).
Both [run 40009539625](https://github.com/marceltheodorwende-ops/BalanceFieldResearch/actions/runs/40009539625) and [run 40009532539](https://github.com/marceltheodorwende-ops/BalanceFieldResearch/actions/runs/40009532539) completed their finite-controls job successfully.
Steps include the original PDF SHA256, first audit, new pair_audit.py (exact fiber witnesses and 36 source events), all seven existing boundary tests, and upload of both JSON result files.
The six changed files in the continuation were read back byte-for-text from the published code commit and matched the prepared contents. Protocol was committed separately first at 67edd7837f0414c27e0550c71393ad576d24fd69.
The initial ordering assertion correction is retained in PAIR_DERIVATION.md. No input/coefficients were changed to obtain the pair-switch counterexample.
These checks cover the source-derived full-persistence history factor. Physical current/clock and general selection/seed extension remain open.
