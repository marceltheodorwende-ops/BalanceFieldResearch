# Typed phase/input bridge
This package extends the exact energy-phase chart to externally supplied torque and impulses, while using smooth q,p coordinates at rest. DERIVATION.md gives the full chain, units, work balance, inverse/composition law, conditional robustness, input-wise factor closure and identifiability requirements. It explicitly distinguishes a constructed mechanical extension from a force or torque derived by canonical BFG.

Six local mathematical/code controls pass. The predeclared audit uses4500 already permitted passive states from15 attempt-1 recordings with three hypothetical normalized kicks each:13500 controls, zero chart-domain failures, maximum work residual1.554e-15 (criterion1e-12). These hypothetical controls are not real intervention measurements, a new empirical sample, or a forecast improvement. No refit, holdout access, download or new empirical workflow. Source and calibration hashes are published under results/.

Primary real-state source: EnzeXu/Damped_Pendulum_Dataset at cbf82673641ecd65e902ad5c38a048387649a2a0; paper https://openreview.net/forum?id=xvQYvYEGhj. Only15 attempt-1 files allowed. Source hashes in results/provenance.json; no archive including reserved attempts was fetched. Existing calibration is from development seconds0–30. Apparatus/clock uncertainty remains as documented in prior packages.

Reproduce from this directory (numpy and scipy dependencies):

    python -m unittest discover -p 'test_*.py'
    python audit.py ../bfg-realization-development-2026-10-07/data ../pendulum-mechanical-identification-2026-10-07/results/models.csv results

Next physical evidence must supply independently measured torque/impulse and timing. The equations specify exactly how those inputs would identify inertia and constrain a proposed d-to-torque bridge. No causal effect is claimed from these passive recordings.

FORCE_DERIVATION_AUDIT.md additionally proves the current constant-input scalar kernel cannot support a regular rank2 attracting-pendulum factor at its fixed point. This is a restricted obstruction, not a universal rejection of matrix BFG.
