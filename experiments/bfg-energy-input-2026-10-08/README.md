# Real-data energy/input bridge and phase closure

Active source: Dynamic Order, sections84,86,88–89; scalar f and the separately declared input model are used. Observable E=w²/2+a(1-cos(theta)) is additionally supplied mechanical energy per inertia, not SI joules or canonical formation stock. y=E/s and positive geometric input are additional hypotheses. This package tests feasibility on15 real development recordings, not universality or confirmation.

## Constructed causal feedback

On0<y<1/4, f is strictly increasing with image(0,1/4). For any desired retention r with0<r*y<1/4, define

    d_r(y)=f_inverse(r*y)-y.

If0<d_r(y)<3/4, then f(y+d_r(y))=r*y exactly. This is causal: r is fitted on development calibration and the input uses current y, not the next target. It is a new feedback policy, not the constant-input theorem's exogenous d. Its closed-loop derivative is r, not automatically the16/27 exogenous bound. Near y=0, d_r(y)~sqrt(r*y/2)-y and its derivative is singular. It does not preserve a positive geometric reserve indefinitely when r<1. A positive geometric input also does not imply physical energy injection: under the declared bridge, deltaE=(r-1)E<=0. The input is a coordinate/control construction, not an identified external physical power source.

An inverse input using measured next y can exactly reconstruct admissible calibration pairs. That is an oracle diagnostic only; it is never used to forecast. All4485 calibration pairs admit such input, but this does not prove a prospective physical law. Arbitrary admissible outcome sequences can be encoded when the input is selected from their future values.

## Energy alone fails physical factor closure

For supplied passive sine mechanics with b>0, E'=-b*w². Choose0<E<a. Two states with equal E are(theta=0,w=sqrt(2E)) and(theta=arccos(1-E/a),w=0). Their energy derivatives are respectively-2bE and0. Thus equal energy does not give equal projected successors for sufficiently short positive time. The energy-only projection fails the paper's section89 fiber criterion. A state-dependent energy-only retention policy cannot recover phase-dependent dissipation for every physical state. At b=0 this particular obstruction disappears; the statement is conditional.

Keeping measured angle and velocity gives a closed mechanical state and an energy prediction from its future trajectory. Those mechanics remain additionally supplied; their successful comparison does not derive the force law from BFG. Next BFG realization must retain an independently prepared phase-sensitive variable or demonstrate an appropriate averaging regime instead of assuming energy is sufficient.

## Protocol, data and comparison

PROTOCOL.md was fixed before candidate evaluation. A subsequent completeness amendment adds the strong full-sine mechanical rival with identical coefficients and scores. Source15 attempt-1 recordings, EnzeXu/Damped_Pendulum_Dataset commit cbf82673641ecd65e902ad5c38a048387649a2a0; primary Xu et al., TMLR2026 https://openreview.net/forum?id=xvQYvYEGhj. Reserved attempts2/3 remain unopened. Source hashes and published coefficient hash are in summary.json.

Calibration seconds0–30: scale s=8*max calibration energy, constant d by bounded least squares, passive r by clipped linear least squares. No validation-based scale adjustment. The factor8 is a declared coordinate choice, not uniquely BFG-derived. Initial angle/velocity and gravity coefficient come from prior published calibration. Predictions start every0.1s in seconds30–60, horizons0.1,1.6,6.4s, using only the initial measured state. Models are persistence, autonomous f, constant input, passive retention, equivalent causal BFG feedback, and full nonlinear mechanical energy. Autonomous recursion is computed in log-state coordinates, preserving positive latent geometry even when displayed energy underflows; a literal zero-load canonical event is not run.

All15 included,100% forecast coverage, no excluded pairs. Relative RMSE divides by each recording's target energy RMS, then averages equally. Overlapping windows and repeatedly reused development data preclude independent confirmation. No confidence interval or significance claim.

| Horizon | Persistence | Autonomous | Constant input | Retention / causal feedback | Full sine mechanics |
|---|---:|---:|---:|---:|---:|
|0.1s,4485pairs|0.108735|0.940689|1.315278|0.108342|0.107224|
|1.6s,4260pairs|0.136327|1.000000|2.323410|0.150575|0.117845|
|6.4s,3540pairs|0.290570|1.000000|2.786275|0.334963|0.138288|

The fixed positive input is a poor predictor under this energy bridge. The constructed feedback matches retention to numerical tolerance; that candidate is worse than persistence at longer horizons. Full sine mechanics is strongest in the tested family, with6.4s error52.4% below persistence. This is an exploratory comparator result, not new BFG-only force emergence. Preserve all negative results and do not tune this bridge on reserved data. A stable latent fixed point is insufficient for a physically accurate scalar energy forecast.

## Verification and reproduction

Four controls passed: independent rational inverse f(1/2)=8/45; causal feedback identity across declared states; log-state positivity through64events; inverse domain gates. An initial local test invocation lacked the sibling import path; corrected workspace PYTHONPATH passed. GitHub sibling layout resolves the same import normally. Synthetic cases are code controls only; scores above use real data.

    python -m unittest -v test_energy_input.py
    python energy_input.py ../bfg-realization-development-2026-10-07/data ../pendulum-mechanical-identification-2026-10-07/results/models.csv results

Pinned numpy2.3.5/scipy1.17.0. SHA256SUMS preserves code, protocol, all per-record scores, fitted parameters and source provenance. One bounded GitHub reproduction(max45minutes) checks hashes, downloads only pinned development recordings, runs controls and regenerates results.
