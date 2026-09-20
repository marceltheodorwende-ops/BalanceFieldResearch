> Historische Reviewnotiz. Der aktuelle konsolidierte Stand steht im übergeordneten README; spätere Korrekturen sind dort ausgewiesen.

# Selbstkontrolle der CTC-Gegenprüfung

## Prüfgegenstand

Der neu eingereichte Text enthält die Abschnitte 1–7 meiner vorherigen Gegenprüfung, keine neue reparierte CTC-Konstruktion. Ich habe diese Aussagen erneut algebraisch geprüft und den Stabilitätseinwand direkt mit den V4-Gleichungen 30–36 abgeglichen. Die Gesamtentscheidung „wesentliche Überarbeitung erforderlich“ bleibt bestehen. Die folgenden Präzisierungen begrenzen meine eigenen Aussagen.

## Bestätigte Befunde

1. **Typfehler:** V4 definiert J:H→H⊕H, S=J*J:H→H, E=JJ*:H⊕H→H⊕H. Daher ist J S (A⊕A) S J* in diesen Typen undefiniert. Bereits H=C² ergibt Größen J:4×2, S:2×2 und A⊕A:4×4. Ein abstrakter Isomorphismus H≃H⊕H in unendlicher Dimension würde zusätzliche, ausdrücklich zu wählende Identifikationen erfordern und rettet die angegebenen Formeln nicht automatisch.

2. **Korrekte Kompression:** E(A⊕A)E eingeschränkt auf Ran(E) und J*(A⊕A)J eingeschränkt auf Ran(S) sind über J unitär äquivalent. Unter gemeinsamer Reduktion erhält Restriktion Produkte und Adjungierte, weshalb der bedingte Gram-Satz gilt.

3. **Quadratwurzel:** Für N=[[2,1],[1,2]] und E=diag(1,0) ist die Wurzel der Kompression sqrt(2), während die komprimierte Wurzel (sqrt(3)+1)/2 beträgt. Numerisch 1.41421356 gegenüber 1.36602540. Die allgemeine Vertauschung ist falsch.

4. **Lokale/globalen Flüsse:** Die Lösung von Phi'=Phi² ist Phi(t)=Phi(0)/(1−t Phi(0)). Bei positivem Anfangswert besteht trotz B=0 ein endlicher Blow-up. Das Beispiel betrifft die im CTC-Text verwendete allgemeine Schlussregel, nicht einen Widerlegungsbeweis für die konkrete Engine-Gleichung.

5. **Jordan-Witness:** Für T=[[1,1],[0,1]] bleibt e1 fix, obwohl T^n unbeschränkt wächst. Ein Witness-Test allein ist daher kein Nachweis globaler Potenzbeschränktheit.

6. **Unbeschränkte Graphmetrik:** Auf l² mit ∇e_k=k e_k und c=W=L=I gilt Y e_k=k²e_k und ||e_k||_G²=1+k². Es gibt keine endliche obere Normäquivalenzkonstante zur ursprünglichen Hilbertnorm. Der Graphraum bleibt dennoch ein geeigneter eigener Hilbertraum.

## Stärkerer Stabilitätsgegencheck direkt innerhalb der V4-Neutralformeln

Wähle H=C², Y=diag(0,9), G=diag(1,10), Witnessprojektor P=I und aktuellen Zustand D=(1,1). Dann

    C=diag(1,1/10), B_N=diag(0,9/10),
    Lambda_keep=11/10, Lambda_up=81/10,
    omega_keep=81/92, omega_up=11/92.

Der anhand dieses D festgelegte gestapelte Analyseoperator lautet

    A_D x = sqrt(81/92) Cx ⊕ sqrt(11/92) B_N x.

Für den aktuellen Zustand ist die V4-Paketabschätzung korrekt:

    ||A_D D||_(G⊕G)² = 891/460 ≤ 11/2 = ||D||_G²/2.

Für den anderen Vektor e1 gilt bei denselben festgehaltenen Gewichten jedoch

    ||A_D e1||_(G⊕G)² = 81/92 > 1/2 = ||e1||_G²/2.

