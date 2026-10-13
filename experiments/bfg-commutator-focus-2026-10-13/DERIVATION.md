# P80 — A declared commutator input gives an actual rotating canonical factor

## Source, model and status boundaries
Sole source: The Balance Field Equation: Dynamic Order and Recursive Structure Formation, 8 October 2026, 144 pages, SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Sources: II83 (121–123) types/quotient; II84–85 (124–143) complete ambient event and covariance; II86 (144–150) balances; II87 (152) finite autonomous seed capacity; II88 (153–158) scalar and expressly driven regimes/viability; II89 (160–162), Part I22–23 (89–95) factor and extra clock; II90 (163–164) typed full-persistence lift; Part I62–65 and Appendix A (172–192) complete regular differential chain. P76 derived the smooth representative from these canonical equations. This note extends INPUT, not the canonical event. No input policy or SI identification is claimed to be a theorem of the autonomous kernel.

Declare n=2, P=I, R=r0 I with r0>0 in formation units, K arbitrary Hermitian in the same units. Inherited normalized witness W=(I+A/2)/2 has eigenvalues 1/4,3/4. Add an external dimensionless Hermitian orientation label L, inherited across events, with A=4(W-I/2), A²=L²=I, tr A=tr L=0 and AL=-LA. Set Caxis=-i[L,A]/2. In a permissible fixed frame A=sigma_x, Caxis=sigma_y, L=sigma_z. In the raw SVD successor frame the added label is transported as L+=V* L V, exactly as inherited W; returning to the smooth ambient representative gives L+=L. All labels transform together with the actual tuple under unitary conjugation; L is a declared environment variable, not silently substituted for the evolving K. The nonparallel W,L frame has only central stabilizer, so invariant coordinates below are regular on this specified extended quotient.

Input hypothesis Hinput: D(Y)=dI+i t[L,Y], d=29/90, real dimensionless t in [.9,1.1]. Feed X=Y+D(Y) into the otherwise unchanged complete canonical event. Restrict to the invariant geometry slice Y=sI+uA+v Caxis near Y*=y*I, y*=8/45. Tr(LY)=0 is the slice condition. This policy uses a commutator and no chosen mechanical flow, potential, stiffness, frequency or target solution. It is nevertheless an additional, empirically unverified coupling. Its physical resource/source interpretation is OPEN.

## Full canonical update and exact planar rotation
For 0<X<I the selection is I, both loads are positive, PG=I, full column rank is two and seed complement is empty. Define c=(I+X)^-1, b=Xc,

alpha=tr(R X²c)/tr(R(I+X²)c), M=alpha c²+(1-alpha)b²,
T_c=sqrt(alpha)c M^-1/2, T_b=sqrt(1-alpha)b M^-1/2.

The complete smooth representative is Y+=M, K+=T_c K T_c+T_b K T_b, R+=R, W+=W, L+=L, P+=I. The representative follows from ambient SVD Aanalysis=[sqrt(alpha)c;sqrt(1-alpha)b], Aanalysis* Aanalysis=M, as in P76. Sum T_j²=I but K is generally NOT fixed. Repeated singular values at the scalar fixed point do not obstruct smooth positive matrix functions; no division by individual singular-value gaps is used.

Put z=u+iv. The identities i[L,A]=-2 Caxis and i[L,Caxis]=2A give preinput z_x=(1-2it)z and x=s+d. Let r=|z_x|, x_±=x±r,

alpha=[x_+²/(1+x_+)+x_-²/(1+x_-)]/[(1+x_+²)/(1+x_+)+(1+x_-²)/(1+x_-)],
g_alpha(q)=[alpha+(1-alpha)q²]/(1+q)².

Then s+=(g_alpha(x_+)+g_alpha(x_-))/2 and
z+=eta(s,|z|)(1-2it)z,
eta=[g_alpha(x_+)-g_alpha(x_-)]/(2r).
At r=0 the smooth limit is g'_alpha(x)=2(x-alpha)/(1+x)³. Matrix functional calculus proves the slice invariant. At (s,z)=(y*,0), x=1/2, alpha=1/5, eta=a=16/135>0. By continuity eta>0 on a small neighborhood, uniformly for compact t range. Thus nonzero native planar z has EXACT event phase increment phi(t)=-atan(2t), not an externally inserted pendulum solution. Its magnitude is nonlinear and scalar-coupled. Native (u,v) alone is NOT closed: varying s with the same nonzero z changes eta; the numerical independent example in controls.json checks this explicitly. Do not promote the planar tangent to full native-coordinate closure.

## Entire endogenous differential and admissible local domain
P76's derivative, which includes load and alpha differentiation, is DM(E)=aE+(lambda-a)tr(E)I/2 at X=I/2, lambda=224/675. Input differential is E+i t[L,E]. On the three-dimensional slice this yields DT(0)=diag(lambda,B_t),

