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

Vor zusätzlicher Kandidatenauswertung: Weil K und F dieselbe Formationseinheit tragen und der bekannte Seedzeuge Delta tr(PK)=-9/4, Delta tr F=9/4 hat, prüfe auch E_act=tr(PK)+tr F und E_amb=tr K+tr F als natürliche ungewichtete Gesamtbestände. Drei neue feste synthetische nichtterminale Teilträgerfälle n=3,4,5, Zufallsseed20261024; keine Parameteranpassung. Ein robuster von null verschiedener Defekt widerlegt universelle Erhaltung dieses Kandidaten, nicht mögliche andere physikalische Brücken. Die zufällige Kompensation im bisherigen Einzelzeugen wird ausdrücklich nicht als allgemeines Gesetz übernommen.

Auswertung Runde39 abgeschlossen: Quellen-/Kandidatenbericht und vollständiger n=4-Numerikzeuge in PHYSICAL_IDENTIFICATION*.md. Hypothesen und additive Kandidaten vor ihren jeweiligen Kontrollen veröffentlicht. Sieben unterschiedliche frische Quellaufrufe; zusätzliche reine Fixture-Erfassungswiederholungen getrennt. Lokale numerische Befunde und exakte Beweise ausdrücklich getrennt. Dokumentationsrunde ohne Code-/Workflowänderung.


## Runde 40 – vorab: zertifizierter kombinierter Bestandsrest

Ausgangspunkt Runde39: E_act=tr(PK)+tr F hat exakten Defekt tr K(B4-P)-ell_F, bisher mit numerischen Gegenkontrollen. Ziel: einfacher rationaler zulässiger Zustand und zertifizierter nichtverschwindender Rest statt bloßer Gleitkommazahl. Kandidat vor Auswertung: n=3, P=diag(1,1,0), F=diag(1,21/50,0), W=P/2, K=-diag(1,2,3), Y=[[1/4,0,1/10],[0,1/2,1/10],[1/10,1/10,1/2]]. Erwartete alpha=1/10. Prüfe Positivität, Analyse-Rang, nichtterminale eindeutige Seedentscheidung, exakte Seed-Kompensation. Zertifiziere B4 über eine rationale Näherung Q an (A0†A0)^(-1/2), A0=sqrt(10)A; Fehler durch exakte Residuen und positive Sylvester-Abschätzung begrenzen. Falls Restintervall0 enthält, Ergebnis offen behalten. Frische Originalkontrolle dieses Zustands und einer unitären Eichversion. Keine physikalische Energiebrücke daraus behaupten. Dokumentations-/Zertifikatsrunde ohne Produktions-/Auditcodeänderung; ausführbare Reproduktionsrechnung kann als Markdown dokumentiert werden.

Auswertung Runde40: ACTIVE_STOCK_DEFECT.md und ACTIVE_STOCK_CERTIFICATE.md mit rationalem Ausschluss von Defekt0, dokumentierter Korrektur des symbolischen Lastterms und zwei finalen Originalkontrollen (plus einem vorangehenden explorativen Aufruf). Keine Quell-/Audit-/Workflowänderung. Die früheren n=4/5-Zufallsfälle werden nicht rückwirkend exakt zertifiziert; neuer einfacher Zeuge.


## Runde41 – vorab: zulässige lineare Bestandskombinationen und erhaltene Teilklassen

Ziel: Den Runde40-Gegenzeugen weder überverallgemeinern noch durch nachträgliches Gewichten reparieren. Auf Q_selection=I, Formation/Witness unterstützt auf P, Rang r, nichtterminalen Ereignissen prüfe B4>=0, supp B4<=P, tr B4=r und B4<=2P. Erwartung: X=B4-P ist spurfrei auf P, Rang1 erzwingt X=0, skalares PKP erzwingt Delta E_act=0; reduzierender P-Y-Sektor ebenfalls. Außerhalb dieser Bedingungen bleibt signierter kohärenz-/anisotropieabhängiger Rest.

Kandidatenklasse vor Auswertung: E_{a,b}=a tr(PK)+b tr F mit festen reellen zustands-/ereignisunabhängigen Koeffizienten. Verwende den exakten Rang1-Zeugen aus Runde38 (Delta A=-9/4,Delta F=9/4) und den zertifizierten Rang2-Zeugen aus Runde40, um zu entscheiden, ob irgendeine nichttriviale Wahl universelle Erhaltung erreicht. Keine neuen versteckten Reserven oder nachträglich zustandsabhängigen Gewichte.

