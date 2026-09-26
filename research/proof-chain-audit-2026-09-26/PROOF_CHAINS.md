# Explicit proof chains and their limits

Throughout, spaces are finite-dimensional real or complex Hilbert spaces. Adjoints refer to the specified Hilbert inner products, not silently to a graph metric. Zero active rank is a separate terminal case. “Open” is relative to the cited source chain; this review is not an absence theorem about every BFG manuscript.

## G — Intrinsic-Gram successor

### G0. Source premises
The September 22 architecture gives neutral responses and a cross-fed analysis map. Its successor Gram factorization establishes positivity for supplied factors. The later [completion source, sections 0–2](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/CANONICAL_SELF_RECLOSURE_AXIOM.md) explicitly declares the intrinsic-Gram choice. [Architecture repair, B1–B4](../architecture-repair-2026-09-26/REPAIR.md) distinguishes the added identification and metric.

Let A:H→K be nonzero, S=(ker A)⊥, T=Ran A, and A=JQ its polar decomposition. J:S→T is unitary, Q=(A* A)^(1/2).

### G1. Additional constitutive premise
Require a Hermitian successor Y+ on T to satisfy, for every x∈S,

    <Jx,Y+Jx> = ||Ax||².                                    (G1)

This is a load-identification law, not positivity alone. It must be marked DECLARED until derived independently.

### G2. Conditional existence and uniqueness
Define

    Y+ = J(A* A)|S J* = (AA*)|T.                            (G2)

Polar decomposition gives the equality and verifies (G1). If H1,H2 both satisfy (G1), <v,(H1−H2)v>=0 for every v∈T. Polarization gives H1=H2. Since A has strictly positive retained singular values, Y+>0 on T.

For A=UΣV* in reduced SVD coordinates, [Y+]U=Σ². Degenerate singular-value frames change the coordinate matrices jointly by unitary equivalence; they do not change this operator.

### G3. Why the extra premise is necessary
Without (G1), both S0=A* A|S and S0+S0² are positive, dimensionless if S0 is, and unitarily covariant. Transport both by J. They differ for nonzero S0 and neither uses a fitted scalar. Thus those requirements do not select (G2). This is a counterexample to the listed reduced requirements, not certification against every possible BFG axiom.

For a positive target Z, B=sqrt(Z), W=L=I yields L*B*WBL=Z. If B=D_cov c is additionally required and c is invertible, D_cov=sqrt(Z)c^(-1) realizes it. If c is singular, or D_cov must satisfy derivative/locality conditions, this construction need not respect those roles. Factor existence is not role reconstruction.

### G4. Status
Conditional theorem proved. Historical derivation of (G1), metric choice and all independent factor-role laws OPEN. A G-weighted output norm in (G1) would instead produce A*G_out A; it cannot be substituted without changing the law.

## S — Neutral-Contrast Selection

### S0. Source premises and added identification
The exact neutral algebra is

    C=(I+Y)^(-1), B=Y(I+Y)^(-1), Z=C−B=(I−Y)(I+Y)^(-1).

For Y≥0, a spectral value y has z=(1−y)/(1+y). Consequently z>0 iff y<1.

The [selection document, section 0](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/NEUTRAL_CONTRAST_CLOSURE_GAIN.md) explicitly declares the identification sign(ΔC)=sign(Z). A generic rule “retain iff closure gain is positive” does not identify that gain with Z.

### S1. Defect in the stated sign-uniqueness argument
Section 1 lists dependence through contrast, sign reversal under exchange, zero at balance, a gain that “cannot decrease” with increasing contrast, and no new state-dependent coefficient. It then concludes an odd **strictly increasing** representation.

Under the literal weak-monotonicity requirements, take

    g(z)=0 for every z.                                     (S1)

It depends only on contrast, is odd, has zero at balance, is nondecreasing, and introduces no coefficient. Yet for Y=(1/2)I, Z=(1/3)I, and

    1_(0,∞)(g(Z))=0 ≠ I=1_(0,∞)(Z).                         (S2)

Thus the five requirements as written do not prove the claimed selector. If “sign reversal” is intended already to demand nonzero gain for every nonzero contrast, that is an additional strict premise that must be stated. A reversal of sign alone also does not establish equality of magnitudes g(−z)=−g(z).

