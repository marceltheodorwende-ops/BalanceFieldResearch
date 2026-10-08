# BFG empirical research program

Authorization: the repository owner requested continued background research,
completion reports and subsequent experiments, prioritizing real measurements
and extending beyond EEG into physics, chemistry or biology.

## Completed EEG experiment

Branch: experiment/real-eeg-covariance-2026-10-07.
Protocol freeze: 37f31b1b8aae878418fe2510a55b7896bb114579.
Paper source: 76d9e87b4275ec41b3dcd84434e2ee3791a8d076.
Successful completed workflow: 37681346583.
Published results commit: d1e4a2d8bb02de4ea2cbc97c7fd6d590d23c40b9.
GitHub report: experiments/real-eeg-covariance-2026-10-07/README.md.

69 held-out people, 3,685 prediction pairs; 100% model coverage;
28 rejected windows in the entire cohort, zero excluded recordings.
Mean relative Frobenius error: BFG 0.8674, persistence 0.5864,
linear 0.6655, frozen geometry 1.2206.
Paired BFG-minus-persistence 0.2810, 95% CI [0.2193,0.3299];
BFG-minus-linear 0.2019 [0.0428,0.3134];
BFG-minus-frozen -0.3532 [-0.8150,-0.0539].
Frozen practical success criterion failed. This tests the additional EEG
bridge, not a general rejection of the abstract BFG construction.
Seven code controls passed. Independent spectral calculation reproduced all
3,685 held-out losses (max absolute residual 7.105427357601002e-15);
subject bootstrap and artifact checksums independently verified.
MATHEMATICAL_ASSESSMENT.md documents derivation and conditional bridge theorem.

Initial run 37674587952 failed downloading before empirical evaluation.
Official AWS mirror plus official SHA256 verification repaired transport.
Run 37680650640 had invalid YAML; 37680964493 produced identical empirical
results but publication failed because of root gitignore; corrected publication
completed in 37681346583. Do not repeat or announce those as new findings.
Reporting record: completed negative EEG result, independent verification and
next frozen pendulum protocol are included in the current user-facing completion
report on 2026-10-07. Do not send a duplicate EEG completion notification.

## Current priority: exploratory realization

Strategy changed by the user on 2026-10-07. Prioritize the two-stage realization
below before additional confirmatory experiments. The previous pendulum protocol
25855b7d44417ea7c23da62630a63290cf25a3d3 remains an immutable historical proposal;
its holdout evaluation is deferred and must not be launched automatically.

### Stage 1: development-only exploration

Use the current architecture only on development observations. Test feasibility,
stress the carrier map and find failure modes. Track each mapping proposal and
whether its structure is derived from BFG, independently motivated measurement
assumptions, or a fitted convenience. Changing a bridge is allowed here but all
results remain exploratory. Performance alone does not establish derivation.

For the existing pendulum candidate on experiment/real-pendulum-decay-2026-10-07,
only attempt 1 (15 recordings) may be downloaded or inspected. Attempts 2 and 3
(30 recordings) remain sealed. Primary source and pinned commit:
EnzeXu/Damped_Pendulum_Dataset, cbf82673641ecd65e902ad5c38a048387649a2a0.
The linear energy bridge is a hypothesis, not an established BFG realization.
Check carrier-state identifiability, preparation, units/scale, basis invariance,
rank/gates/terminal behavior, clock, observables, noise robustness and forecast
information availability. Report failures and missing physical identifications.

Specify intervention logic and falsifiable response predictions, including what
interventions the real dataset actually supports. Passive recordings cannot
establish causal intervention effects. If intervention evidence is absent,
document the missing dataset or design instead of claiming causal confirmation.

Already inspected EEG holdout subjects cannot confirm any revised hypothesis.

### Stage 2: frozen confirmatory realization

Proceed only when a derivation dossier and reproducible implementation fully
specify the claimed BFG-derived structure, with all additional empirical
assumptions explicitly separated. Freeze carrier map, preparation, state update,
observables and clock, intervention logic, rivals, preprocessing, exclusions,
sample/split, uncertainty procedure and decision rule in a commit before
accessing untouched subjects/data. Include strong physical/statistical rivals.
If no testable bridge exists, document the open requirement and remain in Stage 1.
Confirmatory claims are limited to the frozen realization and supported tests;
prediction and intervention claims must be distinguished.

Preserve independent test observations and prohibit development downloads that
include holdout files. Do not tune scientific criteria using held-out outcomes.
Current task: assemble the development-only realization/derivation dossier,
then run bounded exploratory analyses; do not resume the old pendulum holdout
instruction. Prefer mathematically justified conclusions over positive scores.
Strategy update is reported to the user; no empirical result claimed.

## Rules for subsequent experiments

Use real open measurement datasets as primary evidence. Synthetic inputs are
permitted for implementation controls, not as substitutes for empirical results.
After finishing the current experiment, select a justified non-EEG experiment
in physics, chemistry or biology. State precisely which additional preparation,
clock, observable or transition bridge is being tested; the paper does not
already supply these physical identifications. If a predictive bridge cannot be
specified, record that obstacle rather than inventing a derived physical law.

Freeze each question, preparation, preprocessing, model, baseline, split and
loss before held-out evaluation. Never tune to a previously inspected holdout
and present it as independent confirmation; use genuinely new test observations
for revised hypotheses. Keep at most one new empirical experiment active.
Use dedicated branches and bounded GitHub Actions runs (at most 45 minutes per
run). Do not merge into main, rewrite papers, use paid services, contact third
parties or access restricted data without separate authorization.

