# Internal mode graphs and an exact source-channel continuity identity

23 October 2026. BFG only. [Preregistered protocol](MODE_GRAPH_PROTOCOL.md), including its channel-current extension committed before evaluation.
Source: pinned complete Dynamic Order, Parts I/II; unchanged full-persistence update and its previously derived double-commutator identity.
All graphs, node choices and interpretations below are declared mathematical readouts, not an assumed physical spatial manifold.

## 1. Natural retained-mode graphs

On C choose the retained orthogonal Y-spectral projectors Q_i, or a complete retained refinement from the previous Y/F/W construction. Each block satisfies Y Q_i=y_i Q_i. Distinct refined blocks may have equal y_i.
Let R_F=F/tr F, and define for i!=j
a^F_ij=tr(Q_i R_F Q_j R_F),
a^W_ij=tr(Q_i W Q_j W),
b_ij=tr(Q_i K Q_j K).
They equal squared Hilbert-Schmidt norms of the corresponding crossblocks, so are nonnegative, symmetric, unitary invariant edge weights.
The normalized F/W edges are dimensionless; b has squared formation units. These are candidate INTERNAL adjacency/coherence weights, not calibrated distances or energy fluxes.

The node stocks are
q_i=tr(Q_i K), f_i=tr(Q_i F), w_i=tr(Q_i W).
With T_a positive functions of Y, Q_i T_a=t_a(y_i)Q_i, the source gives
Q_i K_+ Q_j=h_ij Q_i K Q_j,
h_ij=sum_a t_a(y_i)t_a(y_j)>0.
Therefore
q_i,+=q_i, f_i,+=f_i, w_i,+=w_i,
a^F_ij,+=a^F_ij, a^W_ij,+=a^W_ij,
b_ij,+=h_ij² b_ij.
Equal-load refined blocks have h_ij=1. Distinct-load coherences attenuate, with no transfer of these Y-node stocks.
All finite-step edge supports are retained because h_ij>0, although weights can shrink.

For simple Y, the graph readout (y_i,q_i,f_i,w_i,a^F_ij,a^W_ij,b_ij) is closed:
alpha is computed from the complete y_i/f_i list, y_i,+=g_alpha(y_i), and all other successors follow the formulas above. Offdiagonal phases are not required for this magnitude evolution.
For higher-rank blocks the same formulas hold; within-block b_ii=||Q_i K Q_i||² is an additional fixed norm if a full norm budget is retained, rather than being inferred from q_i².
The identity
||K||²_HS-||K_+||²_HS=sum_ij (1-h_ij²)b_ij
is a coherence norm loss, not demonstrated physical energy dissipation.

## 2. Guessed phase currents fail this node continuity equation

An algebraically natural antisymmetric candidate is
J^R_ij=2 Im tr(Q_i R Q_j K), R=R_F or W.
It is gauge invariant and J^R_ji=-J^R_ij. Because R is dimensionless, it has K-stock units as an event-integrated candidate, not a calibrated rate.

Test Delta q_i+sum_j J^R_ij=0.
The true source has Delta q_i=0 on these retained Y-mode nodes, so this candidate would need zero divergence universally. It does not.

Take exactly
Y=diag(1/5,3/10),
F=[[1,i/2],[-i/2,1]], W=F/2,
K_±=[[1,±1],[±1,1]].
F,W are positive and K_± positive semidefinite. Both full states have identical graph readouts above, including q=(1,1) and b12=1.
The source has alpha=8/133, h12=31/sqrt(1001), h12²=961/1001.
It retains the node stocks while b12 decreases by 40/1001.
But J^F_12=J^W_12=±1/2, so the continuity defect is (±1/2,∓1/2).

The current candidates also have opposite values on the SAME graph fiber. Thus they are not observables of this magnitude-only graph, although the graph update itself remains closed. This is a scoped II89 readout distinction, not a failure of full-state closure.
The source evolution gives J^R_ij,+=h_ij J^R_ij; it does not impose the required universal divergence cancellation.

## 3. Continuity alone cannot supply a missing oriented current

For a finite chosen undirected graph, orient its E edges and let B be its incidence matrix.
The equation Delta q+Bj=0 reduces here to Bj=0.
A forest has no nonzero antisymmetric divergence-free internal edge flow: remove leaves recursively. For a graph with V nodes and c connected components, rank B=V-c (a spanning forest supplies V-c independent columns and every column sums to zero per component), hence
dim ker B=E-V+c.
Cycles leave circulation freedom. Zero stock change therefore neither proves every edge current must vanish on cyclic graphs nor selects one physically meaningful current.

A triangle example illustrates the limitation of the guessed candidate even when its initial divergence vanishes:
Y=diag(1/5,1/4,3/10),
F has diagonal 1 and offdiagonal 1/4, W=I/3,
K has diagonal 2, K12=K23=-i, K13=i and conjugates.
Both F and K are positive. Initially J^F_12=J^F_23=J^F_31=1/6.
Unequal source h_ij factors do not retain this circulation. At the next state its divergence is approximately
(0.00234719,0.000332128,-0.00267932),
although every Y-node stock remains fixed.
This is an explicit negative result for that formula, not a prohibition of all source-derived currents.

