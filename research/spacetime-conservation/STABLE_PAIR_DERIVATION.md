# Invariant spectral-pair selection: a current-state factor on a BFG class

Date: 23 October 2026. BFG-only continuation under MANDATE.de.md.
Prerecorded candidate and controls: STABLE_PAIR_PROTOCOL.md, committed before the first control run.
Source: complete Dynamic Order, Parts I and II, unchanged pinned full ambient update. The following restricts a source domain; it does not change its law or identify a physical sector.

## 1. Correct derivative and the admissible spectral class

Write g_alpha(y)=[alpha+(1-alpha)y^2]/(1+y)^2, r(y)=y^2/(1+y^2), f(y)=g_(r(y))(y).
The correct fixed-alpha derivative is
g_alpha'(y)=2[(1-alpha)y-alpha]/(1+y)^3.
Its turning point is alpha/(1-alpha), not alpha.

**Documentation correction.** DERIVATION.md section 8 previously printed the wrong general fixed-alpha-derived coefficient. At Y=yI, F=I, the correct traceless coefficient is
a(y)=2y(1-y)/[(1+y^2)(1+y)^3].
The scalar coefficient remains lambda(y)=f'(y). At y=1/2 these are a=16/135 and lambda=224/675, exactly the values the existing numerical audit used. Thus the printed general formula is corrected; the earlier checked point values and determinant defect remain valid. Additional full-source derivative controls at y=1/4,1/3,1/2 support the corrected formula.

[BFG DOMAIN RESTRICTION] Consider autonomous full persistence
P=I, F>0, W>=0, tr W=1, K Hermitian,
with spectral extrema m=min spec Y and M=max spec Y satisfying
0<m<=M<=1/2, m>=2M^2.
Call this class C. For selecting an unambiguous two-smallest pair, require n>=2 and simple spectrum. The strict interior m>2M^2, M<1/2 is nonempty for every finite n>=2: any distinct spectrum in [1/5,3/10] works. This is a sufficient mathematical restriction, not a claim that the source uniquely selects C or rank two.

In a Y eigenbasis let f_i=<e_i,F e_i>>0 and h(y)=(1+y^2)/(1+y). Then
alpha=[sum_i f_i h(y_i) r(y_i)]/[sum_i f_i h(y_i)].
Thus r(m)<=alpha<=r(M)<1/2, and
alpha/(1-alpha)<=M^2<m.
The derivative is therefore strictly positive on [m,M]. Source eigenvalue ORDER is retained in a step; off-diagonal F,K,W do not alter this weighted-mean bound.

## 2. Exact invariance certificate

Since partial g_alpha(y)/partial alpha=(1-y)/(1+y)>0 for y<1,
f(m)<=m_+=g_alpha(m)<=M_+=g_alpha(M)<=f(M).
The scalar f is strictly increasing on (0,1), as
f'(x)=4x(1-x^3)/[(1+x)^3(1+x^2)^2]>0.

The exact identity needed to propagate the class is
f(2x^2)-2f(x)^2 = 8x^5 P(x)/D(x),
D(x)=(1+x)^4(1+x^2)^2(1+2x^2)^2(1+4x^4)>0,
P(x)=4+4x+12x^2+6x^3+12x^4-8x^5+4x^6-15x^7.

For 0<x<=1/2, write
P(x)=L(x)+x^4(1/2-x)[8+15(x^2+x/2+1/4)],
L(x)=4+4x+12x^2+6x^3+(49/8)x^4+4x^6>0.
Every term of the remainder is nonnegative, so P>0 and f(2x^2)>2f(x)^2 on this entire interval. This is an algebraic positivity proof, not a sampling argument; stable_pair_audit.py checks the exact identities.

Consequently
m_+ >= f(m) >= f(2M^2) > 2 f(M)^2 >= 2 M_+^2,
and M_+<=f(M)<=f(1/2)=8/45<1/2.
Hence C is invariant and maps into its strict spectral-extrema interior. The complete source event is nonterminal and same-rank on this exact full-persistence domain: positive loads, positive analysis singular values, no selection loss and no seed complement. This does NOT claim a floating-point code can follow arbitrarily many events below its rank tolerance.

## 3. Spectral gaps and current-state recoverable pair

For any y in [m,M],
g_alpha'(y) >= c(m,M)
=2(m-M^2)/[(1+M^2)(1+M)^3] > 0.
Indeed the numerator (1-alpha)y-alpha is minimized by y=m, alpha=r(M), and the positive denominator is bounded above by (1+M)^3.