B_t=a [[1,2t],[-2t,1]]=rho_t R_phi,
rho_t=a sqrt(1+4t²), phi=-atan(2t).

The two directions A,Caxis evolve, mix and have complex eigenvalues a(1±2it). Both invariant observables u=tr(AY)/2 and v=tr(Caxis Y)/2 respond independently. Formation/witness are inherited; full K transport at the scalar point has delta K+=delta K since sum t_j delta T_j=0. Nothing here proves contraction of the entire tuple. L is fixed on the tested leaf; arbitrary changing labels/R or off-slice directions are outside this proof.

Use Euclidean norm ||E||_slice=sqrt((s-y*)²+u²+v²); operator norm ||E||op<=sqrt(2)||E||_slice. On t in [.9,1.1], .16<rho_t<lambda<.4<sqrt(rho_t). Continuity and compactness give a common positive radius delta with ||DT(E)||<=q0=.4 on its closed ball. Reduce delta until ||E||op<y*/2 and (1+2*1.1)||E||op<1/4 and 2*1.1||E||op<d/2. Then Y>0, D>=dI-2|t|||E||op I>dI/2, and spectrum X lies in (1/4,3/4). Loads are strictly positive with uniform local margins, no selection/rank/seed terminal occurs, and ||T(E)||<=.4||E|| keeps the ball invariant. This is an existential analytic local ball, NOT a numerically certified maximum radius. Sample preparations in controls do not quantify a global guarantee. Local geometric perturbations decay at most .4^n on this leaf; label, K and formation directions preclude any claimed strict full-state stability. Uniformity holds for frozen t choices in the stated compact interval, not arbitrary adaptive switching.

## Exact full nonlinear rank-two endpoint factor
Let T_t be the centered three-dimensional smooth map and Pplane(E)=(u,v). Define N_t(E)=Pplane T_t(E)-B_t Pplane(E). Taylor's theorem gives ||N_t(E)||<=c||E||² and ||DN_t(E)||<=c'||E|| on a possibly smaller uniform ball. Since B_t is normal, ||B_t^-n||=rho_t^-n. The successive rescaled iterates differ by

B_t^-(j+1) Pplane T_t^(j+1)(E)-B_t^-j Pplane T_t^j(E)
=B_t^-(j+1) N_t(T_t^j(E)).

The value is bounded by c rho_t^-1 (q0²/rho_t)^j ||E||². Its derivative is bounded by c' rho_t^-1 (q0²/rho_t)^j ||E||, using ||DT_t^j||<=q0^j. Both geometric series converge uniformly because q0²=.16<min rho_t. Therefore

Z_t(E)=lim_{n→∞} B_t^-n Pplane T_t^n(E)
=Pplane(E)+sum_{j>=0}B_t^-(j+1)N_t(T_t^j(E))

is C1, DZ_t(0)=Pplane, hence rank two locally, and index shifting gives EXACT Z_t(T_t(E))=B_t Z_t(E). The bounds also give ||Z-Pplane||<=c||E||²/[rho_t(1-q0²/rho_t)] and ||DZ-Pplane||<=c'||E||/[rho_t(1-q0²/rho_t)]. These quantify the existence proof; c,c',delta are not measured apparatus parameters. The factor depends on full scalar geometry as required for closure, not just a fitted native projection. It is invariant under simultaneous gauge transformations because u,v,s and T are invariantly defined by inherited labels. K remains fully updated but is absent from this factor. No prescribed external target dynamics occurs in its construction.

For the spectral implementation, orientation cancels in rescaling: Z_t is a nonlinear positive radial scale of the initial z, with scalar dependence. This follows from the exact eta product and positive local eta; the phase factors are already B_t. At z=0, Z=0 by definition. Its derivative at equilibrium is the native plane and rank two is preserved nearby.

## Conditional physical kinematics, force, energy and ambiguity
EXTRA Hclock: independently fixed constant duration tau>0 in seconds; not supplied by d,t or a. EXTRA Hflow: select a real continuous generator logarithm of the closed factor return. The explicit branches are

G_m=ell I+omega_m J, J=[[0,-1],[1,0]],
ell=log(rho_t)/tau<0, omega_m=(phi+2pi m)/tau, m integer.

Every exp(tau G_m)=B_t. A fixed update and fixed clock do NOT choose m. For t≠0 each omega_m≠0. EXTRA Hangle: theta=g Z_1, dimensionless radians with gain g>0, and physical velocity defined kinematically as theta_dot=g(ell Z_1-omega_m Z_2). The chart S_m has rows (g,0),(g ell,-g omega_m), determinant -g² omega_m, so rank two. Units of its rows differ (angle, angle/second), which is intentional; raw determinant is not an SI-invariant numerical conditioning metric. Small |omega| makes this chart sensitive and t→0,m=0 loses rank.

