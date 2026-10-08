# BFG derivation and proof register

Version 2026-10-07. Status refers to the stated hypotheses, not universal
physical emergence. Numerical controls corroborate calculations, not general
theorems. Every continuation must maintain this register.

| ID | Statement / obligation | Basis and additional assumptions | Current status | Evidence / next step |
|---|---|---|---|---|
| P01 | Scalar canonical update f(y) | Full selected 1D carrier, positive loads, no seed | Derived on this branch | movement tests compare 100 actual ambient updates |
| P02 | Clock N(f(y))=N(y)+1 | Constructed phi coordinate, fixed reference y0 | Derived, physically uncalibrated | NONLINEAR_OBSERVABLE.md and movement README |
| P03 | Linear-energy retention <=0.356299 | Physical E=s*y is an extra hypothesis | Conditional bound derived; candidate fails development feasibility | INTERNAL_MATH.md |
| P04 | Regular C1 energy bridge to exponential decay impossible near zero | h'(0) finite nonzero, physical g'(0) in (0,1) | Conditional obstruction derived | earlier EEG MATHEMATICAL_ASSESSMENT.md |
| P05 | Inverse-log readout yields geometric decay | Added H_p, free C and p | Derived representation; physical readout not independently justified | NONLINEAR_OBSERVABLE.md |
| P06 | Formation-only inherited readout is stationary | Full selection/rank, no seed; joint instrument inheritance | Conditional obstruction derived | STATIONARY_READOUT_OBSTRUCTION.md |
| P07 | Calibrated scalar projection reproduces linear pendulum motion | Added mechanical generator, physical clock and preparation | Exact conditional representation derived; emergence unproved | movement README, GENERALIZED_MOTION.md |
| P08 | Mass/inertia/torques uniquely identified from angular motion | Conventional mechanical torque model | Nonidentifiability demonstrated by common scaling | mechanical identification README |
| P09 | Physical energy unit and seconds fixed by BFG | No independently justified coupling supplied | Open physical requirement; exhibited calibration freedom | CONDITIONAL_PHYSICAL_EXPLANATION.md |
| P10 | Frequency and drag arise from BFG alone | Need constraints beyond fitted mechanical generator | Open derivation | Audit allowable BFG couplings and rival realizations |
| P11 | Instrument-aware latent state is measurable | PASCO resolution plus dataset processing | Exploratory evidence, incomplete uncertainty model | MEASUREMENT_AND_STABILITY.md |
| P12 | Baffle intervention corresponds to BFG operator action | Geometry/medium/inertia calibration needed | Conditional mechanical action; BFG action open | PHYSICAL_CLOSURE_AUDIT.md |
| P13 | Shared calibrated realization has independent predictive support | Fixed protocol, strong rivals, untouched observations | Not evaluated; holdout sealed | Freeze only after justified structure exists |

## Automatic execution rule

On each continuation choose the next dependency that can be addressed concretely.
Work on P09/P10/P12 by constructing restricted coupling candidates and testing
uniqueness, dimensional calibration, shared parameters and intervention constraints.
Use mathematical counterexamples to eliminate arbitrary choices before fitting.
For empirical checks use attempt-1 development data only and retain failures.

Do not mark P09/P10/P12 proved because P07 represents an already supplied
mechanical flow. Existing nonidentifiability arguments constrain the current
assumptions; they are not a universal impossibility theorem for every future BFG
extension. Any additional axioms or coupling principles must be separately named,
supported and tested. Update evidence and status after each substantive package.

## Additional shared-calibration evidence

P14: a(L)=gL/(L^2+I0/m) is derived conditional on a point bob and constant
pivot inertia. Shared ratio fits 15 development records with nearly unchanged
motion scores and fewer parameters; Action37689622515 verifies reproduction.
This constrains P10 using an added mechanical hypothesis, not a BFG-only proof.
P15: U_j=U^(2^j) implies U_(j+1)=U_j^2 and exact dyadic clock consistency.
This is derived temporal hierarchy, not observed physical fractality. Three
scalar controls pass. Fractal extensions are optional and require justification.


