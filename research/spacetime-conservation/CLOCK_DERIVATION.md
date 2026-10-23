# State clocks, scalar unit ticks and physical-time ambiguity

23 October 2026. BFG-only. Preregistered checks: [CLOCK_PROTOCOL.md](CLOCK_PROTOCOL.md).
Source: unchanged pinned Dynamic Order, Parts I/II; sections 23, 55, 70.4 and II89. Standard real analysis is applied to the already derived source update. This is a mathematical construction, not a clock calibration.

## 1. Source requirements and the declared domain

[SOURCE] Section 23 distinguishes event count k from physical durations T_clock([Xi])>0 and requires independent calibration. II89 further requires sum T_clock=∞ for unbounded physical time, and a separately constructed continuous flow satisfying the discrete endpoint condition. Positivity alone establishes neither condition.

Work on the full-persistence invariant class C proved in STABLE_PAIR_DERIVATION.md:
P=I, F>0, 0<m<=M<=1/2, m>=2M². Rank n is constant; no selection/seed event is covered.
The simple-spectrum condition is needed only for the previous two-smallest selector, not for the clock results below. In aligned representatives Y_+=g_alpha(Y), and M_+<=f(M) where
f(y)=2y²/[(1+y)²(1+y²)].
All eigenvalues and log ratios here are dimensionless source quantities.

## 2. A uniform envelope and two opposite accumulation behaviors

For 0<y<=1/2,
f(y)/y = 2y/[(1+y)²(1+y²)] <= 2y/(1+y)² <= 4/9.
The last inequality has the exact certificate
4/9 - 2y/(1+y)² = 2(1-2y)(2-y)/[9(1+y)²] >=0.
Consequently M_k <= (4/9)^k M_0 on C.

Consider three DECLARED candidate duration functions on the SAME full BFG trajectory:
d_const(Xi)=1,
d_load(Xi)=tr(Y)/n,
d_log(Xi)=ln[tr(Y)/tr(Y_+)].
They are all positive and invariant under simultaneous source unitary changes; d_log uses the deterministic source successor, hence is also a function of the current state, not an independent future input.
For positivity, M_+<=4M/9 < M alone is insufficient to prove trace decrease, so use the pointwise bound:
alpha<=r(M), g_alpha is increasing on [m,M], but a stronger direct estimate is available:
g_alpha(y)<=g_(r(M))(y) and the class ensures alpha/(1-alpha)<=M²<m.
Rather than infer a pointwise ratio bound from this, note that each ordered eigenvalue strictly decreases:
g_alpha(y)<y is equivalent to alpha(1-y²)< y+y²+y³.
Since alpha<=r(M)<=M²<=m/2<=y/2 and 1-y²<1, this inequality is strict.
Thus tr(Y_+)<tr(Y), as required.

Their sums differ:
- sum d_const=∞.
- sum d_load <= sum M_k <= 9M_0/5 <∞.
- sum_(k<N) d_log = ln[tr(Y_0)/tr(Y_N)] ->∞, since tr(Y_N)<=n(4/9)^N M_0 ->0.

These are exact infinite-orbit mathematical statements on C. They do not claim the floating-point implementation can pass its rank tolerance indefinitely.
Multiplying any duration by a common positive constant t_* with units seconds gives possible additional clock maps of the source's declared type, with either finite or unbounded accumulated time. No value of t_* or choice among these maps follows from this argument.
The finite load-clock sum is a concrete Zeno-type candidate, not a physical prediction and not a claim of finite-event termination. A measured clock would have to select/reject it independently.

## 3. A constructive state-only unit-tick coordinate

Do not infer from the missing physical clock that no state-only event coordinate exists.
On the scalar full-persistence branch Y=yI, 0<y<=3/10, all other neutral source data held fixed,
y_+=f(y).
This is a separate admissible subbranch, not a simple-spectrum two-mode selection theorem.
Let y_j=f^j(y), d(y)=(1+y)²(1+y²), and a_j=-ln(2y_j)>0.
The exact scalar recurrence is
2f(y)=(2y)²/d(y),
a_(j+1)=2a_j+ln d(y_j).
Therefore define
A_N(y)=2^-N a_N
      =a_0+sum_(j=0)^(N-1) 2^-(j+1) ln d(y_j).

