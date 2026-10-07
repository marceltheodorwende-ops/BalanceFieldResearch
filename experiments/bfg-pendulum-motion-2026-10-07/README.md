# A calibrated BFG representation of pendulum motion

Status: constructive exploratory realization with explicit mechanical
calibration. The canonical scalar BFG step is unchanged.
Physical coefficients and observables are additional hypotheses; no emergence
of mechanical laws from BFG alone is claimed.

## How motion is represented

Use the scalar state (K,F,W,Y,P), with W=P=1, F>0 and 0<Y<1.
The actual ambient BFG update yields

    K_plus=K, F_plus=F, Y_plus=f(Y),
    f(y)=2*y^2/((1+y)^2*(1+y^2)).

There is no complement or seed in this nonterminal one-dimensional case.
K may store a real phase and F a positive amplitude square.
Unlike the failed stationary formation-only readout, physical observables
now depend explicitly on the evolving geometry Y.

Let phi(f(y))=phi(y)^2 be the previously constructed scalar coordinate.
For fixed reference y0=0.25 define

    N(y)=log2((-log(phi(y)))/(-log(phi(y0)))).

Then N(y0)=0 and N(f(y))=N(y)+1, exactly.
Declare one internal event to correspond to calibrated physical duration dt.
Thus t=dt*N(Y). This is an added clock calibration, not physical seconds
selected by the dimensionless BFG map.

## Physical preparation and readout

Assume the underdamped linear equation
theta_ddot+b*theta_dot+a*theta=0, with a>b^2/4 and b>=0.
These coefficients are effective mechanical ratios, estimated on development.
Put omega=sqrt(a-b^2/4). For initial theta0,w0 define

    q=(w0+b*theta0/2)/omega,
    F=theta0^2+q^2,
    K=atan2(-q,theta0), Y=y0.

The observable is

    theta=sqrt(F)*exp(-b*t/2)*cos(omega*t+K),
    w=-sqrt(F)*exp(-b*t/2)*
        (b*cos(omega*t+K)/2+omega*sin(omega*t+K)).

It reconstructs the measured initial state and evolves to the exact linear
oscillator state at dt after one actual canonical BFG step. It also represents
successive states for arbitrary integer event counts in exact arithmetic.
Consequently this declared projection satisfies a semiconjugacy to that
linear mechanical flow on the scalar branch.

This is an encoding through a chosen clock/observable: the mechanical
frequency and damping are built into the projection, not predicted internally.
A fixed calibrated a,b,dt and readout must accompany any physical claim.
Choosing new coefficients or observables per target is not universal prediction.
The phase variable is defined modulo 2*pi in the physical projection.
The exact rest state F=0 would trigger zero-load gates; rest requires a
declared terminal/limiting completion and is not claimed as a nonterminal
representation. No evaluated inputs here have zero amplitude.

## Numerical representation

Raw y converges too fast to remain representable in double precision over
many events. The equivalent internal coordinate l=log(phi(y)) updates as
l_plus=2*l; N=log2((-l)/(-l0)).
This numerically stable coordinate stores the mathematically conjugate scalar
recursion. It is not a newly assumed physical force law. The published checks
cover 600 clock events, while raw y is used only for short controls.
Trajectory forecasts beyond one-step reset require careful numerical handling,
and exact encoding does not establish robustness to uncertain coefficients.

## Real development-data check

Use the same 15 attempt-1 PhysioNet-independent real pendulum recordings.
Effective a,b are taken from the preceding viscous fits on seconds0–30.
Forecast consecutive 0.1-second blocks in seconds30–60 using only their initial
measured angle/velocity. No future measured states enter a forecast.
4,485 transitions; all 30 reserved attempt-2/3 recordings remain unopened.

Mean per-record RMSE divided by the corresponding persistence increment RMSE:

| Observable | Calibrated BFG representation | Persistence |
|---|---:|---:|
| Angle | 0.082509 | 1 |
| Angular velocity | 0.255849 | 1 |

These are exploratory internal temporal validation scores.
The representation is mechanically equivalent to the linear oscillator.
It cannot provide independent superiority over that same oscillator.
The preceding nonlinear sin(theta) rivals remain a different comparison.
Short-horizon success does not validate physical universality or causal
interventions, and no confidence interval or confirmatory success is claimed.

## Verification

Six controls pass: initial reconstruction, independent matrix-exponential
comparison, exact clock increment, 600-event stable coordinate, underdamped
domain rejection, and 100 actual ambient BFG state updates/readouts.
The last check preserves F,K and recovers f(Y), then matches the independent
linear state-transition matrix. Synthetic cases are controls only.

Reproduce with the preceding pinned NumPy/SciPy environment:

    PYTHONPATH=../real-eeg-covariance-2026-10-07 python -m unittest -v test_motion.py
    python evaluate.py ../bfg-realization-development-2026-10-07/data ../pendulum-mechanical-identification-2026-10-07/results/models.csv results

Derived forecasts, per-record statistics and source provenance are published.
A bounded GitHub reproduction verifies code and development pipeline.
Read the run status before claiming remote completion.

## What changed scientifically

A movement-bearing calibrated BFG representation now exists for the linear
underdamped approximation. The earlier energy-only and inherited-formation-only
failure findings remain. The actual internal geometry supplies an event clock;
the physical readout supplies calibrated oscillatory phase and damping.

The next task is to constrain that clock and readout independently and test
shared physical intervention parameters. Without such constraints, reproducing
a known oscillator is a mathematical realization, not its uniquely derived
physical explanation. The model remains exploratory until an appropriate
new protocol is frozen before opening independent test observations.