## P16 — Weakly nonlinear phase observable (conditional approximation)
Cubic sine expansion and fundamental-harmonic averaging give psi'=Omega-a A²/(16 Omega), with A=A0 exp(-bt/2); integrated closed form and initial-state preparation are implemented in experiments/bfg-long-horizon-2026-10-07. Additional mechanical law, calibration, small-amplitude and weak-damping assumptions are explicit. This is not an exact BFG-only pendulum derivation. Four independent controls passed.

## P17 — Long-horizon developmental stress
The linear observable fails relative to the nonlinear mechanical rival at 6.4 s. The revised phase observable reduces angle error 59.6%, remains slightly worse than that rival, and supplies no independent confirmatory evidence. All 15 development recordings included; untouched attempts remain untouched. See package for normalization and dependence limits.


## P18 — Exact conditional nonlinear realization
Global Lipschitz flow and its composition law, together with the derived canonical scalar clock, prove Pi_alpha U = Phi_dt Pi_alpha. Full sine dynamics, rest, large amplitudes and rotations are represented without a small-angle approximation. Additional generator, physical units and clock calibration remain explicit. Six local implementation controls passed. See experiments/bfg-nonlinear-realization-2026-10-07.

## P19 — Nonunique nonlinear force selection
A passive alpha family with identical BFG map/encoding/clock and equilibrium linearization has distinct accelerations. A periodic second-harmonic family further shows that angle periodicity does not select sine uniquely. These are proved counterexamples under the stated current realization assumptions, not a universal impossibility claim for all future BFG extensions. P10 remains physically open; a rigid-arm uniform-gravity premise selects sine only conditionally.


## P20 — Conditional geometric selection of sine
Rigid fixed-length arm, uniform gravity, linear-in-height potential and calibrated inertia imply V=mgL(1-cos theta), torque=-mgL sin theta. Derived under explicit additional physical coupling assumptions; not BFG-only selection. Package bfg-force-selection-2026-10-07.

## P21 — Harmonic development stress and identifiability
Real15 attempt-1 recordings: adding nonnegative second-harmonic potential worsens6.4s forecasts, with scaled condition up to221.66. Near-rest Taylor expansion exposes combinations A+2C and A+8C; confounding is a plausible limitation, not a uniquely proved error cause. Preserve negative result, no holdout tuning. Three local independent controls pass; remote reproduction pending.


## P22 — Conditional stability and global counterexample
For supplied sine generator a,b>0, |theta0|<pi,E0<2a, energy invariance and LaSalle prove convergence to downward rest. At b=0 convergence not implied. Upright eigenvalue(-b+sqrt(b²+4a))/2>0 refutes absolute global stability. Weighted log-norm gives finite-horizon sensitivity bound, potentially loose. Two local controls pass; see stability package. P21 prior remote reproduction37691694923 verified successful in ledger.

## P23 — Real-data robustness stress
Fifteen development recordings;11 one-factor scenarios; clock/frequency sensitivity materially amplifies6.4s error for both better nonlinear realizations. No joint worst-case guarantee, no complete measurement uncertainty, no new force derivation. Preserve all failures and no exclusions. Remote reproduction pending.

P23 remote verification: Action37692412238 completed success; nine controls and real-data stress scores verified. Conditional sensitivity evidence, not absolute stability or a completed forecast repair.


## P24 — Forward clock-only energy error bound
For supplied passive sine generator a>0,b>=0, integrate |w|<=sqrt(2E0) and |w'|<=a min(1,sqrt(2E0/a))+b sqrt(2E0) over the perturbed forward-time segment. Exact conditional bounds and real-state sufficient tolerances in experiments/bfg-clock-budget-2026-10-08. Three local code controls corroborate bounds/time rescaling; no joint uncertainty guarantee.

## P25 — Physical time calibration ambiguity
With t=c*tau and u=cw, recorded dynamics have a_obs=c²a,b_obs=cb. If angular velocity shares the recorded clock, parameters and physical time scale cannot be independently separated from these trajectories alone. Independent physical velocity/frequency/time evidence could break the ambiguity. Explicit conditional obstruction; physical seconds coupling P09 remains unresolved.


