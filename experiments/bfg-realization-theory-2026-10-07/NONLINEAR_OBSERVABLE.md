# Exact nonlinear observable for scalar BFG decay

## Mathematical construction

For f(y)=2y^2/((1+y)^2(1+y^2)), 0<y<1, put
a(y)=1/((1+y)^2(1+y^2)), and y_j=f^j(y). Define

    log phi(y) = log(2y) + sum_{j=0}^infinity 2^(-j-1) log a(y_j).

The series converges absolutely: |log a(y_j)|<=log 8 and its coefficients
sum to one. Direct index shifting gives the exact identity

    phi(f(y))=phi(y)^2.

Also phi(y)~2y as y->0. The scalar contraction implies y_j->0.
It follows from the identity and this limiting behavior that 0<phi(y)<1
throughout 0<y<1. This is the real Böttcher coordinate for this branch.

Since f is strictly increasing on (0,1), and phi is strictly increasing
locally near zero, iteration extends the increasing coordinate to this
interval. Local regularity follows from the convergent analytic construction;
one can alternatively use the usual superattracting fixed-point coordinate
theorem. These statements apply to the scalar map, not an arbitrary full
matrix trajectory.

Let t(y)=-log phi(y)>0. Then t(f(y))=2t(y).
For any p>0 and C>0, choose an observable

    H_p(y)=C*t(y)^(-p).

It satisfies exactly

    H_p(f(y))=2^(-p)*H_p(y).

Thus every desired fixed event retention q in (0,1) can be represented by
p=-log(q)/log 2. This is an exact mathematical family, not merely a fitted
numerical approximation. An appropriate C and initial y can place a finite
physical energy range in the observable's range.

## Why the earlier obstruction is respected

As y->0, H_p(y)~C*log(1/(2y))^(-p). Extend H_p(0)=0.
Then H_p(y)/y->infinity. The bridge is not C1 with finite derivative at zero.
It therefore evades, rather than contradicts, the theorem ruling out a
regular C1 energy bridge with finite nonzero derivative.
Such an inverse-log observable needs independent physical justification;
it is extremely different from the original linear energy readout.

The same calculation also shows why geometric contraction rates depend on
the observable. Superquadratic convergence of internal y does not imply the
same physical energy damping rate under an unrestricted nonlinear projection.

## Empirical meaning and identifiability

Choosing p to equal a fitted physical decay factor would make predictions
identical to that decay model. Better errors would then be attributable to
that fitted physical law encoded in the bridge, not independent BFG evidence.
This construction is a warning about observational equivalence and also a
precise candidate for further physical derivation.

A confirmatory realization must justify C,p and the observable independently,
calibrate the carrier preparation and clock, and derive intervention effects
that distinguish it from physical decay rivals. The full scalar R4 inherited
formation and kernel variables must still be accounted for; projecting a
scalar load is not complete-state identification.

Length and baffle changes could in principle constrain a common observable
and intervention map. Fitting a separate arbitrary p for every condition
would remove much of that discriminating power. A credible next development
test requires shared calibrated parameters and cross-condition constraints.

## Verification and next work

conjugacy.py checks 999 y-values and four powers with numerical residuals
1.7763568394002505e-15 for the logarithmic identity and
2.220446049250313e-16 for retention. These are mathematical code controls,
not empirical validation. All reserved physical holdout files remain sealed.

Next steps, development only:
- Analyze whether a shared physically calibrated observable can be derived,
  rather than freely choosing p to reproduce each condition.
- Audit noise amplification and inversion near small y.
- Determine whether angle/velocity measurements identify a richer carrier
  and a closed physical projection.
- Specify actual intervention operators and independently calibrated clocks.
- Preserve the exact equivalence to decay rivals in any decision rule.

Status: a stronger constructive mathematical result is available. A fully
derived physical realization and independent empirical superiority are open.

