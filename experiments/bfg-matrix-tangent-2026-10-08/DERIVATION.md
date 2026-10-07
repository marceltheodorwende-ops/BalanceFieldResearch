# Full-persistence matrix dynamics and a local oscillatory-factor test
Active source: Dynamic Order, SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Direct sources: sections84.1–84.4 canonical event,62–64 regular differential chain,88.2 explicitly scalar input example,89(161)–(162) factor/clock criterion,90.1 compatible full-persistence lift. This package does not change the autonomous canonical event or claim Theorem7 is already a matrix-input theorem.

## A. Exact natural-frame quotient representative
Assume finite dimension n>=2, full persistence P=I, F positive definite, W a density, K Hermitian, and0<Y<I. Then Q=I and selection/metric projectors are I. Let C=(I+Y)^-1, B=I-C, G=I+Y, lc=tr(G C F C), lb=tr(G B F B), alpha=lb/(lc+lb), beta=1-alpha. Both loads are positive. The canonical analysis is A=[sqrt(alpha) C; sqrt(beta) B], with R=A†A=alpha C²+beta B² positive definite.
The reduced SVD A=U Sigma V† admits the polar frame E=A R^-1/2=UV†. Conjugating the successor by V returns a representative in the original carrier frame:

    Y+=R,
    K+=R^-1/2 (alpha C K C+beta B K B) R^-1/2,
    F+=F, W+=W, P+=I.

Indeed E†(K directsum K)E gives the kernel formula; section84.4 transport V† yields the stated F,W inheritance after conjugation. This is not an extra physical update. It is a gauge-covariant representative of the canonical successor. Even at repeated R eigenvalues, the polar formula is smooth on the positive definite domain; no differentiable choice of individual SVD eigenvectors is asserted.

## B. Internal changing directions, without a manufactured phase
In a continuously tracked eigenframe of Y, write ci=1/(1+yi), bi=yi/(1+yi), ri=alpha ci²+beta bi². Then

    K+_ij = gamma_ij K_ij,
    gamma_ij=(alpha ci cj+beta bi bj)/sqrt(ri rj).

The numerator is the inner product of normalized real positive two-vectors (sqrt(alpha)ci,sqrt(beta)bi)/sqrt(ri). Therefore0<gamma_ij<=1, gamma_ii=1 and gamma_ij=1 iff yi=yj. Thus the Hilbert–Schmidt norm of K cannot increase in this sector; offdiagonal kernel phases are preserved in that eigenframe, while magnitudes can change. This is internal evolving matrix information, not simply a copied scalar. It does not supply a rotating pendulum phase: positive attenuation is not an oscillation. Eigenvalue crossings require consistent frame bookkeeping, and fixed external matrix entries are not automatically quotient observables. F,W and K relative to Y can supply gauge-invariant preparations/observables, but a physical instrument still needs identification.

## C. Explicit isotropic-input extension and its full matrix tangent
To test whether the simplest driven matrix version removes the scalar limitation, DECLARE the additional map which replaces Y by Y+dI before the canonical event, with constant d and all other inputs unchanged. This matrix input is a new coupling hypothesis. Work only near an isotropic fixed point Y*=y*I, x=y*+d in(0,1), y*=f(x), f(x)=2x²/[(1+x)²(1+x²)]. Such a point exists for scalar d in(0,3/4); no global contraction of this matrix extension follows.
At this point alpha=x²/(1+x²). A perturbation H of Y gives

    delta alpha = [2x/(1+x²)²] mu_F(H),
    mu_F(H)=tr(FH)/tr(F),
    delta Y+ = s H+t mu_F(H) I,
    s=2x(1-x)/[(1+x²)(1+x)³],
    t=[(1-x)/(1+x)] [2x/(1+x²)²].

Derivation: lc=tr(F)/(1+x), lb=x² tr(F)/(1+x). Differentiate lc and lb in H and use the quotient rule; F perturbations cancel in delta alpha because lb/lc=x² at isotropy. For R=alpha C²+beta B², delta C=-H/(1+x)² and delta B=-delta C. Its fixed-alpha derivative gives sH; its alpha derivative is(C²-B²)delta alpha=[(1-x)/(1+x)]delta alpha I. This yields the claimed expression.
Since mu_F(I)=1, the weighted-trace direction has eigenvalue s+t=f'(x), and every mu_F-traceless direction has eigenvalue s. Both are positive for0<x<1; s<f'(x)<=16/27. This establishes multiple internal contracting directions rather than the scalar's single direction, but their tangent modes here are real, not an oscillatory pair.
The natural-frame K differential is delta K+=delta K: the Y-dependent first-order terms cancel between numerator and R^-1/2 on both sides at isotropy. Equivalently gamma_ij differs from1 only at second order in eigenvalue separations. F and W have identity differentials; no Y coupling enters their update. Thus the local fixed-point derivative has only the real eigenvalues1,s,f'(x). This statement is on the fixed full-persistence stratum; P perturbations changing its rank, terminal transitions and seeds are outside it. Gauge removal cannot create nonreal eigenvalues from these invariant tangent spaces.

## D. Physical factor test
Suppose a C1 gauge-invariant physical projection to the fixed attracting pendulum has a time-h semiconjugacy at this fixed point, with a>0,b>0,h>0. For underdamped a>b²/4 and sin(h sqrt(a-b²/4))!=0, the derivative M=exp(h[[0,1],[-a,-b]]) has two nonreal eigenvalues. Differentiation of the factor identity gives DPi DU=M DPi. Every source eigenvector has real eigenvalue in{1,s,f'(x)}, whereas M has none real; therefore DPi vanishes on all source eigenspaces, hence DPi=0. The source derivative is diagonalizable in the decomposition above. No regular rank2 oscillatory factor exists in THIS isotropic constant-input matrix construction.
This is a restricted local theorem, not a universal obstruction for all matrix BFG. Resonant event durations, overdamped targets, anisotropic fixed/periodic states, non-full persistence, nonconstant/environmental inputs, singular projections or separately evolving instruments require different analysis. A state-dependent positive physical clock does not itself manufacture a generator. Existing readouts with a supplied mechanical flow remain additional constructions, not counterexamples to these premises.

## E. Control evidence and next constructive route
Thirty independent complex matrix preparations agree with the full Ambient implementation to1.61e-15. Kernel phase/HS statements checked on the same code controls. Central differences at three steps verify the analytic matrix derivative and zero kernel-Y derivative. Synthetic checks only; no real data, no new forecast or holdout. Derived equation tolerances are fixed in code; controls do not replace the proof.
The simple isotropic matrix extension supplies two or more independent contracting directions, but does not resolve force selection or a regular oscillatory factor. Next examine anisotropic noncommuting configurations with gauge-invariant instruments and the full regular differential chain; test actual nonlinear closure rather than insert desired force terms. The passive pendulum data remain available only for a justified development bridge, not to tune a universal claim.