## P26 — Source-pair compatibility and exact balances
World Formula sections7,12–13 and Dynamic Order84–86 agree on the autonomous ambient kernel. Fresh40complex controls corroborate weighted loads and Formation delta=seed-loss. Sources separately archived; overlapping Part I is not independent evidence. See joint-paper-intake package.

## P27 — Finite autonomous seed capacity
Dynamic Order Theorem6: after first event Q=I and p_next=p+delta; n nonincreases and each nonempty admissible complement adds one rank. At most n1-p1 further seeds on an infinite nonterminal autonomous orbit, then full persistence. Finite trajectories may terminate; environmental extensions not covered. Conditional proof reviewed, no empirical hierarchy claim.

## P28 — Positive driven regime and conditional tensor lift
Dynamic Order Theorems7–8: constant0<d<3/4 gives geometry contraction bound16/27 and one positive fixed point; full-persistence tensor lift commutes, seeded replication may terminate by degeneracy. Fresh numerical controls pass. Input and lift are additional declared models, not an autonomous physical forcing law or universal stability.

## P29 — Old-clock incompatibility with driven fixed point
N(f(y+d))=N(y+d)+1 generally differs from N(y)+1; measured code control increment .5296568030878593 at y=.25,d=.15. If yk converges to y*>0 and N is continuous there, N(yk+1)-N(yk) tends to0 and cannot identically equal1. New event bookkeeping or singular/augmented clock needs explicit declaration and physical calibration. Current pendulum readout cannot absorb the new input unchanged.


Current source policy: latest user instruction makes Dynamic Order the sole active paper, with its complete Part I and Part II. Earlier P26 source-pair references describe intake history; equations may now be cited directly from Dynamic Order84–90 and its appendices. Mathematical-control Action37698742480 and PDF checksum verified successfully. P27–P29 retain stated conditional scope; no new empirical force or universal stability claim.


## P30 — Explicit augmented event representation
Dynamic Order sections88–89 permit declared input models and separate event bookkeeping. Define (Xi,n) successor=(U_d Xi,n+1), outside canonical five-component state; a supplied Phi_(hn) decoder has exact closure for fixed physical h. Construction resolves geometry-only clock obstruction, not independent seconds or force calibration.

## P31 — Driven scalar bounded-input robustness
Using Theorem7 derivative L16/27 and input/output margins proves bound L^k e0+(L rho+eta)(1-L^k)/(1-L), limit16rho/11+27eta/11. Variable input generally has no fixed point. Five local controls pass; no empirical confirmation or full-state contraction claimed. See bfg-driven-clock package.


## P32 — Causal geometric retention feedback
Dynamic Order scalar f is monotone on(0,1). Additional d_r(y)=f_inverse(r*y)-y realizes r*y whenever declared input domain holds. Exact equivalence to fitted retention; no independent physical forcing or prediction gain. Closed-loop derivative is r; input derivative becomes singular near zero and positive reserve is not maintained for r<1. Four local controls pass.

## P33 — Energy-only physical closure obstruction and development comparison
For supplied sine mechanics b>0, equalE states(theta0,w=sqrt2E) and(theta=acos(1-E/a),w0) have energy derivatives-2bE and0. Thus energy-only factor fails for short times under Dynamic Order section89. Real15-record test favors full phase-sensitive sine mechanics over scalar models; no exclusions/holdout, remote reproduction pending.

P32/P33 remote verification: Action37699807418 success; source/hash verification, four controls and full real-development scores match local results. Negative scalar bridge and phase-sensitive mechanical comparison retained; no holdout accessed.


## P34 — Exact energy–phase physical factor closure
Statement: for the additional passive sine generator, the punctured libration well is exactly represented by (e,phi modulo2pi), with the equations in experiments/bfg-exact-energy-phase-2026-10-08/DERIVATION.md. Source: active Dynamic Order section89 factor/clock criterion; dependency P33 and explicit-counter extension. Additional premises: a>0,b>=0, calibrated mechanics/seconds, |theta|<pi,0<e<2. Proof: invertible q,p chart and chain-rule derivation; invariant energy bound; rest treated separately. Counter-limits: energy alone fails closure, phase ill-conditioned near rest, rotations outside chart, alternative force generators still possible. Four independent controls pass;15-record exploratory equivalence meets1e-5 numerical criterion. Status: proved under additional physical assumptions and locally development-validated; not BFG-only emergence or new superiority.

