# Two-mode carrier: selector limits and a source-derived environment factor

Date: 23 October 2026. Continuation of the first BFG-only round.
Authority: MANDATE.de.md; preregistration: PAIR_PROTOCOL.md, committed before this calculation.
Active mathematical source: complete Dynamic Order, Parts I and II, pinned in SOURCE_MANIFEST.json. Implementation baseline remains the unchanged full ambient update.
No external physical mechanism is introduced. Standard spectral and trace algebra is used explicitly as mathematics.

## 1. Domain, readout choice and covariance

[SOURCE BFG / PREVIOUSLY DERIVED] Work on autonomous full persistence P=I, 0<Y<I, F>0, W>=0 with tr W=1. The aligned event is
Y_+=g_alpha(Y), F_+=F, W_+=W,
K_+=Phi_(Y,alpha)(K),
where g_alpha(y)=[alpha+(1-alpha)y^2]/(1+y)^2 and
alpha=Lambda_B/(Lambda_C+Lambda_B),
Lambda_C=tr[F(I+Y)^(-1)], Lambda_B=tr[F Y^2(I+Y)^(-1)].

[DECLARED OBSERVABLE SELECTION RULE] At an INITIAL state with simple Y spectrum, select the two lowest eigenvalues and their spectral projector S. This is a source-natural readout rule, not a source theorem choosing this rule uniquely or identifying it with physical spacetime.
If G is a simultaneous unitary source change, the selected projector changes to GSG^dagger. A frame Z for Ran S is only defined up to U(2); all compressed matrices must transform together. This gives a covariant two-mode block and its simultaneous-unitary quotient, not four gauge-invariant physical coordinates.

[EXACT SELECTOR LIMIT] Reapplying the same two-smallest rule at every event need not retain the initial pair.
Let Y=diag(1/10,1/2,9/10), F=diag(1,1,10), W=I/3, P=I. The exact source alpha is 3479/8839 and the successor eigenvalues, in the ORIGINAL labels, are
353260/1069519, 19276/79551, 782060/3190879.
They satisfy y_2,+ < y_3,+ < y_1,+. The initially selected labels {1,2} become {2,3} under instantaneous reselection.
This is not a degeneracy ambiguity: both endpoints have distinct eigenvalues. It does not prove that no other source-natural rule or gap-preserving restricted class exists.

Hence retain the initial pair as transported HISTORY data for the following theorem. Because Y_+ is a function of Y, S commutes with every later Y on this sector. In source SVD coordinates S is transported by the same frame map; in the aligned representative it is fixed. A spectral collision does not erase the retained history label, but it may prevent reconstructing that label uniquely from current Y alone.

## 2. The compressed pair is not autonomous

Define the local block
B_S=(K_S,F_S,W_S,Y_S), X_S=Z^dagger X Z.
W_S is subnormalized, with mass tr W_S, not automatically a canonical trace-one witness. Its normalized version needs that mass recorded separately. Neither W_S nor that mass enters the source alpha on this sector.

Take n=3,
Y=diag(1/4,1/2,3/4),
F^(w)=diag(1,1,w), w=1 or 2,
W=I/3, K=sigma_x direct-sum 0, P=I.
The same initial two-smallest S is selected in both states, and ALL local blocks above coincide (as does the local witness mass). Source global alphas are
alpha_1=113/541, alpha_2=361/1457.
The first successor pair Y differs in its first diagonal component by exactly
18396/788237 > 0 (approximately 0.02333815845).
Proof: g_alpha(1/4)=(1+15 alpha)/25; substitute the exact loads.

[REFUTED IN THIS READOUT] The pair block fails the section-II89 fiber criterion. It is not a standalone copy of the canonical two-dimensional BFG: using F_S alone to compute its load weight changes the actual dynamics. The complement affects it even if all off-block matrices vanish in this exact witness.
This does not refute the complete global tuple, a driven local pair with source input, or a richer closed factor. Adding other global summaries was not exhaustively classified.

## 3. The current alpha alone is not an autonomous environment state

A useful one-step control input is the actual global alpha. However it is not sufficient as a retained state for repeated autonomous evolution.

Set
Y=diag(1/4,1/2,2/3,3/4), F0=I4, W=I4/4,
K=sigma_x direct-sum 0_2, P=I4.
Write b(y)=y^2/(1+y), h(y)=(1+y^2)/(1+y).
The initial alpha0 is 169/723. Define d_i=b(y_i)-alpha0 h(y_i) and
F1=diag(1,1,1+d_4,1-d_3)
  =diag(1,1,1609/1446,2030/2169)>0.
The perturbation preserves total B-alpha0 H because d_3*d_4-d_4*d_3=0. Thus the complete pair blocks and CURRENT alpha coincide, and the first successor Y is identical in the entire four-dimensional system.

Since F is inherited, the two next alphas are nevertheless different:
alpha_next,0=172459907159094472849/4543864531997075245654,
alpha_next,1=180171141780700562297803/4750325571038905337543278.
Their exact difference is the nonzero rational in pair_results.json, approximately -2.6289110249e-5.
The first local Y component after TWO events consequently differs by approximately -1.8259304672e-5; its exact rational certificate is also stored there.

[REFUTED IN THIS AUGMENTATION] Pair plus current alpha is not an autonomous iterative factor. This is not a theorem excluding every finite collection of environmental moments, nor a claim that the complementary formation stock is the same in these two states. The pair-plus-alpha candidate is exactly the one tested.