For ordered eigenvalues,
y_(i+1),+-y_i,+ >= c(m,M)[y_(i+1)-y_i].
Along N events the initial gap is bounded below by its positive initial value times the finite product of c(m_k,M_k). Every finite-step gap remains positive, so a simple spectrum stays simple.
There is no uniform positive gap for infinite event count: M_(k+1)<=f(M_k)<M_k implies M_k->0. This is an exact spectral collapse at an infinite limit, not a finite-time or SI-clock statement.

Define S2(Y) to be the spectral projector on the two smallest eigenvalues. On C with simple spectrum,
S2(g_alpha(Y))=S2(Y)
in the aligned representative, or S2,+ = V^dagger S2 V in the source successor SVD frame.
Thus the CURRENT full state recovers the same selected pair at every event. The historical label needed for the general pair theorem can be removed on this class. The projection is covariant under simultaneous source unitaries; its frame is still only defined modulo U(2).

The existing pair-plus-complementary-spectral-measure theorem now becomes a current-state factor on this declared class:
Zeta(Xi)=(K_S,F_S,W_S,Y_S,mu_E), S=S2(Y).
Its update is exactly the one in PAIR_DERIVATION.md section 4. No extra remembered projector is required, because the selector commutes with the actual update here. The environment measure remains necessary for the stated factor, and no minimality claim is made.

The rule "select the TWO lowest modes" is still a declared source-natural observable rule. Proving its invariance is not proving why nature selects two modes, why they are spatially local, or why their Hermitian determinant is a physical spacetime metric.

## 4. Complementary mass plus mean is still insufficient

Test a smaller environment readout on the invariant class itself.
Fix pair eigenvalues (1/5,9/40), F=I4, W=I4/4, P=I4, K=sigma_x direct-sum 0_2.
Compare full spectra
Y_A=diag(1/5,9/40,1/4,3/10),
Y_B=diag(1/5,9/40,13/50,29/100).
Both have simple spectra and lie in the strict class C. Their selected pair blocks coincide. Complementary formation mass mu_E(1)=2 and first moment integral y dmu_E=11/20 coincide.

Nevertheless
alpha_A=14821/260873,
alpha_B=146777/2588077.
The first selected successor Y component differs by
g_(alpha_A)(1/5)-g_(alpha_B)(1/5)
=45155264/675159411221>0
(approximately 6.68808925e-5).
This follows by exact substitution and is reproduced by the full ambient SVD update.

[REFUTED IN THIS SMALLER READOUT] Pair plus complementary zeroth and first moments is not closed, even when pair selection itself is dynamically stable. This is a distinct candidate from pair-plus-current-alpha in the preceding round. No result here rules out a richer finite moment representation, or the combination of additional summaries not tested.

## 5. Fresh verification

- Symbolic fixed-alpha derivative identity and the global positivity certificate above.
- 16 exact rational diagonal preparations at n=2,3,4,5 across three exact events each: 48 exact checks of the class, strict order and gap bound.
- 12 complex full-source preparations at n=3,4,5,6 across three events each: 36 events. The current reselected pair projector agrees with the initial transported pair to <3e-13; local factor kernel residual is <4e-15 and the source-class/gap-bound violations are zero in these tests.
- Independent full-source derivative differences at y=1/4,1/3,1/2: all errors <8e-10 at h=1e-5 (predeclared tolerance 1e-7).
- The exact moment witness agrees with the full source update to about 1.1e-17.
- The source Git blob is checked before import; no empirical evaluations or source changes occur.

The first finite check happened to satisfy a gap bound computed from an incorrect derivative expression. Independent symbolic differentiation exposed that mistake. The bound was corrected before the final run; the domain and witness inputs were unchanged. Passing finite samples is not the proof of the universal bound. Protocol amendment and corrected DERIVATION.md retain this distinction.

## 6. What has advanced and what remains

Advanced: a nonempty source-invariant class now supports a stable, current-state two-mode selector and the exact spectral-environment factor without an additional pair-history label. A simple two-moment environment compression still fails.
Open: why this restricted class and rank-two observable are physically selected; how the pair defines spatially separated events and transport; physical clock calibration; local full four-current, action and Einstein limit.
The source SVD/R4 coordinate transport is internal gauge transport, not by itself spatial motion.

Next useful dependency: derive the complete componentwise kernel/formation exchange for this concrete current-state factor, including whether a source-selected complementary charge can supply the damped pair components. Do not choose a compensator backward from the desired residual. General selection/seed transitions remain a separate extension; the invariant full-persistence theorem must not be promoted across them.

