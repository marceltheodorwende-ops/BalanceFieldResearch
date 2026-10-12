# P77 — Exact local nonlinear resonant factor, without force selection

## Contract, source and status distinctions

Dependency: P76's unresolved even-resonance nonlinear closure. Determine whether two evolving, gauge-invariant directions of its constant-isotropic-input carrier admit a complete local nonlinear endpoint factor, and whether that construction selects a force. Completion requires a convergent construction with derivative/rank proof, gauge and terminal checks, rival forces, independent numerical controls, and verified publication/register/EEG mirror. No empirical experiment or data access is needed for this existence/nonidentification question.

Sole mathematical source: Dynamic Order, 8 October 2026, 144 pages, SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. II83–85 (121–143) supplies the canonical update; Appendix A (172–187) its endogenous differentials; II88.2 (155–156) supplies the separately declared input pattern; II88.3 (157–158) distinguishes viability and transverse stability; II89 (161–162) and Part I22–23 supply factor and extra-clock conditions; II90 (163–164) supplies the conditional tensor transfer. P76 derived the smooth full-persistence representative directly from these rules. The limit lemma below is proved here, not attributed to a theorem stated in the paper.

**Result:** a C1 rank-two, gauge-invariant nonlinear endpoint factor exists locally for an explicitly chosen constant-input realization and an externally specified resonant damped sine flow. No target flow is put in the input. It IS put in the observable conjugacy and the extra clock/physical interpretation. Two different sine laws work with the same kernel, input, clock and damping. This is a representation and a concrete force-nonselection result, not a BFG-internal derivation of mechanics or a calibrated prediction.

## 1. Fixed carrier and independently defined canonical coordinates

Take n=2, P=I, R=r0 I with fixed r0>0 in formation units, normalized W>0, arbitrary Hermitian K. Before every event apply the EXTRA dimensionless input dI with d=29/90. Set y*=8/45 and x*=y*+d=1/2. On 0<Y+dI<I define C=(I+Y+dI)^-1, B=(Y+dI)C, alpha=tr(R B(Y+dI))/tr(R(C+B(Y+dI))), M=alpha C^2+(1-alpha)B^2, H=M^(1/2), T_C=sqrt(alpha) C H^-1 and T_B=sqrt(1-alpha) B H^-1. The quotient successor has smooth ambient representative

G(Y)=M, K'=T_C K T_C+T_B K T_B, R'=R, W'=W.

This is exactly P76's canonical SVD representative, with the declared input; all supports are I and the seed complement is empty. At Y=y*I,

DG(E)=a E+(lambda-a)tr(E)I/2,
a=16/135, lambda=224/675.

Thus lambda^2<a<lambda<sqrt(a). In Frobenius norm the derivative norm is lambda, and the traceless subspace has eigenvalue a. Fix q=17/50: lambda<q<sqrt(a). By continuity there is a sufficiently small closed Frobenius ball about y*I on which ||DG||<=q, G maps the ball into itself, and 0<Y+dI<I with positive load/rank reserves. No numeric radius or physical preparation is inferred from that existence statement.

Define e=Y-y*I, Qe=e-tr(e)I/2, and e_j=G^j(Y)-y*I. Taylor's theorem on this ball gives

Qe_{j+1}=a Qe_j+N(e_j), ||N(e)||<=C||e||^2, ||DN(e)||<=C1||e||.

Hence the **canonical fast observable matrix**

Z(Y)=lim_{n->infinity} a^-n Qe_n
    =Qe+sum_{j>=0} a^-(j+1) N(e_j)

exists in C1. Indeed ||e_j||<=q^j||e|| and ||D e_j||<=q^j, so both the value and derivative series are bounded by geometric series with ratio q^2/a<1. The value tail is <=C||e||^2/a (q^2/a)^n/(1-q^2/a); the derivative tail has the analogous C1||e|| bound. These constants require a specified neighborhood for numerical certification. Uniform C1 convergence gives

Z(G(Y))=a Z(Y), DZ(y*I)=Q.

All terms are unitarily covariant. This is a full nonlinear identity, not a tangent approximation or a frozen-load update. Repeated eigenvalues cause no frame choice: the construction uses smooth matrix functions and trace projections.

## 2. Invariant labels and two gauge-invariant evolving directions

