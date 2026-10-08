# Typed event-phase extension, tensor-level transfer and force closure

8 October 2026. This is a separate research construction. The original paper is unchanged.

## One active step and completion criteria
P45 leaves alternative carrier/readout/clock compatibility open. Construct and audit an explicitly extended carrier, not silently alter the canonical update. Derive event return, instantaneous kinematics, seam regularity, level-transfer compatibility, and force-selection/closure limits. Exact symbolic identities and independent numerical controls plus publication and register/ledger verification complete THIS candidate audit; the physical pendulum question stays open unless a force and physical preparation are established.

## Sources and status of added structure
Sole active source: Dynamic Order PDF, SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Section84(124)–(138) supplies the canonical event. Sections62–64 give regular derivatives; section89(161)–(162) explicitly requires factor closure and separately constructed physical flow/clock. Section88.4(159) is an independent mediator, not the canonical generator, and is not substituted here. Section90(163)–(164), Theorem8, gives the conditional full-persistence tensor lift used below. Sections68.1,69.2–69.3,70.1/70.4 require physical calibration/preparation. Dependencies P39/P41/P44/P45.

Canonical part: the full-persistence commuting F/Y geometry factor R with formation weights (1/3,2/3) from P44. Additional part: one dimensionless intra-event phase s, a declared positive duration h and a selected smooth readout. They are NOT new components proved to exist in canonical Xi. No external sine mechanics is built into this construction. Existence of a continuous representation is distinct from a physically selected force.

## Local extended carrier and exact return
On an open neighborhood U where det DR!=0, R is a local diffeomorphism onto V=R(U). P44's exact nonzero determinant gives such a U near (.2,.7). Introduce two local event strips with coordinates (y,s), and glue their endpoint collars by
 (y,s) -> (R(y),s-1).
This is a smooth local transition because R is invertible on U. The vector field Z=(0,0,1/h) transforms to the same vector field: the derivative of R applied to the zero y velocity is zero and phase speed is unchanged. Flowing for h from an event section therefore returns exactly to R(y) on the successor section. The return is the canonical GEOMETRY FACTOR, not a planar time-h map; the carrier has a third phase direction and section transition coordinates. P45's planar same-connected-readout theorem is not contradicted.

Only a finite local seam/strip atlas is asserted. Longer smooth suspension requires compatible inverse charts at every visited event. R need not be globally invertible and a global mapping torus is not claimed. Without such inverse charts one can still specify a hybrid forward reset (y,1)->(R(y),0), but must not call it a globally smooth invertible flow. Canonical rank/seed transitions outside the P44 preparation are not covered.

## Explicit observable with actual instantaneous derivative
Put g(y)=y1-y2, q0=g(y), q1=g(Ry), v0=q1-q0, v1=g(R²y)-q1. v0 and v1 are prescribed dimensionless endpoint velocities in phase units; they are an additional interpolation/readout choice, not inferred instantaneous physical velocities.

Find a polynomial Q_y(s) of degree at most5 with endpoint values and derivatives
 Q(0)=q0, Q'(0)=v0, Q''(0)=0,
 Q(1)=q1, Q'(1)=v1, Q''(1)=0.
Writing Q=sum_i c_i s^i fixes c0=q0,c1=v0,c2=0; the three remaining endpoint equations uniquely fix c3,c4,c5. Explicitly
 Q=q0+(v0)s+(-10q0+10q1-6v0-4v1)s³
   +(15q0-15q1+8v0+7v1)s⁴+(-6q0+6q1-3v0-3v1)s⁵.
This is solved directly from the boundary equations in check.py, including a general nonzero endpoint-acceleration check; no mechanical generator is assumed.

Declare theta=A Q_y(s), omega=(A/h) Q'_y(s), acceleration=(A/h²) Q''_y(s), A!=0. Since y is fixed within a strip and ds/dt=1/h, theta_dot=omega and omega_dot=acceleration exactly. Here A is an angle conversion, h is seconds per event only if independently calibrated; the mathematical controls use A=h=1 without claiming measured units.

At a seam, q1(y)=q0(Ry), v1(y)=v0(Ry), and both accelerations are0. These identities hold for every y in the chosen neighborhood, including their tangential derivatives. In a seam chart expressed through R^-1, the piecewise readout is C2 across the seam: value, first and second phase jets match, together with tangential/mixed derivatives. Third derivatives need not match; no C3 physical observable or globally smooth mechanical force is claimed. For an infinite admissible nonterminal sequence with constant h>0, sampled elapsed time kh diverges; global strip existence is a separate condition.

At event sections (theta,omega)=(A g, (A/h)(g composed R-g)), a rescaling of P44's regular H chart. Its two geometry directions are locally independent at the proven witness. Inside a strip a third state variable remains; event-section rank2 is not a proof of a closed planar physical flow.

## Exact alternative readouts and force nonidentifiability
Let chi(s)=s³(1-s)³(s-1/2)² and Q_lambda=Q+lambda chi for any constant dimensionless lambda. chi and its first TWO derivatives vanish at both0 and1. Thus ALL variants have exactly the same sampled angle, velocity and acceleration, the same canonical return R and the same declared h,A; they remain C2 across each seam.

At s=1/2, chi=chi'=0 but chi''=1/32. Hence theta_lambda and omega_lambda agree EXACTLY with the base readout at that instant, whereas acceleration_lambda-acceleration_0=A lambda/(32h²). This gives an explicit force-selection counterexample: canonical events, endpoint jets, clock and even that instantaneous angle/velocity do not select a unique acceleration across allowed readout hypotheses. Lambda is not fitted; it is a proof witness of remaining freedom. No physical force law may be attributed to the original BFG from this interpolation alone.