## 4. A sufficient closed extension from existing BFG data

[BFG DERIVED, GIVEN THE INITIAL PAIR HISTORY]
Let E_Y be the spectral measure of Y on the complementary subspace S^perp and define the finite positive formation-weighted measure
mu_E(A)=tr[F (I-S) E_Y(A)].
For simple initial spectrum this is
mu_E=sum_(j outside S) f_j delta_(y_j), f_j=<e_j,F e_j>>0.
Repeated complementary eigenvalues may be merged by adding their weights.

Define the environment-assisted state
Zeta=(K_S,F_S,W_S,Y_S,mu_E)
modulo simultaneous pair U(2) frame change. This is a mathematical observable/history factor of the existing source, not a new physical law.
All Y and alpha values are dimensionless; F and the measure weights have formation units, not established joules.

Compute
L_C=tr[F_S(I2+Y_S)^(-1)] + integral (1+y)^(-1) dmu_E(y),
L_B=tr[F_S Y_S^2(I2+Y_S)^(-1)] + integral y^2(1+y)^(-1) dmu_E(y),
alpha=L_B/(L_C+L_B).
Define C_S=(I2+Y_S)^(-1), B_S=Y_S C_S,
M_S=alpha C_S^2+(1-alpha)B_S^2,
T_C,S=sqrt(alpha) C_S M_S^(-1/2),
T_B,S=sqrt(1-alpha) B_S M_S^(-1/2).

Then the closed factor update is
Y_S,+=M_S,
K_S,+=T_C,S K_S T_C,S+T_B,S K_S T_B,S,
F_S,+=F_S, W_S,+=W_S,
mu_E,+=(g_alpha)_*mu_E.

Proof:
1. S commutes with Y, so every function of Y, including both channel factors, is block diagonal for S direct-sum S^perp.
2. Global traces of F times functions of Y depend only on its pair block and complementary diagonal spectral weights. Off-block F does not contribute to those traces.
3. Pair compression of Phi(K) contains no off-block K term: Z^dagger T K T Z=T_S K_S T_S.
4. F and W are inherited in the aligned representative; their pair blocks and complementary formation weights are fixed.
5. Every complementary eigenvalue is pushed through the SAME source g_alpha. This gives the stated measure pushforward and closes the next alpha calculation.

Thus the update of Zeta is determined by Zeta; the section-II89 fiber implication holds on this declared full-persistence history domain. The proof does NOT require K,F,W to be jointly block diagonal. Off-block information can be discarded for this factor on this sector. This is a sufficient environment description, not a proven globally minimal one.

If the complementary dimension is fixed finite, the measure can be stored as finitely many atoms with fixed formation weights. Its size may grow with the ORIGINAL complement dimension; no universal fixed-size local compression has been proved. Across general carrier/selection/seed or terminal events this full-persistence factor is not established and must not be silently reused.

## 5. Conservation and Lorentz carrier in this extension

The pair kernel channel has sum_j T_j,S^2=I2, hence tr K_S is exactly conserved even when global alpha is supplied by mu_E. It is still a formation-unit kernel invariant, not a physical energy determination.
For Herm(C^2), det X=x0^2-|x|^2 provides the standard algebraic Lorentz carrier and the positive future cone. The actual pair event damps noncommuting Pauli components as before; adding the source spectral environment explains its weight but does not repair null-cone preservation or supply four conserved physical currents.

No physical time calibration, spatial separation/transport, translation generator, metric action or Einstein equation was introduced. This factor is coupled through GLOBAL source loads; calling mu_E a spatial bath or its trace an energy would add an unproved physical identification.

## 6. Fresh verification and retained correction

pair_audit.py checks exact rational selection and both fiber witnesses, then compares the factor to the pinned complete source update for 12 complex preparations at n=3,4,5,6 and three events each. Off-block K,F,W are explicitly nonzero. Four simultaneous-unitary projection controls pass. Maximum factor residual is below 3e-15 for the tested cases; tolerance was fixed at 1e-10.
The exact next-alpha gap and two-step pair gap are checked independently against full source SVD events. The unchanged kernel Git blob is checked before import.

The initial audit asserted an unnecessarily stronger complete reversal of the P1 eigenvalue order. Exact evaluation rejected it. Inputs and the pair-invariance question were kept fixed; the actual strict order is 2,3,1 (one-based), which still proves the predeclared pair-switch obstruction. This correction is retained here; no source coefficient or witness was retuned.

## 7. Updated next dependency

There is now a concrete source-derived ENVIRONMENT-ASSISTED two-mode factor rather than only an abstract request for a local projection.
The next constructive question is whether BFG selects a physical class where that initial pair/history and complementary spectral state have an independently justified event/transport interpretation, and whether source conservation can be organized into a local four-current there.
Immediate alternatives to investigate:
- a source-justified, gap-controlled pair selection retained under the actual dynamics;
- a richer current based on the factor plus its complementary measure, with all exchange components explicitly derived;
- selection/seed transition laws for that factor rather than importing the full-persistence theorem across rank events.
None of these has been proved by the present result. The pure pair and pair-plus-alpha failures identify exactly why discarding the environment is insufficient, while the closed measure extension supplies a concrete mathematical object for the next run.

