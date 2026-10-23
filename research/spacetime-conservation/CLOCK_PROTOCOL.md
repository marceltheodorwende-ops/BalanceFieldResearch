# Clock candidate protocol — BFG only

23 October 2026. Authority: MANDATE.de.md. Preregistered before new evaluations.
Source: pinned Dynamic Order, Parts I/II, sections 23 (equations 88–91), 55, 70.4 and II89 (equation 162). The source requires an additional independently calibrated positive quotient clock and separately constructed continuous flow; these requirements are not replaced here.

## Candidate domain and questions
Autonomous full persistence on the previously proved invariant class C: P=I, F>0, 0<m<=M<=1/2, m>=2M^2. Scalar subbranch Y=yI with 0<y<=3/10 is an admissible separate control (no simple-spectrum selector is used there).

T1. Test a uniform spectral envelope M_+<=q M with q=4/9, using the existing f bound, before claiming a summability result.
T2. Compare dimensionless candidate durations d_const=1, d_load=tr(Y)/n, and d_log=ln[tr(Y)/tr(Y_+)] on the SAME source trajectory. Prove positivity/quotient invariance and either divergence or a finite bound for each sum. A common seconds scale would be an extra calibration, not derived.
T3. On the scalar branch f(y)=2y^2/[(1+y)^2(1+y^2)], test the exact event coordinate:
a_0=-ln(2y); a_(j+1)=2a_j+ln d(y_j), d(y)=(1+y)^2(1+y^2);
A(y)=lim 2^-N a_N, tau(y)=log_2 A(y).
Prove existence, positivity, a geometric truncation bound and A(f(y))=2A(y), rather than inferring them from finite samples.
T4. Test the nonuniqueness tau_e=tau+epsilon sin(2pi tau), with declared epsilon=1/(8pi). Since this is a strictly increasing function of tau and has period-one correction, it should preserve unit increments. Determine whether this is a derived model clock or a physically selected clock; do not conflate them.
T5. No finite continuous extension of a unit-tick state coordinate to the scalar limit y=0 is expected. Prove or reject by taking the limit, without treating y=0 as an admissible nonterminal source state.
T6. Positive time assignment does not change a finite endpoint map; it cannot by itself eliminate the previously established kernel-component defect.

## Fresh controls and acceptance
Check symbolic rational envelope and scalar recurrence identities with SymPy.
Use 12 complex preparations (three each n=3,4,5,6), seed 20261027, two full-source events each: 24 events. Compare source eigenvalues to the envelope, load/log positivity, telescoping log sums and 1/(1-q) bound; normalized residuals <=1e-10.
Scalar controls at y=1/5,1/4,3/10: one full-source event each in n=2; require the source Y to equal f(y) I within 1e-10.
For tau evaluate log-domain recurrence with N=48; track the rigorous analytic tail bound ln d(3/10)/2^N, independent from floating-point roundoff. Unit-tick and perturbed-unit-tick residuals <=1e-10; record all values and do not claim rigorous machine intervals. Log-domain extrapolation after the source event is an independent analytic control, not 48 full-source events.
Retain any failure/correction and no source changes. Publish derivation, executable audit and JSON evidence; extend existing CI proportionately, verify GitHub separately. No physical clock calibration, continuous generator, spatial current or Einstein claim.
