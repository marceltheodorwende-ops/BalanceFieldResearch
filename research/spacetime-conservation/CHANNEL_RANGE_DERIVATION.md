# Channel range on an internal path: exact two-hop transfer and controlled tails

23 October 2026. BFG-only. [Preregistered protocol](CHANNEL_RANGE_PROTOCOL.md).
Source: pinned complete Dynamic Order, Parts I/II, unchanged full ambient update. This tests a declared internal formation-node graph, not an assumed physical spatial lattice or spacetime causal cone.

## 1. The source channel is a matrix function with a range question

On full persistence write beta=1-alpha and D=alpha I+beta Y²>0.
The previously derived operators simplify EXACTLY to
T_C=sqrt(alpha) D^-1/2,
T_B=sqrt(beta) Y D^-1/2.
Indeed M=(I+Y)^-2 D, and the commuting positive functions of Y give M^-1/2=(I+Y)D^-1/2. The I+Y factors cancel.
This is an algebraic form of the SAME source update, not a replacement channel.

Choose formation eigenmodes as nodes, F=diag(1,...,n), and declare the path adjacency through
Y=(1/4)I+epsilon A_path, 0<epsilon<=1/40.
Here A_path has ones only between consecutive nodes.
Every spectrum lies in [1/5,3/10], hence in C; the source remains nonterminal at the exact level.
The graph and node labels are covariant when the entire state and formation projectors are conjugated together.

The question is specific: does Y having only nearest-neighbor offdiagonal entries imply that the actual one-event population transition
P_ij=|(T_C)_ij|²+|(T_B)_ij|²
also has only nearest-neighbor support?
No such implication is assumed.

## 2. Exact three-node counterexample to the one-hop rule

Take n=3, epsilon=1/40, W=I3/3 and K=diag(1,0,0).
The source yields
alpha=3779/63763,
m=1/4-sqrt(2)/40, M=1/4+sqrt(2)/40,
with the third eigenvalue 1/4.
Let t_C(y)=sqrt(alpha)/sqrt(alpha+beta y²).
The spectral projectors of the three-node path give the endpoint coefficient
(T_C)_13=[t_C(m)+t_C(M)-2t_C(1/4)]/4.

It is STRICTLY positive. Direct differentiation gives
t_C''(y)=sqrt(alpha) beta (2beta y²-alpha)/(alpha+beta y²)^(5/2).
The source weighted-mean bound implies alpha/beta<=M², while
2m²-M²=(102-60sqrt(2))/1600>0.
Thus t_C is strictly convex throughout [m,M], and its centered second divided difference is positive.
This establishes nonzero range without inferring exact positivity from floating-point noise.

Numerically evaluating the independently specified exact spectral formulas gives
(T_C)_13≈0.0008571978507857012,
(T_B)_13≈-0.0026515227357522073,
P_31≈7.765360973602495e-6>0.
For this initially diagonal K, the complete source population at node 3 is exactly P_31. The source-derived integrated current from node 1 to node 3 is likewise P_13.
But Y_13=0 and the declared path distance is two.

Therefore strict one-hop propagation on THIS candidate internal Y-adjacency graph is refuted.
This result does not prove that every possible finite interaction radius fails in every BFG sector, or that a physical Lorentz-causal law has been violated. One recursive event has no independently derived spatial length or duration here.

## 3. Constructive approximate range bound

The nonzero tail must not be removed from the source to enforce a desired answer.
Instead let
d_min=min spec D>0, d_max=max spec D,
c=(d_min+d_max)/2,
H=I-D/c,
r=||H||_2=(d_max-d_min)/(d_max+d_min)<1.
The operator-norm convergent binomial series is
D^-1/2=c^-1/2 sum_(j=0)^infinity c_j H^j,
c_j=binomial(2j,j)/4^j, 0<c_j<=1.