## 4. Constructive alternative FROM the actual channel

Do not stop at the failed guessed current. For ANY retained orthogonal node decomposition P_i with sum_i P_i=I, use the actual source T_a and define
J^Phi_ij=sum_a Re tr(P_i T_a P_j [T_a,K]).
No compensating reservoir, Hamiltonian or target continuity defect is inserted.

**Antisymmetry.** Since T_a,K are Hermitian, C_a=[T_a,K] is anti-Hermitian. Conjugating tr(P_i T_a P_j C_a) and cyclically permuting gives minus tr(P_j T_a P_i C_a). Hence J^Phi_ji=-J^Phi_ij, including zero diagonal.

**Exact continuity.** The full-persistence channel obeys
K_+-K=-1/2 sum_a [T_a,[T_a,K]].
For q_i=tr(P_i K), Hermiticity gives
Delta q_i=-sum_a Re tr(P_i T_a [T_a,K])
         =-sum_j J^Phi_ij.
Thus
q_i,+-q_i+sum_j J^Phi_ij=0
is an exact event-integrated INTERNAL K-stock continuity equation from the same BFG dynamics.
It holds at any full-persistence event with the stated retained projectors, not merely at the finite numerical samples. It does not cover general changing-rank/seed/terminal events.

For Y-mode nodes, P_i commutes with each T_a and P_i T_a P_j=0 for i!=j, so this current is zero. The fixed-stock result is reproduced constructively.

For formation-eigenmode nodes, P_i need not commute with Y or T_a. Formation is an aligned constant, so its spectral projectors provide a retained covariant node decomposition; use whole eigenspaces at a degeneracy instead of choosing arbitrary lines. J^Phi can then be nonzero and exactly describe a change in those node stocks.
Each traced expression is covariant under simultaneous source unitaries. The formula depends on full coherences and source operators; population-only or magnitude-graph closure in this DIFFERENT node basis has not been proved.

## 5. Exact nonzero formation-node transport example

Use the same two-dimensional Y,F,W as section 2, but K=I+sigma_y.
The ascending F eigenprojectors are P1=(I+sigma_y)/2, P2=(I-sigma_y)/2.
The source sends K to I+h sigma_y, h=31/sqrt(1001), so
(q1,q2)=(2,0) -> (1+h,1-h).
The channel-derived integrated flux is exactly
J^Phi_12=1-h≈0.0201837110764,
J^Phi_21=-J^Phi_12.
It has the required sign and magnitude for both node balances. The original numerical source agrees to <2e-16 in the continuity residual.

This is genuine redistribution of an explicitly defined internal kernel stock for a retained source-derived node choice; it is not the vanished Y-node flow in different words.
It is still not spatial energy transport. Formation eigenmodes have not been shown to be separated physical places, and K has no derived energy/momentum calibration here.

## 6. Fresh evidence, limits and next dependency

Final mode_graph_audit.py run:
- 12 complex preparations, n=3,4,5,6, two source events each: 24.
- Four extra gauge-source controls.
- Two opposite-current graph-fiber witnesses, two triangle events and one nonzero source-current witness: 33 full source calls overall.
- Exact two-node coefficients, current/stock balance, positivity and chain/triangle incidence kernels.
- Maximum source-current continuity residual <7.6e-15 and antisymmetry residual <1.1e-15; gauge-current residual <6.2e-16.
- All other recorded identity residuals <9e-14, below the predeclared 1e-10.
- Actual formation-node transfer reaches about 0.03084 in the complex controls. Guessed-current continuity defects are retained as EXPECTED negative results, not hidden as passing currents.

The initial audit passed. Explicit positive-principal-minor, source-current gauge, and independent graph-alpha/load checks were added to document the preregistered scope, followed by the fresh final run. Recomputing the graph alpha independently gives a largest norm-budget residual of about 8.04e-14; the initially rounded documentation bound <8e-14 is corrected to <9e-14 here. The predeclared 1e-10 acceptance criterion is unchanged. No source coefficients, inputs or acceptance bounds changed.
GitHub CI is recorded separately for the published code commit.

Advanced: a closed internal coherence graph, precise failure of guessed phase currents on its retained mode stocks, and a nonzero antisymmetric source-channel current with exact internal continuity on formation nodes.
The required next step is to test whether a reduced formation-node description retains the coherences needed by this flux, and whether source-derived adjacency from the channel can support a justified spatial/local interpretation. Full matrices currently carry that information.
A positive duration would turn the event-integrated identity into a chosen-time rate identity but would supply neither physical units nor locality. No spatial displacement, full four-current, stress tensor, action or Einstein dynamics is established here.