## P35 — Conditional positivity and observable conditioning
Statement: e0 exp(-2bt)<=e(t)<=e0<2; angle inverse Jacobian bounded by1/sqrt(1-e_max/2), phase Jacobian norm1/sqrt(2e). Log-energy RK4 stages retain the upper energy domain because all log derivatives are nonpositive; accuracy separately controlled, no global floating-point guarantee. Dependencies P34. Counterexamples: rest phase undefined, separatrix conditioning diverges, phase need not increase under strong damping. Status: proved conditional invariant-region/conditioning statements; finite-horizon controls passed; absolute physical or predictive stability not claimed.


## P36 — Exact signed mechanical input interface
Active Dynamic Order88.2 and89(161)–(162), dependencies P30/P34. Under explicitly supplied torque/inertia, forced q,p chain yields e_dot=-bp²+pu and impulse e+=e-kappa sqrt(2e)sinphi+kappa²/2. Exact work, inverse/composition, translation nonexpansiveness and rest-safe q,p demonstrated; phase singularity and forced chart exits explicit. Positive d does not select signed j. Conditional derivation and code/domain audit passed; passive measurements supply no causal confirmation. Evidence: bfg-input-phase-2026-10-08/DERIVATION.md.

## P37 — Calibrated impulse/inertia identification
Known nonzero J and independently calibrated delta w imply I=J/delta w under instantaneous-kick premise; unknownJ leaves common scaling. Finite-pulse three-regressor integral system uniquely identifies(a,b,1/I) exactly when full column rank. Conditional linear-algebra derivation, no actual calibrated torque data or identified I claimed.

## P38 — Driven scalar regular-factor tangent obstruction
Constantd scalar source has DU=diag(1,1,lambda),lambda<=16/27. For fixed passive targeta,b>0 and h>0, M=exp(hJ) has no eigenvalue1. Differentiated semiconjugacy gives BDU=MB; first two columns vanish, leaving rankB<=1. Nonresonant underdamped target forcesB=0. Thus no regular rank2 physical-state factor at the driven scalar fixed point under these premises. This does not rule out singular/orbit-specific readout, counter extension or matrix BFG. General proof and independent numerical Sylvester control pass. Evidence: FORCE_DERIVATION_AUDIT.md. Next dependency: matrix regular differential and internal force-selection constraints.


## P39 — Full-persistence matrix quotient dynamics
From active Dynamic Order84.1–84.4, P=I,0<Y<I,F>0 gives natural-frame Y+=R=alpha C²+beta B² and K+=R^-1/2(alpha C K C+beta B K B)R^-1/2, F/W/P unchanged. In Y eigenframe K entries attenuate by positive Gram correlations gamma<=1; HS norm nonincreases and phases unchanged in tracked frame. Exact derivation;30 independent complex Ambient controls agree to1.61e-15. Not a physical instrument/force derivation. Evidence bfg-matrix-tangent-2026-10-08.

## P40 — Isotropic matrix-input tangent and oscillatory-factor obstruction
Explicit additional input Y->Y+dI, not an undeclared canonical rule or scalar Theorem7 matrix extension. At isotropic fixed point derivative is H->sH+t tr(FH)/tr(F)I with real eigenvalues s and f'(x); other fixed-stratum directions neutral. Multiple internal evolving geometry directions exist. Under fixed nonresonant underdamped physical target and C1 factor, intertwining forces DPi=0 because source tangent eigenvalues are real, target eigenvalues nonreal. Conditional local proof, three-step independent numerical derivative checks pass. Does not cover anisotropic/periodic states, seeds, rank changes or all matrix BFG. Next dependency: anisotropic noncommuting instrument closure.


