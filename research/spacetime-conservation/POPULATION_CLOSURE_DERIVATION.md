# Formation-node population closure, classical sector and exact coherence memory

23 October 2026. BFG-only. [Preregistered protocol](POPULATION_CLOSURE_PROTOCOL.md).
Source: unchanged pinned complete Dynamic Order, Parts I/II; aligned full-persistence channel and the source-current identity in MODE_GRAPH_DERIVATION.md.
All statements below are mathematical source consequences on declared readout domains, not a physical spacetime identification.

## 1. Positive channel weights are not yet an autonomous population model

Use rank-one formation eigenprojectors P_i on a simple-F full-persistence stratum. Formation is retained in alignment, so these nodes are retained and source-unitary covariant.
In their orthonormal eigenbasis let
q_i=K_ii, D(K)=diag(K_11,...,K_nn), O=I-D,
P_ij=sum_a |(T_a)_ij|².
Here P denotes a TRANSITION MATRIX, not the source carrier projector (which is I throughout this investigation).

P_ij>=0, P_ij=P_ji and every row and column sums to one: the T_a are Hermitian and sum_a T_a²=I.
For a diagonal K,
q_i,+=sum_j P_ij q_j,
J^Phi_ij=P_ij(q_i-q_j).
The second identity follows directly from [T_a,D(K)]_ji=(T_a)_ji(q_i-q_j). This is a source-derived diffusion-type integrated flux, not an imported Hamiltonian or assumed diffusion law.
For general Hermitian K,
q_+=P q+diag Phi(O K).
The coherent correction need not vanish. The source keeps those coherences; erasing them after each step would change the dynamics.

These weights are dimensionless; q and integrated flux have formation units. If K is positive, q is nonnegative, but arbitrary source K need not be positive or a probability state.
The formation/Y geometry determining P_k also evolves. A time-varying P_k schedule is not inferred from q alone.

## 2. Exact criterion and its scope

At a given event, population readout closes for ALL Hermitian K iff
D Phi O=0.
Proof: all states with the same diagonal differ by an offdiagonal Hermitian operator; the II89 fiber criterion is precisely that its successor diagonal vanish.
Since Phi is Hilbert-Schmidt self-adjoint and D,O are orthogonal projections, this is equivalent to
O Phi D=0,
or invariance of the formation-diagonal algebra under Phi.
For repeated closure the criterion must hold at every event, and the retained geometry/channel parameters must themselves be included in a closed readout or declared external input.

This criterion concerns POPULATIONS. For n>=3, coherence-dependent divergence-free edge circulations can still exist even when D Phi O=0. Closure of every individual source-current edge additionally requires its coherent functional to vanish or be retained. The prior cycle-space discussion therefore remains relevant.
For two nodes an antisymmetric edge current is fixed by the node change, so population closure also fixes that single edge flux.

## 3. Exact population-fiber counterexample with fixed channel geometry

Set
R=[[3/5,-4/5],[4/5,3/5]],
F=R diag(1,2) R^T=[[41/25,-12/25],[-12/25,34/25]],
Y=diag(1/5,3/10), W=I2/2, source carrier I.
The formation-basis kernels
K_F,±=I±sigma_x/2
are positive with the SAME q=(1,1), the SAME offdiagonal magnitude 1/2, and the SAME channel weights P. They differ only in a coherence sign relative to the fixed source geometry.

The source gives
alpha=1451/24976,
h²=32775625/34141016, 0<h<1.
In this formation basis,
[Phi_F(sigma_x)]_11=A(h), [Phi_F(sigma_x)]_22=-A(h),
A(h)=168(1-h)/625>0.
Consequently
q_+,±=(1±A/2,1∓A/2).
Their first successor populations differ by
A≈0.00542985985682.
The Markov-only expression P(1,1)=(1,1) misses both corrections.

This refutes population-only closure even when the full channel geometry AND coherence magnitudes are supplied. It does not refute the full matrix dynamics, a richer phase-sensitive projection or every special noncommuting-node sector.

## 4. Diagonal initialization does not remove subsequent memory

In the same tilted basis start with K_F,0=diag(2,1)>0.
The first population step is exactly P_0 q_0 because initial coherence is zero. But the source generates
(K_F,1)_12=A(h_0)/2.
The actual second populations therefore differ from the repeatedly dephased Markov model by
q_2-P_1 P_0 q_0
=(1,-1) A(h_1)A(h_0)/2,
approximately (5.21694623e-6,-5.21694623e-6).
Both h values are source-derived at their respective events; no coefficient is fitted to the observed defect.
Keeping only an initially diagonal preparation does not authorize silently replacing each later K by D(K).

