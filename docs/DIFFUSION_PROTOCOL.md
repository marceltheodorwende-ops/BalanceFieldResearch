# Fixed diffusion check D1

Specified before running this check. This is a deterministic mathematical
validation protocol, not an external preregistration or a held-out learning study.

Independent process assumption: on an undirected nonnegative weighted graph,
each edge carries flux w_ij(x_j-x_i). Thus dx/dt=-Lx and the sampling operator
is R=exp(-dt L). This transport is derived from the stated flux law; the flux
law itself is a model assumption, not a theorem of BFG.

Fixed design: path, cycle, star (center vertex 1), complete; n=4,6,8;
uniform edge weights 0.5,1,2; initial states e_0 and (e_0+e_last)/2.
36 graphs, two states each, 72 runs. dt=0.2, horizon=20 steps. No fitting.

Target: norm(x_20-mean(x_0))/norm(x_0-mean(x_0)). Compute the target by
20 matrix-vector steps. Predict it from the full Laplacian modal formula.
Also report the spectral-gap upper bound exp(-20 dt lambda_2), which is a
bound, not an exact prediction. Connected graphs only in this protocol.

Numerical acceptance: absolute modal prediction error <=1e-10; no upper-bound
violation above 1e-10; total state sum preserved within 1e-10. Retain every run.
This validates two evaluations of the same linear model, not physical data.

BFG observation map: Y=dt L+alpha I, alpha=0.2. The offset is an explicit extra
load choice. Measure initial projected loads, reciprocal weights and dual gain.
For connected graphs W=span(1). Check the predicted loads
lk=n mean(x)^2/(1+alpha), lu=alpha^2 lk.

Preselected identifiability example: n=4, weight=1, initial e_0, path versus
star centered at vertex 1. Both have degree(vertex 0)=1, so projected loads,
weights and gain coincide under this map; their diffusion recovery can differ.
This addresses those readouts only, not all BFG quantities or representations.

Report numerical results and negative findings without choosing or tuning
alternative features after seeing outcomes. Any new predictive model requires
a separate protocol with an observation budget, target and held-out data.
