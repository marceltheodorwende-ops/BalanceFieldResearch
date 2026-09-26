# BFG finite balance laws and conditional invariants

Date: 26 September 2026. Status: AI-assisted mathematical derivation for review, not independent peer review or empirical validation. BFG source author: Marcel Theodor Wende. This note is a new research stage, not an amendment of historical manuscripts.

Source: *Balance–Field Framework (BFG): Canonical Minimal Finite Closure and Universal Reclosure*, 26 September 2026, equations (9)–(40), archived at repository commit `c1c481ab4e63f7cf7bd54d1c8593030f3e1923b7`, `research/canonical-minimal-finite-closure-2026-09-26/`. Equation numbers below belong to this note. All results concern finite-dimensional complex Hilbert spaces with their declared inner products and nonterminal events. No external physical law is assumed.

## 1. Neutral partition is not a quadratic conservation law

Write C=(I+Y)^(-1), B=Y(I+Y)^(-1), Y>0. Functional calculus gives

    C+B=I,  CB=BC>0,  C²+B²+2CB=I.                         (1)

For every vector x,

    ||Cx||²+||Bx||²+2<x,CBx>=||x||².                       (2)

Proof: square C+B=I; C and B are commuting Hermitian operators. The last term is real and strictly positive for x≠0. Therefore additive complementarity of amplitudes is not conservation of the sum of their squared norms. Replacing the cross term by an unobserved physical reservoir would require a new model.

For any positive density F, cyclicity of trace likewise gives

    tr(CFC)+tr(BFB)+2tr(CBF)=tr(F).                        (3)

For the source's metric projector J=P^(G), define A_C=JC, A_B=JB and strictly positive loads L_C=tr(G A_C F A_C†), L_B=tr(G A_B F A_B†). The paper's reciprocal weights uniquely obey

    α=L_B/(L_C+L_B), β=L_C/(L_C+L_B),
    αL_C=βL_B, αL_C+βL_B=2L_CL_B/(L_C+L_B).               (4)

This is an instantaneous channel-balance identity, not a statement that either load is constant across recursion. The G-weighted loads must not be confused with the Euclidean Gram A†A used for Y_+ in the paper.

## 2. Exact inherited-formation balance for one transport

Let T:H→H_+ be the R4 partial isometry in equations (27)–(33), S=T†T its initial projection, and F the formation density at the input of this stage. Let e=0 when the emergent complement is empty; otherwise e=−λ_min(K_E)>0 when the source's simple-negative-ground gate passes. The seed projector Π has rank one and is orthogonal to Ran(T). Define F_+=TFT†+eΠ (omit Π when e=0). Then

    f_+−f=−l_F+e,
    f=tr(F), l_F=tr((I−S)F)≥0.                            (5)

Proof: tr(TFT†)=tr(SF); tr(eΠ)=e. Positivity gives l_F≥0. Moreover l_F=0 iff the support of F lies in Ran(S), since l_F=||(I−S)F^(1/2)||_HS².

Consequently f is conserved at this event iff e=l_F. Inherited formation alone cannot increase, but the seed can offset or exceed the loss. The paper's seed rule does not itself assert e=l_F. Equation (5) is a formation-mass balance, not yet an energy law: tr(F) has no established physical energy calibration here.

## 3. Selection and R4 together: an explicit conditional composition

The prose in section 5 says Selection transports formation without normalization and renormalizes the retained identity witness. Section 8 does not label every density as pre- or post-Selection. We therefore state the sequential interpretation explicitly rather than silently identifying these inputs.

Let T0 be Selection, T1 the subsequent R4 transport, and let each act on its own declared source/target carrier. Assume the section-8 densities are the outputs of Selection. Put

    M=T1 T0, D=M†M, 0≤D≤I.                               (6)

Although each Ti is a partial isometry, their product need not be; D need not be a projector. With original density F0, the complete inherited-plus-seed update is

    F_next=M F0 M†+eΠ,
    tr(F_next)−tr(F0)=−tr((I−D)F0)+e.                     (7)

The loss separates exactly into two nonnegative contributions:

    tr((I−D)F0)
      =tr((I−T0†T0)F0)
       +tr((I−T1†T1) T0 F0 T0†).                         (8)

Proof: insert I−T0†T1†T1T0=(I−T0†T0)+T0†(I−T1†T1)T0. If the executable source uses a different placement of Selection, (5) remains valid for each displayed R4 stage, while (7) must be matched to that implementation before being called its full update law. This note does not certify that correspondence.

## 4. Identity normalization versus retained identity mass

For W≥0 with tr(W)=1 and one partial isometry T, let p=tr(SW)>0. The paper defines

    W_+=TWT†/p, tr(W_+)=1.                                (9)

The value one is imposed by normalization. The unnormalized trace is p≤1. For the sequential convention in section 3, the two normalization factors multiply to p=tr(M W0 M†), and the normalized final witness is M W0 M†/p. This follows by cancellation of the first normalization factor in the second stage.

Along a nonterminal sequence define q_0=1 and q_(n+1)=q_n p_n. Then

    q_N + Σ_(n=0)^(N−1) q_n(1−p_n)=1.                    (10)

Proof: q_n−q_(n+1)=q_n(1−p_n), followed by telescoping. The ledger is nonnegative and records retained versus lost witness mass. It is bookkeeping derived from the trajectory; it is not an additional autonomous state variable or a physical conserved charge. At p=0 the normalized update is undefined and the terminal gate applies.