Publish code, provenance, exclusions, sufficient statistics, uncertainty,
results and limitations. Verify GitHub upload and the actual run outcome before
claiming completion. Maintain this ledger with current branch/run, completed
experiments and already-reported outcomes to avoid duplicate reports.

## Reporting

On each completion report what was tested, how it finished, sample size,
comparison results, uncertainty, limitations and GitHub links. If blocked, say
what failed and whether any results exist. Continue with one justified next
experiment after a completed result; avoid indefinite loops of identical retries.

## Development audit checkpoint (2026-10-07)

Published on experiment/real-pendulum-decay-2026-10-07 under
experiments/bfg-realization-development-2026-10-07/.
Local development analysis completed: 15 real recordings, 1,364 pairs,
zero rejected pairs; no holdout files downloaded or inspected.
Mean relative L2 errors: scalar BFG 0.712943, persistence 0.065288,
in-sample fitted decay 0.054072. Five standalone controls passed;
1,000 comparisons with the existing ambient update matched to 1.67e-16.
Rounding stress did not repair the mismatch. INTERNAL_MATH.md derives a
scale-independent 35.63% maximum energy retention; all development pairs
retained more than 50%. This rejects this added linear scalar energy bridge
as a feasible candidate, not the full BFG architecture.
REALIZATION_DOSSIER.md states carrier, closure, reset, clock and intervention
requirements. Confirmation gate remains unmet. The old holdout protocol is
still deferred. A bounded development-only verification workflow accompanies
publication; inspect actual status before reporting remote verification.
Next: use internal mathematics to audit nonlinear observables, independent
clock calibration and carriers retaining angle/velocity; label additional
hypotheses and do not tune for positive holdout results. No justified full
physical map is claimed. Continue development only. Preserve failed candidates.
User requested regular GitHub checkpoints and occasional meaningful progress
reports, including failures. Notify on completed work packages or important
obstacles, without duplicating this reported checkpoint.

## Internal mathematical construction and verification repair

NONLINEAR_OBSERVABLE.md in experiments/bfg-realization-theory-2026-10-07/
derives phi(f(y))=phi(y)^2 and H_p(f(y))=2^(-p) H_p(y) for an
inverse-log observable. Numerical controls: 999 inputs and four powers,
residuals below 1.8e-15. This constructs scalar decay equivalence but does
not derive physical energy or establish independent predictive superiority.
A fitted per-condition p simply encodes the fitted decay rival. Audit shared
physical calibration and intervention constraints before promoting a bridge.
User explicitly requests creative use of internal mathematics and authorizes
routine GitHub work without repeated permission questions.
First development verification run 37683972787 failed before download/evaluation
because text publication normalized CRLF CSV files while manifest hashed CRLF.
Repair canonicalizes CSV output to LF and regenerates affected hashes;
numeric values and scientific design unchanged. A single repair push starts
one bounded replacement run; check latest run before any further launch.
Local tests remain passing. All holdout files remain sealed.

## Verified publication checkpoint

Replacement GitHub Action 37684530408 completed successfully.
All five controls, 15-file source verification, development analysis,
rounding stress, structural-bound calculation and artifact upload succeeded.
Logs reproduce local counts and errors exactly. Artifact 11510835869,
BFG-development-only-realization, 80,581 bytes, expires 2026-11-06.
Audit and constructive theory published at commit
 efa2e929ee9e15e496e8194163eb90af01530f53 (without leading whitespace).
No active empirical run at this checkpoint. No holdout files accessed.
The user-facing checkpoint reports completed development audit, failed linear
bridge, constructive nonlinear observable and outstanding physical derivation.
Do not repeat these completion findings as new results. Next package remains
shared observable calibration, identifiability/closure and intervention audit,
with development-only code and regular GitHub checkpoints. Strong mathematical
results are valuable even when no physical realization is yet justified.

## Revision policy requested by owner

At every poor development result, investigate mathematical restructuring of
BFG carrier, preparation, observable, clock and intervention representation.
Be creative with internally valid combinations, but preserve failed versions.
Record failure mechanism, exact derivation, new assumptions, parameter freedom,
comparison with rivals and remaining identifiability obligations for each version.
Treat empirical universality as a hypothesis/aspiration, not an established fact.
Do not rewrite negative findings, invent physical bridges or optimize an opened
holdout. Revised hypotheses stay development-only until a new full protocol is
frozen and untouched confirmation data are available. If a new construction
merely encodes a rival, report that equivalence explicitly. Next meaningful
updates should describe both constructive successes and unresolved obstacles.

## Physical calibration / intervention audit

New development-only package: experiments/bfg-realization-theory-2026-10-07/
PHYSICAL_CLOSURE_AUDIT.md, calibration_audit.py and calibration_result.json.
A fixed inverse-log observable imposes constant event retention. Rounding-only
feasibility intervals on existing 1,364 development pairs have empty intersection:
lower 1.51589, upper 0.61761; conflicting witnesses are within the same recording.
Not a full sensor-error model; apparent increases do not establish energy creation.
A mathematically explicit continuous interpolation and rate intervention map is
constructed, but reproduces an ordinary exponential decay rival in new coordinates.
Physical observable, rate/intervention calibration, clock and full carrier closure
remain unestablished. The user's request to close the point does not supply a
physical derivation. Report this limitation honestly and continue the listed
development tasks; never claim the physical bridge is completed or open holdout.
This checkpoint's findings are reported to the user; no duplicate notification.

