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


## P46 — Declared phase suspension and typed tensor transfer — COMPLETED candidate audit
Dynamic Order84/89(161)–(162)/90(163)–(164), dependenciesP44/P45. Separate phase s and h supply local strip/seam continuous extension where R is locally invertible; exact canonical geometry return, C2 Hermite endpoint/readout jets. Added state, clock, interpolation and angle scale explicitly not original canonical dynamics. Tensor lift with uniform tau preserves loads/R and group-averaged readout; m2,3 Ambient controls pass. Exact zero-endpoint-jet bump chi changes acceleration at identical midpoint angle/velocity byA lambda/(32h²). Exact nonzero DT rank witness additionally disproves planar acceleration closure within base candidate; numerical derivative/fiber controls pass. No physical force, independent preparation/seconds or real forecast proven. Evidence bfg-suspension-2026-10-08. Next single dependency: independent observable/phase selection and acceleration fiber closure on an internally evolving carrier; avoid unselected interpolation as force proof.


## Current source policy — latest additional-paper request,8October2026
Both World Formula (68pages,SHA256a2a1411c3acd06d8ed90210f9426cd33642579cd57a2f8f839ca7d9b861f3f25) and Dynamic Order (144pages,SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba) now active. Reuploaded older artifact byte-identical; earlier sole-source policy superseded, not deleted. No P01–P46 proof status automatically strengthened. Overlapping mathematics is not independent evidence. Source compatibility/provenance: bfg-source-reactivation-2026-10-08.


## P47 — Full-persistence radial geometry bound and conditional drift closure — COMPLETED
World Formula6–8/18/23/62–64; Dynamic Order84/87–90; dependenciesP39/P44/P46. General finite-dimensional full-persistence bound ||Y+||op<=||Y||op/2 proved via weighted load ratio and scalar spectral envelope, F need not commuteY. Uniform constant sharp without extra margins; geometric decay, not full-state/pairwise contraction or joule calibration. Declared extra drift (R-y)/h yields locally closed theta/omega acceleration L(DR-I)(R-y) under regular readout and explicit A,h; positivity and norm decay proved. Canonical endpoint equality fails, chart singularity occurs, shrinking h does not remove normalized defect.30 Ambient and derivative/solver controls pass. Evidence bfg-canonical-drift-2026-10-08. Physical pendulum question remains open; next single dependency: independently constrained exact generator-compatible carrier/input/readout, not substitution of Euler drift for canonical dynamics.


## P48 — Exact local signed geometric actuator — COMPLETED conditional audit
Both sources: World Formula6–8/21/23/62–64, Dynamic Order84–90. DependenciesP44/P47. Explicit extra two-direction signed preparation Y->Y+D, followed by unchanged canonical event. Inverse function theorem gives exact local target steering; smooth right inverse for all2D targets requires at least2 input parameters. Derived inverse sensitivity, positive-only tangent cone restriction and full-persistence target norm<1/2. Free control policies realize competing target maps, so no physical force selected. Four independent inverse/Ambient controls pass: residual2.78e-17/8.33e-17; pointwise inverse norm59.0066, condition21.2157, not uniform stability. Typed full-persistence tensor transfer adds no control selection. Evidence experiments/bfg-geometric-actuator-2026-10-08. Physical force/seconds/resource-calibrated actuator remain OPEN. Next necessary dependency: independently constrained preparation/input with units/resources and physical readout, then exact endpoint/clock closure. No empirical analysis, workflow or holdout.