Frische Kontrollen: Rang1-Zeuge; Runde40-Geometrie mit K=-diag(1,2,3), vertauschten ersten beiden K-Eigenwerten und K=-I. Vier Originalaufrufe; Geometrie/Lasten vorab identisch, keine Parametersuche. Prüfe X-Eigengrenzen, Spur und Vorzeichenumkehr/Skalarerhaltung sowie getrennte aktive und Formationsdefekte. Exakte Klassenbeweise und Quellenkontrollen dokumentieren; keine physikalische Energie-No-Go-Aussage außerhalb dieser linearen Klasse. Dokumentationsrunde ohne Quell-/Audit-/Workflowänderung.

Auswertung Runde41: LINEAR_STOCK_LIMIT.md und LINEAR_STOCK_CHECKS.md. Exakte Zwei-Zeugen-Elimination aller nichttrivialen festen Gewichte, positiver/stützter/spurfreier Rest mit Schranke, hinreichende erhaltene Teilklassen sowie exakte Vorzeichenumkehr am gleichen Kanal. Vier Originalkontrollen bestanden. Physikalische Energieabbildungen außerhalb der festen linearen Klasse ausdrücklich nicht ausgeschlossen. Keine Quell-/Audit-/Workflowänderung.


## Runde42 – vorab: genügen Seed-/Rangdaten als Zusatz zur skalaren Bilanz?

Konstruktiver Test auf der rationalen n=3-Geometrie aus Runde40. Eingangs-P,F,W,Y fest, Analyse-Rang3 und Seedkomplement1. Definiere D=sum U_r U_r†=sum A0_r H^(-1) A0_r† (rational), X=B4-P, Z0=D-(3/2)P, Z=Bseed-P/2=Z0-X. Im realen 2x2-Aktivblock schreibe Z=[[z1,z2],[z2,-z1]] und setze L=[[z2,-z1],[-z1,-z2]], außerhalb P0. Kandidaten K±=-2I±L. Erwartung: gleiche ambiente/aktive Eingangsspur, gleiche volle F/W/Y/P, gleiche Rangdaten und gleicher Seedwert-2, aber verschiedene aktive Ausgangsbestände, falls Wedge w=X11 Z0_12-X12 Z0_11 !=0. Denn tr L=tr(L Bseed)=0, tr(LX)=2w.

Zertifiziere w!=0 mit rationalem D und dem bereits unabhängig nachprüfbaren inversen-Gramwurzel-Zertifikatsverfahren aus Runde40, inklusive rationaler Fehlerübertragung. Numerische Näherungen zur Konstruktion allein zählen nicht als exakter Faserzeuge. Zeige K±<0 durch ||L||<=1/2. Frische Originalkontrollen beider Zustände (zwei Aufrufe), prüfe gleiche Seed-/Formationszuwächse und alle nicht-K-Felder, verschiedene Ausgangsspuren sowie prognostizierten Defekt±2w. Wenn w0 oder Zertifikat unentschieden, Ergebnis offen behalten. Quellenbindung, keine neue physikalische Reserve und keine nachträglichen Gewichte. Dokumentations-/Zertifikatsrunde ohne Audit-/Workflow-/Quellcodeänderung.

Auswertung Runde42: SEED_STOCK_CLOSURE.md und SEED_STOCK_CERTIFICATE.md. Neuer exakt definierter algebraischer Kernelpaar-Zeuge; rationales Wedge-Zertifikat schließt0 aus. Gleicher Seedwert-2 und gleiche Nicht-Kernel-Folgefelder folgen exakt, zwei frische Originalkontrollen bestätigen. Die ausgeschlossene Korrekturklasse ist K-blinde additive Zustandsfunktion bzw. direkte Gegenbuchung aus aktuellem Seed-/Rangdatum, keine allgemeine Energiebrücke. Dokumentation ohne Code-/Workflowänderung.


## Runde43 – vorab: konstruktive aktive Kernelreduktion

