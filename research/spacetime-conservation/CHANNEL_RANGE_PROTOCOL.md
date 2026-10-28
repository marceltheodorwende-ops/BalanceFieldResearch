# Channel range on a declared formation-node chain — preregistered protocol

23 October 2026. BFG only; MANDATE.de.md governs.
Source: unchanged pinned Dynamic Order Parts I/II and aligned full-persistence channel.
Candidate adjacency: formation eigenmodes ordered by F=diag(1,...,n), with nearest-neighbor Y=y0 I+epsilon A_path. This graph is a declared internal readout, not physical space. y0=1/4, epsilon<=1/40 puts the controls in C.

## Questions
R1. Reexpress the actual source operators as
T_C=sqrt(alpha)(alpha I+beta Y²)^-1/2,
T_B=sqrt(beta)Y(alpha I+beta Y²)^-1/2.
Check the cancellation of I+Y analytically and numerically; do not replace the source update.
R2. Exact n=3 chain: epsilon=1/40, F=diag(1,2,3), W=I3/3, K=diag(1,0,0). Y13=0. Derive alpha exactly and prove a nonzero endpoint channel coefficient, hence P31=sum_a |T_a,31|²>0, using the spectral second divided difference of t_C(y). Establish a sign/convexity certificate on [1/4-sqrt(2)epsilon,1/4+sqrt(2)epsilon], not only a floating-point tail.
R3. If the strict one-hop candidate fails, test approximate locality rather than truncate the source: let D=alpha I+beta Y², c=(d_min+d_max)/2, H=I-D/c, r=||H||<1. Derive the binomial inverse-square-root expansion and a rigorous geometric truncation bound. For path-tridiagonal Y, the degree-N H polynomial has bandwidth 2N, and Y times it bandwidth 2N+1. State the resulting distance-dependent amplitude/transition bound and its spectral assumptions.
R4. Exact alternative: source channel operators preserve disconnected reducing blocks of Y. Distinguish no cross-block K-stock transfer from autonomous subsystem closure, since global alpha still depends on all formation/load data.
R5. Do not infer Lorentz-causality violation, physical propagation speed, a spatial dimension or Einstein dynamics from an internal-chain tail. Separate exact support, norm approximation, floating precision and physical geometry.

## Fresh controls
Exact symbolic alpha and n=3 spectrum, the t_C second-derivative/sign certificate, positive chain admissibility and binomial coefficients. Independent scalar spectral evaluations of the exact endpoint formula.
12 complete source events: n=3,4,5,6 at epsilon=1/40,1/80,1/160, with K=diag(1,0,...), W=I/n. Verify source K_+, population q_+=P e1, source operator cancellation, and N=0,1,2 approximation/error bounds. Record long-range weights; only claim strict exact nonzero where independently proved.
Four additional simultaneous-unitary source checks (epsilon=1/40, each dimension).
Four disconnected-block source controls (n=4,5,6,7), block-diagonal Y comprising paths with the same y0/epsilon, diagonal positive F. Check zero cross-block transitions/flux and component stock invariance using a generic Hermitian K with crossblock coherence. Final total 20 complete source calls.
Identity and inequality numerical residuals <=1e-10. No positive lower bound is inferred from a tail near machine precision; report all minimum magnitudes and distinguish full-source output from matrix-function estimates.
Publish protocol first, then proof/audit/results/status and necessary CI step; verify explicit GitHub code commit independently from local results. Original source, tolerances, licenses and empirical outputs remain untouched.