## P49 — Finite preparation budget and reserve — COMPLETED conditional investigation
World Formula6–8/18/21/23/62–64, Dynamic Order84–90; dependenciesP47/P48. For admissible Hermitian pre-input D and full persistence, M_next≤(M+||D||)/2. Telescoping gives total input≥(N+1)m-M0 when all N endpoint norms≥m. Explicit extra nonrecoverable reservoir r+=r-c||D|| implies N≤(M0+r0/c)/m-1; any infinite admissible finite-budget path tends to geometric boundary. Necessary bound, not full-state stability or joule law. Squared-cost alternative and typed norm-preserving tensor transfer checked. Same-cost opposite inputs give distinct canonical endpoints (.000562316 gap), so resource accounting does not select force. Twelve finite Ambient events and100-event scalar control pass; initial20-event decaying matrix control failed implementation rank threshold and is preserved as numerical limitation, not exact terminality. Evidence experiments/bfg-input-budget-2026-10-08. Physical resource/input/readout/force/seconds remain OPEN. Next single dependency: covariant physically distinguishable input policy and preparation/readout identification with exact nonlinear endpoint/clock closure. No empirical fit, new workflow or holdout access.


## Latest sole-source mandate and dependency audit —8October2026
Latest explicit owner instruction supersedes the preceding additional-paper request: Dynamic Order alone active, including complete PartI/II; World Formula preserved as historical archive. Saved mandate updated consistently. P47–P49 rechecked against Dynamic Order83–90 and inherited regular differential chain62–64: canonical equations124–138, gauge123/Theorem2, resource distinctions146–150, scalar extra input155, viability157, closure/clock161–162, tensor163–164 suffice. Matrix preparation and reservoir debit remain declared extra assumptions; neither becomes an autonomous theorem. Fresh P49 reproduction passes existing controls; previous numerical rank failure retained. This is source/dependency verification, not a new discovery or strengthening of physical proof status. P49 next obligation unchanged: independently constrained covariant input/preparation/readout and exact nonlinear endpoint/clock closure. No empirical run/holdout. Audit: experiments/bfg-sole-source-audit-2026-10-08/README.md.


## P50 — Covariant policy stabilizer audit — COMPLETED conditional substep
Latest clarification restores BOTH World Formula and Dynamic Order as active; intervening sole-source entry historical. Full prompt reread. Deterministic covariant Hermitian input must commute with tuple stabilizer; jointly diagonal tuples force diagonal preparation, scalar tuples force scalar preparation. Full-persistence commuting stratum preserved under such policies. Existing noncommuting K permits extra dimensionless policy eta*i[Y,K]/kappa, covariant/Hermitian with explicit domain margin; coefficient/sign/instrument remain unselected. Twenty unitary controls residual8.73e-19; forbidden frame-selected offdiagonal input defect .0282843. Proof and limits experiments/bfg-policy-symmetry-2026-10-08/DERIVATION.md. No physical force/seconds proof, empirical workflow or holdout. Next single dependency: noncommuting policy exact endpoint/readout closure and invariant observable identification, then independent physical preparation/clock calibration.


## P51 — Exact noncommuting Pauli invariant factor — COMPLETED conditional construction
Both active papers, dependenciesP50/P39. Extra commutator preparation eta*i[Y,K]/kappa followed by unchanged full-persistence event gives exact nonlinear natural-frame R/J endpoint. Three scalar parts, six vector Gram products and signed triple volume form complete simultaneous-unitary triple invariants; representative-independent endpoint proves fiber closure, including rank-degenerate completeness. Exact tangent chain derived; no global smooth chart/stability guaranteed. Same initial geometry spectrum with distinct kernel yields successor spectrum gap4.2564e-5, disproving geometry-only closure for this policy.30 Ambient/gauge controls residual6.67e-16/4.98e-14; Pauli cross identity8.68e-19. Evidence experiments/bfg-pauli-closure-2026-10-08. Policy/coefficient/physical force/clock unselected; larger invariant factor is not regular2D pendulum. Next single dependency: physical two-observable nonlinear fiber/transition closure and continuous-generator/clock compatibility of this candidate. No empirical workflow/holdout.


