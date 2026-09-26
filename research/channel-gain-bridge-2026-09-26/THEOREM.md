# Exact channel-load contrast and the remaining closure-gain bridge

Date: 26 September 2026. AI-assisted mathematical review of internal BFG formulas.
This note derives an observable already determined by the BFG channel loads. It does not identify that observable with general admissible closure gain without an additional argument.

## 1. Fixed inputs and source
Use the finite [master-state load definitions](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/MASTER_STATE.md):
Y>=0, G=I+Y, C=G^(-1), B=YC=I−C, and the G-orthogonal persistent projector P, so P²=P and P*G=GP. The formation density rho>=0 may have rank greater than one.

    ell_C = tr(GPC rho C P*),
    ell_B = tr(GPB rho B P*).

Define the already computable **channel-load difference**

    D_P(rho)=ell_C−ell_B.                                   (1)

This name is deliberately narrower than closure gain Delta C_A in the older selection grammar. Mathematical symbols C and Delta C_A have different roles.

## 2. General identity
Let M=P*GP=GP, a positive Hermitian operator. Cyclicity of trace gives

    D_P(rho)=tr(H_P rho),
    H_P=C M C−B M B
       =C M+M C−M.                                         (2)

The last equality follows by substituting B=I−C and expanding. No commutation between P and Y is assumed.

Without projection, P=I, all neutral operators commute and

    H_I=G(C²−B²)=G(C−B)(C+B)=GZ=I−Y.                       (3)

Thus

    D_I(rho)=tr((I−Y)rho).                                  (4)

Using ordinary unweighted channel norms instead would give Z; the actual master loads use G. Their magnitudes must not be conflated.

## 3. Persistent-support theorem
Assume additionally

    Ran(rho) subset Ran(P).                                 (5)

Then, even when [P,Y] is nonzero,

    D_P(rho)=tr((I−Y)rho).                                  (6)

Proof for a vector v∈Ran(P): Pv=v and PCv+PBv=v. In the G inner product,

    ||PCv||_G²−||PBv||_G²
      =2 Re <v,PCv>_G−||v||_G²
      =2 Re <v,Cv>_G−||v||_G²
      =<v,(2I−G)v>
      =<v,(I−Y)v>.

The second equality uses G-orthogonality of P, not P*=P. Decompose rho as a positive sum of rank-one projectors on Ran(rho) and sum the vector identity. This proves (6).

This theorem does not assert that every state in every historical BFG update satisfies (5). Formation and identity-witness densities are different; the witness support condition cannot silently be transferred to rho_F. Check the actual selection/event stage before applying (6).

## 4. Modewise consequence and limits
If v is a Y-eigenvector with eigenvalue y and Pv=v, then

    D_P(vv*)=(1−y)||v||²,
    sign D_P(vv*)=sign[(1−y)/(1+y)]=sign z.                  (7)

Hence neutral contrast really is the sign of a source-defined channel-load difference on these modes. This is a proved internal algebraic connection, not a freely invented gain function.

If [P,Y]=0, then P also commutes with G and is an ordinary orthogonal projector; (2) reduces to

    H_P=P(I−Y).

The positive spectral subspace of H_P is therefore Ran(P) intersect Ran(1_[0,1)(Y)). Without this compatible decomposition, a global identification of these spectral selectors is not supplied by (6).

Moreover, positive total gain is not the same as every occupied mode having positive gain. For P=I, Y=diag(1/2,2), rho=diag(3,1), equation (4) gives 1/2>0 although rho occupies a y=2 mode. A total-load condition alone therefore does not derive modewise export of all y>=1 modes.

## 5. Exact counterexample without the support restriction
Take

    Y=diag(1/4,1/2), G=diag(5/4,3/2), w=(1,1)^T,
    P=w(w*Gw)^(-1)w*G=[[5/11,6/11],[5/11,6/11]],
    d=(1,−9/10)^T, rho=dd*.

P is exactly the G-orthogonal projector onto span(w). The persistent range can be realized by the ordinary power-bounded recursive operator

    R=P0+(1/2)(I−P0), P0=ww*/2.

Yet Ran(rho) is not contained in that range. Equation (2) gives

    H_P=[[15/44,7/22],[7/22,3/11]],
    det H_P=−1/121,
    ell_C=1/275, ell_B=4/275,
    D_P(rho)=−3/275<0.                                     (8)

Both loads are strictly positive. Meanwhile

    Z=diag(3/5,1/3)>0.

Thus positive neutral contrast on every ambient mode does not imply a positive projected channel-load difference for arbitrary formation density.

This is a counterexample to the unrestricted load identity/sign implication under the stated projector/load assumptions. It is not certified as a full nonterminal orbit of the Selection-first implementation. That implementation can change the density before the split; the relevant support condition must then be checked anew. It does not refute the declared selector itself.

## 6. What has advanced, and what remains open
Established here:
- a general Hermitian observable H_P for the difference of existing BFG loads;
- exact reduction to I−Y without projection or with persistent-supported formation density;
- a modewise contrast-sign identity on compatible persistent modes;
- an exact counterexample to extending that identity to arbitrary projected states;
- a distinction between aggregate positive load and modewise retention.

Still OPEN:
- whether the older admissible-closure increment Delta C_A is this channel-load difference;
- whether the relevant formation density always satisfies the required support condition at the point where a proposed selection proof uses it;
- a general spectral selection characterization in the noncommuting/rank-changing setting;
- any inference from these algebraic identities to a universal natural law.

The missing bridge is now more concrete: prove independently that closure improvement is measured by the channel-load difference in the relevant state sector, and justify modewise rather than merely aggregate selection. Redefining closure gain to equal (1) is a possible explicit completion, but not a derivation from an independent notion of closure.

This result sharpens, and does not reverse, the [source audit](../selection-source-check-2026-09-26/SOURCE_CHECK.md) and [three-rule audit](../proof-chain-audit-2026-09-26/PROOF_CHAINS.md).

## 7. Verification and audit boundary
The proof is exact algebra. A separate Python standard-library Fraction calculation checked the rational loads, matrix determinant and the supported vector w: D_P(ww*)=5/4=w*(I−Y)w. No floating tolerances were used. An initial attempt to use SymPy found it unavailable; no dependency was installed, and the successful arithmetic check uses Fraction only.

No production code, source document, historical result or held-out dataset was changed. No empirical validation is claimed. The three BFG audit principles of explicit premises, negative-result preservation and source/interpretation separation are maintained.
