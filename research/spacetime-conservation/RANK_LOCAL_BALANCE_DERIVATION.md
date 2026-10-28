# Lokale Bilanz bei Auswahl-, Analyse- und Seed-Rangereignissen

## Quelle und Typisierung

Unter erklärten BFG-Annahmen abgeleitet mit Standardmathematik aus demselben gepinnten vollständigen Update. Betrachtet wird ein tatsächlich abgeschlossener nichtterminaler Quellschritt. Sein alter Kernelraum hat Dimension n, der neue Analysenkernelraum Dimension m. Die tatsächliche Analyseisometrie U wird in ihre beiden n-mal-m-Blöcke U_C,U_B zerlegt. Aus der unveränderten Quelle folgt

K_+=U_C^dagger K U_C+U_B^dagger K U_B.

Dies gilt auch, wenn m!=n oder der aktive Träger P seinen Rang ändert. Der Seed-Schritt ergänzt im geprüften Originalupdate F_+ und P_+, nicht nachträglich die schon berechnete Kernelmatrix K_+. Sein Einfluss auf aktive Effekte und spätere Ereignisse darf trotzdem nicht weggelassen werden.

Ein allgemeiner Kernelfehlbetrag der ganzen Raumspur war bereits in Runde 1 bewiesen; er wird hier nicht als neu ausgegeben. Neu geprüft wird seine lokale adjungierte Form für unterschiedliche Räume und die getrennte Bilanz des aktiven Trägers. Terminale Ausgänge besitzen keinen solchen vollständigen Nachfolgezustand und erhalten hier keine erfundenen Nachfolgerladungen.

## Exakter lokaler Rücktransport von Beobachtungen

Für einen positiven Ausgabeffekt Eout_a auf C^m definiere den auf den alten Raum zurückgezogenen Effekt

B_a=U_C Eout_a U_C^dagger+U_B Eout_a U_B^dagger >=0.

Für jeden positiven Eingabeeffekt Ein_a auf C^n liefert Spurdualität exakt

qout_a=tr(Eout_a K_+)=tr(B_a K),
Delta q_a=qout_a-tr(Ein_a K)=tr[K(B_a-Ein_a)].

Dabei sind Labels und Eingabe-/Ausgabeauswertungen explizite Beobachtungszuordnungen; keine gleiche Raumdimension oder Identität der lokalen Flächen wird vorausgesetzt. Auch wenn Effekte aus dem tatsächlichen Nachfolger konstruiert werden, bleibt die Identität richtig. Sie liefert jedoch kein geschlossenes reduziertes Update, wenn diese Effekte oder die Quelle noch den vollständigen Kernel benötigen.

## Ambienter Kernel und aktiver Träger sind verschiedene Bestände

Bei normierten ganzen Raumüberdeckungen sum Ein_a=I_n und sum Eout_a=I_m gilt mit D=U_C U_C^dagger+U_B U_B^dagger

sum Delta q_a=tr[K(D-I_n)].

Dies ist genau die bekannte volle signed Kernelbilanz, jetzt lokal aufgelöst. U^dagger U=I_m impliziert tr D=m, aber nicht D=I_n und auch nicht D<=I_n. Daher ist kein rein antisymmetrischer interner Strom mit verschwindender Gesamtänderung automatisch gegeben.

Beobachtet man dagegen nur die aktiven Träger, sum Ein_a=P und sum Eout_a=P_+, lautet die andere exakte Bilanz

sum Delta qactive_a=tr[K(D_active-P)],
D_active=U_C P_+ U_C^dagger+U_B P_+ U_B^dagger.

Außerhalb voller Persistenz können K und P unterschiedliche Information tragen; die Quelle setzt hier nicht K=PKP voraus. Ambienter Kernelbestand und aktiver Trägerbestand dürfen deshalb nicht als dieselbe Energiegröße behandelt werden. Für negative oder allgemein vorzeichenbehaftete K haben auch diese mathematischen Bestände keine automatische positive-Energie-Interpretation.

## Exakter echter Seed-/Dimensionszeuge

Setze n=3,
Y=diag(1/5,2/5,3/5),
v=(sqrt(3)/2,1/2,0), P=vv^dagger, F=W=P,
K=-diag(2,3,5).

