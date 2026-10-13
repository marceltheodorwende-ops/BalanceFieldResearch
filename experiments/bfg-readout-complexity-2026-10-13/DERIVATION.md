# P79 — Finite nonlinear readouts, sensitivity cost and kinematic closure

## Statement, assumptions and active source

Following P78, test a concrete nonlinear family that does not insert a prescribed mechanical trajectory: fixed polynomial/rational readouts of the two gauge-invariant evolving coordinates p of P77. Derive their necessary complexity, conditioning and physical-velocity obligations. No favorable coefficients, clock or preparation are fitted. These readout and apparatus hypotheses are EXTRA; this is not a universal BFG no-go.

Sole source: Dynamic Order,8October2026,144pages,SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. II83–85(121–143) and AppendixA172–187 supply the canonical endogenous update. P77's n2,full-persistence,R=r0I,constant inputd=29/90 construction proves p+=a p,a=16/135,retaining K transport and gauge invariance. PartI22–23(87–91)/II89(161–162) require actual factor/clock/endpoint closure; event seconds, physical readout and generator are not kernel axioms. II88.2(155) is a declared input extension, not autonomous dynamics. The algebra below also holds for any fixed0<a<1 and any number of factor coordinates sharing the same multiplier.

Let p_k=a^k p0, with a fixed readout theta=H(p;ell), where ell denotes invariant labels. Along this actual orbit ell is constant. Assume all observed states lie in the declared readout domain and recordings are successive canonical events or a forward subsequence. Readouts involving discarded scalar geometry, changing policies/labels, independent clocks or other evolving multipliers lie outside this family.

## 1. Polynomial and rational complexity bound

If H is a multivariate polynomial of total degree D, restriction to the ray gives h(r)=H(r p0)=sum_{d=0}^D c_d r^d. True observation parameters r_i=a^{k_i} decrease strictly for increasing event indices. Suppose L ordered reported angles q_{i0},...,q_{i(L-1)} have alternating adjacent differences, each magnitude>2epsilon. Every true angle within its measurement box has the same strict alternating directions. The mean-value theorem gives L-1 ordered points between the r_i with alternating nonzero derivative signs. Continuity then gives at least L-2 distinct roots of h' in disjoint gaps between those points. A nonzero polynomial h' of degree at mostD-1 has at mostD-1 real roots. Therefore

D >= L-1.

If h' is identically zero, the ray readout is constant and cannot have L>=2. For L<2 no positive degree lower bound is inferred. Hidden multivariate dimension adds coefficients but not additional ray powers; neutral label parameters do not defeat the bound. Offsets/gain sign preserve the number of alternating directions. Nonuniform/skipped forward events preserve ordering and the same bound; no event-to-seconds inference is needed.

If H=P/Q with total degrees m,n and Q nonzero on the connected ray segment, h'= (P'Q-PQ')/Q^2. Its numerator has degree at mostm+n-1 (with possible further cancellations). Thus the same reasoning yields

m+n >= L-1.

A zero derivative numerator again means a constant rational readout on that segment. Rational poles between observations invalidate the domain hypothesis and cannot be silently used as a regular measurement bridge. This is a necessary degree-sum bound; it does not identify the coefficients, conditioning, force, inertia or a sufficient fit.

The sequential extrema algorithm in PROTOCOL.md need not be optimal: any independently verified alternating chain supplies a valid lower bound. A stronger chain could strengthen it; no maximal complexity discovery is claimed. Real empirical outcomes are development-only conditional statements.

## 2. Finite sensitivity and preparation cost

Assume independently a Lipschitz constant L_H for H on a connected region containing the segment between p_i,p_j, and radius R=||p0|| in the chosen factor norm. Then

|theta_j-theta_i| <= L_H R (a^{k_i}-a^{k_j}).

Reported endpoints imply |theta_j-theta_i| >= |q_j-q_i|-2epsilon. Taking k_i=i,k_j=j for the separately declared one-event-per-row hypothesis gives

L_H R >= (|q_j-q_i|-2epsilon)/(a^i(1-a^(j-i)))

when the numerator is positive. More skipped events have k_i>=i and k_j-k_i>=j-i; the denominator is not necessarily bounded above by a^i(1-a^(j-i)) for arbitrary skips! Accordingly this exact expression is asserted ONLY for one event per row. A conservative bound for arbitrary forward skips is L_H R >= (|q_j-q_i|-2epsilon)/a^i, because a^{k_i}-a^{k_j}<=a^i. This correct distinction is retained in code/report; preparation at an earlier starting index only strengthens the conservative bound.

For fixeda=16/135 the logarithmic expression is

log10(L_H R) >= log10(|q_j-q_i|-2epsilon)-i log10(a)-log10(1-a^(j-i)).

It avoids numerical underflow and measures a joint readout/preparation requirement, not a measured condition number. Scaling factor coordinates inversely rescales L_H and R; their product is unchanged under uniform scaling. No R=1 normalization, physical factor noise, SI gain or maximum allowed L_H R is invented. As freea approaches1, this particular rapid-contraction cost changes; there is no uniform enormous bound across all possible a.

If a chosen readout has state error delta p, its Lipschitz forward error is at mostL_H||delta p||. A large *necessary* L_H R does not prove actual measurement noise or a universal prediction failure; it means a quantitative sensitivity/preparation certificate is needed before asserting robustness. Increasing degree alone does not supply it. The data's error boxes are sensitivities, not certified apparatus accuracy.

## 3. Why these bounds cannot be promoted to an arbitrary nonlinear obstruction

