# Frozen protocol: first BFG spacetime/conservation round
Frozen before new audit execution, 23 October 2026. Authority: MANDATE.de.md.

## Scope and source
Active source: Dynamic Order (8 October 2026), Parts I and II; SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Baseline commit 457f23df6d9ccb15cf17916f3c3eac113b23c370.
Source sections: II83-85 (complete ambient update and quotient), II86 (weighted loads and formation accounting), II89 (fiber closure and clock), II90 (conditional tensor lift), II91.1 (additional spacetime/action).
Existing implementation: experiments/real-eeg-covariance-2026-10-07/experiment.py, function update. Import only; do not run its empirical download/evaluation entry point.

## Predeclared questions and candidates
C1: Is tr(K) invariant on the autonomous full-persistence sector P=I, 0<Y<I, rho_F>0, rho_W positive trace one? Compare the complete source update to the independently derived aligned channel.
C2: Is E_F=tr(rho_F K) conserved? Test the exact two-dimensional example Y=diag(1/4,1/2), rho_F=[[1,1/2],[1/2,1]], K=sigma_x, rho_W=I/2. Compare to Y=(3/8)I for scalar-readout fiber closure, holding all other inputs fixed.
C3: Does tr(K) remain invariant outside that sector? Test n=2, P=diag(1,0), Y=I/2, rho_F=rho_W=P, K=-I. Use the complete update, including the nonempty admissible seed complement.
C4: Which fixed linear K-readouts are conserved for every K in one full-persistence event? Derive the adjoint fixed-space condition, not just examples.
C5: What does scalar contraction imply about continuous first integrals depending only on scalar y, with other scalar-branch constants fixed?
C6: Can an injective pullback/congruence of positive G supply Lorentz signature? Can an internal natural rank-one time projector be selected at a fully isotropic state?
C7: Test a BFG-internal alternative: use the real vector space Herm(C^2), determinant quadratic form and positive cone. Distinguish this standard algebraic Lorentz carrier from physical spacetime, dimensional selection and dynamics. Test the actual K channel on a determinant-null input K=I+sigma_x. Null-to-timelike behavior rejects interpreting this channel as a Lorentz/conformal frame transformation, not Lorentz-covariant physics in general.
C8: Compute the scalar-point derivative of the actual Y update at Y=I/2 with rho_F=I, keeping all endogenous weights differentiated. Test a null tangent I+sigma_x in the determinant lift. Do not fit a new metric to make this pass.
C9: Test completeness of action/energy claims: a telescoping reservoir and a multiplier action that encode an arbitrary update are additional constructions, not source-selected physical energy or a Noether stress law.

## Evidence and predeclared bounds
Exact symbolic proofs and rational/algebraic two-by-two witnesses are primary. Use Python fractions/SymPy for independent exact certificate calculations.
Use the existing complete complex update for numerical cross-checks, not a substituted scalar map.
Numerical seed 20261023; 32 complex full-persistence preparations, 8 each in dimensions 2,3,4,5. Require normalized matrix/trace residuals <=1e-10. Add 12 simultaneous unitary-gauge controls, 16 positive-matrix cone controls, four dimensions including 2 and 3 for internal-metric checks, and exact counterexamples C2/C3/C7.
Derivative comparison: central differences h=1e-4,1e-5,1e-6; require best norm error <1e-7 and record all errors. Finite differences corroborate the analytic derivative only.
Expected nonzero defects require lower bounds derived from the exact witnesses, not tolerance-tuned after execution.
Import the existing audit only for source checks; make no empirical or full-suite pass claim. Check source blob SHA before execution. Record runtime versions and SHA256s; avoid machine-identifying environment fields.
A failed control remains a failure and triggers analysis, not coefficient fitting.

## Completion outputs
DERIVATION.md: explicit propositions, proofs, assumptions, counterexamples and boundaries.
audit.py + test_audit.py + results.json: fresh reproducible checks and failures if any.
STATUS.md + README.md: question-to-evidence ledger, exact remaining dependency, and reproduction instructions.
A completed first round is a checked research result with open gates, not a completed physical Einstein derivation.

## Pre-execution source-algebra amendment and additional exact balance check
Before new audit execution, direct rank analysis corrected the original C3 seed expectation: P=diag(1,0), Y=I/2 has analysis rank one and no seed complement. Keep that rank-drop witness. Add C3b: v=(sqrt(3)/2,1/2), P=vv^dagger, F=W=P, Y=diag(1/4,1/2), K=diag(-1,-2); analysis rank two and a one-dimensional negative seed complement. Both are documented in DERIVATION.md.
After the first control run passed, extend the investigation (C10) to the exact complete-event trace defect: with U_C,U_B the two blocks of the actual analysis isometry, D=U_C U_C^dagger+U_B U_B^dagger, test tr K_+-tr K=tr[K(D-I)]. Use 24 predeclared random partial-carrier cases (6 each at n=2,3,4,5), K negative definite with nondegenerate compressed eigenvalues, mixed Y in (.15,.8), F,W supported on P. Record terminal cases rather than dropping them; require all nonterminal residuals <1e-10 and report the number. A telescoping signed history ledger follows algebraically; do not call it a positive physical reservoir or local stress.




Runde 24: [Vorabprotokoll für unteres Paar-Gedächtnis](LOWER_PAIR_MEMORY_PROTOCOL.md). Auswertung und Prüfkorrektur sind in LOWER_PAIR_MEMORY_DERIVATION.md festgehalten.