For S_N=c^-1/2 sum_(j=0)^N c_j H^j,
||D^-1/2-S_N||_2 <= c^-1/2 r^(N+1)/(1-r).
Consequently
||T_C-sqrt(alpha)S_N||_2 <= sqrt(alpha/c) r^(N+1)/(1-r),
||T_B-sqrt(beta)Y S_N||_2 <= sqrt(beta/c) M r^(N+1)/(1-r),
where M=||Y||_2 for the positive source Y.

For a path-tridiagonal Y, D and H have bandwidth two. Thus S_N has bandwidth 2N and Y S_N bandwidth 2N+1.
If the declared path distance d(i,j)>2N+1, the approximants vanish at that pair and
P_ij <= [(alpha+beta M²)/c] r^(2N+2)/(1-r)².
For d>=2 choose N=floor((d-2)/2). The same support-counting argument extends to a declared sparse graph using its graph distance, with Y connecting at most one edge per multiplication.

This is a rigorously controlled, state-dependent approximate-range statement. The constants depend on the current spectrum and alpha. No uniform event-time, continuum-limit, system-size or SI propagation speed is established. If r approaches one, this bound becomes weak; positivity alone does not select a physically useful uniform locality scale.
The bound constructs finite-band approximants for analysis. Those approximants are NOT substituted into the source channel and are not claimed to preserve all source identities after truncation.

## 4. Exact alternative: disconnected reducing blocks

If a component projector Q commutes with Y, every source T_a is block diagonal relative to Q and I-Q.
Therefore there are exactly zero cross-component transition weights and source-current edges, and
tr(Q K_+)=tr(Q K)
for arbitrary K, including nonzero cross-component coherence.

This gives an exact source-supported separation property for disconnected reducing blocks, in contrast to the failed one-hop condition inside a connected path.
It is not full subsystem autonomy: alpha still depends on all formation/load data. The pair/environment fiber witnesses already show that global-load dependence can affect local evolution. Zero cross-block stock transfer must not be promoted into an operational physical no-signalling theorem.

## 5. Fresh controls and numerical limits

Final channel_range_audit.py run:
- 12 source events for n=3,4,5,6 at epsilon=1/40,1/80,1/160, with a positive single-node initial kernel.
- Four additional simultaneous-unitary source checks.
- Four disconnected-block source events, n=4,5,6,7, with generic cross-component kernel coherences.
- Total: 20 complete source calls.
- Exact rational alpha, three-node spectrum and convexity certificate, symbolic derivative and positive binomial coefficients.
- Independent 50-digit evaluations of the exact endpoint formulas, compared to the source and to matrix-function reconstruction.
- Degree N=0,1,2 operator-norm approximation checks with the analytic tail bounds and exact bandwidth support; all tested distance-bound violations were zero.
- Maximum source/reconstruction or block-stock residual <2.6e-15, below the predeclared 1e-10 criterion.

The smallest recorded endpoint transition estimate in the longer/weaker paths is about 2.69e-19. These are matrix-function magnitude estimates; the source comparison has an absolute matrix error scale around 1e-15 and does not certify relative positivity of populations that small.
The exact nonzero theorem is the independently proved three-node witness above. Longer-path samples are not a universal exact support proof.
The largest r among these finite controls was about 0.17645. This does not establish a uniform bound for every source state.

The initial audit passed. Its result label was clarified to say nearest-neighbor counterexample, rather than suggesting that all finite interaction radii had been excluded, and the final run was repeated. No source operator, test input or acceptance threshold changed.
GitHub CI evidence is recorded separately for the explicit published code commit.

## 6. Consequence for the physical bridge

Advanced: a source-derived strict two-hop counterexample, conditional geometric range bounds, and exact separation of disconnected Y blocks.
Open: why this declared internal graph should represent spatial adjacency, what sets its metric/dimension and event duration, whether controlled many-event/coherence effects support an effective local limit, and how all four physical current components would be identified.
The next useful calculation is the stability of a chosen locality description under repeated Y updates and the global alpha feedback; an initially sparse Y need not remain sparse in this node basis.
No Einstein equation, Lorentz-causality conclusion or calibrated physical transport law is asserted.