## 5. A constructive noncommuting two-mode population sector

Do not turn the generic obstruction into a universal no-go.
Use the unbiased reference
R_u=1/sqrt(2)[[1,-1],[1,1]],
F=R_u diag(1,2) R_u^T,
the same diagonal Y with unequal eigenvalues and W=I2/2.
Here [F,Y]!=0, yet in formation coordinates
Phi_F(sigma_z)=h sigma_z,
while both offdiagonal Hermitian basis directions have zero successor diagonal.
The closure criterion holds.

The exact population transition is
P=(1/2)[[1+h,1-h],[1-h,1+h]],
with nonzero edge weight (1-h)/2 and source flux
J_12=[(1-h)/2](q_1-q_2).
It applies to EVERY K, including coherent K, in this declared two-mode geometry.

To make the reduced state autonomous, retain y1,y2 as well as q. The unbiased formation diagonals in the Y frame are equal, so
alpha=[sum_i y_i²/(1+y_i)]/[sum_i (1+y_i²)/(1+y_i)],
y_i,+=g_alpha(y_i),
q_+=P(y1,y2) q.
The Y eigenprojectors are retained on C and F is retained, hence the unbiased relation persists. This supplies a closed source-derived population-and-load factor on this special sector. It does NOT mean q alone determines physical time or the evolving P.

The positive test states
K_F,A=diag(2,1)+sigma_x/5+3sigma_y/10,
K_F,B=diag(2,1)-sigma_x/5-3sigma_y/10
have opposite coherences and identical populations. Two successive full source events give identical population trajectories, with Markov residual <1.2e-15.
This is a genuine conditional internal transport model, without claiming that the source physically selects this basis/domain or that every small perturbation retains it.

## 6. Exact reduction with memory rather than an invented reservoir

For a general time-dependent source channel Phi_k (its F/Y trajectory is independent of K), define operator blocks
M_k=D Phi_k D, A_k=D Phi_k O,
B_k=O Phi_k D, C_k=O Phi_k O.
Writing d_k=D K_k and o_k=O K_k gives
d_(k+1)=M_k d_k+A_k o_k,
o_(k+1)=B_k d_k+C_k o_k.

Eliminate o without changing the source:
d_(N+1)=M_N d_N
 +A_N C_(N-1)...C_0 o_0
 +sum_(j=0)^(N-1) A_N C_(N-1)...C_(j+1) B_j d_j.
Products are time ordered as written; an empty product is identity.
This follows by repeated substitution of the second block equation, and is valid for every finite event horizon on the retained-node full-persistence domain.
For N=1 it reproduces
d_2=M_1 d_1+A_1 B_0 d_0+A_1 C_0 o_0,
including the exact diagonal-initial-state correction above.

The memory is generated by existing offdiagonal source data, not an independently posited physical environment or compensating energy store. Retaining the full o_k gives an exact Markov state again; no minimal sufficient coherence compression is established here.

## 7. Fresh verification and retained reporting failure

Final population_closure_audit.py run:
- 12 complex preparations, n=3,4,5,6, two source events each: 24.
- Four additional gauge-source controls.
- Eight prescribed source events: two tilted fiber witnesses, two diagonal-initialization events, and four unbiased A/B events. Total: 36 complete calls.
- Exact rational source alpha/h², tilted coupling, positive witness states and unbiased diagonal-algebra identity.
- Maximum population-plus-coherence residual <8.3e-15, current-decomposition residual <2.5e-16 and two-event memory residual <5.5e-15.
- Generic Markov-only error reached about 0.01931; diagonal-algebra leakage reached about 0.01203. These are retained model defects, not passing population-only dynamics.

The first execution passed its mathematical/control assertions but failed JSON export because a SymPy Rational matrix was not serialized. Exact entries were converted to strings and the final audit rerun. The mathematical formulas, witness inputs and tolerance were unchanged; redundant independent-formula calls were also consolidated.
GitHub CI for the explicit published code commit is recorded separately.

## 8. What is now closed, and what is still missing

Closed: the source-current identity with full matrix data; a special two-mode population/load factor with a nonzero exact edge flux; and an exact general reduction retaining coherence memory.
Not closed by the tested coarse readout: generic formation-node populations plus magnitudes/channel weights. More coherences or their induced history are required.

Next substantive dependency: examine the channel-generated edge support and spatial locality without assuming that internal formation modes are physical places. Sparse/finite-range behavior, distance/clock calibration and a physically selected four-component current must be tested rather than inferred from a stochastic matrix. No Lorentz spacetime action or Einstein equation is derived here.