Cayley-Hamilton gives G_m²-2ell G_m+(ell²+omega_m²)I=0. Hence the exact closed linear physical flow, conditional on these extra premises, has

theta_ddot=-gamma theta_dot-kappa_m theta,
gamma=-2ell>0 [s^-1], kappa_m=ell²+omega_m²>gamma²/4 [s^-2].

S_m B_t S_m^-1 is its exact event return, not merely its tangent. A chosen inertia Iphys>0 [kg m²], another physical premise, yields E=Iphys(v²+kappa_m theta²)/2 [J] and E_dot=-Iphys gamma v²<=0. This is a conditional linear-oscillator energy identity, not identification of formation stock with energy. Near the geometry equilibrium, mapped trajectories stay within the proved factor domain at event times. Continuous physical interpolation is an added model; its validity between events is not evidence from the kernel.

Concrete rival branches m=0 and m=1 for t=1 have different omega² and kappa, but the SAME coupled canonical update, factor Z, clock, gain and sampled angle sequence; kinematic velocity identification differs. Independently fixed velocity or intervening times could distinguish them; angle endpoints alone cannot. Different tau also rescale gamma,omega,kappa; d,t,labels/gain/inertia need independent preparation/environment/instrument calibration. This construction makes actual discrete rotation possible without a target flow in the input or Z, but does NOT supply a unique physically selected generator or a full sinusoidal force. Native phase per event is amplitude-independent in the local eta-positive domain. An amplitude-dependent physical phase, nonlinear potential and interventions require an independently constrained additional observable/flow hypothesis and new closure proof. Replacing theta with arbitrary H(Z) generates D²H(GZ,GZ)+DH G²Z, which is not automatically -kappa sin(theta)-gamma theta_dot. No arbitrary nonlinear readout repair is performed.

## Boundaries, source-wide controls and typed lift
At t=0, B=aI recovers P77/P79. Principal radial generator and kinematic angle/velocity have rank<=1 at equilibrium. Nonzero m aliases remain additional choices. At |t|=10, rho>1, so the present contraction/factor convergence hypotheses fail; this is not a universal impossibility theorem for alternative constructions. Outside the local eta-positive region, an additional sign change can alter phase; no global phase theorem is stated. D is not globally positive: on sufficiently large planar perturbations its smaller eigenvalue d-2|t||z| is negative. The positivity/terminal result is local. F=0, R non-scalar, variable environment labels, selection crossing, changing rank, seed and off-slice perturbations need separate analysis.

Whole-paper search considered autonomous scalar monotonicity and finite seed capacity (II87/88), full matrix update and quotient, weighted load balance, formation/loss/seed and historical witness (II86), entropy/diversity, regular differential chain, viability certificates (II88/Part I20), factor/clock (II89), tensor lift (II90). In this local full-persistence extension msel=m4=1, stock tr R and witness history are preserved, seed=0, formation entropy log2 is constant. These exact balances impose no choice of m, gain, seconds or inertia; they must not be called mechanical energy conservation. The commutator policy is an explicitly introduced environment commitment, not deduced from balances or finite seed theorem. No tensor or fractal architecture is needed for rotation.

For a justified exact lift of this construction only: Y,K,P,L map to their tensor product with I_h, R,W map to tensor product with I_h/h. Set A_h=4h(W_h-I_(2h)/(2h))=A⊗I_h and C_h=-i[L_h,A_h]/2=Caxis⊗I_h. Use normalized traces tr(A_h Y_h)/(2h), tr(C_h Y_h)/(2h), tr Y_h/(2h). The declared commutator input and every full-persistence matrix function/channel commute with this lift; trace loads acquire the compensating auxiliary trace and alpha is unchanged. Thus s,u,v,T,B,Z and all physical ambiguities agree exactly on the lift image. Total formation/witness are preserved; entropy gains log h as replicated bookkeeping. Off-image perturbations and replicated seed degeneracy are not covered; no physical fractality follows.

Status: actual rotating canonical tangent and exact local nonlinear rank-two endpoint factor PROVED UNDER the declared commutator input/label/slice hypotheses. Conditional linear force/energy PROVED with additional clock/logarithm/angle/inertia premises. Physical coupling choice, branch, seconds, full sine law, independent nonlinear instrument/preparation, interventions and universal application remain OPEN. Next necessary dependency: independently calibrated environment/frame, physical instrument/preparation and event-phase/time constraints for this alternative, then a frozen comparison on allowed development data against prior versions and strong nonlinear mechanical rivals. Do not label branch selection or interpolation as an internal force derivation.