## Conditional physical explanation checkpoint

CONDITIONAL_PHYSICAL_EXPLANATION.md published on the pendulum branch.
Derives passive torque power balance and weak-viscous exponential energy
envelope kappa=b/I; adds explicit quadratic and dry-friction rivals and baffle
drag scaling. These are declared mechanical assumptions, not derivations from
BFG axioms. Connects their viscous envelope exactly to the scalar continuous
BFG representation. Demonstrates nonuniqueness under free observable and clock:
internal f does not determine C,p,kappa, energy units or seconds.
Inspected source metadata lacks calibrated inertia, COM/mass, baffle geometry,
drag coefficients and full uncertainty. Physical explanation is conditional;
unconditional BFG coupling derivation remains open. User-facing report states
this distinction. No holdout access or new active empirical run.
Next development package: fit and compare physically motivated viscous,
quadratic and dry-friction models on attempt-1 angle/velocity, audit state
identifiability and sensor uncertainty, seek independent coupling constraints.

## Autonomous closure work queue

Owner requests execution of open work packages in the existing background
continuation, not repeated lists of missing assumptions. Work sequentially:
1. Audit primary sensor/apparatus metadata and a defensible measurement model.
2. Identify estimable parameter combinations; fit strong viscous/quadratic/dry
   friction rivals on the 15 allowed development recordings and inspect residuals.
3. Develop BFG carrier, observable, clock and projection, separating derivation,
   assumptions and fitted conveniences; expose equivalence to mechanical rivals.
4. Seek shared calibration and intervention transformations with discriminating
   predictions across conditions. Keep all 30 reserved recordings sealed.
Each continuation must deliver a concrete verified code/data/theory/source
checkpoint, or demonstrate a specific obstruction and advance the next solvable
package. Retain negative findings and status: derived, hypothetical, empirically
examined, rejected or nonidentifiable. No invented proof or guarantee of universal
closure. Existing hourly background task updated; no additional automation.
Notify on meaningful new completed packages or important obstacles; avoid repeats.

## Immediate development mechanical identification

New package: experiments/pendulum-mechanical-identification-2026-10-07/ on
experiment/real-pendulum-decay-2026-10-07. The owner explicitly requests regular
updates on this same branch and short German status every 60 minutes; this
supersedes earlier no-routine-status language. Existing hourly task updated.
Local completed analysis on 15 attempt-1 recordings: integral balance fitting
in first 30 seconds, causal 0.1-second forecasts in second 30 seconds. Gravity,
viscous, quadratic, dry and mixed rivals. Mean RMSE relative to velocity
persistence: .255719, .255082, .253407, .255719, .253407 respectively.
These are exploratory temporal development comparisons, not holdout results
or BFG prediction success. Four meaningful controls passed. RK4 substep
sensitivity <5.3e-8 rad/s. Full source provenance and model/prediction tables
published. Only ratios mg*ell/I,b/I,c/I,tau_c/I are conditional estimands;
common scaling proves absolute mass/inertia/torques unidentifiable from these
angular trajectories alone. Mixed design condition reaches 38.57.
A single bounded remote reproduction workflow starts with this package push.
Check it before claiming remote success or launching another empirical run.
Next: primary sensor/geometry calibration and measurement consistency, window
and horizon sensitivity, then shared cross-condition BFG coupling constraints.
Keep all reserved attempts 2 and 3 sealed. This local checkpoint is reported;
future status may repeat current state but must label it as unchanged.

Mechanical identification reproduction run: 37686204956, observed in progress.
Do not launch another empirical workflow while it is active. Local analysis
and GitHub summary publication verified; remote completion not yet claimed.

## Measurement, sensitivity and carrier checkpoint

Previous mechanical run 37686204956 verified successful; logs match local scores,
four controls and verified development downloads; artifact 11512175109 uploaded.
MEASUREMENT_AND_STABILITY.md adds primary PASCO PS-3220 resolution evidence
(0.18 degrees, 2000 divisions/revolution) and diagnostics on 15 attempt-1 records.
Mean angle/velocity balance error ~1.07%. Rounding-only exceedance 36.65%; an
illustrative half-encoder-step endpoint envelope reduces it to 0.0223%.
This is not a calibrated sensor accuracy or complete velocity uncertainty model.
900 window/horizon/model configurations are published, with common 40–60 second
development validation; no best configuration selected. Gravity explains most
short-horizon improvement; friction ranking differences remain small.
REFERENCE_CARRIER.md and reference_carrier.py construct an anchored positive
Gram carrier retaining signed angle and velocity with explicit instruments.
200 reconstruction/joint-unitary controls passed (max residual 6.89e-15).
Operator preparation is a hypothesis; physical transition closure is not proved.
Next: test actual ambient update and instrument propagation for that candidate,
with measurement-aware observables and strong mechanical rivals, development only.
Keep 30 reserved recordings sealed. This package push starts one bounded updated
mechanical diagnostic reproduction; verify status before another empirical run.
Hourly status and regular publication remain on this existing branch. Report the
checkpoint as exploratory; do not turn the representation into a physical proof.

## Verified sensor/carrier checkpoint and next direction