For any finite distinct event parameters r_i=a^{k_i}>0 and arbitrary values theta_i, the Lagrange polynomial h(r)=sum_i theta_i product_{j!=i}(r-r_j)/(r_i-r_j) interpolates them with degree at mostnumber_of_points-1. This mathematical existence is not a recommended fit, conditioning guarantee, physical calibration or force selection. Exact interpolation of seen development data is not independent evidence. Its Vandermonde determinant is product_{i<j}(r_j-r_i), illustrating sensitivity of close/small nodes; no such high-degree repair is performed.

An analytic example can produce any finite number of oscillations without singular rank: Pi(p1,p2)=(p1+sin(Cp2),p2) is an invertible triangular analytic chart with determinant1, and along p1=0,p2=a^k r0 its angle can have arbitrarily many finite changes when the EXTRA constantC is large. The conjugate endpoint map Pi(a Pi^-1(z)) is exactly closed; C is a supplied readout scale, not a BFG-selected physical constant. This chart need not satisfy physical velocity kinematics or the sine force.

Analytic h near0 is eventually monotone along a ray unless it is constant there: the first nonzero coefficient c_m gives h'(r)=m c_m r^(m-1)+O(r^m), whose sign is fixed for sufficiently small positiver. Thus an infinite tail of certified directional alternations accumulating at0 is incompatible with a nonconstant analytic ray readout. Finite noisy records neither certify an infinite tail nor furnish a uniform analytic neighborhood/jet bound, so this is not a real-data global exclusion.

Smoothness alone is weaker. For fixeda in(0,1), define f(r)=exp(-1/r^2) sin(pi log(r)/log(a)+pi/2) for r>0 and f(r)=0 for r<=0. All derivatives at0 vanish: each derivative is an exponentially flat factor times finitely many inverse powers/log oscillatory bounded terms. Pi(p1,p2)=(p1+f(p2),p2) is a global C-infinity triangular diffeomorphism with determinant1. Along p1=0,p2=a^k, its angle alternates sign forever, though the amplitudes decrease faster than any power. Pi(a Pi^-1(z)) closes exactly. This supplies a regular smooth counterexample to extending the analytic eventual-monotonicity claim to every C1/C-infinity observable. It supplies no physical instrument, causal intervention or force law. Finite resolution eventually masks these oscillations.

## 4. Kinematic velocity is a further independent selection rule

A second number labelled velocity is insufficient. Suppose an EXTRA continuous generator on p is the principal radial choice X(p)=ell p with ell=log(a)/tau<0 and tau>0 supplied in seconds. If theta=H(p) is C2, actual physical velocity must be V=DH(p)X(p). At the fixed point p=0,

D V(0)=ell D H(0).

The two rows of D(theta,V) are proportional, so rank<=1. No regular two-dimensional position/physical-velocity chart at equilibrium follows from this radial generator, however nonlinear H is. A positive C1 state-dependent radial speed X(p)=ell(p)p has the same rank restriction with ell(0); C2 is needed for the displayed differential. This is a scoped kinematic obstruction on a declared generator, NOT on all discrete BFG realizations.

There are other continuous generators with the same discrete factor. Let J=[[0,-1],[1,0]], A_j=ell I+(2pi j/tau)J for integerj!=0. Then exp(tau A_j)=aI. With theta=u^T p for a fixed nonzero rowu and physical V=u^T A_j p, the chart has determinant proportional to(2pi j/tau)||u||^2 and rank2. Cayley-Hamilton now gives

theta'=V, V'=2ell V-(ell^2+(2pi j/tau)^2)theta.

This is a full linear oscillator law DERIVED UNDER the additional rotating-generator and angle premises. It is not an internally selected BFG force: all integerj give the same canonical return and extra clock but different stiffness. Arbitrary nonlinear H gives acceleration D^2H(X,X)+DH A_j^2p; this formula imposes the actual position/velocity/force compatibility to be checked, not a reason to assume it equals -kappa sin(theta)-gamma V. P77 imposed that sine flow through a readout conjugacy; P78 exposed the additional phase/chart selection needed to distinguish branches.

## 5. Supporting source combinations and typed level transfer

Whole-paper search is directed at these missing readout/kinematic constraints. II83–85/AppendixA retain full nonlinear/matrix transport before p projection. Gauge invariance holds for p and every H(p) here. II86 stock/witness balances and spectral diversity do not supply readout degree, jet/scale bounds or physical velocity. II87 finite seed capacity does not change the radial factor or create independently measured directions. II88.2 input and II88.3 local viability/stability preserve the P77 domain but do not select the continuous logarithm branch. II88.4's independently supplied mediator would add a generator premise; it cannot be mislabeled as internal derivation. PartI22–23/II89 require the full physical kinematic/endpoint bridge, beyond discrete fiber closure.

On the full-persistence lift image II90(163–164), P77's normalized trace p_m equals p. Therefore the same ray restriction, degree cost and principal/rotating-generator distinction transfer exactly. Formation stock/witness normalization remain, ranks multiply, discarded tensor coordinates add no independently calibrated phase/readout. Off-image states and seed branches need separate treatment; seed replication may terminate T_seeddeg. No physical fractality or extra independent evidence follows from replication.

Status: complexity/sensitivity bounds, analytic/smooth alternatives and kinematic statements are proved under their explicit hypotheses. Real outcomes test the frozen polynomial/rational/radial-factor interface, not arbitrary nonlinear BFG. Parent physical force, actual event alignment/preparation, SI clock and independent nonlinear measurement selection remain OPEN. Next necessary dependency: a force-independent nonlinear measurement law with quantitative domain/jet/sensitivity bounds AND a separately constrained nonradial physical generator/carrier or phase selection. A high-degree interpolant or freely chosen logarithm branch does not discharge that dependency.