For a single R4 step with p=1, T is isometric on supp(W), so W and W_+ have the same nonzero eigenvalues. Thus purity and spectral entropy are preserved at that lossless stage. With loss they are not generally preserved: W=diag(1/2,1/2), T=(1,0) gives p=1/2 and W_+=(1), increasing purity from 1/2 to 1. This is a counterexample for the transport-normalization operation, not a claim of a fully constructed BFG orbit.

## 5. The observable test for a proposed conservation law

For a fixed event and Hermitian observables O on the input and O_+ on the output,

    tr(O_+ F_next)−tr(O F0)
      =tr((M†O_+M−O)F0)+e tr(O_+Π).                      (11)

This is cyclicity of trace applied to (7). A sufficient event-wise criterion for conservation is M†O_+M=O and e tr(O_+Π)=0. We do not assert necessity for the nonlinear full dynamics, because M, Π and e depend on the state and two terms may cancel. Taking O=O_+=I recovers (7).

For a normalized witness, instead,

    tr(O_+W_next)−tr(OW0)
      =tr((M†O_+M−pO)W0)/p.                              (12)

Any claimed energy, momentum or charge must supply its observable, physical interpretation, units and a proof of (11) or (12) along the actual update. A name alone does not supply that proof.

## 6. Conserved blocks and dissipated mismatch on the declared stratum

Assume exactly the neutral-compatible persistent stratum for which the paper's equations (38)–(40) hold, with α,β>0 and positive neutral eigenvalues yi. All comparisons use the same active frame. Write

    K'_ij=χij K_ij,
    χij=(α+β yi yj)/sqrt((α+β yi²)(α+β yj²)).             (13)

The vectors vi=(sqrt(α),sqrt(β)yi)/sqrt(α+β yi²) have unit norm and χij=<vi,vj>. Hence 0<χij≤1 and χij=1 iff yi=yj. It follows that

    Eλ K' Eλ=Eλ K Eλ, tr(K')=tr(K),
    tr(O K')=tr(O K) whenever [O,Y]=0.                    (14)

Here Eλ are the spectral projections of Y. Proof: within each eigenspace χij=1; commuting observables are block diagonal in these eigenspaces. These are exact algebraic invariants for this stratum, not identified physical charges.

Direct expansion gives the nonnegative defect

    ||K||_HS²−||K'||_HS²
      =αβ Σij (yi−yj)² |Kij|²/
          ((α+β yi²)(α+β yj²)) ≥0.                       (15)

It vanishes iff [Y,K]=0. If dmin=min_i(α+β yi²) and dmax=max_i(α+β yi²), then

    αβ ||[Y,K]||_HS²/dmax² ≤ defect
       ≤ αβ ||[Y,K]||_HS²/dmin².                         (16)

Thus the commutator quantitatively controls one-step quadratic mismatch loss. This does not prove monotonicity of a global physical energy or entropy across Selection, changes of carrier, and seeding.

For frozen Y,α,β only, repeated (13) gives K^(n)_ij=χij^n K^(0)_ij and converges to Σλ Eλ K^(0) Eλ. If there are cross-eigenspace entries, r=max_(yi≠yj)χij<1 bounds their Hilbert–Schmidt norm by r^n times its initial value. This frozen-map limit is not the full BFG orbit, which reconstructs Y and its weights.

## 7. A source-derived counterexample to neutral-load conservation

In a retained one-dimensional source take P=1, Y=y with 0<y<1, formation F=f>0, and G=1+y. The paper's equations (17)–(24) give

    L_C=f/(1+y), L_B=f y²/(1+y),
    α=y²/(1+y²), β=1/(1+y²),
    y_+=2y²/((1+y²)(1+y)²).                              (17)

At y=1/2, α=1/5, β=4/5 and y_+=8/45, not 1/2. In fact y_+<y because (1+y²)(1+y)²−2y=1+2y²+2y³+y⁴>0. Thus even the retained scalar Gram reconstruction does not conserve tr(Y). This calculation is exact and independent of f. It does not specify an otherwise omitted R4 implementation or prove a complete nonterminal orbit.

## 8. Scope of the result and next proof obligation

The finite formulas establish partition identities, formation loss/source balances, normalized-witness accounting, and stratum-specific invariants and dissipation. They do not yet derive physical energy conservation, a local spatial continuity equation, Maxwell equations, Einstein equations, or quantum measurement laws.

A cumulative export variable can always turn (7) into a telescoping identity. That mathematical construction alone does not derive an environment with physical dynamics. Carrier-dimension nonincrease likewise does not imply finite-time termination or convergence of a full orbit.

Before a continuum limit: identify all Selection/R4 inputs and carriers in the frozen implementation; choose a physically justified observable; specify a time parameter and a family of updates tending to identity; prove a generator limit on a fixed-rank stratum with spectral gaps; then examine what happens at gap closures and terminal events. A discrete map at one step size does not by itself fix a unique continuous interpolation. Deriving spatial locality is a further obligation.

No code, source paper or previous result was modified. No numerical or empirical experiment was run for this note. The proofs and the rational scalar example above are the evidence, with full-event conclusions explicitly conditional on the stage-composition convention.