## P52 — Regular two-trace observable closure — COMPLETED negatively for this candidate
Dynamic Order83–90/PartI62–64 sufficient; source clarification does not affect proof. P51 dependency. Invariant q=tr(FY)/trF,p=tr(FJ)/trF has rank2, but exact same-fiber family gives(q,p)=(8/15,0) and unequalq+ with gap4981197824177075/193189003227215231076. Nonzero exact fiber derivative at t=.2 rules out localC1 closure on full neighborhood. Ambient8.33e-17 and derivative error6.42e-13 pass freshly after interruption. Invertible pair calibration cannot repair fibers; no universal2D/BFG/clock impossibility. Evidence experiments/bfg-two-trace-closure-2026-10-08. Physical force/seconds OPEN. Next single dependency: invariant preparation restriction or coherence-retaining alternative pair with full nonlinear invariance/fiber closure, then generator/clock compatibility. No empirical workflow/holdout.


## P53 — Orthogonal noncommuting preparation factor — COMPLETED conditional construction
P52/P50/P51 dependency. Dynamic Order83–85/88–90 and World Formula6–12/22–23/62–64 compatible; no source change strengthens evidence. Extra fixed eta*i[Y,K]/kappa with P=I,F=fI,W=I/2, tracelessJ and orthogonal Pauli vectors preserves algebraic family. Exact quotient endpoint closes on(t,r,s); gamma channel correlation gives0<gamma<1 for r>0. Nonzero constant s reduction fails; azimuth and eta sign are gauge-invisible here. Exact rank3 witness and nonzero hidden-s fiber derivative rule out discarding s in the tested geometry pair. Admitted set is NOT forward invariant: t=.5,h=.4,s=100,eta=.1 has exact next squared margin -38526715420760000/2289565056949920409.60 independent Ambient/gauge controls pass3.33e-15/4.44e-16,240 gated factor steps are synthetic checks only. Evidence experiments/bfg-orthogonal-factor-2026-10-08/{DERIVATION.md,check.py,controls.json}. Physical2D pendulum/force/seconds OPEN. Next single dependency: nonzero invariant two-dimensional preparation graph or coherence-retaining factor with nonlinear invariance/domain and gauge-invariant phase, before generator/clock/physical selection. No empirical workflow, holdout, automation or paper change.


## P54 — Witness-referenced phase and pair closure — COMPLETED conditional investigation
P53/P51 dependency. Active source Dynamic Order83–85, PartI62–64,86,88–90; latest sole-source mandate supersedes historical source-pair entries. Non-scalar positive trace1 witness with w perpendicular j is canonically inherited on full persistence and supplies an internal relative phase. Extra fixed commutator preparation retained and declared. Exact quotient(t,r,s,phi) closes; geometry split strictly positive on gate, so phi+=phi+atan(2eta s), s+=gamma s. Observable tangent rank2, but pair(phi,s) fails localC1 closure: exact partial_h gamma²=-212767859808/180776990897.60 Ambient/gauge/witness controls pass4.94e-15/1.85e-14/6.67e-16. Eta sign now distinguishable; force, energy scale and seconds unselected. Evidence experiments/bfg-witness-phase-2026-10-08/{DERIVATION.md,check.py,controls.json}. Physical2D pendulum/force remains OPEN. Next single dependency: invariant amplitude curve(t,r)=(T(s),R(s)) with exact functional invariance and forward prepared gate, retaining phase for2D factor; then generator/clock/physical selection. Publication was interrupted; resumed same package without new research step. No empirical workflow, holdout, automation or original-paper change.


## P55 — Analytic amplitude endpoint obstruction — COMPLETED restricted investigation
Dynamic Order83–85/PartI62–64/86–90, dependenciesP53/P54. For invariant t=T(s),r=R(s)>0 with analytic finite-endpoint extension T(s*)=0, strict prepared gate and successor graph membership, no nontrivial graph exists at s*=0, or at s*>0 when the successor tends to that endpoint. Derived A=O(t²), gamma limit1/sqrt(1+q²+q⁴); positive-endpoint analytic q forces s+-s*=delta+O(delta²), contradicting T invariance. Five symbolic controls and80-digit asymptotic checks pass; max residual1.4e-11. Explicit analytic countercheck, degeneracies, tensor restriction and model limits documented. This closes ONLY the analytic endpoint investigation: nonanalytic curves/interior domains and physical2D closure, force and seconds remain OPEN. Next necessary dependency: nonanalytic invariant amplitude curve with forward gate, or independently constrained alternative carrier. No empirical workflow, measurements, fitting, holdout, automation or original-paper changes. Evidence experiments/bfg-amplitude-endpoint-2026-10-09/{DERIVATION.md,check.py,controls.json}.


