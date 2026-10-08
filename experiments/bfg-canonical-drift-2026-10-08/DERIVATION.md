# Internal geometry decay and a locally closed drift hypothesis

8 October 2026. Separate research note; both original manuscripts remain unchanged.

## Active obligation and completion criteria
Following P46, examine an observable/acceleration choice on two internal evolving directions without arbitrary phase interpolation. Derive an intrinsic bound on the canonical geometry, construct a declared drift from that update, prove its conditional local acceleration closure and stability, and test whether it meets the canonical endpoint-flow obligation. Complete with general proofs, sharpness/counter-limits, independent Ambient/derivative/solver controls, publication and verified register/ledgers. This is one candidate audit; any surviving physical claim remains open.

## Sources, compatibility, and premises
Both currently active artifacts:
* World Formula (6 October 2026,68pages), SHA256 a2a1411c3acd06d8ed90210f9426cd33642579cd57a2f8f839ca7d9b861f3f25. Sections6–8 equations(21)–(31) give metric/load/analysis definitions; sections9–14 define quotient/inheritance/seed; section17(69)–(71) scalar damping; section18(72)–(75) distinguishes discrete and continuous Lyapunov statements; section23(89)–(91) requires independent clock/flow compatibility; sections62–64 differential chain.
* Dynamic Order (8 October 2026,144pages), SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Section84(124)–(138) repeats the compatible canonical kernel; section87 Theorem6 finite autonomous seed capacity; section88.3(157)–(158) viability/transverse scope; section88.4 independent mediator is not a canonical generator; section89(161)–(162) closure/clock; section90(163)–(164) conditional tensor lift. Inherited material is not independent evidence.

Dependencies P39/P41/P44/P46. Internal theorem assumes any finite dimension n, P=I,0<Y<I,F>0, arbitrary Hermitian K and density W. F need NOT commute with Y. The local two-coordinate drift construction further restricts to the P44 preparation: n=2,[F,Y]=0, formation ratio1:2 with invariant formation labels. Additional hypothesis: y_dot=(R(y)-y)/h for declared h>0. This ODE is constructed from the update, not asserted to be its exact generator. No mechanical sine law or fitted rival is inserted.

## New canonical geometry bound: norm(Y_next)<=norm(Y)/2
Let M=||Y||_op,0<M<1. On full persistence Q=Tsel=PG=I and the natural-frame geometry successor is R=alpha C²+beta B², where C=(I+Y)^-1, B=I-C. In a Y eigenbasis write eigenvalues y_i and diagonal formation masses f_i>0. Trace cyclicity gives
 lc=sum_i f_i/(1+y_i), lb=sum_i f_i y_i²/(1+y_i).
Offdiagonal formation entries do not enter these trace loads. Thus b=lb/lc is a weighted mean of y_i² and satisfies 0<b<=M². Since alpha=b/(1+b), alpha<=M²/(1+M²).

For any0<y<=M<1, r_alpha(y)=[alpha+(1-alpha)y²]/(1+y)² is increasing in alpha, since partial_alpha r=(1-y²)/(1+y)²>0. Therefore
 r_alpha(y)<=phi_M(y)=(M²+y²)/[(1+M²)(1+y)²].
Differentiation gives phi_M'(y)=2(y-M²)/[(1+M²)(1+y)³]; its only stationary point in[0,M] is a minimum. Its maximum on this interval is attained at an endpoint:
 phi_M(0)=M²/(1+M²), phi_M(M)=2M²/[(1+M²)(1+M)²].
For the first endpoint, M²/(1+M²)<=M/2 is equivalent to (1-M)²>=0. For the second endpoint, 2M²/[(1+M²)(1+M)²]<=M/2 follows from (1+M)²>=4M and1+M²>=1. These inequalities are strict for0<M<1. Taking the largest successor eigenvalue proves the stated bound, invariant under the SVD quotient frame.

