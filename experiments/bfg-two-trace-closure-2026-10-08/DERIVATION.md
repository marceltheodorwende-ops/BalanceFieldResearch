# P52 — Regular two-trace projection fails nonlinear closure

## Active step and premises
Resume interrupted P52; no new parallel package. Source for this proof: Dynamic Order, including PartI. Full persistence dimension2,P=I,F>0,witnessI/2,J=K/kappa with fixed positive formation-unit kappa. EXTRA fixed eta=.1 policy Z=Y+eta*i[Y,J], require0<Z<I. Canonical update unchanged after preparation. Candidate q=tr(FY)/trF,p=tr(FJ)/trF is dimensionless, not calibrated angle/instantaneous velocity. Statement: rank2 but local nonlinear fiber closure fails. Completion: exact proof, independent controls, publication and verified dual ledgers. No empirical data/holdout.

## Source and search
Dynamic Order83 equations121–123 types/units/gauge,84 equations124–138 canonical endpoint,85 covariance,86 accounting,87 finite autonomous seed scope,88 input/viability/mediator,89 equations161–162 fiber closure and independent clock/generator,90 tensor163–164; PartI62–64 differential chain. Whole-text supporting search in bfg-search52.txt inspected closure,clock,quotient,covariance,tensor,viability,mediator,balance. No accounting or hierarchy label removes transverse kernel information. P51 exact endpoint is a dependency, not a new discovery. Pending source clarification does not affect this proof.

## Rank and exact endpoint
Trace cyclicity proves gauge invariance and Hermiticity makes q,p real. At fixedF, variations(deltaY=I,deltaJ=0) and(deltaY=0,deltaJ=I) map to(1,0),(0,1). Small variations retain strict domains. Thus rankDPi=2; these trace-changing directions are not gauge directions.
C=(I+Z)^-1,B=Z C,lc=tr(F C),lb=tr(F Z² C),alpha=lb/(lc+lb),R=alpha C²+(1-alpha)B².
From84/P51, natural-frame Y+=R,F+=F, so q+=tr(FR)/trF. Positive loads/full rank/empty complement ensure nonterminality.

## Exact same-fiber counterexample and local obstruction
Y=diag(1/5,7/10),F=diag(1,2),J(t)=[[0,t],[t,0]] gives q=8/15,p=0 for everyt. Z(t)=[[1/5,-it/20],[it/20,7/10]]. Positivity of Z andI-Z require t²/400<7/50 andt²/400<6/25; hence |t|<sqrt56 is an admissible open family.
Exact rational matrix algebra:
q+(0)=1049825/5212404;
q+(1/5)=67192573825000/333569890024821;
difference=4981197824177075/193189003227215231076≠0.
Thus equation161 fails. More strongly,
dq+/dt at t=1/5=468887175530377750000/1818207943709187974573853≠0.
The family tangent lies in kerDPi. A C1 endpointT withPi U=T Pi would imply D(Pi U)v=0 there by chain rule, contradiction. Nonzero derivative supplies unequal successor states in every sufficiently small full neighborhood, so this is a LOCAL closure obstruction as well as global counterexample. Exact proof does not depend on rounded discrepancy.

## Scope, alternatives, levels and physical force
Invertible reparameterization of(q,p), including nonzero affine angle/velocity calibration, preserves fibers and cannot repair failure. Therefore this pair cannot supply a fixed-duration autonomous physical endpoint on the witness neighborhood. Hidden-state-dependent clocks, different observables, singular reductions or restricted invariant preparations are not excluded. No universal BFG/2D impossibility claimed.
Fixingt would add a preparation restriction. Its invariance under the entire controlled update must be proved before treating it as a2D carrier; subsequent resets are extra inputs. eta=0/commuting kernels remove this particular witness but require separate closure tests. Adding a single coherence measure has no proved sufficient closure here. P51 full invariant triple retains lost information but is larger than requested physical pair.
Uniform full-persistence tensor transfer preserves this failure through the specified normalized base readout; replication does not recover discarded base information. Other carriers/seed branches require independent analysis.
This is not a force derivation or intervention measurement. Scalarsq,p have no supplied seconds, inertia, angle instrument or force law. Candidate investigation ends negatively; physical question stays open.

## Conditioning and independent checks
Property tested is exact closure, not dynamics/prediction stability. Differentiability with nonzero derivativea gives |q+(t+eps)-q+(t)|≥|a eps|/2 for sufficiently small eps; no numerical certified radius or global regularity claimed. Prepared-domain and load margins deteriorate near boundaries.
check.py recomputes exact endpoints/derivative, rank directions and admissible spectra, compares complete Ambient natural-frame geometry and checks centered derivative. Acceptance: exact gap/derivative nonzero, Ambient<1e-10, derivative error<1e-9, both events nonterminal. Reproduction after interruption passes: Ambient8.33e-17; derivative error6.42e-13; gap2.578406503976079e-5. Synthetic math/code only.
Reproduce: PYTHONPATH=<directory containing Ambient experiment.py> python check.py with numpy/sympy. controls.json records actual results.

## Status
Rank2 PROVED; candidate local/full-domain nonlinear closure DISPROVED. P52 investigation completed only after verified publication/register/dual ledgers. Original code and numerical evidence retained after interruption; no new result duplicated.
Next necessary dependency: invariant preparation submanifold or alternative coherence-retaining pair fromP51, prove full nonlinear invariance/fiber closure then continuous-generator/clock compatibility before development fit. Physical pendulum/force/seconds OPEN; no empirical workflow/holdout.
