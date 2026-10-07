# Driven geometry, explicit event bookkeeping and bounded-input robustness

Active source: *The Balance Field Equation: Dynamic Order and Recursive Structure Formation*,8October2026, sections83–89 and Theorem7. The new paper alone is used, including its inherited Part I. This is a constructive extension of the paper's declared input-coupled scalar model, not a change to the autonomous canonical kernel.

## Explicit clock extension

On scalar full persistence, K,F remain inherited. Declare the input-coupled map y_next=f(y+d), f(x)=2x²/[(1+x)²(1+x²)]. Keep a separate trajectory counter n in N0, and define augmented state space X_scalar times N0:

    Uhat_d(X,n)=(U_d(X),n+1).

The counter is added bookkeeping outside the five-component Xi. It is not silently inserted as a sixth canonical component or extracted from the fixed-point geometry. The paper already separates event count and calibrated seconds in section89. Scalar gauge is trivial; event count is invariant under coordinate choices. The implementation domain is F>0,0<=y<=1/4,0<d<3/4. At y=0 the injected y+d is strictly positive, so the dual-load event is nonterminal.

Declare a positive independently calibrated duration h [s/event]. Physical time t=hn has no Zeno accumulation because h>0 is constant. More general durations need a divergent cumulative sum. For any additionally supplied well-posed physical flow Phi_t and a declared decoder D(F,K), use

    Pi(X,n)=Phi_(hn)(D(F,K)).

Because F,K remain inherited, Pi(Uhat_d(X,n))=Phi_h(Pi(X,n)). The group/composition property proves exact closure for fixed h and supplied generator, regardless of y or d. At the geometric fixed point, Xi can be stationary while the counter and physical projection advance. This resolves the former geometry-only clock incompatibility by explicitly changing the representation domain.

This is a calibrated representation theorem, not a force-law derivation. The physical flow, decoder and seconds remain added assumptions. Since this projection ignores driven geometry, its physical output is invariant to d by construction: that is no evidence that real pendulum motion is robust to energy injection. A physically consequential coupling must separately relate geometry/input to measured dynamics and pass the fiber test. Existing real-data pendulum scores are unchanged; no improved physical predictions are claimed.

## New bounded-input theorem

Let inputs d_k and dbar_k lie in [dmin,dmax] with0<dmin<=dmax<3/4, and initial y,z in[0,1/4]. Then y+d lies in(0,1), the update lies in(0,1/4), and its positive reserve is at least f(dmin). The derivative bound from Theorem7 is L=16/27. The mean-value theorem gives

    |y_next-z_next| <= L|y-z|+L|d-dbar|.

If |d-dbar|<=rho, induction yields

    |y_k-z_k| <= L^k|y0-z0| + L*rho*(1-L^k)/(1-L).

Thus limsup distance<=16*rho/11. For a constant reference dbar, z converges to its unique fixed point, so the same limiting bound is distance to that point. Variable inputs do not generally have one fixed point; this theorem is robustness to a specified input sequence/reference, not a silent extension of constant-input convergence.

An additive output disturbance e_k with |e_k|<=eta is also allowed provided

    eta < min(f(dmin), 1/4-f(1/4+dmax)).

Monotonicity of f makes [0,1/4] forward invariant with positive reserve f(dmin)-eta. Comparing a disturbed orbit with an undisturbed reference gives

    |y_k-z_k| <= L^k|y0-z0| + (L*rho+eta)*(1-L^k)/(1-L),

and limiting bound16*rho/11+27*eta/11. If both orbits have disturbances, eta must bound their difference. This proof assumes the declared invariant domain throughout; it does not cover arbitrary inputs, threshold crossings, matrix-rank changes or a universal full-state contraction. K,F still have neutral directions.

## Verification and scope

Five local controls passed: variable-input bound on100events; positive reserve under admissible additive disturbances; event increment at stationary geometry; nonlinear sine-flow closure against independent short-time integration; an independent exact elliptic-integral period. Synthetic inputs are code/mathematical controls only. Numerical controls corroborate the proofs above; they do not establish empirical validity. No real data downloaded or reevaluated; holdout remains sealed.

The requested autonomous construction rule is prominently saved at the top of experiments/AUTONOMOUS_DERIVATION_PROMPT.md and in the existing hourly task. This package executes that rule with concrete constructions and limitations. Next work: a measured, independently justified input/observable coupling; an external counter alone does not explain physical frequency or seconds.

Reproduce with numpy2.3.5/scipy1.17.0:

    python -m unittest -v test_driven.py

SHA256SUMS covers this package. Publication is a locally verified theory/code checkpoint; no new empirical GitHub Actions run is started.