Every successor stays positive and below1. A is full column rank, witness selection succeeds, and the complement is empty, so this branch continues nonterminal. Formation and witness remain inherited in the natural frame. Iteration yields M_k<=2^-k M_0. There is no finite-time exact hit atY=0, but the limiting boundary can have zero B-load and is not a nonterminal equilibrium asserted by the theorem.

The constant1/2 is the best uniform bound without extra conditioning restrictions. Set Y_e=diag(e,1-e),F_e=diag(e,1),0<e<1/2. As e decreases to0, the high geometry mode dominates both loads, alpha tends to1/2, and the small-mode successor tends to1/2. M tends to1, so M_next/M tends to1/2. Each finite e is admissible; the limiting boundary itself is excluded. A fixed lower formation-conditioning or spectral-margin assumption might improve the constant but is not imposed silently.

Using Dynamic Order Theorem6, an infinite nonterminal AUTONOMOUS orbit eventually reaches full persistence. The above bound then applies from that event onward. This corollary does not cover external inputs, changed dimensions/preparation, seed transitions before full persistence or arbitrary driven updates. It does not imply full-state contraction: neutral formation/witness and scalar K directions remain. Nor does it give a pairwise Lipschitz contraction between two states. It is a dimensionless radial geometry bound, not a proved energy or time-in-seconds law.

## Declared two-direction drift and exact local acceleration closure
Now restrict to formation ratio1:2 and define the smooth two-dimensional geometry factor R as above. Let L=(1,-1), V(y)=R(y)-y, g(y)=Ly. Declare y_dot=V(y)/h. This is a different continuous mediator hypothesis, built from the canonical map but requiring an additional evolution premise.

Set theta=A Ly and omega=(A/h) L V(y), A!=0. Direct differentiation gives
 theta_dot=omega,
 omega_dot=(A/h²) L[DR(y)-I] V(y).
The readout Pi=(theta,omega) is a fixed rescaling of P44's H. At y0=(1/5,7/10), det DH=18076941875/236768239296!=0 (existing P44 witness, not a new rank discovery). Hence Pi has a smooth inverse on some open neighborhood U. Define the COMPLETE local acceleration function
 a_drift(theta,omega)=(A/h²) L[DR(Pi^-1(theta,omega))-I] [R(Pi^-1(theta,omega))-Pi^-1(theta,omega)].
This proves a closed local second-order system theta_dot=omega,omega_dot=a_drift(theta,omega), for trajectories remaining in the invertible chart. There is no extra interpolation/phase variable and no supplied mechanical force embedded in a decoder. This is a positive conditional acceleration-closure result for the DECLARED drift, not a force law derived from the discrete kernel alone. A carries angle units, h carries seconds only if measured; inertia, energy and sine selection are not determined.

At the code-control center with A=h=1 the acceleration is-.5180668730571788. This number is a synthetic model value, not an observed pendulum force. Changing h rescales frequencies/velocities by1/h and acceleration by1/h²; neither paper fixes h or A. Other continuous coupling hypotheses can be constructed, so the premise is falsifiable and not uniquely selected by the canonical rule.

## Dynamical stability, domain and robustness under the stated model
For positive y, every R_i(y)>0, so y_i_dot>=-y_i/h and y_i(t)>=y_i(0) exp(-t/h)>0 at finite times. For M(t)=max_i y_i(t), the upper Dini derivative obeys
 D^+ M<= [M/2-M]/h=-M/(2h).
Therefore M(t)<=M(0) exp(-t/(2h))<1. For any finite horizon, the lower and upper bounds keep the solution in a compact positive region on which the rational field is smooth, proving finite-horizon continuation. The geometry approaches zero only asymptotically. This is radial geometric stability under the additional drift, not physical Lyapunov energy or observable inversion stability.

For the two-coordinate observables, |theta|<=|A|M, and |omega|<=(3|A|/(2h))M, using |g(R)|<=M/2 and |g(y)|<=M. Thus their magnitudes decay while the readout is defined; the local force inverse need not remain regular. Controls show DH changes sign along the geometry trajectory: a chart singularity intervenes by continuity. The globally valid geometry ODE does not thereby become a globally closed planar observable ODE.