Diagnostic reproduction run 37687167706 completed success; steps, logs and
upload verified. Remote measurements match local consistency and sensitivity
statistics. No empirical workflow currently active at this checkpoint.
Reference carrier encoding controls passed, but the inherited-formation readout
has a proved stationarity obstruction under full selection/rank and no seed:
F_plus=V_dagger F V and jointly inherited instruments preserve trace ratios.
100 actual ambient-update controls match to 3.56e-15. Published proof and
stationary_readout_control.py preserve the negative result.
Next: construct and audit geometry-dependent observables involving Y or a
physically justified instrument transition; do not retry the same inherited-F
readout as if motion could appear from a coordinate change. Keep preparation,
clock, physical identification and closure explicit. Development only.
This checkpoint is reported to the user; hourly summaries can mention it as
completed, but must not announce it as a new result again. All 30 reserved
recordings remain unopened. Regular updates stay on the pendulum branch.

## Constructive calibrated pendulum motion realization

Package experiments/bfg-pendulum-motion-2026-10-07/ constructs motion from
canonical scalar K,F,Y state: K stores phase, F amplitude squared, geometry
Y supplies N(Y)=log2((-log(phi(Y)))/(-log(phi(0.25)))); N(f(Y))=N(Y)+1.
Physical readout depends on Y as well as inherited K,F, removing the earlier
formation-only stationary-readout obstruction. Physical frequency, damping
and seconds per event are explicit additional calibrations, not BFG predictions.
Six controls passed, including 100 actual ambient updates and an independent
linear oscillator matrix-exponential check; stable coordinate covers 600 events.
On 15 real development recordings and 4,485 0.1-second transitions, mean RMSE
relative to angle/velocity persistence is .082509/.255849. Calibration uses
viscous coefficients fitted in seconds0-30; evaluation seconds30-60 of attempt1.
This is mathematically equivalent to a linear underdamped oscillator; no
independent superiority, physical universality or causal emergence is claimed.
The representation is movement-bearing but conditionally calibrated. Preserve
prior failures. All 30 confirmation recordings remain sealed.
This push starts one bounded reproduction workflow. Check status before another
empirical run. Next developmental work: independent/shared clock and observable
constraints, full-trajectory robustness and intervention calibration; compare
nonlinear mechanical rivals rather than counting coordinate encoding as a win.
Publish and report this as a constructive exploratory checkpoint.

## Verified movement and extended-domain checkpoint

Motion Action37688045722 completed success; six controls, 15-file source fetch,
real development scores and artifact upload verified. Logs reproduce .082509
angle and .255849 velocity increment-relative RMSE on 4,485 pairs.
The calibrated movement representation is published and reproducible.
GENERALIZED_MOTION.md and generalized_motion.py extend the readout to undamped,
critical, overdamped and free linear motion. Shifted formation F=1+r^2 permits
physical rest with positive BFG loads. Exact semiconjugacy follows from the
geometry clock and matrix-exponential group property. 110 actual ambient checks
and two analytic controls pass; largest residual 2.45e-15.
These are valid mathematical representations with supplied mechanical generator,
not force parameters derived from BFG alone. No physical universality or
independent superiority is claimed. No reserved data were accessed; no empirical
run active at this checkpoint. User asks to overcome limitations: address each
specific coordinate/model restriction with verified extensions, preserve true
scientific constraints and do not invent a universal proof. Next work concerns
shared independent calibration, full-trajectory errors and intervention constraints.
This checkpoint is reported to the user; hourly status should label it completed.

## Autonomous derivation mandate activated

Owner explicitly requests automatic treatment of every open derivation without
further prompting. Existing hourly continuation updated, no new automation.
Exact mandate saved in experiments/AUTONOMOUS_DERIVATION_PROMPT.md; working
proof obligations and evidence saved in experiments/DERIVATION_REGISTER.md.
Prioritize independent energy/time coupling, frequency/drag derivation and
intervention action. Each package must execute concrete derivation, controls,
primary-source audit or allowed development analysis; no repeated wish list.
A closed derivation requires stated premises and valid reasoning. If not implied,
prove the specific obstruction/nonuniqueness, identify an additional hypothesis
and continue with the next solvable dependency. No automatic guarantee of proofs.
Keep calibrated representations distinct from physical emergence; retain all
failed variants, sealed holdout, bounded runs and main/paper restrictions.
Hourly German status and regular publication on the same pendulum branch remain.
This automation/configuration checkpoint is reported; no new empirical proof
or physical result is claimed merely from activating the mandate.

## Shared calibration and optional hierarchy checkpoint

New package experiments/bfg-shared-calibration-2026-10-07/ on pendulum branch.
Exploratory apparatus hypothesis gives a(L)=gL/(L^2+lambda), lambda=I0/m.
One global ratio .0022888769594424643 m^2 replaces 15 gravity coefficients:
16 total fitted coefficients versus30 free, including15 viscous rates.
On 15 development recordings, angle/velocity persistence-relative errors
.082510/.255771 nearly match free-frequency .082509/.255849. This is not
statistical superiority or a BFG-only gravity derivation. Three numerical
controls passed; no reserved data accessed. A bounded reproduction starts
on package push; check actual status before another empirical run.
Mathematical dyadic levels U_j=U^(2^j) give exact shared clock increments and
coarse/fine compatibility. Three scalar controls pass. This is temporal
self-similarity, not a physical fractal-dimension claim.
Owner clarification: apply fractal/hierarchical methods only where justified;
no blanket fractal architecture and no extra fractal fitted parameters now.
Next: test shared parameters at longer horizons, sensor-aware trajectory
uncertainty and discriminating intervention constraints. Clock units and absolute
inertia remain additional calibration/nonidentifiability obligations.
This local checkpoint is reported; remote completion must be independently read.

