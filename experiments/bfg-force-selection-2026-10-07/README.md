# Force selection: conditional geometry and real-data harmonic stress

## Selection theorem under additional physical premises

Assume a planar rigid arm of fixed length L>0, a bob of mass m>0, uniform gravitational acceleration vector, potential linear in vertical height, and independently calibrated inertia I>0. These are named additional physical coupling premises, not canonical BFG axioms. With downward angle theta and upward vertical coordinate z(theta)=-L*cos(theta), the gravitational potential relative to rest is

    V(theta) = mg*(z(theta)-z(0)) = mgL*(1-cos(theta)).

Virtual work gives torque tau=-dV/dtheta=-mgL*sin(theta). With passive viscous torque -B*w and constant inertia, angular balance yields

    theta'' + (B/I)*theta' + (mgL/I)*sin(theta) = 0.

The assumptions select sine up to the calibrated coefficient. A linear-in-height premise explicitly forbids a second-harmonic potential; angle periodicity and passivity alone do not, as proved in the preceding nonlinear package. Units: V [J], torque [N m], I [kg m²], mgL/I [s^-2], B/I [s^-1]. Rest, reflection symmetry and 2pi periodicity agree. The exact nonlinear BFG readout can represent this selected flow via its derived event clock, but that representation does not derive these physical premises.

A length-change intervention under the additional point-bob plus shared pivot-inertia hypothesis gives a(L)=gL/(L²+lambda), lambda=I0/m, already tested in the shared-calibration package. Drag-only changes predict invariant potential when geometry/mass remain fixed. Available passive recordings do not establish a calibrated causal intervention; baffle inertia/geometry can confound that prediction.

## Development experiment

Question: do the existing observations justify adding a passive second harmonic, or does its extra flexibility harm forecasting?

15 real attempt-1 recordings only, from EnzeXu/Damped_Pendulum_Dataset pinned cbf82673641ecd65e902ad5c38a048387649a2a0. Primary paper: Xu et al., TMLR 2026, https://openreview.net/forum?id=xvQYvYEGhj. Use existing pinned source downloader; source SHA256 hashes saved in results/provenance.json. No attempt-2/3 file accessed. Exploratory protocol developed after earlier development analysis; not confirmatory evidence.

Compare three separately fitted nonnegative integral-balance models:

    linear: theta'' + A*theta + b*w = 0
    sine: theta'' + A*sin(theta) + b*w = 0
    harmonic: theta'' + A*sin(theta) + C*sin(2*theta) + b*w = 0.

A,C,b>=0 make the harmonic potential A*(1-cos(theta))+C*(1-cos(2*theta))/2 nonnegative and E'=-b*w². Nonnegative potential does not imply that zero is the only potential minimum. Fit 299 disjoint 0.1-second integral blocks whose end time is below30 s. Normalize design columns before NNLS and undo scaling. Forecast starting from measured angle/velocity in seconds30-60 at 0.1-second spacing, horizons0.1 and6.4 s, with RK4 step<=0.005 s. No future state feeds into a forecast. All15 recordings included, no exclusions. Longer windows overlap.

Scores divide each recording's RMSE by target RMS, then average equally across records. No independent-window bootstrap or significance claim. Linear coefficients here are refitted for the linear equation; the earlier linear BFG comparator reused sine-calibrated coefficients, so these are different named comparisons.

| Horizon | Model | Angle normalized RMSE | Velocity normalized RMSE |
|---|---|---:|---:|
|0.1s|linear|0.040139|0.126644|
|0.1s|sine|0.040024|0.126094|
|0.1s|second harmonic|0.040027|0.126120|
|6.4s|linear|0.217691|0.236686|
|6.4s|sine|0.088291|0.128745|
|6.4s|second harmonic|0.345298|0.357471|

Pairs4485 at0.1s and3540 at6.4s. Additional harmonic is positive in14/15 fits, yet forecasting is much worse at6.4s. Scaled harmonic design condition ranges30.44–221.66. Small-amplitude expansion explains the confounding:

    A*sin(theta)+C*sin(2theta)
      = (A+2C)*theta - (A+8C)*theta³/6 + O(theta⁵).

Near rest the linear combination A+2C is strongly observed while A,C separately require sufficient reliable amplitude-dependent information. Data errors and approximate integral fitting can amplify coefficient instability. The condition number is a diagnostic, not a calibrated uncertainty interval or proof of the unique cause of failure. More nonlinear flexibility is not automatically useful. Preserve this failure; do not select the harmonic model or tune on sealed data. The sine law performs better within this tested family, but this does not establish unique truth or BFG-derived forces.

## Verification and reproduction

Three mathematical/code controls pass: geometric torque by independent finite differences, linear RK4 against matrix exponential, harmonic RK4 against adaptive DOP853, both solvers compared at6.4s. Controls are synthetic only; empirical results above use real data. Code, parameters, per-record scores and provenance are retained.

    python -m unittest -v test_selection.py
    python selection.py ../bfg-realization-development-2026-10-07/data results

Pinned numpy2.3.5/scipy1.17.0. SHA256SUMS covers published files. One bounded GitHub Action reproduces verified source downloading, controls and scores with max45 minutes. Remaining physical coupling, measurement uncertainty, holdout freezing and genuine intervention constraints stay explicit. No new BFG force-selection axiom has been proved.
