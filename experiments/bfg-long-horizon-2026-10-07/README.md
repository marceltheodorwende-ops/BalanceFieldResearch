# Development-only long-horizon pendulum realization

Question: can a fixed analytic phase correction reduce the long-horizon error of the calibrated BFG representation?

This is exploratory, motivated by observed development errors. It is not a confirmatory test or a derivation of mechanical forces from BFG alone. All 15 attempt-1 recordings are included; attempts 2 and 3 remain untouched. Source: EnzeXu/Damped_Pendulum_Dataset, pinned commit cbf82673641ecd65e902ad5c38a048387649a2a0; real PASCO measurements, Xu et al., TMLR 2026, https://openreview.net/forum?id=xvQYvYEGhj. Source files and SHA checks are supplied by the existing development downloader.

## Conditional derivation

Assume the additional mechanical equation theta'' + b theta' + a sin(theta) = 0, weak damping and small amplitude. Set Omega = sqrt(a-b²/4). The cubic expansion sin(theta) = theta-theta³/6+O(theta⁵) and fundamental harmonic cos³(psi) = (3cos(psi)+cos(3psi))/4 give the leading frequency correction psi' = Omega-a A²/(16 Omega). Averaging uses A(t)=A0 exp(-bt/2); omitted higher harmonics, higher amplitude orders and damping cross terms make this an approximation, not an exact solution.

With F=A0² and phase K, integrating gives

    psi(t) = K + Omega*t - a*F/(16*Omega) * (1-exp(-b*t))/b
    theta(t) = sqrt(F)*exp(-b*t/2)*cos(psi(t))
    w(t) = -sqrt(F)*exp(-b*t/2)*(b*cos(psi(t))/2 + psi'(t)*sin(psi(t)))

For b=0 the integral factor is t. The existing BFG carrier keeps F,K invariant and advances its geometric event clock N; use t=0.1*N. Macroblocks 2^j are powers of the same event map, not evidence of spatial fractality. This is a revised observable on that carrier. Parameters a,b, the clock-to-seconds mapping and the mechanical equation are additional assumptions. There is no new fitted correction coefficient: 1/16 comes from the stated cubic approximation. Initial F,K reconstruct both measured initial angle and velocity through the fixed-point preparation in phase_corrected.py. Gates require an underdamped regime, positive phase rate, convergence and amplitude <=1 rad; no gate caused an exclusion on these data.

## Evaluation

Reuse published coefficients fitted on seconds 0-30, without refitting. Forecast seconds 30-60 at 0.1-second start spacing and horizons 0.1,0.2,0.4,0.8,1.6,3.2,6.4 seconds. Every forecast uses only its initial state. Longer-horizon pairs overlap and are not independent. Scores are per-record RMSE divided by target RMS, then equally averaged across the 15 records. This differs from earlier normalization by persistence increments. No confidence interval or significance claim is made.

The strong rival integrates the full sine mechanical equation with the identical free a,b, RK4 step <=0.005 seconds. Shared-inertia calibration is a separate existing comparator. At 6.4 seconds, 3540 pairs:

| Model | Angle normalized RMSE | Velocity normalized RMSE |
|---|---:|---:|
| Persistence | 1.499186 | 1.502682 |
| Linear BFG, free calibration | 0.218393 | 0.249122 |
| Linear BFG, shared calibration | 0.218229 | 0.245549 |
| Phase-corrected BFG observable | 0.088297 | 0.128974 |
| Full nonlinear mechanical rival | 0.088291 | 0.128745 |

The correction reduces angle error by 59.6% and velocity error by 48.2% relative to the free linear representation. It does not outperform the mechanical rival. The original linear failure remains published. Remaining limitations include measurement quantization, offline cleaned data, overlapping windows, externally calibrated dynamics and approximation error. A frozen confirmatory structure and decision rule must precede any access to untouched attempts; these results do not authorize tuning on holdout data.

## Reproduction

From this directory, after the existing development downloader:

    python -m unittest -v test_phase.py
    python evaluate_long.py ../bfg-realization-development-2026-10-07/data ../pendulum-mechanical-identification-2026-10-07/results/models.csv ../bfg-shared-calibration-2026-10-07/results/models.csv results

Tests use independent elliptic-integral periods, a matrix exponential small-amplitude reference, exact initial-state reconstruction and domain rejection. Synthetic inputs are code controls only. results/recordings.csv preserves all per-record outcomes; results/summary.json gives all horizons. SHA256SUMS covers the published package. GitHub Actions reproduces it with a 45-minute upper bound.