Shared calibration reproduction Action37689622515 completed success; three
controls, development-only source fetch, calibration and artifact upload verified.
Remote logs match the local shared ratio and all comparator scores. No active
empirical run at this checkpoint. The user-facing report includes this success
and the restriction of fractal approaches to justified applications.

## Per-execution mandate reminder

Every continuation first reads the saved autonomous derivation prompt, proof
register and current ledger. Diagnose poor development results by cause, derive
justified mathematical revisions and compare against previous versions/rivals.
Preserve failures and additional assumptions; no holdout leakage or changed
success criteria to conceal failure. Existing automation and saved prompt updated.


### Long-horizon phase correction — local completion, remote reproduction pending
15 real attempt-1 recordings; coefficients unchanged from development seconds 0–30; holdout untouched. Seven horizons 0.1–6.4 s. At 6.4 s (3540 overlapping pairs), target-RMS-normalized angle/velocity errors: free linear BFG 0.218393/0.249122; phase-corrected observable 0.088297/0.128974; nonlinear mechanical rival 0.088291/0.128745. Improvement is exploratory and conditional on a mechanically derived cubic phase approximation, not emergence of the force law. Four independent controls pass; halved RK4 step agrees within 1e-5 on a representative long-horizon recording. All 15 included, no amplitude-gate exclusions. Package experiments/bfg-long-horizon-2026-10-07 preserves full results and derivation. Remote completion/report status must be recorded after verification.

Remote verification: GitHub Actions run 37690703502 completed successfully; package checksums, 15 pinned real-source downloads, four controls and all seven forecast horizons reproduced. Logs match the published 6.4-second scores; result artifact uploaded. New results reported to the user in this execution (avoid duplicate completion reports). Next priority: bound the conditional phase approximation and assess fixed interventions/rivals on development data, then freeze the complete confirmatory protocol before any holdout access. No active empirical run remains.


## Exact nonlinear representation and force-selection checkpoint
New package experiments/bfg-nonlinear-realization-2026-10-07 proves conditional exact semiconjugacy to the full sine pendulum flow, without the earlier small-angle amplitude gate. Unchanged canonical F,K inheritance and event clock; shifted positive preparation includes rest and rotations. Supplied mechanical flow and seconds calibration remain additional assumptions, not BFG emergence. A globally Lipschitz passive family alpha*sin(theta)+(1-alpha)*theta shares the identical encoding, clock and small-motion linearization but different accelerations. Even periodicity does not uniquely select sine: normalized sine-plus-second-harmonic family supplies a further explicit counterexample. Six local controls passed (actual ambient update, composition, elliptic periods, matrix exponential, energy/nonuniqueness, encoding). No new empirical evaluation or downloads; all reserved attempts remain untouched. Previous real-data scores preserved. Package and proof register published and verified; reported as a new theory/code-control checkpoint, not new empirical success. Next priority: an independently justified force/potential selection and intervention coupling; do not use the supplied flow as its own emergence proof.


## Conditional force selection and nonlinear development stress
User explicitly requests nonlinear BFG in every continuation: repository mandate and existing hourly automation updated, no additional automation. New package experiments/bfg-force-selection-2026-10-07 derives sine torque conditional on rigid-arm geometry, uniform gravity and potential linear in height; those are extra physical premises, not BFG-only axioms. Fifteen real attempt-1 files, unchanged0-30s integral fitting and30-60s forecasting, no exclusions/holdout access. At6.4s, target-normalized angle/velocity RMSE: refitted linear .217691/.236686; sine .088291/.128745; passive second harmonic .345298/.357471. Harmonic design condition30.44–221.66; extra flexibility worsens development prediction. Three independent controls pass. All coefficients/scores/provenance preserved. One bounded remote reproduction starts on publication; verify before claiming completion. Next: constrain shared physical coupling/interventions and measurement uncertainty rather than proliferating unconstrained harmonics. Local findings reported as exploratory; remote status pending.

Remote force-selection reproduction37691694923 completed successfully: published checksums verified, only15 pinned development files fetched, three controls passed, scores match local analysis, result artifact uploaded. Harmonic angle and velocity errors each worsen in14/15 recordings at6.4s. New completion/negative findings reported in this execution; avoid duplicate completion claims. No active empirical run remains. User requested15-minute continuations; automation service supports at most hourly, so schedule was not changed and no workaround automation was created. Nonlinear mandate is saved both in repository and existing hourly task.


## Nonlinear robustness checkpoint
Protocol fixed before this exploratory stress evaluation;15 real attempt-1 recordings, no refit or exclusions, holdout sealed. Package experiments/bfg-stability-2026-10-07 compares sine-flow realization and phase observable at0.1,1.6,6.4s under11 nominal/one-factor scenarios. At6.4s clock plus1% raises sine angle/velocity normalized errors from .088291/.128745 to .351789/.360452; phase version .351338/.360201. Hypothetical range, not observed clock miscalibration or joint confidence box. All scenarios retained.4200/4500 states meet the conditional asymptotic basin certificate;300 in len5_cond1_1.csv have fitted b=0 and only energy-well stability, not certified attraction. Explicit upright instability refutes absolute global stability. Two new mathematical controls pass, prior solver/phase controls included in remote reproduction. No empirical stabilization fix claimed. Next priority: independently justified clock/frequency calibration and horizon-dependent sensitivity budgets; do not tune on reserved data. One bounded GitHub reproduction starts with package publication; completion pending.

