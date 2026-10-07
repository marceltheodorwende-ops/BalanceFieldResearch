# Exact energy–phase realization
A phase-retaining, exact coordinate bridge resolves the previously demonstrated energy-only closure failure, conditional on the full sine mechanical generator. See DERIVATION.md for proof, source sections, assumptions and counter-limits; PROTOCOL.md was written before this evaluation.

Four independent controls pass, including DOP853 comparison. On 15 real development recordings, all origins satisfy the chart (dimensionless energy 0.0028054–0.2100716), with no exclusions or holdout access. Maximum absolute discrepancy from Cartesian RK4 is 1.027e-6, below the predeclared 1e-5 criterion. At 6.4 seconds (3540 overlapping forecast pairs), mean target-RMS-normalized angle/velocity errors are 0.088291/0.128745, matching the strong full-sine rival; persistence is 1.499186/1.502682. This validates a representation, not a new predictive improvement. Reused development data are not independent confirmation; overlapping forecasts and shared calibration preclude treating pairs as independent subjects.

Source: EnzeXu/Damped_Pendulum_Dataset, pinned cbf82673641ecd65e902ad5c38a048387649a2a0, attempt-1 CSVs only; primary publication https://openreview.net/forum?id=xvQYvYEGhj. Per-file hashes in results/provenance.json. Existing coefficient hash recorded in summary.json. CSV precision and nominal timestamp grid do not establish sensor or clock accuracy. Raw data are fetched only through the existing strict development allowlist.

From this directory in the repository:

    python -m unittest discover -p 'test_*.py'
    python evaluate.py ../bfg-realization-development-2026-10-07/data ../pendulum-mechanical-identification-2026-10-07/results/models.csv results

Dependencies: numpy, scipy; all derived scores are published. Local verification completed; no new GitHub Actions run is claimed. Next obligation: independently constrained input/phase coupling and physical calibration rather than rebranding a supplied flow as BFG emergence.