Auf der BFG-intern nach einem nichtterminalen Ereignis geltenden Klasse Q_selection=I, F/W unterstützt auf P prüfe Pi_act=(PKP,F,W,Y,P). Erwartung: Alle Analyseblöcke erfüllen P U_t=U_t, weshalb kompletter K_+ und Seed ausschließlich von PKP abhängen; K außerhalb/zwischen dem aktiven Träger ist für das nächste vollständige Ereignis unsichtbar. Keine Behauptung für einen initialen echten Q!=I-Auswahlschritt.

Zusätzlich prüfe bei festem Nicht-Kernel-Zustand die Injektivität k=PKP -> K_+. Mit Yp=Y|P-Kompression, Hp=I_P+Yp und Z=P V Sigma K_+ Sigma V† P lautet Kandidat Hp Z Hp=alpha k+beta Yp k Yp. In einer Yp-Eigenbasis sind die Multiplikatoren alpha+beta mu_i mu_j positiv; dies soll eine explizite lineare Rekonstruktion liefern. Prüfe Unitalität I_P->I_m und Rang r² der vollständigen K-Ausgabe, ohne vier K-Komponenten mit vier physikalischen Raumzeitdimensionen gleichzusetzen.

Frische Kontrollen: rationale n=3/r=2-Geometrie aus Runde40 mit zwei K, die sich ausschließlich in P-Kreuz-/Komplementblöcken unterscheiden (zwei Originalaufrufe), plus ein fest generierter komplexer n=4/r=2-Fall, Seed20261026 (ein Originalaufruf). Vergleiche volle Nachfolger/Terminalstatus, Rekonstruktion, Unitalität und reellen Rang4; Toleranz1e-10. Terminalfälle dokumentieren, keine Nachfolger erfinden. Exakter allgemeiner Beweis getrennt von numerischer Kontrolle. Dokumentationsrunde ohne Quell-/Audit-/Workflowänderung.

Auswertung Runde43: ACTIVE_KERNEL_QUOTIENT.md und ACTIVE_KERNEL_CHECKS.md. Exakte Faser-Geschlossenheit der aktiven Matrixreduktion unter Q=I, explizite Inversion und Unitalität/Rang r² bewiesen. Drei vorab festgelegte Originalereignisse alle nichtterminal und Prüfassertionen bestanden. Die Aussage betrifft vollständiges K_+ bei voller behaltenen Nicht-Kernel-Struktur, nicht nur aktive Ausgangskompression oder physikalischen Viererimpuls. Dokumentation ohne Code-/Workflowänderung.


## Runde44 – vorab: ausgewählter Kernelblock bei echter Anfangsselektion

Prüfe allgemeine ereignisbezogene Reduktion Pi_sel=(Psel K Psel,F,W,Y,P), Psel=Tsel Tsel† aus der unveränderten Quelle. Erwartung: Psel U_t=U_t, daher vollständiger K-Nachfolger/Seed durch diesen Block bestimmt; Rekonstruktion aus Runde43 mit Psel statt P überträgt sich bei festem ausgewähltem Rang. Frühe Terminalfälle bleiben K-unabhängig bzw. werden mit Status behandelt. Keine pauschale Reduktion auf ursprüngliches PKP bei Q!=I.

Exakter vorab benannter Gegenzeuge für ursprüngliches PKP: n=2,Y=diag(1/2,2),v=(1,1)/sqrt2,P=F=W=vv†,K±=-2I±diag(1,-1). Gleiche ursprüngliche aktive Kompression und ambiente Spur, aber erwartete ausgewählte Kompressionen-1/-3; vollständige Originalereignisse sollen dies entscheiden. Alpha-Kandidat1/5, Ausgangslast8/45, kein Seed bei m=1.

Frische Kontrollen: diese zwei Fälle; dieselbe Geometrie K=-2I und K+H mit H=[[0,.2],[.2,.4]], ausgewählter H-Block0, zur vollen Nachfolgergleichheit (zwei weitere Aufrufe); ein komplexer n=4/r=2-Fall, Seed20261027,Y=diag(.2,.4,.7,1.4), für ausgewählte Rekonstruktion und Unitalität (ein Aufruf). Insgesamt5, keine Parametersuche; Terminalfälle nicht wegfiltern. Toleranz1e-10. Exakte Quelle/Beweis und lokale Kontrollzahlen dokumentieren, keine neue physikalische Brücke. Dokumentation ohne Audit-/Workflow-/Quellcodeänderung.