## P41 — Exact anisotropic spectral/coherence observable factor — COMPLETED
Active Dynamic Order84(129)–(138),89(161), dependencyP39. Full persistence,P=I,0<Y<I,F>0. Define mu=sum tr(FPi_a)/trF delta_y_a and nu_ab=tr(Pi_a K Pi_b F). Loads/alpha determined bymu; mu+ is r_alpha pushforward and nu+ product-map pushforward of gamma*nu. Group summed coefficients handle exact eigenvalue collisions and noncommuting formation/kernel without additional physical dynamics. Canonical terminality nonterminal on domain. General conditional proof completed, code and100 Ambient/100 gauge comparisons pass1e-10, collision handling checked. Evidence bfg-anisotropic-closure-2026-10-08. Not physical angle/velocity identification or force emergence.

## P42 — Necessary information and chart-exit witnesses — COMPLETED
Same Y spectrum/different formation weights yield distinct geometry successors; same(mu,trFK)/different coherence yields distinct kernel-trace successors. Both inadequate projection counterexamples established. An admissible event with eigenvalue collision is nonterminal; simple-spectrum chart exit is not canonical terminal. Global(mu,nu) factor resolves that exact collision. Numerical1e-12 grouping convention separately declared. Scope restricted full-persistence factor, no universal guarantee.

## Next single active obligation after P41/P42 publication
Determine whether a regular signed two-observable physical reduction of the derived factor satisfies a complete closed transition. Do not start independent experiments or treat internal factor closure as physical force-law proof. P09/P10/P12 and physical calibration remain open; preserve existing counterexamples and no holdout access.


## P43 — Direct signed-coherence candidate — completed negatively
Dynamic Order84/89(161), P41. Two admissible same(Re z,Im z) states have distinct successors. Adding mu repairs noncolliding chart closure but radial gamma damping fails direct theta=A Re z,w=B Im z force response from positive angle/zero velocity at sufficiently short positive steps. Restricted proofs and independent Ambient/DOP853 controls pass; not a rejection of all nonlinear geometry-mixing reductions. Evidence bfg-signed-readout-2026-10-08. Physical force question remains open. Next single dependency: regular geometry-retaining physical reduction and complete transition.


## P44 — Regular canonical geometry-delay factor — COMPLETED under preparation
Dynamic Order84(124)–(138),89(161)–(162),62–64; P39/P41/P43. On P=I,0<Y<I,[F,Y]=0 with F eigenvalues f,2f, formation-labeled geometry has exact canonical R map. H=(y1-y2,g(Ry)-g(y)) has exact nonzero determinant18076941875/236768239296 at(.2,.7); det DR=-321243859375/52720394616576 also nonzero. Two genuinely evolving directions and local complete nonlinear transition proved by inverse function theorem. Conditional inverse bound2/sigma0 on explicitly stated derivative-controlled ball; no certified numerical radius or global stability. Chart singular at isotropic geometry although canonical state continues.40 Ambient/derivative/inverse code controls pass. Event acceleration derived, but secant velocity is not instantaneous physical velocity; seconds/angle/force selection remain extra open bridges. Evidence bfg-geometry-delay-2026-10-08. Next single dependency: independent physical readout/clock selection and continuous-generator compatibility, before empirical fitting.


## P45 — P44 continuous-flow orientation/clock audit — COMPLETED with restricted obstruction
Dynamic Order84/89(161)–(162),62–64; dependenciesP39/P44. The already established negative det DR at(.2,.7) rules out fixed-duration C1 planar flow realization through a single regular readout on a connected domain containing source and successor. Liouville/chain-rule proof; no universal matrix/carrier impossibility. H chart changes orientation between endpoints, hence any connecting path crosses chart rank loss; positive chart transition determinant does not repair a global regular bridge. State-dependent clock determinant=det Dphi_tau*(1+grad tau dot F); ordered clock factor>0 preserves obstruction. Positive tau alone insufficient: translation F=(1,0),tau=2-2x gives det=-1. Independent finite differences and nonlinear mechanical variational controls pass. Two-event aggregation also negative at this witness, not an all-horizon theorem. Physical force, independent instrument/seconds remain OPEN. Evidence bfg-flow-compatibility-2026-10-08. Next single dependency: physically justified alternative carrier/readout with regular event-to-event domain and explicit clock ordering, then nonlinear generator check before empirical fitting.
