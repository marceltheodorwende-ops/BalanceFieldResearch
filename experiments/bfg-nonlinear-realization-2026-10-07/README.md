# Exact nonlinear motion representation and a force-selection counterexample

## Result and premises

The canonical scalar BFG representation is not restricted to linear motion. Its already derived event clock satisfies N(U(X))=N(X)+1; its scalar formation F and phase K are inherited unchanged. This package constructs an exact conditional nonlinear representation and proves that the same construction does not uniquely select a force law. No new empirical claim or holdout evaluation is made. Synthetic cases below are mathematical controls only; the previous real-data long-horizon result remains the empirical development evidence.

Declare physical parameters a>=0 [s^-2], b>=0 [s^-1], duration dt>0 [s], and a dimensionless additional hypothesis alpha in [0,1]. On unwrapped angle theta [rad] and velocity w [rad/s], choose

    theta' = w
    w' = -a*((1-alpha)*theta + alpha*sin(theta)) - b*w.

alpha=1 is the full sine pendulum, alpha=0 the linear oscillator. Intermediate alpha is a counterexample family, not a proposed discovered force. Radians are dimensionless in these formulas; coding uses reference units 1 rad and 1 rad/s to make the carrier dimensionless. Physical inertia, torque and clock calibration remain additional assumptions.

## Existence and exact closure

The vector field is globally Lipschitz on R² because the derivative of its restoring function is (1-alpha)+alpha*cos(theta), whose absolute value is <=1. Its growth is at most linear. Therefore unique solutions exist for every finite positive or negative time and define a flow Phi_t with Phi_(t+s)=Phi_t composed with Phi_s. Damping does not obstruct mathematical backward uniqueness; backward motion is not a passive physical experiment.

Prepare normalized x0=theta0/theta_star, q0=w0/w_star, F=1+x0²+q0² and K=atan2(-q0,x0). F>=1 keeps BFG loads positive, including rest. Decode theta0=theta_star*sqrt(F-1)*cos(K), w0=-w_star*sqrt(F-1)*sin(K). Rest has K arbitrary. Declare the projection

    Pi_alpha(X) = Phi_(dt*N(Y))(decoded(F,K)).

Since U preserves F,K and advances N by one,

    Pi_alpha(U(X)) = Phi_(dt*(N(Y)+1))(decoded(F,K))
                  = Phi_dt(Pi_alpha(X)).

Thus equality of projected physical states implies equality of their projected successors for fixed a,b,alpha,dt. This is exact semiconjugacy, without a small-angle expansion, weak-damping condition or amplitude gate. Rotations and the separatrix are allowed. The theorem concerns the exact mathematical flow; nonlinear.py computes it numerically with DOP853 and stated tolerances. Raw-Y underflow still requires the previously published stable clock coordinate for long BFG event sequences.

## Energy and dissipativity

For this family define normalized mechanical energy

    E_alpha(theta,w) = w²/2 + a*((1-alpha)*theta²/2 + alpha*(1-cos(theta))).

Differentiate using the declared vector field:

    dE_alpha/dt = w*w' + a*((1-alpha)*theta+alpha*sin(theta))*theta'
                = -b*w² <= 0.

E_alpha is nonnegative. At alpha=1 its potential is periodic; theta is unwrapped, and rotations remain possible. Multiplying by independently calibrated inertia gives physical joules. This energy is not the scalar formation F, which encodes initial data and stays inherited.

## Why this does not derive the sine force from BFG

Every alpha in [0,1] uses the identical canonical BFG update, initial encoding and event clock, and every member is passive. All have the same equilibrium linearization [[0,1],[-a,-b]]. Yet at theta=pi/2, w=0 their accelerations are -a*((1-alpha)*pi/2+alpha), which differ when a>0. Hence those BFG assumptions, passivity and small-motion frequency cannot uniquely imply alpha=1.

Even adding angle periodicity does not select sine uniquely: the family g_c(theta)=(sin(theta)+c*sin(2*theta))/(1+2*c), c>=0, is periodic, has g_c'(0)=1, and has nonnegative periodic potential [1-cos(theta)+c*(1-cos(2*theta))/2]/(1+2*c). Its force is distinct for c>0. It again admits a globally Lipschitz flow and the same BFG clock representation. This provides a concrete further counterexample rather than relying on a vague missing assumption.

A conventional additional selection premise is a rigid arm in a uniform gravitational field: height ell*(1-cos(theta)) gives potential m*g*ell*(1-cos(theta)), torque -m*g*ell*sin(theta), and a=m*g*ell/I. This selects the sine law conditional on apparatus geometry and gravitational coupling. Those premises are not derived here from BFG. A BFG-specific selection principle must independently restrict the physical projection/potential; embedding the supplied solution in Pi is not such a principle.

## Verification and limits

Six local controls passed: actual ambient BFG update including rest and rotation; nonlinear flow composition; independent exact undamped periods using complete elliptic integrals at amplitudes .3,1.5,2.8 rad; independent linear endpoint via matrix exponential; conservative/dissipative energy and distinct force outcomes; initial encoding/rest. These corroborate implementation, not general theorem proofs. The derivations above supply the stated proofs.

No new data were downloaded. The 30 reserved attempt-2/3 recordings remain closed. Previous phase correction is retained as an efficient approximation; this exact representation is mathematically identical to its supplied mechanical rival and therefore adds no independent predictive advantage. Next development question: independently constrain energy/coupling and intervention maps, rather than counting an encoded rival as BFG superiority.

Reproduce from this directory with numpy==2.3.5 and scipy==1.17.0:

    python -m unittest -v test_nonlinear.py

Sibling imports use the published pendulum-motion and real-EEG modules. SHA256SUMS covers this package. No new empirical workflow is required for this theory/code-control checkpoint.
