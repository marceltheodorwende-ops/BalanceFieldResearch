# Matrix tangent and internal-force audit
A new exact quotient representative computes the full-persistence matrix BFG update without differentiating arbitrary SVD frames. It identifies genuinely evolving offdiagonal kernel magnitudes and multiple geometry tangent modes. DERIVATION.md gives sources, derivation and scope.

For the explicitly declared simplest isotropic matrix-input extension, two geometry tangent eigenvalues at d=.15 are .178902 and .428499. They are real. A conditional factor theorem excludes a regular nonresonant underdamped pendulum factor at this fixed point. This is a narrowing of one construction, not a universal negative result for matrix BFG or a proof of the physical force law.

30 independent complex Ambient controls pass; maximum formula discrepancy1.6002e-15. Three-step finite differences verify the analytic tangent. No real-data analysis, new empirical result, holdout access or workflow started. Synthetic cases serve only mathematical/code controls. All previous positive and negative physical results remain unchanged.

From this directory in the repository, with numpy and scipy:

    python control.py results

It imports the existing Ambient implementation in ../real-eeg-covariance-2026-10-07/experiment.py but executes no EEG/download code. Active source is exclusively Dynamic Order. Results/control.json records local verification (filename controls.json); no remote reproduction claimed. Next: anisotropic/noncommuting matrix and instrument closure, with explicit units and internal force-selection constraints.
