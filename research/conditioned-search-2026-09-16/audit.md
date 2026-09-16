# BFG audit: conditioning repair

Sources: the three owner-provided audit DOCX files and SHA-256 register in
../../docs/BOUNDARY_PROTOCOL.md. This is a scoped engineering correction using
standard SVD least squares; scientific/empirical BFG validity remains open.

- Audit Complete Edition: define the claim narrowly, compare old and repaired
  methods under the same budgets, preserve all physical thresholds, retain
  the numerical-versus-certified distinction. No BFG novelty is inferred.
- Audit Workflow Master: diagnosis, prospective repair protocol, method,
  result data and audit are separated. Previous stage files are not rewritten.
- Context Recovery Protocol: continue from 9f6c969 and its four unresolved
  complete4 cases; preserve that historical failure and replay older catalogues.

No-retuning status: known-case exploratory repair. The cutoff was selected
after inspecting Jacobian spectra, then fixed before the repair evaluation.
This is not independent preregistration or out-of-sample confirmation.

Safety gate: the exact certifier remains unchanged, and tests show that a
small floating residual still fails without a sufficient rigorous enclosure.
Invalid cutoffs are rejected; the previous default remains available. All
existing status decisions are preserved in the two recorded catalogues.

Limitations: very small symmetric networks, one initial-state family, limited
times, no independent replication, no real-world noise study. SVD truncation may
discard meaningful weak directions elsewhere. Further validation and human
scientific review remain outstanding.

Verification history: the CLI configuration parsing defect was corrected and
regression-tested. The initial subprocess test also encountered Windows access
errors in TemporaryDirectory; the harness now uses a uniquely named output
file in the workspace with explicit cleanup. The final suite is rerun after
these fixes; failed intermediate checks are not counted as passing evidence.