Auswertung Runde44: SELECTED_KERNEL_QUOTIENT.md und SELECTED_KERNEL_CHECKS.md. Exakter ausgewählter Quotient einschließlich früher/Seed-Terminalfälle, Rekonstruktion auf positiv geladenen Analysezweigen und exakter ursprünglicher-PKP-Gegenzeuge. Fünf Originalaufrufe alle nichtterminal; keine alternativen K-Transportregeln eingeführt. Dokumentationsrunde ohne Audit-/Workflow-/Quellcodeänderung.


## Runde45 – vorab: Leckagerang, Seedrang und endliche Trägerfüllung

Prüfe exakte Formel m=r+ell mit r=rank P_sel und ell=rank[(I-P_sel)Y P_sel], aus Ran A†=Ran P_sel+Y Ran P_sel. R4 hat Rang r; nichtterminaler aktiver Ausgangsrang ist r bei ell0 und r+1 bei ell>0 (genau ein Seed). Also d_out=m-r_out=max(ell-1,0). Nach dem ersten nichtterminalen Ereignis gilt Q=I, ell<=d_in=n-r und damit d_out<=max(d_in-1,0). Prüfe Folgerung: ausgewählter Rang2 erreicht bei nichtterminaler Fortsetzung spätestens nach zwei vollständigen Ereignissen P=I; allgemein spätestens nach r_sel Ereignissen vom positiv geladenen ersten Analysezweig aus. Bei Terminalität endet die Aussage ohne erfundenen Nachfolger.

Vorab Kontrollen: exakte rationale Blockrankbeispiele ell=0,1,2,3; Originalquelle an reduzierendem n4/r2-Fall (1 Ereignis), rationalem n3/r2-Runde40-Fall (1), generischem komplexem n4/r2-Fall (max2) und n6/r3-Fall (max3), Zufallsseed20261028 in dieser Reihenfolge der generischen Fälle. Insgesamt höchstens7 Originalaufrufe, alle Terminalfälle dokumentieren. Prüfe m, r_out, d-Abnahme und tatsächliche P=I-Füllung; keine Aussage über physikalische Zeit, kein künstliches Fortsetzen numerisch terminaler Fälle. Behalte Zahlen-/Ranktoleranzgrenzen. Dokumentation ohne Audit-/Workflow-/Quellcodeänderung.

Auswertung Runde45: CARRIER_FILLING.md und CARRIER_FILLING_CHECKS.md. Exakter Rang-/Defizitbeweis einschließlich terminaler Grenze; vier rationale Blockrankprüfungen und alle sieben vorab vorgesehenen Originalereignisse nichtterminal/bestanden. Rang2-/Rang3-Folgen füllen den verbleibenden Träger in2/3 Ereignissen. Keine physikalische Zeit-/Raumbehauptung und keine zusätzliche lokale Selektorregel. Dokumentation ohne Code-/Workflowänderung.


## Runde46 – vorab: Energieerwartung der manuskriptinternen Quantenkandidaten

Physikalische Identifikation ausdrücklich nur als Hypothese: rho_Q=W oder rho_Q=F/tr F (I57/I68/I70), H=epsilon_E K+E0 I mit unabhängig festzulegender Einheit/Nullpunkt. Prüfe im vollen Persistenzsektor, wo W,F im ausgerichteten Quellrahmen konstant sind, E_rho=tr(rho K) statt nur tr K. Erwartung: Delta E_rho=tr[(Phi(rho)-rho)K]; Erhaltung für jedes K genau dann, wenn [rho,Y]=0. Dies wäre eine bedingte Kandidatengrenze, kein No-Go für offene physikalische Systeme oder andere Brücken.

Vorab exakter Zeuge P=I2,Y=diag(1/5,3/10),F=I2,W=(I+sigma_x/2)/2,K±=2I±sigma_x. Erwartet alpha8/133 und Kohärenzfaktor h=31/sqrt(1001)<1, beide K positiv. Vergleiche E_W und E_F/trF; feste Einheit/Nullpunkt dürfen den Defekt nicht wegkalibrieren. Zusatzkontrolle W=I/2 sowie komplexe unitäre Eichversion des Plus-Falls, Seed20261029. Insgesamt4 Originalaufrufe; exakte symbolische Defekt-/Kommutantenrechnung getrennt von numerischen Kontrollen. Keine neuen quantenphysikalischen Gesetze importieren, keine erfundene Reservoirenergie. Dokumentation ohne Audit-/Workflow-/Quellcodeänderung.

