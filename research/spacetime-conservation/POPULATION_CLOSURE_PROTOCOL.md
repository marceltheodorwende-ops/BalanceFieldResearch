# Formation-node population closure and memory — preregistered protocol

23 October 2026. BFG only, under MANDATE.de.md. Source: unchanged pinned Dynamic Order Parts I/II and the actual aligned channel Phi_k(K)=sum_a T_a K T_a.
Domain: autonomous full persistence in C, simple formation spectrum for the rank-one numerical node basis. Formation projectors are aligned constants. Physical spatial interpretation is not assumed.

## Questions and candidates
P1. In the formation eigenbasis define P_ij=sum_a |(T_a)_ij|². Derive positivity, symmetry and double stochasticity. For K diagonal in that basis, test q_+=P q and J^Phi_ij=P_ij(q_i-q_j).
P2. Do not assume a diagonal preparation stays diagonal. For D=formation dephasing and O=I-D, derive q_+=P q+diag Phi(O K) and the exact criterion for autonomous population closure FOR ALL K: D Phi O=0, equivalently (by channel self-adjointness) O Phi D=0.
P3. Fixed exact tilted basis: R=[[3/5,-4/5],[4/5,3/5]], F=R diag(1,2) R^T, Y=diag(1/5,3/10), W=I2/2. In formation coordinates K_±=I±sigma_x/2 have identical populations and identical coherence magnitudes but opposite signs. Derive and test differing next populations despite identical channel P; positivity must hold.
P4. In the same tilted basis start with K=diag(2,1). Use two source events to compare actual populations to P1 P0 q0. Derive the nonzero coherence-memory correction rather than resetting coherences between events. No dephasing is inserted into the source law.
P5. Natural alternative, unbiased basis: R=1/sqrt(2)[[1,-1],[1,1]], F=R diag(1,2) R^T, same Y,W. Determine whether the formation diagonal algebra is channel-invariant despite [F,Y]!=0. Test arbitrary offdiagonal inputs with equal populations:
K_A=diag(2,1)+sigma_x/5+3sigma_y/10,
K_B=diag(2,1)-sigma_x/5-3sigma_y/10.
Run two events for each and check a genuinely closed population chain if the criterion holds. This is a two-mode conditional sector, not a generic n-mode theorem.
P6. Derive the block equations d_+=M_k d+A_k o, o_+=B_k d+C_k o and exact eliminated-coherence memory formula. Label this mathematical reduction, not a new physical reservoir, fitted force or local spatial current.

## Fresh controls
Exact symbolic tilted-basis population/coherence coupling, positive inputs, source alpha/h and the unbiased closure identity.
12 complex preparations (three each n=3,4,5,6), seed 20261101, Y in [.2,.3], positive noncommuting F/W, generic Hermitian K; two full source events each (24). Use fixed initial formation eigenbasis. Check P stochasticity, q update with coherence, current decomposition and two-event memory identity; residuals <=1e-10. Record the Markov-only error instead of treating it as a passing model.
Four extra simultaneous-unitary source controls (case 0, first event each n).
Two tilted K_± source calls, two tilted initially diagonal events, and four unbiased A/B events: eight witness source calls, final total 36.
Expected nonzero witness defects must agree with the independently derived formulas, not a tolerance-adjusted input. Retain failures and source numerical cutoffs.
Publish this protocol before evaluation, then proof/audit/results and status; add the necessary research CI step and verify explicit code-commit CI separately. Do not claim physical clock, length, energy-momentum or Einstein completion.
