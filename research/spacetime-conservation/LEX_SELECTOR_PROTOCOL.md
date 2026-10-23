# Lexicographic Y/F/W selector — preregistered protocol

23 October 2026. BFG only; MANDATE.de.md governs. Source is the unchanged pinned Dynamic Order Parts I/II.
Domain: autonomous full persistence in extrema class C, allowing degenerate Y. No physical locality or uniqueness is assumed.

## Candidate and checks
L1. Refine ordered spectral blocks of Y by the spectrum of each compressed F block, then refine any remaining F-degenerate block by compressed W. Keep whole unresolved terminal blocks. Define S2 only when the cumulative terminal-block ranks reach exactly two; do not split a remaining block with an arbitrary eigensolver basis.
L2. Prove unitary covariance, commutation [S2,Y]=0, and aligned persistence of every refined block on C. F and W are aligned constants; distinct Y blocks remain ordered there. Determine whether the earlier pair plus complementary formation-weighted spectral measure is still closed for this current-state selector, including Y degeneracies.
L3. Test the preceding exact collision successor Y=diag(50/209,386/1881,50/209), F=diag(1,1,41762/20625), W=I/3. Y/F should select original modes {2,1} (one-based). Test a Witness-needed case: Y=diag(1/5,1/4,1/4,3/10), F=I4, W=diag(1,2,3,4)/10; expect {1,2}.
L4. Preserve unresolved symmetry and continuity limits. At Y=(1/4)I3,F=I3,W=I3/3,K=I3 the selector must return unresolved, not a numerical rank-two subspace. Compare Y=diag(1/5,1/4-epsilon,1/4+epsilon), F=diag(1,2,1), W=I3/3 at epsilon=0,1/1000,1/100000: determine whether S2 is continuous at the exact tie.
L5. Construct the equal-Y selected-pair alternative: Y=diag(1/5,1/5,3/10,3/10), F has diagonal (1,2,3,4), F13=1/4, F24=i/5 and conjugates; W=I4/4 with W12=(1-2i)/40 and conjugate. The selector should choose {1,2}. Use F-refined eigenlines for E3 and the nonzero W offdiagonal for transverse axes. For a generic Hermitian K with nonzero selected coherence and nonzero pair/rest block, test all four relational local kernel coordinates conserved while global cross-Y coherence is damped. Distinguish this degenerate-load sector from the earlier unequal-Y damping theorem, and from physical four-current conservation.

## Fresh evidence
Exact symbolic diagonal selectors, collision/Witness examples, unresolved block and discontinuity; exact positivity and alpha for L5, and the source h=1 identity for equal loads.
12 complex preparations (three each n=3,4,5,6), seed 20261030, with repeated lowest Y eigenvalue in n=3 or repeated second Y eigenvalue in n>=4. For each dimension, cases 0/2 use nondegenerate formation within the tied Y block, case 1 uses scalar formation there and a nondegenerate Witness block. Permit nonzero formation/Witness couplings to other Y blocks without disturbing the specified compressions; keep positivity.
Two full-source events per preparation: 24. Four additional independent gauge-source calls (case 0, event 0, each dimension). Check reselected S, covariance and closed pair update with the retained complementary measure, normalized residuals <=1e-10.
L3 two witness calls plus L5 one call give 31 full source calls overall. Do not use source evaluations for the unresolved/discontinuity proof.
Numerical grouping tolerance is 1e-10 times max(1,operator norm), only for reproducing exact deliberately degenerate examples; verify all distinct test gaps exceed it comfortably. This is not a physical degeneracy law or a continuation regularization.
Publish exact proof, audit, JSON and status; verify CI separately. Failed controls remain visible. No source/empirical changes, no spatial displacement/Einstein inference.