Auswertung Runde46: QUANTUM_ENERGY_READOUT.md und QUANTUM_ENERGY_CHECKS.md. Quellenstellen I57/I68.2/I70 nachgelesen; exakte Erwartungsbilanz/Kommutantenbedingung und positiver n2-Zeuge, vier Originalereignisse bestanden. Offene/angetriebene physikalische Energieoperatoren und andere Brücken nicht ausgeschlossen. Kein Reservoir erfunden; bedingter relativer Spektraltest setzt unabhängige Präparation/Brücke voraus. Dokumentation ohne Code-/Workflowänderung.


## Runde47 – vorab: kann das vollständige C/B-Kanalregister den Energieerwartungsrest tragen?

Prüfe im vollen Persistenzsektor die kanonische mathematische Isometrie V=sum_a |a> tensor T_a des hergeleiteten Hermiteschen K-Kanals. Dies ist eine Darstellung, kein bereits physikalischer BFG-Umweltzustand; tatsächliches W_+=W nicht durch Phi(W) ersetzen. Registerzustand Gamma(W)_ab=tr(T_a W T_b). Erwartung: Gamma hängt nur von W-Diagonalblöcken in Y-Eigenräumen ab, weil alle T_a Funktionen von Y sind. Beliebige registerlokale Hermitesche Energie R zieht sich zu sum R_ab T_a T_b zurück und kommutiert mit Y. Teste damit additives Operatorbilanz-Schema K+e0 I=Phi(K)+V†(R tensor I)V; außerhalb [K,Y]=0 erwartetes Offdiagonalhindernis.

Exakte Zeugen wie Runde46: F=I,Y=diag(1/5,3/10),K=2I+sigma_j, W±=(I±sigma_j/2)/2 für j=x,y. Beide W je Paar strikt positiv, identisches vollständiges Gamma, erwartete entgegengesetzte Witness-Energiedefekte. Symbolisch TC=diag(sqrt(8/13),sqrt(32/77)),TB=diag(sqrt(5/13),sqrt(45/77)); prüfe Gamma-Gleichheit, unital/isometrisch und Offdiagonalhindernis auch für beliebiges komplex Hermitesches R. Vier Originalaufrufe, Toleranz1e-12, keine Reservoir- oder Wechselwirkungsgleichung ergänzen. Kein Ausschluss allgemeiner System-Register-Wechselwirkungsenergie oder anderer physikalischer Dilatationen. Dokumentation ohne Audit-/Workflow-/Quellcodeänderung.

Auswertung Runde47: CHANNEL_REGISTER_ENERGY.md und CHANNEL_REGISTER_CHECKS.md. Isometrie-/Registergleichheit und allgemeines registerlokales Offdiagonalhindernis exakt bewiesen; vier originale x/y-Kohärenzfälle bestanden. Ein physikalisches Reservoir oder veränderte Witnessdynamik wurde nicht eingeführt. Gekoppelte System-Register-Energie und andere Brücken bleiben außerhalb der ausgeschlossenen additiven Kandidatenklasse. Dokumentation ohne Code-/Workflowänderung.


## Runde48 – vorab: positive Zustandskompensation bei H proportional K

Untersuche als Alternative zur ausgeschlossenen additiven Registerenergie eine veränderte physikalische Zustandsablesung rho_out, ohne die tatsächliche Quellregel W_out=W zu ändern. Im vollen Persistenzsektor soll tr[rho_out Phi(K)]=tr[rho K] für jedes K bei festem Y,F gelten. Erwartung: Selbstadjungiertheit/Injektivität erzwingen rho_out=Phi^(-1)(rho), und diese inverse Schurabbildung ist bei h<1 nicht positiv auf allen Dichten. Grenze: einzelne gemischte Zustände können zulässig bleiben; keine allgemeine physikalische Brücke oder offene Systeme ausschließen.