Using a fixed ambient Pauli component as an observable would fail quotient invariance. We instead derive the needed label from actual K transport. Let L_Y(K)=T_C K T_C+T_B K T_B. At scalar geometry L=identity and its first geometry derivative vanishes by T_C^2+T_B^2=I (P76). Consequently on the same small ball

||L_Y-Id||<=C2||e||^2, ||D_Y L_Y||<=C3||e||.

The ordered products L_{Y_{n-1}}...L_{Y_0} converge to a bounded linear map A_infinity(Y) because sum ||e_j||^2<infinity. Their derivatives converge too: the derivative of the jth factor is bounded by C3 q^{2j}||e||, and all partial products are uniformly bounded by exp(C2 sum ||e_j||^2). Thus

K_infinity(Y,K)=lim K_n=A_infinity(Y)K

is C1, covariant, and invariant under the **full** successor. At the scalar equilibrium K_infinity=K and D_Y K_infinity=0. K has NOT been silently frozen away from equilibrium.

Choose a reference state K0=k0 sigma_z, k0>0 in formation units, and W0=(I+sigma_x/2)/2 (strictly positive, trace one). Define quotient-invariant real readouts

p1=tr(K_infinity Z)/(2k0),
p2=2 tr((W-I/2)Z).

At the reference scalar state, if E=cx sigma_x+cy sigma_y+cz sigma_z, Dp(E)=(cz,cx). The rank is two, both directions have eigenvalue a, and neither is a neutral-only readout. Rank remains two on a sufficiently small neighborhood of this reference state. The nonparallel K0 and W0 have only scalar common unitary stabilizers; the quotient is regular here despite scalar Y. Simultaneous conjugation of Y,K,W leaves both traces unchanged, including K_infinity. Fixing R=r0 I is an invariant preparation hypothesis, not an open assertion over arbitrary R. For bounded K and W near W0 all these claims hold locally.

Since K_infinity and W are invariant, the exact factor identity is

p(U_d Xi)=a p(Xi).

Its fibers are closed, all states in the chosen invariant geometry ball are nonterminal, and terminality is therefore constant there. Discarded scalar geometry, the remaining traceless direction and neutral labels need not be reconstructible from p. This is a rank-two factor, not a bijection from the entire carrier.

## 3. Nonlinear resonant sine-flow bridge, fully constructed

Supply EXTRA a constant duration tau>0 in seconds. Set gamma=-2 log(a)/tau>0 and, for ANY integer j>=1,

omega_j=2 pi j/tau, kappa_j=omega_j^2+gamma^2/4.

These are compatibility choices, not measured frequencies or damping. Declare the external nonlinear vector field on z=(theta,v)

F_j(z)=(v,-gamma v-kappa_j sin(theta)).

Angle is dimensionless radians, v has units s^-1, gamma s^-1, kappa s^-2. Its full finite-time map Psi_j=flow_j^tau has derivative at zero exp(tau A_j)=a I, because A_j has eigenvalues -gamma/2 +/- i omega_j. This is even resonance, with a positive repeated multiplier. Choosing a fixed invertible unit conversion S from dimensionless p to (angle, angular speed) is another bridge assumption; it is not an SI calibration. Norms below use fixed compatible units.

For a C2 local map Psi with Psi(0)=0 and D Psi(0)=a I, choose a<q_t<sqrt(a). A sufficiently small ball has ||D Psi||<=q_t and is forward invariant. The same telescoping proof as Section 1, now with all components retained, constructs

h_j(z)=lim a^-n Psi_j^n(z),
h_j(Psi_j(z))=a h_j(z), Dh_j(0)=I.

Uniform C1 convergence and the inverse-function theorem give a C1 local inverse. Shrink the carrier and physical neighborhoods so S p lies in the image of h_j and trajectories stay inside their domains. Define

Pi_j(Xi)=h_j^-1(S p(Xi)).

Then EXACTLY

Pi_j(U_d Xi)=h_j^-1(a S p(Xi))
              =Psi_j(h_j^-1(S p(Xi)))
              =flow_j^tau(Pi_j(Xi)).

Rank D Pi_j=2 locally. Differentiating the exact identity gives the complete nonlinear tangent closure D Pi_j(U_d Xi) D U_d(Xi)=D Psi_j(Pi_j Xi) D Pi_j(Xi), including endogenous loads and K transport. The constant clock has DC=0; a state-dependent clock cannot be substituted without a new proof. Fiber closure follows from the exact factor identity. The whole sine law, including its amplitude-dependent finite-time effects, is included rather than replaced by the linear approximation. It enters through the externally constructed h_j, so those effects are NOT new BFG-derived physics.

