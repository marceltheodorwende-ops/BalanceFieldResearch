# Frozen protocol: source-selected two-mode carrier and environment closure

Date: 23 October 2026. Continuation under MANDATE.de.md and the user's explicit background authorization. Baseline research head: 3f76bc0deeaedb5477145788dd17157df571c4a8.
Active source and unchanged kernel are those in SOURCE_MANIFEST.json. Scope: autonomous full persistence P=I, 0<Y<I, F>0; aligned representative from DERIVATION.md section 1. No new physical coupling, clock, sign or source equation.

## Questions fixed before evaluation
P1. Choose the spectral subspace of the two smallest simple Y eigenvalues. Derive quotient covariance and test whether this instantaneous selection is retained after an event. Exact witness: n=3, Y=diag(1/10,1/2,9/10), F=diag(1,1,10), W=I/3, K with a nonzero off-diagonal entry in the first two coordinates.
P2. Keep the selected initial pair as transported history data. Is the compressed tuple autonomous? Exact fiber witness: Y=diag(1/4,1/2,3/4), F=diag(1,1,w), w=1 versus w=2, fixed full K with pair sigma_x and zero complement, W=I/3. Pair compression is identical; derive the actual global alpha and successor pair differences as exact rational/algebraic values.
P3. Is adjoining current alpha enough for an autonomous iterative pair factor? Exact fixed Y=diag(1/4,1/2,2/3,3/4), F0=I, W=I/4. Let b(y)=y^2/(1+y), h(y)=(1+y^2)/(1+y), alpha0=sum b/sum h, d_i=b(y_i)-alpha0*h(y_i). Set F1=diag(1,1,1+d_4,1-d_3). Require positive weights and verify equal initial alpha. Compute next alpha exactly using the common successor Y and fixed F; retain a nonzero difference or a failed witness without retuning.
P4. Seek a sufficient source-derived closed extension retaining only the pair block and the complementary formation-weighted spectral measure. Derive pushforward update of that measure and the source global alpha. Treat the initial pair label as history; do not claim a unique physical two-mode selector.
P5. Check the closed extension against the pinned full ambient update in 12 random complex preparations, n=3,4,5,6 (three each), with mixed full K,F,W and simple separated Y. Three consecutive events per preparation; hold the initial pair labels in the aligned representation. Seed 20261024; relative matrix/trace residuals <1e-10. Confirm off-block K,F,W need not vanish. Test 4 simultaneous unitary changes for projection covariance. Record terminal/numerical failures and do not alter the source tolerance.
P6. Independently verify two consecutive exact fiber examples using the full update, and verify that pair trace K is conserved in this sector even when current pair components damp. No local physical energy-momentum or spacetime conclusion follows from trace conservation alone.

## Outputs and limits
PAIR_DERIVATION.md: proofs, exact selector/fiber witnesses, sufficient extension and remaining physical gap.
pair_audit.py + pair_results.json: symbolic and full-update controls, source pin via audit.py.
Update STATUS.md, README.md and narrow CI to include this extension. Do not rerun unrelated first-round controls unless the CI workflow does so as an integrated check.
An exact environment-assisted factor is progress, not an autonomous isolated pair, derived physical clock, spatial current, unique n=2 selection or Einstein equation.