Remote stability reproduction37692412238 completed successfully: package hashes, pinned15 development downloads, all nine controls(3 solver+4 phase+2 bounds), stress metrics and artifact upload verified. Logs match4200/4500 asymptotic basin states and both clock-plus worst scenarios. New stability findings reported to user in this execution; avoid duplicate completion announcements. No active empirical run remains. This diagnoses sensitivity and proves conditional dynamical stability; it does not yet claim an empirically stabilized forecast or absolute guarantee.


## Clock-only analytic budget checkpoint
Package experiments/bfg-clock-budget-2026-10-08 derives exact conditional model-to-model bounds |delta theta|<=sqrt(2E0)*epsilon*h and |delta w|<=[a min(1,sqrt(2E0/a))+b sqrt(2E0)]*epsilon*h for forward clock perturbations epsilon<=1. On all15 real attempt-1 development records, no exclusions/refit/holdout access, a common sufficient clock tolerance at6.4s is0.07255% for extra per-record angle NRMSE<=0.05, or separately0.03804% for maximum additional angle error<=0.01rad. These are declared illustrative allowances, not confirmed clock accuracy or new confirmation criteria. Code preserves all per-record budgets/source hashes. Three local independent controls passed. Time rescaling t=c*tau proves effective a_obs=c²a,b_obs=cb; shared-clock angle/velocity do not independently identify seconds calibration. Uniform CSV grid alone does not settle it. No new empirical workflow needed for analytic checkpoint. Publication and local checks verified; reported as new conditional error-budget result, not improved measured forecast or independent calibration. Next: primary clock accuracy/frequency evidence and predeclared operational horizon/error requirement.


## Joint paper intake —8October2026
User resumed work after pause and explicitly requires mathematics from both independent papers. First attachment was byte-identical to the already pinned World Formula PDF; no invented version change. Correct new source is Dynamic Order and Recursive Structure Formation,144pages, dated8October2026, preserved at papers/dynamic-order-2026-10-08/Balance_Field_Equation_Dynamic_Order.pdf, SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Earlier PDF remains unchanged. New manuscript contains old Part I and additional Part II; overlap is not independent evidence.
Package experiments/bfg-joint-paper-intake-2026-10-08 documents source pair, theorem compatibility and fresh40complex matrix controls, exact weighted/formation balances, positive driven fixed point .05596219018384207 atd=.15,100initial values/60steps error2.08e-17, compatible tensor lift and replicated-seed T_seeddeg. Synthetic math/code checks only, no empirical/holdout access. Entire differential/figure package not independently recertified.
New interface result: old event clock under f(.25+.15) advances .5296568030878593, not1. A continuous state-only event clock cannot advance1 along a driven orbit converging to a positive fixed point. Do not insert the input into the old calibrated pendulum model without a new typed clock/observable realization. No improved physical predictions claimed. Source mandate, proof register and existing hourly automation updated/resumed; no new automation or main merge. One bounded mathematical-control workflow starts on publication; remote completion pending. Reporting: new source intake and limits reported this execution; do not repeat as empirical success.


## Latest owner correction — sole active Dynamic Order source
The final explicit instruction supersedes the temporary source-pair instruction: use the complete new144page Dynamic Order manuscript only as active mathematics, including inherited Part I. Older paper remains archived, not active; no deletion or silent manuscript rewriting. All compatible mathematical components of the new manuscript may be combined with explicit typing, domains, gap/rank/seed assumptions and physical bridges; universality remains a research hypothesis as the manuscript states. Repository mandate and existing resumed hourly task updated accordingly. Earlier joint-intake terminology is historical provenance, not current source policy.
Publication verification: new PDF SHA256 matches the supplied bytes; mathematical-control Action37698742480 completed successfully, archive hash verification and fresh controls match local results, artifact11516706292 uploaded. No empirical data or holdout used. This intake/control/source-policy checkpoint reported to user; do not present as new real-data success. No active empirical run remains. Next: consistent input/clock/observable coupling under the sole active paper before applying driven geometry to pendulum forecasts.


## Explicit driven-clock extension and input robustness
Package experiments/bfg-driven-clock-2026-10-08 constructs an explicit separate event counter on X_scalar times N0 for the new paper's input-coupled map. It resolves prior geometry-clock incompatibility without silently adding a canonical Xi component. Supplied Phi_t decoder/h remains a calibrated external physical bridge; projection independence of y,d is structural, not observed robustness to physical forcing. Derived bounded-input estimate L^k e0+(L rho+eta)(1-L^k)/(1-L), L16/27, with positive input/output margins; limiting bound16rho/11+27eta/11. Five fresh local controls pass. No real data reevaluated or holdout access; no improved empirical score claimed. No new empirical workflow. Autonomous mathematical construction priority highlighted at top of saved mandate and existing hourly task. Source remains complete Dynamic Order only. This theory checkpoint reported; next task is physically meaningful, independently calibrated input/observable coupling.


