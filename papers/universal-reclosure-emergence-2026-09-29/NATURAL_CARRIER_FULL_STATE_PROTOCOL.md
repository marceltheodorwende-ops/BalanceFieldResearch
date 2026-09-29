# Natural-carrier full-state and selective-intervention protocol

**Prospective design amendment, 29 September 2026. Status: measurement and intervention design; no natural-system pass claimed.** This supplement supplies a concrete route from natural measurements to the [full finite candidate and strong-emergence criterion](BFG_Universal_Reclosure_and_Emergence_Preprint_2026-09-29.pdf). The mathematical BFG update is held fixed. The physical role map below is an **empirical hypothesis to identify and freeze**, not a theorem derived from Level 0 or a retrospective fit.

## 1. An actionable physical carrier

A controllable three-oscillator electronic circuit is a suitable *candidate* because individual oscillator voltages can be measured and pairwise versus three-body couplings can be changed independently. A published experimental dataset records six x/y voltages from three Rössler-like circuits over 100 × 100 settings of linear and nonlinear coupling for each of four wiring scenarios (Vera-Ávila et al., *Data in Brief* 57 (2024) 111145, doi:10.1016/j.dib.2024.111145; Dataset I doi:10.5281/zenodo.10408252). It is an **exploratory feasibility source**, not a completed BFG removal/restoration study: it has no independently instrumented higher reporter, no fixed full BFG state map, and coupling-strength sweeps do not guarantee paired or randomized return to the same physical condition. Do not treat a synchronization score calculated from the same three voltages as an independent higher measurement.

A new prospective acquisition would need three physical oscillator channels, measured pairwise and three-body drive/current channels, the commanded and measured coupling strengths, common exogenous perturbations, and an **additional dynamically independent downstream reporter** `h` with its own sensor and update. Instrumentation must resolve its direct inputs and possible bypasses. The reporter must remain measurable when the proposed three-body coupling is disabled. The third oscillator cannot simultaneously be counted as an independent higher reporter and as an unmodified source inside the removed triplet without a separate causal account.

## 2. Freeze an identifiable map to every full-state entry

Use one finite carrier `H=R^d`, a fixed dimension, units, sampling grid, calibration window, sensor synchronization correction, uncertainty model and error tolerance. Freeze the following estimators **before** opening confirmatory interventions. A window with an unidentifiable entry is marked `NOT_MAPPABLE`; algebraic values selected for positivity alone are not measurements.

| Full BFG state | Required separately checkable measurement/identification |
| --- | --- |
| `D_cap, coherence, emergence` | Three self-adjoint capacity estimates from separately controlled response channels and a prespecified joint calibration. The observed formation operator must satisfy `K=coherence+emergence−D_cap` with held-out residual within its fixed uncertainty. Measuring only `K` leaves infinitely many capacity triples and fails identifiability. |
| `formation_density rho_F` | Positive nonzero profile reconstructed from a calibrated physical formation coordinate and magnitude; report eigenvalues, trace and sensor error. A chosen rank-one vector chart requires an experimentally justified axis. |
| `witness rho_W` | Separately measured persistence/identity tag mapped to a positive unit-trace operator; show stability and tag transport across all arms. It cannot simply be copied from `rho_F`. |
| `neutral load Y` | Identify a source-to-neutral response `A` with independently measured input and neutral output, then set `Y=A†A` in the *locked* source metric. Test the resolvent against held-out perturbations. The Hessian of the Level-0 formed branch may supply its source metric, but its correspondence to this measured channel is an empirical identification. |
| `recursive transport R_C` | Estimate an autonomous one-step response from time-resolved physical perturbations on a disjoint calibration set; check power boundedness and an isolated peripheral sector. The persistent projector `P` is then computed by the BFG spectral/graph-metric rule, not fitted to the target `h`. |
| `carrier and alignment` | Independent clock, unit and orientation calibrations linking every measured channel to the same finite carrier; record missing channels and uncertainty propagation. |

Check all state gates on untouched calibration data. Run `bfg_universal_state_update` from the **same frozen state estimator and fixed completion laws** in every arm. A failure of rank, positivity, spectral separation or the formation gate is a recorded terminal or indeterminate result, not a license to repair parameters after outcomes are known.

## 3. Physical arms, controls and decision order

Within randomized repeated units, acquire: `FULL` (pairwise coupling `σ1` and proposed three-body coupling `σ2` on), `REMOVE` (the actual three-body signal path physically disabled, `σ2=0`, with `σ1`, drives, export and sensing unchanged), `RESTORE` (same pathway and frozen `σ2` restored), and sham switching. Log the commanded and measured intervention and match or model initial-state/exogenous differences. A computer deletion of the fitted `σ2` term is a **model ablation**, not the physical removal arm. Preserve the raw time series and audit every arm, including failures.

1. Test each source's prespecified persistence/closure gate in `FULL`, `REMOVE`, and `RESTORE`. If source closure fails when `σ2=0`, the higher-channel loss cannot isolate a necessary relation among still-closed sources.
2. Apply the *same* frozen full-state map and finite successor to each arm. Confirm admissibility, identity continuity and any internal novelty separately. These properties do not decide causal irreducibility.
3. Score an independently measured reporter's prespecified recovery/closure `Q(h)`. Require a positive paired `Q_FULL−Q_REMOVE` with its one-sided 95% lower confidence bound above zero after the prespecified multiplicity correction, and recovery under `RESTORE` within the predeclared equivalence margin. Report a sham effect and sensor drift.
4. Fit rival classes on training units only: common driver, additive independent histories, direct pairwise coupling with the same effective memory, alternative physical pathways and matched-capacity latent dynamics. Compare held-out reporter trajectories and all intervention signatures with fixed error tolerances. An exact coordinate clone is logged as an identifiability tie and is not a rival required to lose.
5. Claim **specific irreducible higher closure** only if all preceding gates pass and a selective measurement/intervention identifies the proposed physical mediator against the genuinely distinct rivals. Otherwise report `FAIL`, `INDETERMINATE` or a weaker internal-novelty finding.

## 4. Current evidence gate

The repository's sunspot, CO2 and ENSO series have neither this complete state instrumentation nor physical `FULL/REMOVE/RESTORE` arms; their preflight forecast scores cannot be relabelled as this experiment. The public oscillator recordings offer a promising *screen* for independently varied coupling, but the additional reporter and prospective matched intervention are still missing. **No actual natural-carrier outcome is entered here.** The [full successor audit](FULL_SUCCESSOR_NATURAL_EVIDENCE_AUDIT.md) remains the current result until real measurements satisfying this protocol exist.