Exakter Zeuge wie Runde46, Y=diag(1/5,3/10),F=I,h31/sqrt(1001). Dichten rho_r=(I+r sigma_x)/2 mit r=1,99/100,1/2 und positive K=2I+sigma_x. Prüfe inverse Eigenwerte(1±r/h)/2 und Spektralbedingung: Eingangserwartung2+r liegt für r>h über dem maximalen Ausgangseigenwert2+h. Dann ist selbst für diesen einzelnen K keine positive Spur-eins-Ausgangsdichte energieerhaltend möglich. Symbolisch r=99/100>h durch rationalen Quadratvergleich, nicht numerisches Runden. Komplexe Eichkontrolle des r=.99-Falls, Seed20261030; insgesamt4 Originalaufrufe. Quelle/Alternativhypothese getrennt, kein neues W-Update, kein Reservoir erfinden. Dokumentation ohne Audit-/Workflow-/Quellcodeänderung.

Auswertung Runde48: ENERGY_STATE_POSITIVITY.md und ENERGY_STATE_CHECKS.md. Inverse-Zustandsbedingung/Positivitätsgrenze und stärkeres Einzel-K-Spektralhindernis exakt bewiesen; vier Originalereignisse bestanden. W-Quellupdate unverändert, keine neue Zustandsdynamik oder Reservoirenergie eingeführt; r=.5-Einzelkompensation ausdrücklich positiv erhalten. Dokumentation ohne Code-/Workflowänderung.


## Runde49 – vorab: instantaneous kommutierende Hamiltonian-Kandidaten

Prüfe neue ausdrücklich zusätzliche Energieablesung H_Y=D_Y(K)=sum_lambda P_lambda(Y) K P_lambda(Y), also Projektion auf den aktuellen Y-Kommutanten, statt H=K. Erwartung: Im vollen Persistenzsektor bei unveränderter Y-Spektralpartition gilt D_Yout(Phi K)=D_Y K; bei neuer Eigenwertkollision kann die Projektionsalgebra wachsen und die Erhaltung scheitern. Keine physikalische Auswahl dieses Kandidaten behaupten.

Exakter vorab Zeuge: P=I2,Y=diag(1/5,4/5),F=diag(1,3),K=2I+sigma_x,W=(I+sigma_x/2)/2. Erwartung alpha11/36, g(y1)=g(y2)=25/108, h5/6; dadurch H_Y vorher2I, nachher2I+(5/6)sigma_x. Prüfe dieses Ergebnis exakt, nicht durch Zusammenfassen nur ungefähr gleicher Eigenwerte.

Naheliegende Alternative H_F=D_F K: prüfe F=I+sigma_x/2,Y=diag(1/5,3/10),K=2I+sigma_x,W=(I+sigma_x/2)/2; erwartet unverändertes F-Spektrum, aber H_F folgt der K-Kohärenzdämpfung und ist nicht erhalten. Positive Kontrolle H_Y ohne neue Kollision bei F=I, demselben niedrigeren Y. Komplexe Eichkontrolle des Kollisionszeugen, Seed20261031. Insgesamt4 Originalaufrufe, Toleranz1e-12; dokumentiere eine exakt fixierte Kollisionspartition gegenüber numerischen Cluster-Toleranzen. Historische Spektralprojektoren als zusätzliche retained data, nicht nachträglich als Quellgesetz einsetzen. Dokumentation ohne Audit-/Workflow-/Quellcodeänderung.

Auswertung Runde49: COMMUTING_ENERGY_READOUT.md und COMMUTING_READOUT_CHECKS.md. Exakte rationale Quellkollision25/108 bei alpha11/36,h5/6 und Energieerwartungsänderung5/12; kollisionsfreie positive Teilklasse und H_F-Gegenfall dokumentiert. Vier Originalaufrufe bestanden. Numerische Nähe dient nicht als Kollisionsbeweis; historische Projektoren ausdrücklich zusätzliche retained data. Dokumentation ohne Code-/Workflowänderung.


## Runde50 – vorab: Klassifikation kontinuierlicher K-allein-Energieoperatoren

Prüfe zusätzliche Kandidatenklasse H:Herm_+(C²)->Herm(C²), ausschließlich von K abhängig, unitär kovariant H(UKU†)=U H(K) U† und kontinuierlich auch bei K=tI. Forderung universeller isolierter Erwartungserhaltung bei rho_Q=W für alle vollen Persistenzzustände/W impliziert im ausgerichteten Quellrahmen H(Phi_Y,F(K))=H(K). Ziel: Entscheide, ob nur H(K)=g(tr K/2)I möglich ist; keine Aussage über H(K,Y,F,W,history), eingeschränkte physikalische Präparationen oder offene Austauschsysteme.