## Real energy/input bridge checkpoint
New package experiments/bfg-energy-input-2026-10-08 uses Dynamic Order scalar input map with explicit additional E/s mechanical energy bridge. Fifteen real attempt-1 recordings, calibration0–30s, forecasts30–60s, no holdout/exclusions. Constructed causal input d_r(y)=f_inverse(r*y)-y exactly reproduces fitted retention, rather than adding predictive content.4485calibration oracle inputs admissible but never used for prediction. At6.4s3540pairs, relative energy RMSE: persistence .290570; autonomous1; constant input2.786275; retention/causal feedback .334963; strong full-sine mechanics .138288. All100% coverage. Positive latent fixed point fails this physical bridge; phase matters. A precise equal-energy/unequal-w² counterexample disproves energy-only physical factor closure for b>0. Four local controls pass; scalar log coordinates avoid underflow-induced false terminal events. Negative results retained; no BFG-only force derivation claimed. New broad combination priority saved in mandate and existing hourly task. One bounded remote reproduction starts with publication; completion pending. Next: phase-sensitive independently prepared observable/state, not future-outcome reconstructed input.

Remote reproduction37699807418 completed successfully: package hashes,15 pinned development downloads, four controls and all six-model/horizon scores match local analysis; artifact11517436516 uploaded. Full sine energy forecast beats persistence in all15 recordings at6.4s; mean .138288 versus .290570(52.4%lower). This is strong additional-mechanics comparator evidence, not BFG-only emergence or confirmatory success. New negative scalar bridge, exact feedback equivalence and phase necessity reported this execution; avoid duplicate completion reports. No active empirical run remains. Broad compatible/universal-use research priority is emphasized in saved mandate and existing hourly task; universality remains testable goal.


## Exact phase-retaining closure and rigorous-work checkpoint
Package experiments/bfg-exact-energy-phase-2026-10-08 derives an exact energy/phase chart for the additional passive sine generator. Conditional equations e_dot=-2be sin²phi and phi_dot=sqrt(a)sqrt(1-e cos²phi/2)-b cosphi sinphi close the prior energy-only obstruction. Proved positive finite-time energy and invariant libration well; rest is separate, phase ill-conditioned near rest, separatrix/rotation domain excluded explicitly. Physical generator and seconds remain extra assumptions, not BFG-derived force selection. Four independent local controls pass. Fixed-before-evaluation exploratory protocol,15 real attempt-1 records,0 exclusions, no holdout/refit. At6.4s3540 overlapping pairs, angle/velocity target-RMS NRMSE .088291/.128745 matches full-sine rival; maximum coordinate-versus-Cartesian discrepancy1.027e-6 satisfies predeclared1e-5 rule. Initial e range .0028054–.2100716. No new predictive superiority or independent confirmation. Local package complete, GitHub publication verified before report; no new remote Actions reproduction claimed or launched. Rigorous proof/robustness mandate highlighted and mirrored into existing hourly continuation. Next: independent phase/input coupling and calibrated physical bridge. This new conditional closure/equivalence checkpoint is reported this execution; avoid repeating old scores as new improvement.


## Typed intervention bridge and internal-force tangent audit — 8October2026
Package experiments/bfg-input-phase-2026-10-08 derives forced q,p and energy/phase equations, exact signed impulse/work map, translation nonexpansiveness and conditional torque/inertia identifiability. Mechanical torque, inertia and seconds remain additional premises; positive dimensionless geometry input d does not identify signed physical impulse. New internal scalar audit proves a C1 factor at a constant-input fixed point cannot have rank2 for a fixed attracting pendulum target: neutral K,F columns vanish and only one y tangent column remains. This rules out this regular scalar route, not full matrix BFG or all extensions. Six independent local controls pass, including nonresonant Sylvester rank. Predeclared hypothetical kicks on4500 existing real development states give13500 code/domain applications, zero chart violations and work residual1.554e-15. These are NOT measured interventions or new empirical forecasts. No downloads, fit, holdout or new empirical workflow. Proofs, provenance, results and refreshed mandate published and verified; relevant EEG ledger mirrored. Explicit independent derivation priority, including force-law derivations, saved in repository and existing hourly task. Reported this execution as a conditional construction and scalar obstruction, not physical emergence. Next: matrix-carrier regular derivative/two-direction observable closure and independently calibrated input selection.


## Matrix canonical/tangent checkpoint —8October2026
Package experiments/bfg-matrix-tangent-2026-10-08 derives exact full-persistence natural-frame quotient update and positive Gram attenuation of kernel entries. Thirty complex Ambient controls agree to1.6002e-15; HS/phase controls pass. A declared isotropic matrix input Y+dI has transverse/weighted-trace geometry tangent eigenvalues .178902/.428499 atd=.15, verified by three-step differences; K/F/W tangent neutral. Proved restricted local obstruction to regular nonresonant underdamped factor at this fixed point. Multiple internal directions are constructed, but no pendulum force emergence claimed; anisotropic/noncommuting candidates remain next. Synthetic math/code controls only, no empirical analysis/download/holdout/workflow; previous real results preserved. Latest owner request requires full prompt review before substantive work, including rereading missing portions and after steering; prompt fully reviewed this execution and rule saved/mirrored to existing hourly task. Publication verified before user report; new matrix checkpoint reported here, not new empirical success.


