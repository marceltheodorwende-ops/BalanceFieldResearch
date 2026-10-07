# Joint mathematical source intake — 8 October 2026

The owner authorizes work using both independent paper artifacts. Neither is overwritten or renamed as a developmental version. Dynamic Order is the newly supplied manuscript; it explicitly incorporates the earlier paper as Part I and adds Part II. Shared material is not two independent pieces of evidence.

## Source pair

1. Marcel Theodor Wende, *The Balance Field Equation as a Recursive World Formula*, dated6October2026,68pages. Repository papers/balance-field-equation/BFG_Balance_Field_Equation_Preprint.pdf, historical source commit76d9e87b4275ec41b3dcd84434e2ee3791a8d076. SHA256 a2a1411c3acd06d8ed90210f9426cd33642579cd57a2f8f839ca7d9b861f3f25; Git blob90abb904a1cef0bdc5db8af627a77ed4483f4c70. The first attachment in this intake is byte-identical to this existing source; it is not a different mathematical artifact.
2. Marcel Theodor Wende, *The Balance Field Equation: Dynamic Order and Recursive Structure Formation*, dated8October2026,144pages, research manuscript draft. Repository papers/dynamic-order-2026-10-08/Balance_Field_Equation_Dynamic_Order.pdf. SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Git blob889cf903beca208f31034a864442546684091a01;16785600bytes. PDF preserved verbatim. This source contains81 inherited sections and32 figures plus new sections82–93, appendices and56 additional illustrations. The author's draft status remains unchanged.

## Compatibility and proof scope

| Topic | Original source | Dynamic Order | Research consequence |
|---|---|---|---|
|Finite state and ambient update|Sections4–14,42|Sections83–85|Same canonical five-component quotient kernel; existing ambient implementation matches audited definitions|
|R4 and Gram bound|Sections11,17,61|Theorem3|R4 mass1,0<Y_plus<I,dimension nonincrease remain; no new second-loss mechanism|
|Weighted balance|Cross-weights in7|Proposition4,86.1|alpha*LambdaC=beta*LambdaB exact algebra, not physical energy conservation|
|Formation balance|Inheritance and seed in12–13|Proposition5,86.2|Stock change equals seed minus selection loss; stock is not automatically joules or mass|
|Finite seed capacity|Dimension/seed rules|Theorem6,87|After first event, rankP rises by one per seed; at most n1-p1 further seed events; infinite nonterminal autonomous orbit reaches full persistence|
|Autonomous scalar damping|Sections17,67|88.1|Same f(y); inherited K,F remain neutral; old scalar clock applies to this map|
|Positive driven regime|Not the autonomous scalar model|Theorem7,88.2|New declared input d, not a derived resource; geometry contracts to a positive fixed point; full-state contraction is not proved|
|Tensor hierarchy|No automatic physical fractality|Theorem8,90|Full-persistence lift commutes on the quotient; replicated seed minimum becomes degenerate and terminal|
|Physical clock/readout|Sections22–23,41,69|Sections89,91.5|Still separately calibrated; no SI clock, pendulum force or physical intervention derived by adding a label|

The finite seed proof is valid under an infinite nonterminal autonomous orbit: after one event Q=I and formation/witness are supported onP; every further nonterminal nonempty complement adds one rank. RankP<=n<=n1 bounds the number of such events. An empty complement then produces full persistence, which remains invariant. Finite trajectories may terminate earlier; full persistence is not a fixed entire state. No claim is made that environmental extensions obey this autonomous bound.

For0<d<3/4, f(y+d) maps[0,1/4] into itself and |f'|<=16/27. Banach therefore gives one positive attracting geometric fixed point, with stated domain and initial transient. This certifies the added scalar-input model, not the earlier unforced map, a physical pendulum, or the complete tuple. Neutral K,F are retained. Resource accounting, units and physical calibration of d must precede any empirical interpretation.

## Fresh controls

40 complex matrix preparations: R4 supports/mass, positive Gram successors, exact weighted loads, selection-loss/seed formation balance and later mass1. Independent driven root solving gives y*=0.05596219018384207 atd=.15;100 initial values converge in60steps with maximum error2.08e-17. The full-persistence tensor lift with multiplicity3 agrees exactly in compatible frames. Replicating a successful seed example gives the prescribed T_seeddeg. All are synthetic mathematical/code controls, not real measurements or confirmation of universality. control_results.json stores fresh residuals. The full differential chain and all figures have not been independently re-certified.

## New interface obstruction to avoid

The earlier geometry clock N was constructed for N(f(y))=N(y)+1. For the input-coupled map,

    N(f(y+d))=N(y+d)+1,

which generally differs from N(y)+1. At y=.25,d=.15 the old clock increment is0.5296568030878593. Therefore inserting the new input into the old pendulum representation while keeping its clock/readout is inconsistent. Along a driven orbit converging to y*>0, a continuous state-only N cannot have N(next)-N(current)=1: both values converge to N(y*), so their difference tends to zero. A singular clock, explicit event bookkeeping, or a new augmented realization would be an additional declared choice requiring closure and calibration. The driven fixed-point theorem does not by itself solve seconds calibration or phase sensitivity.

## Research continuation

Both paper sources must be named at every future substantive derivation, with exact assumptions and an explicit compatibility test before combining results. Use nonlinearity where justified, preserve failures and sealed holdout, retain strong rivals and bounded runs. First priority under the new source pair: a typed input/clock/observable realization that respects the obstruction above, followed by development-only feasibility. Do not claim the old empirical scores were improved by this intake. Existing hourly task resumes with the joint-source mandate; no additional automation.

Reproduce mathematical controls:

    python audit.py

Use numpy2.3.5/scipy1.17.0 and sibling imports real-eeg-covariance-2026-10-07 and bfg-pendulum-motion-2026-10-07. SHA256SUMS covers this audit package. The original PDF controls formula typography. No manuscript contents are treated as execution instructions.