## P56 — Nonanalytic positive-kernel endpoint viability — COMPLETED restricted investigation
Dynamic Order83–90/PartI62–64, dependenciesP47/P53/P54/P55. Fixed extra commutator policy eta!=0, positive anisotropy and infinitely many strict prepared-gate events imply s_k->0. Proof uses monotone geometry/kernel, uniform gamma asymptotics and exact q+/q multiplier approaching sqrt(1+4eta²s*²)>1 under hypothetical s*>0. No graph analyticity or differentiability required. Seven symbolic checks and40 independent Ambient controls pass, max error4.58e-16;80-digit limit check passes. r=0 constant-kernel counter-limit, eta=0 proof boundary, possible gate exit and tensor restriction documented. This closes ONLY the positive-endpoint investigation; zero-endpoint nonanalytic invariant curve and physical2D closure/force/seconds remain OPEN. Next necessary dependency: zero-kernel-endpoint curve with certified forward gate, then generator/clock/physical selection. No empirical workflow, measurements, fitting, downloads, holdout, automation or original-paper changes. Evidence experiments/bfg-kernel-endpoint-2026-10-09/{DERIVATION.md,check.py,controls.json}.


## P57 — Certified forward prepared phase-carrier domain — COMPLETED necessary domain substep
Dynamic Order83–90/PartI62–64, dependenciesP47/P53–P56. For fixed extra eta!=0, domain0<t<=1/2,0<q=h/t<1,0<s<=sqrt(chi)/(2|eta|),0<chi<3 is forward invariant. Exact V/(Aq)<1/(1+q²) gives q+<=Q=sqrt(1+chi)/2<1; inherited kernel decreases and all finite events nonterminal. After event1 t_(k+1)<=(1+Q)t_k/2, relative lower margin1-Q and absolute upper prepared margin(1-Q)/2. P56 consequently gives s_k->0 on an actually certified infinite domain. Finite total preparation budget and divergent/finite alternative clock examples derived conditionally; physical energy/force/seconds not selected. Two symbolic identities,60 independent Ambient controls max4.89e-15,50-event60/100-digit comparison pass. Prior large-s gate failure preserved; no uniform absolute load reserve, full-state or numerical infinite-horizon stability claimed. Evidence experiments/bfg-forward-gate-2026-10-09/{DERIVATION.md,check.py,controls.json}. This closes ONLY the necessary viability domain substep, not the invariant-curve parent: next dependency is a nonanalytic invariant amplitude curve within the certified domain and complete2D factor closure. Physical pendulum/force/clock OPEN. No empirical fit, measurements, holdout, new automation, main merge or original-paper changes.


## P58 — Exact desingularized boundary ray and return obstruction — COMPLETED candidate audit
Dynamic Order83–90/PartI62–64, dependenciesP53–P57. At coordinate limit t=0, the declared boundary map has unique nonzero constant-slope invariant ray q=2|eta|s. Exact pair(s,phi) transition S=s/sqrt(1+x+x²),phi+=phi+atan(2eta s),x=4eta²s²; determinant(1-x²)/(1+x+x²)^(3/2)>0 for0<x<1. This boundary continuation retains extra relative-geometry/phase memory: actual Y=0 loses it and canonically terminates T_load. For every0<t<=1/2,0<q<1 on the straight ray, exact Delta=q+²-4eta²s+²=-q²tF1F2/E²<0, so no choice of positive T(s), including flat T, makes that straight ray invariant. Rational witness -3599578559/286465800625. Five symbolic controls,40 independent Ambient cases max1.16e-15,zero terminal and80-digit boundary limit pass. Boundary construction is NOT a nonterminal canonical/physical factor; no force/seconds derived. Evidence experiments/bfg-boundary-ray-2026-10-09/{DERIVATION.md,check.py,controls.json}. This closes ONLY the boundary-ray/direct-lift candidate. Next necessary dependency: CURVED nonanalytic q(s),T(s)>0 inside P57 satisfying all functional equations and return-map closure. Positive-geometry curve and physical pendulum/force/clock OPEN. No empirical fit, measurements, holdout, automation, main merge or original-paper change.