This counterexample concerns the purported derivation. The already declared direct choice ΔC=Z remains a definite candidate.

### S2. Correct conditional sign theorem
Let g be real-valued on an interval containing zero and the spectrum of Z. Assume g(0)=0 and g is strictly increasing. Then for z>0, g(z)>0; for z<0, g(z)<0; equality holds only at zero. Finite spectral calculus therefore gives

    1_(0,∞)(g(Z)) = 1_(0,∞)(Z) = 1_[0,1)(Y).                (S3)

Oddness may be imposed for exact antisymmetry but is not needed for this conclusion. Full strict monotonicity is stronger than necessary: nondecreasing g, g(0)=0 and no nonzero zeros suffice. These are explicit additional assumptions, not consequences supplied by this review.

The complementary selector is 1_[1,∞)(Y); equality y=1 is excluded from retention. This proves only the selection **sign**, not the scale of gain: g(z)=z and g(z)=z³ give the same selector and different gains.

### S3. Status
Neutral contrast identity and threshold algebra: PROVED.
Selector conditional on strict sign preservation: PROVED.
The listed weak requirements imply strict sign preservation: REFUTED AS STATED.
Historical derivation of sign identification and any unique gain scale: OPEN.

Source/target ordering and witness transport remain distinct obligations. The [ordering note](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/SELECTION_FIRST_ORDERING_THEOREM.md) itself distinguishes structural ordering from the new contrast identification.

## R — Neutral transverse recursion

### R0. Inputs
Let Y+>0 on a finite nonzero active carrier. Let P=P*=P² be the already constructed inherited/seeded persistent projector, Q=I−P. Neither this theorem nor the polar transport of a given pair of supports constructs the target support independently.

Set C=(I+Y+)^(-1), q=1/(1+lambda_min(Y+))<1. The [declared recursion rule](../fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/CANONICAL_SELF_RECLOSURE_AXIOM.md) is

    R=P+QCQ.                                                (R1)

### R1. Conditional stability proof
With respect to Ran P ⊕ Ran Q, R has blocks I and T=QCQ|Ran Q. Since 0<C≤qI, 0≤T≤qI. No commutation of P and Y+ is needed. For k≥1,

    R^k=P+Q T^k Q,  ||T^k||≤q^k.

Here T is regarded as an operator on Ran Q, with the inclusions understood. R^0=I separately. Therefore R is self-adjoint and power bounded; its peripheral eigenspace is exactly Ran P. When P=0 it is empty; admissibility decides whether such a state terminates. A statement of nonempty persistence must assume P≠0.

### R2. Failure of uniqueness from stability
For the same Y+ and P, the alternative

    R'=P+Q C² Q                                             (R2)

is also self-adjoint, covariant and power bounded, preserves P and strictly contracts Q. For nonzero Q, C−C²>0 implies QCQ≠QC²Q on Q. Hence R and R' differ without a fitted parameter. This refutes selection by those constraints alone.

If one imposes RP=P, PRQ=0 and QRQ=QCQ, those blocks uniquely give (R1). But the last identity directly prescribes the desired transverse response. Calling it a characterization is not an independent derivation.

### R3. Infinite-dimensional boundary
Strict positivity without a uniform lower bound does not give q<1 in infinite dimension. On ℓ², Y e_n=(1/n)e_n is positive and injective, but C e_n=n/(n+1)e_n and ||C^k||=1 for every k. Thus the finite uniform-contraction proof cannot simply be reused. Strong decay, continuous peripheral spectrum and isolated persistent subspaces must be distinguished. Unbounded domains require further conditions.

### R4. Status
Finite stability for the declared operator: PROVED.
Unique choice from persistence and no fitted coefficient: REFUTED for those constraints.
Historical internal selection of exactly C, construction of P, and general infinite-dimensional closure: OPEN.

## Dependency conclusion
The valid dependency chain is:

    source neutral algebra + supplied state
        → analysis/polar transport
        → [declared Gram identification] → positive successor load
        → [declared sign identification] → selected support
        → inherited/seeded projector construction and gates
        → [declared transverse-response identification] → stable successor recursion.

This schematic marks dependencies, not a replacement of the source-first/target selection ordering in the full master algorithm. Whole-state category closure, formation/witness density updates, event behavior and numerical certificates require their own evidence. The three conditional proofs do not by themselves certify the full physical or continuum theory.