## Completed anisotropic observable-factor step —8October2026
Package experiments/bfg-anisotropic-closure-2026-10-08 closes the active INTERNAL anisotropic full-persistence observable-factor obligation. Exact canonical factor: formation-weighted spectral measure mu and complex kernel/formation coherence measure nu; their pushforward/attenuation laws derived directly from Dynamic Order84 and89(161), including exact eigenvalue collisions. Eigenvalue-only and(mu,trFK) projections fail via preserved explicit witnesses. Compact simple-spectrum chart can exit while canonical update remains nonterminal; richer measure factor resolves that chart limit.100 complete Ambient comparisons and100 unitary controls pass at1e-10 criterion: factor7.11e-15,gauge3.41e-13,collision2.78e-17. Synthetic mathematics/code controls only; no real-data evaluation, downloads, refit, holdout or workflow. Numerical grouping1e-12 explicitly a convention, not universal robustness. Proof/code/results published and verified, register updated and EEG ledger mirrored before report. This step completed before next dependency. Physical two-observable angle/velocity identification, clock and internally selected force remain OPEN, not renamed as solved. Next necessary step: regular signed two-observable reduction of this closed factor and complete nonlinear transition test. Reported this execution as new internal closure, not new physical prediction.


## Signed-coherence candidate completed —8October2026
Package experiments/bfg-signed-readout-2026-10-08: direct(Re z,Im z) candidate fails fiber closure; same pair(.3,.12), different geometry yield successor gap .01547395. Retaining mu repairs chart closure but radial damping cannot supply direct pendulum acceleration from zero imaginary component. Restricted general counterexamples proved; independent Ambient residual5.56e-17 and DOP853 mechanical control pass. Synthetic mathematics/code controls only: no empirical evaluation, downloads, fitting or holdout. Publication interruption recovered by checking latest GitHub head and rerunning local controls before verified publication. This PARTICULAR investigation closes negatively; physical reduction and force-law derivation remain OPEN. Next dependency: regular geometry-retaining physical candidate and full nonlinear transition. New restricted result reported this execution, not a universal impossibility or physical prediction success.

Verified pendulum publication: c0c113cfb4f6ff8b17f90d3cbf4af4934b27d0ba.


## Regular geometry-delay factor checkpoint —8October2026
Package experiments/bfg-geometry-delay-2026-10-08 constructs a local regular signed two-observable factor from canonical full-persistence geometry, with fixed formation ratio1:2 and commuting F/Y preparation. Exact chart and geometry Jacobian determinants nonzero at(.2,.7); complete nonlinear event transition and conditional inverse-conditioning bound proved.40 independent Ambient controls max1.39e-16, derivative8.86e-11, inversion2.14e-15; condition55.42 at center. Isotropic chart rank loss preserved as counter-limit; no global inverse/stability claim. Derived event acceleration is internal, but secant velocity, angle conversion and seconds lack independent physical identification. No sine force, inertia or measured intervention claimed. Synthetic mathematics/code only; no downloads, real-data refit, holdout or new workflow. This local construction step is complete under premises; physical reduction remains OPEN. Next dependency: independently justified physical observable/clock and continuous-generator compatibility. New result reported this execution; previous negatives and real results retained.

Pendulum publication: 785a9cbfb7f9249e8d9a202ca5096b91695c5b18.


## P44 continuous-flow compatibility checkpoint —8October2026
Package experiments/bfg-flow-compatibility-2026-10-08 derives a restricted orientation obstruction from the existing P44 determinant; the determinant itself is not a new discovery. Constant-duration or ordered state-dependent clock plus one regular connected two-dimensional physical readout cannot realize that canonical witness as a C1 autonomous planar flow. Local internal chart remains proved; chart changes orientation between endpoints and cannot be globally regular across a connecting domain. Exact clock formula and positive-duration/order-reversing translation counterexample prevent overclaiming impossibility for every clock. Two-event witness remains orientation reversing, not an all-aggregation theorem. Independent finite differences error3.26e-11 and nonlinear sine variational residual3.34e-16 pass; synthetic code/math only. No real-data fit, downloads, holdout or workflow. This particular flow-audit step completed with its negative conditional result; physical question OPEN. Next dependency: independently motivated alternative carrier/readout and explicit regular-domain/clock ordering before generator and development test. All old results preserved; new compatibility finding reported this execution.

Pendulum publication: 2672a03965dadf978de5d641b59bd00a8498a5f9.


## Explicit phase extension and other-level transfer —8October2026
Package experiments/bfg-suspension-2026-10-08 constructs a declared separate event phase and local continuous strip/seam representation of the canonical geometry factor. C2 Hermite readout supplies exact instantaneous kinematics and matching event jets; phase/h/A remain additional choices, not canonical physical derivations. Exact chi=s³(1-s)³(s-.5)² alternatives preserve all sampled jets yet change midpoint acceleration byA lambda/(32h²). Exact det D(Q,Q_s,Q_ss)=-.94803044927 proves this candidate has no local planar acceleration factor; independent difference residual2.03e-9 and same-model fiber witness corroborate. Theorem8 full-persistence tensor lifts transfer R/readout consistently, complete Ambient controls m2,3 residual5.56e-17; replicated labels do not select force. Endpoint residual6.22e-15. This candidate/level audit completes conditionally with preserved failure of physical closure; physical pendulum remains OPEN. No real-data analysis, fitting, downloads, interventions, holdout or workflow. Owner's explicit search across other levels/carriers added to saved mandate, with typed transfer and return-map proof requirements; full updated prompt reread after steering. Next single dependency: independently constrained observable/phase on a two-direction carrier, enforce acceleration fiber closure and calibrated clock before development fit. New construction and limitations reported this execution, not physical force emergence.

Pendulum publication: 5322083057bdbda2348a685edf6e96e7f69004cc.