Discrete robustness statement fixed before controls: compare RADIAL SIZE to the zero boundary, not two-trajectory forecast error. If each perturbed update is R(Y_k,F_k)+E_k with ||E_k||<=eta and remains in the stated positive full-persistence domain, M_k+1<=M_k/2+eta, giving M_k<=2^-k M_0+2eta(1-2^-k). Positive formation may vary because the bound holds for every F_k>0. If a declared pre-event perturbation has norm<=rho and still preserves0<Y_eff<I, the bound becomes M_next<=M/2+rho/2+eta, with limiting radial bound rho+2eta. These hypotheses do not guarantee positivity or domain by themselves and are not measured uncertainty ranges. No universal input/full-state/prediction stability is claimed.

## Endpoint compatibility failure and its clock limit
The identity y+h(V(y)/h)=R(y) says exactly that ONE explicit Euler step equals the canonical map. Euler is not the exact flow. In normalized time tau=t/h the ODE is dy/dtau=V(y), so its exact time-h endpoint is Phi_1^V(y), independent of h. Shrinking h also increases the declared drift speed and cannot remove this normalized endpoint defect.

At y0 the independent DOP853 solution gives Phi_1=(.14611480100106786,.35158432523115846), while R(y0)=(.1829673985362608,.2106297785052732); norm defect .1456924781441742. A second integration with h=.25 agrees under time rescaling to9.72e-14. These are synthetic controls corroborating the structural distinction. Existing P45 orientation proof also excludes R as a regular planar fixed-duration flow near this witness. Thus this candidate does NOT fulfill the original canonical endpoint-flow equality of World Formula23/Dynamic Order89. No empirical fit is performed to disguise that failure. It could be studied as an additional continuous-coupling hypothesis, but not reported as an exact canonical BFG pendulum realization.

## Other levels and the whole-source search
Dynamic Order Theorem8's full-persistence tensor lift has unchanged loads/alpha and R_m=R tensor I, with trace-one auxiliary density; operator norm is unchanged. The radial1/2 bound therefore transfers to all those declared levels. This does not create a second independently evolving auxiliary geometry or fix the physical clock. Nonfull-persistence seeded lifts can terminate by replicated degeneracy and are excluded. No physical fractality is inferred.

Whole-text search across BOTH active PDFs considered ambient/gauge, projector/polar/SVD differentials, load/formation/witness balances, scalar damping, mediator/Lyapunov/viability, measurement/clock, entropy/diversity, finite seeds and tensor/level transition sections. The compatible definitions justify the new internal radial bound; continuous mediator sections specifically preserve the distinction between additional ODE and canonical generator. Formation/entropy balances give no unique angle, energy or sine potential. This candidate uses these internal restrictions rather than a fitted external oscillator.

## Independent controls and actual result
Predetermined checks:30 full Ambient complex/noncommuting formation cases in dimensions2,3,5, residual<1e-10 and radial ratio<=1/2; exact chain-rule acceleration identity; directional central difference error<1e-8; DOP853 positivity and radial bounds with tolerance1e-10 over normalized horizon6; clock rescaling residual<1e-10; retain endpoint defect>0.01 and chart rank-loss evidence as negative controls. Sharpness sequence independently stored. All pass: Ambient1.67e-16, acceleration1.74e-11, rescaling9.72e-14. Maximum sampled ratio .32086 is not the proven optimum; the near-boundary sequence reaches .499985 and corroborates sharpness.

Status: general canonical full-persistence radial bound PROVED under assumptions; local second-order acceleration closure PROVED under an ADDITIONAL drift hypothesis; global chart and exact canonical endpoint compatibility FAIL for this candidate. No sine force, calibrated seconds, inertia, physical energy, empirical improvement, downloads or holdout access. Code/math controls only.

Next single dependency: seek a physical readout and exact generator-compatible carrier/input whose selection is independently constrained by the load/differential structure; retain this bound as a pre-fit requirement on any full-persistence realization. Do not treat the additional Euler drift as an internally derived exact continuous force. Publication and register/ledger verification close this candidate audit while the overarching physical question stays open.