Set C_*=ln d(3/10)>0. As 0<y_j<=3/10 and d increases,
0<=A(y)-A_N(y)<=C_* 2^-N,
where
A(y)=a_0+sum_(j=0)^∞ 2^-(j+1) ln d(y_j)>0.
This proves convergence, positivity and a computable tail bound. Uniform convergence of the correction series also proves continuity on the open branch.

Shifting the limit index gives
A(f(y))=2A(y).
Hence the continuous dimensionless state function
tau(y)=log_2 A(y)
obeys tau(f(y))=tau(y)+1 EXACTLY.
It is not an extra dynamical variable or a stored event history: it is a function of current y, defined through its deterministic source orbit. Evaluating its series is a mathematical readout computation.

As y->0, A(y)=-ln(2y)+O(1), so tau(y)->∞ and
tau(y)-log_2[-ln(2y)] ->0.
No finite continuous extension of ANY unit-tick state coordinate to y=0 can exist: taking the limit in tau(f(y))-tau(y)=1 would give 0=1. The boundary is not an admissible nonterminal state here; this is a boundary regularity statement.

## 4. What is selected, and what is not

For any epsilon with |epsilon|<1/(2pi),
tau_e(y)=tau(y)+epsilon sin[2pi tau(y)]
also satisfies tau_e(f(y))=tau_e(y)+1.
The reparametrization of tau is strictly increasing because its derivative is at least 1-2pi|epsilon|>0. Our preregistered epsilon=1/(8pi) gives a lower bound 3/4.
These clocks give the SAME unit duration at every discrete endpoint, but different state-coordinate values. They demonstrate nonuniqueness of an interpolating state coordinate; the load-versus-constant examples above separately demonstrate nonuniqueness of endpoint durations.

An additional asymptotic normalization
tau(y)-log_2[-ln(2y)] ->0
does select the constructed tau uniquely among unit-tick functions with that same condition:
the difference of two such functions is invariant along f and tends to zero, so is identically zero.
This is a useful explicit mathematical selection condition. It is NOT imposed by the source as an SI clock law, and it does not select physical time between events. We do not claim nonuniqueness after imposing all possible extra boundary conditions.

Nor does a scalar readout supply an autonomous physical generator, spatial worldline, synchronization rule or Lorentz transformation. Extending this particular Abel coordinate to the nonscalar, globally weighted alpha dynamics is a separate problem; replacing every matrix eigenvalue by f would be wrong.

## 5. Relation to the component-balance result

A positive time assignment preserves the discrete endpoint K_+=Phi_Y(K). In the retained nondegenerate pair it still has
(p0,p1,p2,p3)_+=(p0,h p1,h p2,p3), 0<h<1.
For any finite positive chosen duration, transverse finite differences remain (h-1)p_i/d and are generically nonzero.
Thus a clock alone does not remove the proven fixed-component charge defect or derive a joint physical energy-momentum current.
This leaves open a properly derived interaction/current or relational observable with its own source-supported transport law.

## 6. Fresh checks, correction and scope

clock_audit.py verifies the exact rational envelope/scalar identities and imports the original source only after its Git-blob check.
- 12 complex preparations, n=3,4,5,6, two events each: 24 full source events. Spectral-envelope violation and log-telescoping residual were zero at the recorded precision; all tested load/log durations were positive.
- Three scalar source events at y=1/5,1/4,3/10 agree with f(y)I to <1e-16.
- The log-domain N=48 evaluation has analytic A-tail bound about 2.171e-15. This bound excludes machine roundoff; no rigorous floating-point interval claim is made. Unit-tick residuals, with and without the periodic reparametrization, were <3e-16.
- The 48 log-domain iterations are NOT 48 completed source events; they use the independently derived scalar recurrence and avoid the source's known numerical rank cutoff.

The first executable symbolic assertion compared structurally different SymPy expressions with == and failed before source controls. Replacing it by exact rational cancellation established the SAME identity; formula, inputs and criteria were unchanged. The failure is retained here rather than presented as a successful first run.
GitHub CI is recorded separately in CI_VALIDATION.md.

Advanced: explicit quotient-positive duration candidates with contrasting accumulation, and a constructive scalar state-only unit-tick coordinate with a precise optional uniqueness condition.
Open: source-selected physical calibration, full nonscalar clock/flow, spatial translation and local joint four-current. The next distinct useful question is whether the retained pair and formation/witness references define a closed relational spatial observable and transport, rather than assigning physical seconds to event count.