## 4. Concrete force nonselection and stability boundaries

j=1 and j=2 have different kappa (difference 12 pi^2/tau^2), yet identical U_d, d, R, reference labels, p, S, tau and gamma. At theta!=0 sufficiently near zero their accelerations differ by -12 pi^2 sin(theta)/tau^2. Only h_j and therefore the physical readout change. Both obey the exact nonlinear endpoint identity. Thus kernel + constant input + this clock do not select the sine coefficient. More strongly, replacing sin(theta) by any C2 force with the same linear stiffness yields the same resonant derivative and the same limit construction locally; sine versus such a rival is not selected either. At a fixed j, sin(theta) and theta+theta^3 are distinct examples with the same linearization. Inter-event flow and force are externally specified, not recovered from discrete states.

For each declared sine flow, EXTRA inertia Iphys>0 gives E=Iphys[v^2/2+kappa_j(1-cos(theta))] in joules when Iphys has units kg m^2. Direct differentiation gives dE/dt=-Iphys gamma v^2. Small energy sublevels within |theta|<pi are forward invariant and the equilibrium is locally asymptotically stable (the only invariant zero-dissipation set there is theta=v=0). Canonical p contracts exactly: ||p_n||=a^n||p_0||. On a compact local bridge domain, Lipschitz constants of h_j and its inverse convert this to endpoint error bounds. These are conditional representation bounds, not robustness to arbitrary clocks, labels, inputs, measurement noise or force misspecification. Neutral labels need not converge to the reference values.

No independent physical calibration, identifiable inertia, energy observable, preparation, amplitude range or causal intervention has been supplied. Reused development data could not turn this existence proof into independent confirmation. Off-resonance/odd resonance exclusions from P76 remain; gamma=0 cannot match a<1; load/selection crossings, arbitrary R, singular label configurations, global excursions and tensor perturbations outside the lift image are outside this proof. If lambda^2>=a, the fast-observable convergence argument given here is insufficient; no universal impossibility follows. The chosen x=1/2 satisfies the required strict inequality exactly. The infinite future limit is a mathematical instantaneous function of the state and declared update, not an experimentally available measurement algorithm.

## 5. Supporting search and typed transfer

The whole-paper search was directed at this factor construction: II83–85 and Appendix A supply smooth ambient differential rules; II86 formation/witness balances and entropy/diversity do not supply an independent physical chart, clock or force; II87 finite seed capacity does not create new dimensions or missing labels. The autonomous scalar branch (154) has no positive fixed point and cannot support this reference construction. The explicit input (155) permits the chosen fixed geometry but needs external resource accounting. The independently postulated mediator (159) would introduce external dynamics, so it is not substituted as a kernel generator. II89 (161–162) requires exactly the proved endpoint/fiber identity and extra clock. No bookkeeping or stability certificate identifies SI mechanics.

For the full-persistence tensor lift (163–164), use uniform tau_m=I/m, d I_{2m}, and the lift image. Geometry iterates lift, Z_m=Z tensor I. K_infinity,m=K_infinity tensor I, W_m=W tensor I/m. With p1_m=tr(K_infinity,m Z_m)/(2m k0), and p2_m=2tr((W_m-I_{2m}/(2m))Z_m), both readouts equal their base values. The physical factor and tau therefore transfer exactly on that image. Formation stock and witness mass are preserved, ranks multiply; discarded tensor directions add no independently selected force or sensor. This is a proved typed representation transfer, not physical fractality. Seed replication can produce T_seeddeg and is excluded.

## Verification contract and next dependency

Analytic existence, rank, gauge, full nonlinear closure and nonselection are proved under the explicit local assumptions above. Numerical truncations only check implementation and convergence on synthetic examples; they are not new measurements, radius certifications or a substitute for the convergence proof. Controls must compare high-precision canonical limits, a full ambient SVD/gauge transform, independent matrix-exponential resonance and nonlinear flow endpoint residuals, plus a same-linearization rival. Acceptance thresholds are fixed in check.py before execution.

Next necessary OPEN dependency: independently constrained observable/preparation and measured event-time/phase information that can distinguish these rival readouts and resonance aliases. A physical force derivation remains open. This package discharges the previously open *local existence* question in a declared subclass; it neither solves universal pendulum realization nor renames the physical selection requirement as complete.