A nonzero physical torque would additionally require inertia I and a force/potential rule. Multiplying the constructed acceleration by an assumed I does not identify it or derive a sine torque. General endpoint accelerations a(y) could also be supplied to the Hermite problem, but supplying mechanical accelerations is an additional hypothesis, not an internal derivation.

## Exact within-candidate planar closure obstruction
For the BASE lambda=0 candidate, consider T(y1,y2,s)=(Q,Q_s,Q_ss). The symbolic chain rule gives D(g composed R)=Dg DR and D(g composed R²)=Dg DR(Ry) DR(y). Together with the explicit polynomial these determine DT without any physical premise.

At y=(1/5,7/10), s=1/2, exact rational arithmetic yields det DT approximately -0.9480304492713656, with the exact nonzero numerator and denominator preserved in results/controls.json. This is a genuine exact rank witness, independently checked by central differences (residual2.03e-9).

By the inverse function theorem the image of T contains an open3-dimensional neighborhood. It therefore contains two nearby states with identical first two coordinates (Q,Q_s) and different third coordinates Q_ss. No single-valued acceleration function of just (theta,omega) can describe all these states locally, even without assuming differentiability of that function. This proves failure of a planar autonomous force closure for THIS interpolation/preparation family. It is not a universal BFG impossibility or a claim about every possible higher-level readout.

A separate numerical root control locates an explicit same-model pair: (.2,.7,.5) and approximately(.10090691298721222,.6110377386834029,.51), same angle/velocity to5.56e-17 but acceleration difference-.07119902235186992 in code units. This pair corroborates the exact local rank proof; the root approximation itself is not the general proof. The 3-coordinate readout T is a local regular state representation at the witness, and would give closed LOCAL extended equations via T^-1; it does not select a mechanical acceleration law or establish global invertible charts.

## Other levels: derive what the canonical tensor lift actually transfers
For m>=2 use the paper's L_m with tau_m=I_m/m. On full persistence Theorem8 gives U L_m=L_m U modulo the declared tensor coordinates. In the natural frame, C_m=C tensor I_m, B_m=B tensor I_m; formation F_m=F tensor tau_m. Trace(tau_m)=1 leaves lc,lb and alpha unchanged. Therefore R_m=R tensor I_m. The formation spectral GROUP projectors E_i,m=E_i tensor I_m have rank m. Define y_i,m=tr(E_i,m Y_m)/m, not an unnormalized trace; this returns the original y_i exactly. Each group's formation mass is f_i, so weights remain1/3,2/3.

Thus g, event H, R, and the constructed Q all transfer consistently if the additional phase/h/A convention is held fixed across levels. Lifted dimensions and formation eigenspace multiplicities change; total formation stock and witness normalization are preserved. There are no seeds on this branch. The repeated auxiliary labels supply no extra evolving geometry direction or force-selection equation. The lambda counterexample and within-candidate rank obstruction survive this transfer. Independent complete Ambient SVD controls at m=2,3 agree with R tensor I to5.56e-17.

This is a precise compatibility result on differently sized carriers, not evidence that every physical level unfolds automatically. Nonuniform tau, seed branches, new couplings or observations of auxiliary directions require a distinct proof. In particular seed replication can cause the paper's T_seeddeg terminality. No physical fractality follows from replication or event interpolation.

## Conditional robustness of the interpolation ambiguity
Stability assessed here means bounded readout perturbation at FIXED prepared y, s in[0,1], |lambda|<=epsilon, |A|<=Amax and h>=hmin>0. It is not dynamical attraction or robustness of a fitted forecast. For k=0,1,2 let C_k be the sum of absolute monomial coefficients of chi^(k); on[0,1], |chi^(k)|<=C_k. Therefore angle, velocity, acceleration perturbations are bounded respectively by Amax epsilon C0, Amax epsilon C1/hmin and Amax epsilon C2/hmin². Endpoint jets are invariant for every lambda. The exact midpoint acceleration gap persists for every nonzero lambda. As hmin approaches0 the derivative bounds deteriorate; global observable inversion or dynamical stability is not guaranteed.

## Whole-paper search and interpretation
The accompanying search covers the canonical ambient/gauge structure, differential chain, load and formation balances, entropy/diversity, historical witness, finite seeds, scalar autonomous/driven regimes, viability/transverse certificates, closure/clock and typed lifts. The canonical full-persistence factor and Theorem8 substantiate the event/level portion. The separate phase/h and interpolation explicitly fulfill a CONSTRUCTION obligation motivated by section89; they are not asserted as an existing theorem in the paper. Formation and witness balances, entropy increments and replicated labels supply no missing instantaneous force selection. The independent mediator of section88.4 is not silently substituted.

## Controls and status
Predetermined acceptance: exact Hermite and bump jets; nonzero exact DT rank witness; central-difference determinant <1e-7; endpoint matching<1e-12; kinematic finite differences<1e-8; tensor Ambient agreement<1e-10; numerical fiber matching<1e-10 with acceleration gap>1e-4. numpy/scipy/sympy plus the existing Ambient experiment.py via PYTHONPATH. Synthetic proof/code controls only, no real dataset, fitting, measured interventions or holdout. A parameter-order mismatch in the first draft of the exact-rank calculation was corrected before publication and independently finite-difference checked; intermediate incorrect value is not a physical result.

Status: conditional continuous extended representation and tensor transfer constructed; force nonuniqueness and failure of this candidate's planar closure proved. This completes the candidate audit, not the physical pendulum derivation. Next single dependency: investigate an independently constrained observable/phase selection on a carrier with two internal evolving directions, enforcing acceleration closure (DT rank or fiber test), resource typing and clock calibration before a real-development fit. Preserve this construction/counterexample to reject merely interpolated event realizations as force emergence.
