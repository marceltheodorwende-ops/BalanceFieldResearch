# Frozen protocol: first BFG spacetime/conservation round
Frozen before new audit execution, 23 October 2026. Authority: MANDATE.de.md.

## Scope and source
Active source: Dynamic Order (8 October 2026), Parts I and II; SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Baseline commit 457f23df6d9ccb15cf17916f3c3eac113b23c370.
Source sections: II83-85 (complete ambient update and quotient), II86 (weighted loads and formation accounting), II89 (fiber closure and clock), II90 (conditional tensor lift), II91.1 (additional spacetime/action).
Existing implementation: experiments/real-eeg-covariance-2026-10-07/experiment.py, function update. Import only; do not run its empirical download/evaluation entry point.

## Predeclared questions and candidates
C1: Is tr(K) invariant on the autonomous full-persistence sector P=I, 0<Y<I, rho_F>0, rho_W positive trace one? Compare the complete source update to the independently derived aligned channel.
C2: Is E_F=tr(rho_F K) conserved? Test the exact two-dimensional example Y=diag(1/4,1/2), rho_F=[[1,1/2],[1/2,1]], K=sigma_x, rho_W=I/2. Compare to Y=(3/8)I for scalar-readout fiber closure, holding all other inputs fixed.
C3: Does tr(K) remain invariant outside that sector? Test n=2, P=diag(1,0), Y=I/2, rho_F=rho_W=P, K=-I. Use the complete update, including the nonempty admissible seed complement.
C4: Which fixed linear K-readouts are conserved for every K in one full-persistence event? Derive the adjoint fixed-space condition, not just examples.
C5: What does scalar contraction imply about continuous first integrals depending only on scalar y, with other scalar-branch constants fixed?
C6: Can an injective pullback/congruence of positive G supply Lorentz signature? Can an internal natural rank-one time projector be selected at a fully isotropic state?
C7: Test a BFG-internal alternative: use the real vector space Herm(C^2), determinant quadratic form and positive cone. Distinguish this standard algebraic Lorentz carrier from physical spacetime, dimensional selection and dynamics. Test the actual K channel on a determinant-null input K=I+sigma_x. Null-to-timelike behavior rejects interpreting this channel as a Lorentz/conformal frame transformation, not Lorentz-covariant physics in general.
C8: Compute the scalar-point derivative of the actual Y update at Y=I/2 with rho_F=I, keeping all endogenous weights differentiated. Test a null tangent I+sigma_x in the determinant lift. Do not fit a new metric to make this pass.
C9: Test completeness of action/energy claims: a telescoping reservoir and a multiplier action that encode an arbitrary update are additional constructions, not source-selected physical energy or a Noether stress law.

## Evidence and predeclared bounds
Exact symbolic proofs and rational/algebraic two-by-two witnesses are primary. Use Python fractions/SymPy for independent exact certificate calculations.
Use the existing complete complex update for numerical cross-checks, not a substituted scalar map.
Numerical seed 20261023; 32 complex full-persistence preparations, 8 each in dimensions 2,3,4,5. Require normalized matrix/trace residuals <=1e-10. Add 12 simultaneous unitary-gauge controls, 16 positive-matrix cone controls, four dimensions including 2 and 3 for internal-metric checks, and exact counterexamples C2/C3/C7.
Derivative comparison: central differences h=1e-4,1e-5,1e-6; require best norm error <1e-7 and record all errors. Finite differences corroborate the analytic derivative only.
Expected nonzero defects require lower bounds derived from the exact witnesses, not tolerance-tuned after execution.
Import the existing audit only for source checks; make no empirical or full-suite pass claim. Check source blob SHA before execution. Record runtime versions and SHA256s; avoid machine-identifying environment fields.
A failed control remains a failure and triggers analysis, not coefficient fitting.

## Completion outputs
DERIVATION.md: explicit propositions, proofs, assumptions, counterexamples and boundaries.
audit.py + test_audit.py + results.json: fresh reproducible checks and failures if any.
STATUS.md + README.md: question-to-evidence ledger, exact remaining dependency, and reproduction instructions.
A completed first round is a checked research result with open gates, not a completed physical Einstein derivation.

## Pre-execution source-algebra amendment and additional exact balance check
Before new audit execution, direct rank analysis corrected the original C3 seed expectation: P=diag(1,0), Y=I/2 has analysis rank one and no seed complement. Keep that rank-drop witness. Add C3b: v=(sqrt(3)/2,1/2), P=vv^dagger, F=W=P, Y=diag(1/4,1/2), K=diag(-1,-2); analysis rank two and a one-dimensional negative seed complement. Both are documented in DERIVATION.md.
After the first control run passed, extend the investigation (C10) to the exact complete-event trace defect: with U_C,U_B the two blocks of the actual analysis isometry, D=U_C U_C^dagger+U_B U_B^dagger, test tr K_+-tr K=tr[K(D-I)]. Use 24 predeclared random partial-carrier cases (6 each at n=2,3,4,5), K negative definite with nondegenerate compressed eigenvalues, mixed Y in (.15,.8), F,W supported on P. Record terminal cases rather than dropping them; require all nonterminal residuals <1e-10 and report the number. A telescoping signed history ledger follows algebraically; do not call it a positive physical reservoir or local stress.




Runde 24: [Vorabprotokoll für unteres Paar-Gedächtnis](LOWER_PAIR_MEMORY_PROTOCOL.md). Auswertung und Prüfkorrektur sind in LOWER_PAIR_MEMORY_DERIVATION.md festgehalten.
