# Repeated adjacency evolution: a created edge persists at every finite event

23 October 2026. BFG-only. [Preregistered protocol](ADJACENCY_EVOLUTION_PROTOCOL.md).
Source: unchanged pinned complete Dynamic Order Parts I/II and the source-derived aligned Y update on C.
The graph tested here is the entrywise support of Y in a retained formation-node basis. It is a declared internal candidate, not an identified spatial geometry.

## 1. Different question from the preceding channel tail

CHANNEL_RANGE_DERIVATION.md showed that a nearest-neighbor Y matrix need not yield a nearest-neighbor one-event kernel channel.
Now ask whether the proposed adjacency matrix Y itself stays nearest-neighbor under repeated SOURCE Y updates.
Keep the same initial family
Y0=I3/4+epsilon [[0,1,0],[1,0,1],[0,1,0]],
F=diag(1,2,3), W=I3/3, P_carrier=I3,
0<epsilon<=1/40.
Its spectrum lies in [1/5,3/10], hence C. Formation is an aligned constant, so its three distinct eigenmodes provide fixed covariant node projectors.

## 2. Fixed-alpha monotonicity and convexity on the actual interval

For g_alpha(y)=[alpha+(1-alpha)y²]/(1+y)² and beta=1-alpha,
g'_alpha(y)=2(beta y-alpha)/(1+y)³,
g''_alpha(y)=2[beta(1-2y)+3alpha]/(1+y)^4.
For 0<y<=1/2 and 0<alpha<1, the second derivative is strictly positive.
On the actual C spectral interval [m_k,M_k], the source weighted-mean bound gives
alpha_k/beta_k<=M_k²<m_k,
so the first derivative is strictly positive there as well.

These are FIXED-alpha derivatives used in scalar spectral functional calculus. They are NOT the full derivative of the endogenous state map when its formation/load-dependent alpha is varied. The earlier distinction about endogenous derivatives is retained.

## 3. The actual endogenous alpha sequence still gives the all-finite-event theorem

For one full source trajectory, first compute its actual alpha_0,alpha_1,... from F,Y_k. Define auxiliary scalar interpolation functions
phi_0(t)=t,
phi_(k+1)(t)=g_(alpha_k)(phi_k(t)).
In these functions the already source-computed alpha sequence belongs to that ONE trajectory; it is not recomputed for each interpolation argument t.
Functional calculus gives Y_k=phi_k(Y0).

Let [m0,M0] be the initial spectral interval. Inductively:
- phi_k maps [m0,M0] onto [m_k,M_k], since each step is strictly increasing there;
- g_(alpha_k) is strictly convex and strictly increasing on [m_k,M_k];
- composition preserves convexity, and phi_k is strictly convex for every k>=1.

Explicitly, for k>=1,
(phi_(k+1))''=g''_(alpha_k)(phi_k)(phi'_k)²
 +g'_(alpha_k)(phi_k) phi''_k>0.
At k=0, phi_1''=g''_(alpha_0)>0.
This proves the result with the REAL endogenous schedule. No constant-alpha approximation or desired-target fitting is used.

For the three-node path let a=1/4 and d=sqrt(2)epsilon. The exact spectral projector identity is
(Y_k)_13=[phi_k(a-d)+phi_k(a+d)-2phi_k(a)]/4.
Strict convexity therefore implies
(Y_k)_13>0 for EVERY finite k>=1.
The two original neighbor entries are
(Y_k)_12=(Y_k)_23=[phi_k(a+d)-phi_k(a-d)]/(2sqrt(2))>0.
Thus the initial path becomes a triangle after its first event, and this exact three-edge support persists at every further finite event on this family.

The theorem concerns this family, not arbitrary support monotonicity for every matrix or node choice. Positive Y does not mean every matrix entry must be positive in an arbitrary basis.

## 4. First fill entry and finite corroboration

At epsilon=1/40 the source gives alpha0=3779/63763 and
(Y1)_13=413979576/2486758594075
≈0.00016647356803606555.
This is a rational, strictly positive source Y entry, distinct from the earlier kernel-transition probability P31≈7.76536e-6.

Nine exact rational events were computed: three epsilon values 1/40,1/80,1/160, each across three events.
Each successor has positive endpoint entry, commutes exactly with Y0, and has a rational Gershgorin certificate for C membership. These conservative bounds establish membership without inferring exact spectral inequalities from floating-point samples.

The unchanged complete source was then run for the same three trajectories, carrying its actual K,F,W,Y successors rather than resetting K:
- nine complete source events;
- three additional simultaneous-unitary checks;
- twelve complete source calls overall.
Maximum rational/source Y residual <1.5e-16; retained spectral-frame residual <1.1e-16; unitary-load residual <7.7e-16.
The smallest new-edge entry in these finite controls is about 5.20e-8, above the predeclared audit threshold. The threshold-based edge count is recorded as numerical evidence, not the mathematical definition of support.
The audit completed successfully; no source or witness-input changes were needed.

The exact all-finite-horizon theorem is the composition/convexity proof, not an extrapolation of nine events.
The known source numerical rank cutoff remains unchanged. No claim is made that floating-point code can follow arbitrarily small positive Y forever.

## 5. What is invariant and what is not

All Y_k are functions of Y0. Their spectral-projector algebra is retained, and [Y_k,Y0]=0.
Yet their formation-basis support changes. Spectral covariance and a fixed algebra do not preserve a chosen finite-band representation in a noncommuting node basis.

Meanwhile ||Y_k|| tends to zero by the proved source contraction. Hence the positive created edge can shrink to zero at the infinite boundary while remaining strictly nonzero at every finite event.
Taking graph support and taking the infinite-state limit need not commute. This is a mathematical support observation, not a finite physical-time collapse statement.

A proposed physical graph could instead retain an initial adjacency as an explicit historical reference, or use another source-covariant observable. That is a different declared readout requiring its own closure/locality test.
It cannot be obtained by silently deleting the new Y entries after each step; doing so changes the source dynamics.
The previous finite-band approximation bounds remain valid under their stated conditions but do not prove that this current-Y support stays a path.

## 6. Next dependency

Advanced: the current-Y nearest-neighbor graph is not invariant on the source; a created endpoint edge persists for every finite event in the stated family, with unchanged spectral projectors.
Remaining physical questions: which internal structure selects adjacency, dimension, metric and clock; whether an effective approximation with controlled memory/range supports a local limit; and how an identified energy-momentum four-current would be obtained.
The next concrete mathematical check is whether a retained reference graph can control multi-event source propagation through compositions without equating current sparsity with physical locality. No Lorentz causal speed, spacetime field equation or Einstein derivation is asserted.