Alle Lasten liegen unter eins; Auswahl erhält zunächst den Rang-eins-Träger. Die beiden Analysezeilen sind, bis auf positive nichtverschwindende Faktoren, durch v^dagger und v^dagger Y bestimmt. Sie sind unabhängig. Die gestapelte Analyse hat daher Rang m=2 und ihre Bildfläche ist P C³ in jedem der beiden Zweige. Folglich U U^dagger=diag(P,P) und exakt D=2P.

Der neue Persistenzträger vor dem Seed hat Rang eins, sein Analysenkomplement Dimension eins. Der komprimierte Kernel dort ist negativ, also liefert die tatsächliche Quellregel einen eindeutigen Seed und P_+=I_2. Es handelt sich um eine echte Änderung der Quelldaten: alter Raum Dimension3/aktiver Rang1, neuer Raum Dimension2/aktiver Rang2, keine bloße manuelle Rotation einer Effektliste.

Die beiden Bestandsänderungen sind exakt

tr K_+-tr K=tr[K(2P-I_3)]=11/2,
tr(P_+K_+)-tr(PK)=tr[K(2P-P)]=-9/4.

Der alte ganze Kernel hat Spur -10, der neue Spur -9/2; der alte aktive Bestand ist -9/4. Außerdem besitzt I_3-D die Eigenwerte (-1,1,1). Dies begrenzt ausdrücklich eine Interpretation als positiver Exportoperator. Der Zeuge bestätigt eine wohldefinierte signed Bilanz, keine positive physikalische Reserve und keine vollständige Energie-Impuls-Erhaltung.

## Frische lokale und Eichkontrollen

RANK_LOCAL_BALANCE_PROTOCOL.md vor Auswertung auf GitHub publiziert. Exakt geprüft: Projektoreigenschaft, Analyserang der strukturellen Zweigzeilen, D=2P-Folgerung, Defektzeichen und beide Spurwerte. Die erste lokale Skriptausführung scheiterte vor jeder Rechnung an einer zusätzlichen schließenden Klammer. Der Syntaxfehler wurde korrigiert; Hypothese und Bereich blieben unverändert, die finale frische Ausführung bestand.

Zehn Original-Quellaufrufe: exakter Zeuge, sechs neue negative-definite komplexe Teilträgerpräparationen n=3,4,5 mit je zwei Fällen und drei simultane komplexe Eichkontrollen. Alle sechs Zufallsfälle waren nichtterminal; terminale Status werden vom Audit ausdrücklich aufgezeichnet und nicht zu Nullresultaten umgedeutet.

Die Ausgabe-Effekte sind einfache Eigenprojektoren des tatsächlichen F_+; Eingabe-Testeffekte sind I_n/m. Für die getrennte aktive Bilanz werden P/m und P_+ Eout_a P_+ verwendet. Diese positiven Effektlisten summieren sich jeweils zu den ausdrücklich benannten ganzen bzw. aktiven Trägeroperatoren. Sie sind nachvollziehbare Prüfauswertungen, keine aus der Quelle eindeutig hergeleitete räumliche Partition. Alle geprüften Ausgabe-F-Eigenwerte waren für die Labels getrennt; eine allgemeine Fortsetzung durch weitere Entartungen wird nicht behauptet.

Normierter lokaler Rest 1.4858424106801035e-16, Eichrest 5.376349109788741e-14, Zeugenrest 1.7763568394002505e-15; vorab Schwelle1e-10. Die Randomfälle enthalten sowohl positive als auch negative Änderungen der ambienten Kernelspur. Ihre Ausgangsdimensionen und aktiven Ränge bleiben einzeln dokumentiert, insbesondere Dimension5->4 bei Rang2->3. Keine Langtrajektorie oder unaufgelöste Rank-Cutoff-Fortsetzung behauptet. CI separat in CI_VALIDATION.md.

Nächste Abhängigkeit: eine quellengestützt physikalische Identifikation von Gesamtbestand, Zuordnung und Transport einschließlich dieser signed Auswahl-/Seed-Terme; eine formale Bilanz allein wählt weder positive Energie noch einen Viererstrom. Räumliche Relation, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen. Die vorherigen festen Persistenz-/Effektbilanzen bleiben korrekte Spezialfälle mit ihren eigenen Voraussetzungen.