Damit ist die allgemeine Operatorungleichung A_D* (G⊕G) A_D ≤ G/2 falsch, obwohl die lokale Paketabschätzung aus V4 gilt. Die Bruchrechnung wurde zusätzlich mit exakter rationaler Arithmetik nachvollzogen.

Dies ist ein Gegenbeispiel zur Ableitung einer universellen Operatorabschätzung aus Gleichung 36. Es behauptet nicht, sämtliche zusätzlichen Formationsgates eines vollständigen CTC-Zustands zu erfüllen. Falls ein gesonderter stabiler Unterraum den verletzenden Vektor ausschließt, muss dieser Raum unabhängig definiert und seine Invarianz bewiesen werden. Das Audit hat diesen Anschluss nicht geliefert.

Umgekehrt widerlegt das Beispiel nicht die Kontraktion des tatsächlich erzeugten zustandsabhängigen Pakets. Ein Beweis entlang der ungestörten tatsächlichen Folge könnte auf genau dieser Paketabschätzung aufbauen, wenn die korrekte neue Metrik, der abschließende Resolventenschritt und alle Folgeschritte kompatibel sind. Das wäre getrennt vom behaupteten linearen Switching-/Inputsatz zu untersuchen.

## Präzisierungen meiner vorherigen Gegenprüfung

- **Reduktion ist hinreichend, nicht generell notwendig.** Wo ich von benötigter Reduktion sämtlicher Faktoren spreche, ist dies die sichere Voraussetzung für den vorgeschlagenen gemeinsamen Beweisweg. Spezielle Produktidentitäten können auch unter schwächeren Bedingungen gelten. Ich habe deren Unmöglichkeit nicht bewiesen.
- **Eine neue primitive Verbindung ist nicht automatisch falsch.** Sie macht das Modell umfangreicher. Ob sie intern abgeleitet werden kann, bleibt eine eigene Frage. Das eindimensionale Beispiel zeigt nur die Möglichkeit verschiedener nicht gaugeäquivalenter Gram-Werte im abstrakten Produktmodell; es ist kein Nachweis zweier vollständiger zulässiger Original-BFG-Welten.
- **Die Operatorbedeutung von D_cov c bleibt zu klären.** Die Quellenformel allein erlaubt keine Entscheidung zwischen Operatorverkettung und induzierter kovarianter Ableitung. Der Typfehler im J-Transport besteht unabhängig von dieser offenen Interpretation.
- **Der unendlichdimensionale lokale Formensatz ist ein positiver Befund.** Für geschlossenes dicht definiertes ∇ und beschränkt invertierbare c,L,W^(1/2) ist T=W^(1/2)∇cL geschlossen und dicht definiert. Aus x_j→x und Tx_j→y folgt nach Anwendung von W^(-1/2), dass ∇cLx_j konvergiert; die Abgeschlossenheit von ∇ liefert Tx=y. Dichtheit folgt durch das Urbild des dichten Definitionsbereichs unter dem beschränkt invertierbaren cL. Dieser Baustein sollte erhalten bleiben.
- **Keine Widerlegung der gesamten BFG.** Die Gegenprüfung zeigt Fehler und fehlende Beweise im eingereichten CTC-Gesamtsatz. Sie zeigt nicht, dass eine korrigierte bedingte Erweiterung unmöglich wäre.

## Ergebnis

Die wichtigsten Einwände bestehen die Selbstkontrolle. Die Behauptung „alle sieben Probleme bedingt geschlossen“ bleibt verfrüht. Der nächste belastbare Schritt ist ein korrekt typisierter beschränkter Transport- und Gram-Satz, gefolgt von einer eigenständigen Analyse der tatsächlich erzeugten Zustandsfolge. Aussagen über beliebige lineare Störungen, Eingänge und unbeschränkte Operatoren sind separat zu beweisen.

Originaldateien und GitHub wurden nicht verändert. Dieser Nachtrag ergänzt die Gegenprüfung, ohne historische Befunde zu überschreiben.
