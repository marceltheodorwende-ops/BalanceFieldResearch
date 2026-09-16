# Optional rank truncation in proposal generation

`assess_interior` now accepts `fit_rcond=None` or a finite numeric cutoff in
[0,1). Booleans and nonnumeric values are rejected. All other defaults remain
unchanged. To use the repaired proposal method for this study, set 1e-8.

For Jacobian J=U S V^T, NumPy least squares omits singular directions below
its relative cutoff. Specifying 1e-8 avoids dividing by the small spurious
sensitivities seen in the diagnosis. The choice was fixed from the observed
spectral gap before the repaired evaluation; it was not tuned to acceptance
results. It affects proposals only, not physical admissibility or sensor errors.

The budget, backtracking, projection, rational conversion and certifier are
unchanged. Normalized coordinates are converted back inside ORIGINAL rational
bounds. Only the existing rational whole-history certifier accepts a witness.
Thus even a bad rank estimate cannot directly create a false certificate;
it may instead fail to find one. Rejected candidates never create family alarms.

The cutoff can remove small but physically relevant directions on other
problems. It does not guarantee convergence, eliminate noise, establish unique
parameters or solve arbitrary networks. It is standard numerical linear
algebra, not a new BFG law. Keep numerical search and mathematical acceptance
separate when integrating the option into other workflows.
