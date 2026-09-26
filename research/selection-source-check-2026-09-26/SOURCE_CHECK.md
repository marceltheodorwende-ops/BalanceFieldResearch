# Source check of strict Neutral-Contrast Selection
Date: 26 September 2026. Status: bounded source audit; historical derivation remains OPEN.
BFG author: Marcel Theodor Wende. This is an AI-assisted review note, not a new author-approved preprint.

## Question
Does an independently stated BFG rule force sign(Delta C)=sign(C_N−B_N), rather than merely declaring that identification?

## Source evidence
The sources below were inspected through existing text extractions. Original bytes were not modified. This is a targeted passage audit, not a complete proof audit of the full corpus; PDF extraction may lose mathematical layout.

1. **Full_BFG_Trinitarian_Recursive_Closure_Monograph_Pure_BFG_Strongest_EN_v3.docx**, chapter 10, section 10.2, T9 and the operational checklist.
   Original SHA-256: 29b4e352fa4204a93bf393ffe9639d8d9817a335b8c19fc453922524c434adb0.
   The chapter requires retention for positive closure gain and export for nonpositive gain. It also requires the user of the framework to define selection and what counts as positive closure gain. This supplies the selection grammar, not an identity between that gain and the neutral contrast. In particular, the word “positive” refers to Delta C, not to Z.

2. **BFG_Canonical_Universal_Reclosure_Architecture_Preprint_2026-09-22_FINAL.pdf**, section 4.3, equations (20)–(21), printed pages 4–5.
   Original SHA-256: 1dd543e4d3849854ad3e08bd13e5d2e200156caa871d1683ac466729af4c765f.
   The exact contrast Z=(I−Y)(I+Y)^(-1) encodes the neutral pair losslessly, with C_N=(I+Z)/2 and B_N=(I−Z)/2. This identifies response imbalance. The inspected passage does not identify response imbalance with an independently defined increment of admissible closure. A lossless encoding is not a proof that every gain depends only on that encoding, much less that it is strictly sign-preserving.

3. **BFG_Model_Of_Biological_Organism_Formation.pdf**, sections 10.1–10.10, printed pages 54–58.
   Original SHA-256: bff7ee6ff16b82bb4085552da7ced62e8963eb835ab5e0faa29076fdab23c066.
   Closure is modeled using weighted balance, information, coupling and recursive-stability benefits minus cost and drift. Projection gain is a difference of that closure functional with and without projection. The source expressly allows projection to be neutral, beneficial or destabilizing. No relation in these inspected sections reduces all those terms to Z or proves that their sign is its sign. This carrier-specific construction is not a disproof of a future universal identification; it shows why the identification needs a bridge theorem.

Supplementary screening of BFG_Strongest_Version.pdf and the journal-ready minimal-reclosable-difference selection-series DOCX did not produce the needed bridge. Their spectral persistence and ratio-selection topics must not be substituted for a neutral-gain sign theorem. This negative search result is bounded, not an absence theorem.

The current package itself explicitly labels the identification new:
[Neutral-Contrast Closure Gain, section 0](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/NEUTRAL_CONTRAST_CLOSURE_GAIN.md).
Its [ordering note](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/SELECTION_FIRST_ORDERING_THEOREM.md) distinguishes inherited structural order from that new identification.

## Logical result
The checked chain is:

    retained iff Delta C>0                    [source selection grammar]
    Z=C_N−B_N                                [source neutral algebra]
    sign(Delta C)=sign(Z)                     [missing bridge / declared choice]
    retained iff Y<1                         [conditional spectral consequence].

The third line is not supplied by either of the first two lines.

The previous [proof-chain audit](../proof-chain-audit-2026-09-26/PROOF_CHAINS.md) remains valid. Under the literal weak requirements, g(z)=0 is odd, nondecreasing, balanced at zero and coefficient-free, yet does not produce the contrast-positive selector. This is a counterexample to those listed sufficient conditions, not a physically proposed BFG model. A global nontrivial-closure requirement might exclude this example, but would still need a proof implying the strict sign condition mode by mode.

## A precise weaker sufficient premise
In the scalar spectral setting, suppose g is nondecreasing and g(0)=0. Then

    sign(g(z))=sign(z) for all realized z

holds if and only if g has no zero at a nonzero realized contrast.

Proof: monotonicity gives g(z)>=0 for z>0 and g(z)<=0 for z<0. Excluding nonzero zeros makes both inequalities strict. Conversely sign equality excludes those zeros. Finite spectral calculus then gives the same positive spectral selector. This condition is weaker than requiring g to be strictly increasing everywhere, but still needs its own BFG justification.

For instance, within the scalar reduction an independently justified injective gain readout on the realized contrast values would imply the no-extra-zero condition. General BFG requirements to preserve distinguishability do not automatically make this particular scalar gain map injective: distinguishability could reside in other state variables. That additional implication has not been proved here.

## Authentically open status
- Exact neutral algebra: established.
- Generic positive-gain selection grammar: present in the checked source.
- Conditional spectral selector under sign identification: established.
- Necessity of the sign identification from those sources: not established.
- Weak monotonicity alone sufficient for the selector: false.
- The existing finite candidate with explicitly declared Delta C=Z: not refuted by this audit.

Do not amend the historical sources to make them appear to contain the bridge. The next derivation must define closure gain independently and prove that no nonzero neutral contrast has zero gain, while retaining the monotonicity premise. If the independent gain depends on variables beyond Z, first prove the reduction to a scalar spectral function rather than assuming it.

No simulations, external physical laws or empirical claims were used. Source/claim separation, preservation of negative findings and recoverable source identity follow the three BFG audit documents. No executable behavior changes.