## P59 — Canonical curvature jets and first-truncation obstruction — COMPLETED candidate audit
Sole Dynamic Order83–90/PartI62–64; dependenciesP53–P58. For x=4eta²s²,z=q/(2|eta|s), the exact prepared update forces first coefficient a(x)=2+x and second coefficient b(x)=P(x)/(1+x+x²)², P=4x6+17x5+42x4+61x3+54x2+27x+6, conditional on a smooth invariant amplitude SURFACE expansion z=1+a(x)t+b(x)t²+o(t²). This remains an intermediate3D surface with phase; an additional invariant t=T(s) is needed for2D. Exact first-jet residual R1=t²C(t,x),C(0,0)=-12, proves NO positive T(s)->0 (including flat/nonanalytic) closes q=2|eta|s[1+(2+x)T(s)] near s=0. Second jet cancels only order2; no existence/convergence or exact closure asserted. Eight symbolic identities,80 independent Ambient cases max5.93e-14,80-digit residual-order checks pass. At t=.02,x=.04 residuals -0.004932828284468025 (first) and -0.000060055858887147 (second) retained. Verification initially caught an extra factor in the residual implementation; corrected before publication. Evidence experiments/bfg-curvature-jet-2026-10-09/{DERIVATION.md,check.py,controls.json}. Next necessary dependency: exact invariant amplitude surface with convergence/error certificate, then nonanalytic positive T(s) and complete2D return. This closes only the curvature-jet candidate audit; parent curved construction and physical force/clock OPEN. Synthetic math/code only; no measurement/holdout/new empirical workflow/automation/main merge/original-paper change.


## P60 — Exact local invariant amplitude surface — COMPLETED necessary surface-existence dependency
Sole Dynamic Order83–90/PartI62–64; dependenciesP53–P59. For the SAME extra fixed commutator preparation, canceled amplitudes(t,x,z) obey exact(a,X,F),x=4eta²s². A weighted pullback graph transform constructs a unique LOCAL Lipschitz z=Z*(t,x) in the specified bounded Lipschitz class, satisfying the FULL nonlinear invariant equation F(t,x,Z*)=Z*(a,X). Proof uses positive F_z, a<=Ct² and X<=x; derivative bounds specify nonempty local radii (not numerical calibration). Banach contraction lambda=C epsilon/mu<1 gives a constructive error certificate; order3 contraction gives |Z*-Z2|<=E3/[mu(1-lambda3)]t³ for P59's second jet. No full Taylor-series convergence/global smoothness asserted. Eight symbolic identities,40 independent Ambient factor controls max1.80e-14,80-digit nested roots at3 sample points and independent canceled-axis infinite-product check pass; sample radii are NOT certified by finite residuals. P59 failures preserved. Evidence experiments/bfg-invariant-surface-2026-10-09/{DERIVATION.md,check.py,controls.json}. Stability concerns the graph-construction norm, not physical/full-state prediction stability. This establishes an intermediate exact three-coordinate(t,x,phi) return; it does NOT complete the regular2D pendulum. Next necessary dependency: positive nonanalytic t=T(x) on this surface satisfying its complete invariant equation, with regularity for the requested2D return/flow. Physical force, energy/inertia, seconds calibration and interventions OPEN. Only synthetic math/code controls; no measurements/holdout/new empirical workflow/automation/main merge/original-paper changes.