Beweisplan vor Auswertung: Kovarianz erzwingt [H(K),K]=0. Ein BFG-Kanal mit schräger Y-Achse soll [K,Phi(K)]!=0 ergeben; gleiches H müsste dann mit zwei nichtkommutierenden qubit-Matrizen kommutieren und skalar sein. Transversale Kontraktion r->h r bei festem Spurmittel t und Kontinuität r->0 sollen verbleibende Kontrastabhängigkeit entfernen. Die dabei iterierte Funktionsgleichung ist eine Konsequenz der Forderung für alle Zustände, keine Behauptung eines eingefrorenen Y entlang einer tatsächlichen Quellbahn.

Kontrollen: F=I,Y=U diag(1/5,3/10) U† mit U reale Rotation pi/8,K=2I+sigma_z; erwartete Ausgabe2I+[(1-h)/2]sigma_x+[(1+h)/2]sigma_z, h31/sqrt1001. Symbolisch gemeinsamer Kommutant nur skalare I. Zweiter Originalfall transversales K=2I+sigma_x bei diagonalem Y; dritter komplexe Eichversion des schrägen Falls, Seed20261101. Insgesamt3 Originalaufrufe; prüfe illustrative H=K,K² und normierten traceless-Anteil, sowie positive skalare H=tr(K)I. Keine Operatorumdefinition in der Quelldynamik. Dokumentation ohne Audit-/Workflow-/Quellcodeänderung.

Auswertung Runde50: K_ONLY_ENERGY_CLASSIFICATION.md und K_ONLY_ENERGY_CHECKS.md. Klassifikation H=g(trK/2)I unter vorab genannten Voraussetzungen bewiesen; drei Originalereignisse bestanden. Ein initialer algebraischer Solverfehler vor Originalaufrufen wurde durch zweistufige exakte Kommutatorenrechnung ersetzt und dokumentiert; Quelle unverändert. Keine eingefrorene physikalische Y-Bahn aus der Funktionsgleichung abgeleitet. Dokumentation ohne Code-/Workflowänderung.


## Runde51 – vorab: Witness-Formationspaarung durch Seed-/Rangereignisse

Prüfe direkten Hamiltoniankandidaten H=epsilon_F F+E0 I mit rho_Q=W, ausdrücklich zusätzliche physikalische Identifikation. Mathematischer Kandidat E_WF=tr(WF). Erwartung: R4 transportiert W,F gemeinsam isometrisch; Seedformation liegt im Orthogonalkomplement des Witness. Daher E_WF bleibt bei Q=I und unterstützt eingehendem W/F auch durch echte nichtterminale Seed-/Rangereignisse erhalten. Prüfe stärker tr(W F^p),p=1,2,3 und die zugehörige Witness-gewichtete Formationsspektralverteilung. Keine Energieeinheit, Zeitgeneratorrolle oder vollständige physikalische Bilanz daraus behaupten.

Allgemeine Selektionsgrenze vorab: S=Tsel†Tsel,m=tr(SW)>0, E_out=tr(S W S F)/m. Echte Rangverlustselektion kann daher E ändern. Exakter Gegenfall P=I2,Y=diag(1/2,2),F=diag(1,3),W=I/2,K=-I: erwartet m1/2 und E2->1. Alternative positive Ablesung H2=(trF)W liefert bei verlustfreier Selektion Delta E2=s_seed tr(W²), während H1=F erhalten bleibt. Alternative rho_Q=F/trF,H=F separat prüfen, nicht mit Witnesspaarung gleichsetzen.

Originalkontrollen vorab: rationaler n3/r2-Seedzeuge aus Runde40 (1), Rangverlustselektion oben (1), voller n2-Fall F=diag(1,3),W=(I+sigma_x/2)/2,Y=diag(1/5,3/10),K=2I+sigma_z (1), komplexer n4/r2-Fall Seed20261102 (1) plus dessen unitäre Eichversion (1). Insgesamt5; alle Terminalfälle dokumentieren. Prüfe Moment-/R4-/Seedorthogonalitätsreste, Auswahlformel, natürliche Alternativen und Beispiel nichtäquivalenter erhaltener Operatorablesungen im vollen Sektor. Toleranz1e-10, keine Originaldynamik verändern. Dokumentation ohne Audit-/Workflow-/Quellcodeänderung.