Runde 25: [Vorabprotokoll für den unteren positive-s-Lift](LOWER_PAIR_LIFT_PROTOCOL.md). Exaktes rationales Zertifikat, vier 500-stellige Quellpräfixe ohne Randersetzung, zehn Original-Quellaufrufe; Reichweite in LOWER_PAIR_LIFT_DERIVATION.md.


Runde 26: [Vorabprotokoll zur Formationsrobustheit](LOWER_PAIR_FORMATION_PROTOCOL.md), mit unabhängigem rho-Zertifikat, signed Gegenbeispiel und 14 frischen Original-Quellaufrufen.


Runde 27: [Vorabprotokoll für signed Formation](LOWER_PAIR_SIGNED_PROTOCOL.md), exakter Zweiniveauvergleich, vier hochpräzise positive-s-Präfixe und acht frische Original-Quellaufrufe.


Runde 28: [Vorabprotokoll für beidseitige Aufspaltung](TWO_SIDED_PAIR_PROTOCOL.md), rationales rho-Zertifikat, explizite Stoppregel, exakter Austrittszeuge und zehn frische Original-Quellaufrufe.


Runde 29: [Spektrallücken-Vorabprotokoll](SPECTRAL_GAP_PROTOCOL.md), vorab benannte positive Gegenfamilie, exakte Grenzwerte und sechs Original-Quellaufrufe.


Runde 30: [Vorabprotokoll zur formationsabhängigen Schranke](FORMATION_BOUND_PROTOCOL.md), exakte Identität/Grenzverträglichkeit und neun frische Original-Quellaufrufe.


Runde 31: [Teleskop-Vorabprotokoll](TELESCOPING_MEMORY_PROTOCOL.md), quantitative Sekantenabnahme, sechs hochpräzise positive Präfixe und neun Original-Quellaufrufe.


Runde 32: [Selektorstabilitäts-Vorabprotokoll](SELECTOR_STABILITY_PROTOCOL.md), Sylvesterbeweis, sechs Störungskontrollen und acht frische Original-Quellaufrufe.


Runde 33: [Vorabprotokoll zur F-/W-Auswahlambiguität](TIE_AMBIGUITY_PROTOCOL.md), exakte skalare Quell-/Projektoridentitäten und sechs Original-Quellaufrufe.


Runde 34: [Paarfamilien-Vorabprotokoll](PAIR_FAMILY_PROTOCOL.md), exakte lineare Ränge/Nullräume, positive Faser und acht Original-Quellaufrufe.


Runde 35: [Vorabprotokoll zur nichtskalaren Paar-Geschlossenheit](PAIR_CLOSURE_PROTOCOL.md), exaktes Kanal-Gegenbeispiel, native Rangergänzung und acht Original-Quellaufrufe.


Runde 36: [Vorabprotokoll zur Überlappungsbilanz](OVERLAP_BALANCE_PROTOCOL.md), allgemeiner Hermitescher Strombeweis, exakte Cover und acht Original-Quellaufrufe.


Runde 37: [Vorabprotokoll zur wechselnden Überdeckung](MOVING_COVER_PROTOCOL.md), exakte Zuordnungs-/Kreuztermidentitäten, reiner Rotationszeuge und neun Original-Quellaufrufe.


Runde 38: [Vorabprotokoll zur lokalen Rangereignisbilanz](RANK_LOCAL_BALANCE_PROTOCOL.md), exakter Seed-/Dimensionszeuge, aktive/ambiente Rückzüge und zehn Original-Quellaufrufe.


## Runde 39 – Vorabprotokoll: physikalische Bestandsidentifikation

Ausdrücklicher Nutzerauftrag: vorhandene BFG-Bestände auf physikalische Energie/Impuls prüfen. Ausgangs-Head 8189830b17da41e193b1caeb7f64cc16e1d5abc3. Quellenbindung unverändert.

Vor Auswertung festgelegte Hypothesen und Kriterien:
1. Die direkte Gleichsetzung von K-/Formationsbeständen mit Energie/Impuls muss die Typisierung und Messbrücken aus I41, I55–56, I68.2, I70.1–6 und II86 erfüllen; die bloße Erhaltung einer Spur genügt nicht. Quellenstellen und konkrete Kandidaten getrennt bilanzieren.
2. Prüfe positive gemeinsame Skalierung S_lambda:(K,F,W,Y,P)->(lambda K,lambda F,W,Y,P). Erwartung: Lasten skalieren, alpha und Analyse bleiben gleich; auch ein eindeutiger Seed skaliert, so dass U_BFG S_lambda=S_lambda U_BFG auf nichtterminalen Strata gilt. Gegenkriterium: ein nichtlinearer Skalendefekt oder veränderte Seed-/Terminalentscheidung. Diese Homogenität wäre eine Kalibrierungsfreiheit, kein allgemeines Energie-No-Go.
3. Frische proportionale Kontrolle: zwei originale Quellzustände (volle Persistenz und der bereits exakt belegte Rang-/Seedzeuge), jeweils lambda=1 und 3.7; vergleiche alle fünf Ausgangsfelder und Terminalstatus. Keine Wiederholung aller 38 Audits.
4. Prüfe, welche zusätzlichen Voraussetzungen ein Energieoperator oder Viererstrom benötigt: kalibrierte M_E, Raum-/Uhrabbildung, Symmetrien/Generatoren, geschlossene Dynamik und Auswahl-/Seedbilanz; keine davon nachträglich auf Einstein fitten.

Ergebnisformat: eigener Quellen-/Kandidatenbericht mit Beweis und frischer Kontrollausgabe. Dokumentationsrunde ohne Änderungen an Prüfcode, Workflow oder Quelldynamik; CI des bestehenden Codes bleibt separat ausgewiesen.
