# Next premise check: interface identification versus a coordinate choice

3 November 2026. Follow-up to the existing [derivation/program crosswalk](DERIVATION_PROGRAM_CROSSWALK.md). This is part of the existing research record, not a new paper or fundamental law.

## Question

The earlier BFG formation calculation already yields a positive formed-state Hessian H. The neutral completion, once supplied, already yields its Gram and resolvent. Does H itself uniquely determine the source-neutral coupling and neutral metric, or could the apparent freedom be eliminated by a coordinate normalization?

**Bounded answer:** H alone does not determine them in the class of strictly positive finite quadratic joint assessments. We classify that whole quadratic class and distinguish genuine coordinate changes from inequivalent completions. This does not refute the fixed completion's derivation and does not claim to classify every nonlinear historical BFG model.

## 1. Exact classification of the quadratic interface

Let source and neutral carriers be finite real or complex vector spaces with specified reference inner products. Fix a positive definite Hermitian source Hessian H. Any strictly positive quadratic assessment with that source block has the form

`J(D,eta) = (D* H D + 2 Re(D* B eta) + eta* N eta)/2`,

with joint Hermitian matrix `[[H,B],[B*,N]]>0`.

**Proposition I1.** Such assessments are in bijection with pairs `(L,M)` where L is an arbitrary linear map from the neutral carrier to the source and M is positive definite. The unique representation is

`J(D,eta)=||D-L eta||_H^2/2 + ||eta||_M^2/2`,

`L=-H^-1 B`, and `M=N-B*H^-1 B`.

**Proof.** Expanding the squares gives cross block B=-HL and neutral block N=M+L*HL. Conversely, substituting L=-H^-1B gives the displayed M and reconstructs exactly the original blocks. The block change of variables `(D,eta) -> (D-L eta,eta)` is invertible, so the joint form is positive definite exactly when both H and M are positive definite. This also proves M>0 from the original positive joint form without assuming a particular channel. Uniqueness follows by comparing cross and neutral blocks. QED.

Thus a fixed H leaves the full linear map L and intrinsic neutral metric M undetermined inside this quadratic class. Positivity does not remove that freedom. This is an application of square completion/Schur-complement algebra, not a claim to a new general matrix theorem.

The term 'intrinsic neutral metric' means the metric of the second completed square, M. The neutral diagonal block of the full joint Hessian is N=M+L*HL, not M. Confusing these two matrices can create a false uniqueness argument.

## 2. What the existing elimination determines

For a fixed L and M, strict convexity gives

`eta*=(M+L*HL)^-1 L*H D`,

`J_min(D)=D* [H-HL(M+L*HL)^-1 L*H] D /2`.

Whiten the source by d=H^(1/2)D and define

`Y=H^(1/2)L M^-1 L*H^(1/2)`.

Then exactly

`J_min(D)=d* (I+Y)^-1 d /2`.

This is the same conditional neutral-resolvent derivation already established in the prior bridge. It remains valid. The question is the selection of L and M, not a defect in the minimization. A specified source-response identity determines Y, but not automatically a unique physical neutral carrier or a particular channel representation.

## 3. Coordinate freedom does not explain every difference

Change neutral coordinates by eta=T zeta, with T invertible. The same assessment has L'=LT and M'=T*MT. Its source load is unchanged:

`Y'=H^(1/2) LT (T*MT)^-1 T*L* H^(1/2)=Y`.

Consequently, different coordinate matrices for L and M need not represent different models. That freedom must be quotiented before claiming nonuniqueness.

But let H=M=diag(2,3), and compare L1=I/2 with L2=I/3. Both joint assessments are strictly positive, use the same source Hessian and the same intrinsic neutral metric, and introduce no fitted coefficient. Their loads are Y1=I/4 and Y2=I/9, with retained responses 4I/5 and 9I/10. Distinct source response eigenvalues cannot be removed by an invertible change of neutral coordinates representing the same assessment. Nor can an isometric source-frame change equate their different spectra. These are genuinely inequivalent quadratic completions, not merely whitening conventions. They are logical witnesses only; neither is newly adopted as a BFG law.

For example, T=(2/3)I changes L1 to L2, but it simultaneously changes M to (4/9)H and keeps Y equal to I/4. Resetting M to H after this transformation changes the assessment rather than merely its coordinates. Both original fixed choices L=aI transform covariantly under a simultaneous orthogonal/unitary source-neutral frame change; that covariance does not select a.

The H used here is compatible with the already analyzed formation example K=diag(-1,2): at its real formed minimum e1, the source formula gives H=diag(2,3). In the September example the capacities are c=diag(0,3), aleph=[[1,1/4],[1/4,1]], D=[[2,1/4],[1/4,2]], giving the same K. All that formation data can be held fixed while testing the two candidate quadratic interfaces. We do not claim these candidates obey the later proposed mixed-Hessian rule: they intentionally test the earlier data without that extra rule.

## 4. Check against the existing proposed L0-NC restriction

The September proposal additionally prescribes the mixed Hessian B=-aleph and intrinsic neutral metric M=H. Proposition I1 then gives

`L=H^-1 aleph`,

`Y=H^(-1/2) aleph H^-1 aleph H^(-1/2)`.

Thus the proposal really does fix the channel and metric in its stated same-carrier quadratic sector; the resulting Gram is the square of H^(-1/2) aleph H^(-1/2). It is not empty notation. The two clauses contain independent information: fixing B leaves M free, while fixing M leaves B free. For example, keep L=H^-1 aleph and replace M by 2H; the mixed Hessian is unchanged but Y is halved. Conversely, keeping M=H permits the two different L values above.

These calculations confirm the proposal's own conditional theorem. They do not adopt it, reclassify it as an original axiom, or show that the original formation Hessian already had those two extra joint-block identifications. Its proposed status remains unchanged.

## 5. What was accomplished, and where to stop honestly

The algebraic part of the question is now settled within the stated quadratic class: normalization alone cannot supply the missing interface. We have an explicit classification, a true-coordinate-invariance proof, and inequivalent examples with the same formed Hessian and same neutral metric. The earlier scalar L=1/L=2 and M-variation examples were already in the September records; this follow-up does not claim their first discovery. The added work makes the full block structure and coordinate-invariant distinction explicit.

Still required for a derivation from the earlier primitive set is a source-based reason fixing the mixed source-neutral Hessian and intrinsic neutral metric, or equivalently fixing the resulting assessment. No such reason has been proved by this classification. This is not a theorem that none can exist. We do not invent a new physical postulate to fill it, and we do not repeat the false broader claim that no conditional Gram derivation exists.

The next source question can now be stated precisely: **Does an already accepted BFG premise determine the mixed Hessian B of the joint source-neutral assessment and its intrinsic neutral Schur complement M?** If a proposed invariance principle is used, its exact transformation group and action on both carriers must be written down and checked against the inequivalent witnesses. Qualitative references to symmetry alone do not answer it.

## Reproduction and status

Run `python foundation_audit/verify_interface.py` from the verification-stage folder. It requires SymPy. [Results](interface_results.json) contain three exact positive joint-form fixtures, exact elimination identities, nonorthogonal neutral-coordinate invariance checks, inequivalent response spectra, and the two independent clauses of the existing proposed restriction. The general argument is the written proof above; finite examples do not establish it by themselves. No proof assistant or empirical experiment was used. No published paper or event implementation is changed.
