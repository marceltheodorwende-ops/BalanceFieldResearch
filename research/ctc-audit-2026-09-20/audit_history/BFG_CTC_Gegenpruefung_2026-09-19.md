> Historische Reviewnotiz. Der aktuelle konsolidierte Stand steht im übergeordneten README; spätere Korrekturen sind dort ausgewiesen.

# Gegenprüfung des eingereichten BFG-CTC-Audits

Status: wesentliche Überarbeitung erforderlich. Keine Bestätigung einer Schließung aller sieben Probleme.

## Prüfobjekt und Umfang

Geprüft wurde der vollständig gelesene eingereichte Text „BFG Canonical Transport Completion“ aus dem lokal eingereichten CTC-Entwurf. Der Quellenabgleich erfolgte mit dem bereits extrahierten Text der Unified-V4-PDF vom 12.09.2026, insbesondere S. 6 und 9–11, Gleichungen 17–24 und 37–46. Dies ist eine mathematische Gegenprüfung zentraler Behauptungen, keine erneute vollständige Prüfung aller historischen Quellen. Verweise des Eingabetexts auf eine eigenständige V3-Quelle sind damit nicht verifiziert. V4 verwendet selbst die Bezeichnung einer expanded V3 construction; daraus folgt nicht die Existenz einer bestimmten separaten V3-Datei.

Die Prüfstruktur trennt Quellendefinition, Zusatzannahme, bedingten Satz und offene Behauptung entsprechend den drei Auditdokumenten, deren Anwendung in `dem mathematischen Audit vom 15.09.2026` dokumentiert ist. Originalquellen, Implementierungen und GitHub wurden nicht verändert.

## 1. Blockierender Typfehler im gemeinsamen Transport

Unified V4, Gleichungen 37–39, definiert einen gestapelten Analyseoperator A: H → H⊕H und dessen polaren Anteil J: H → H⊕H. Somit wirken

- S=J*J auf H;
- E=JJ* auf H⊕H;
- A_alt⊕A_alt auf H⊕H.

Das Audit verwendet dagegen wiederholt `J S (A_alt⊕A_alt) S J*`. Diese Komposition ist mit den V4-Typen nicht definiert: S und der verdoppelte Operator wirken auf unterschiedlichen Räumen. Auch die Aussage, J sei von S(H⊕H) aus unitär, verwendet den falschen Initialraum. Der Fehler betrifft die tragenden Konstruktionen in P2, P3, P4, P6 und P7.

Die korrekte V4-Kompression lautet auf H_neu=Ran(E):

    A_neu = E (A_alt⊕A_alt) E | H_neu.

In Supportkoordinaten auf S H lautet sie:

    A_support = J* (A_alt⊕A_alt) J | S H.

Diese beiden Darstellungen sind durch J|SH unitär äquivalent. Sie dürfen nicht zu der im Audit verwendeten dimensionswidrigen Formel vermischt werden.

## 2. Ein reparierbarer, tatsächlich beweisbarer Gram-Satz

Seien a,b,w,l beschränkte Operatoren auf H⊕H, w positiv, und E ein orthogonaler Projektor, der alle vier Operatoren reduziert. Setze a_E=a|EH, entsprechend für die anderen Faktoren. Dann gilt

    (a_E b_E)* w_E (a_E b_E)
      = [(ab)* w (ab)] | EH,

und nach zusätzlichem Einsetzen von l_E gilt dieselbe Aussage für den vollständigen Gram-Ausdruck. Beweis: Reduktion bewirkt, dass Restriktion Produkte und Adjungierte erhält; Einsetzen ergibt die Identität. Positivität folgt aus der Darstellung als T*T.

Für das Audit ist dazu E=JJ* und a=∇⊕∇ usw. einzusetzen, nicht S=J*J an der falschen Stelle. Die Reduktionsvoraussetzung ist zusätzlich. Es wurde nicht gezeigt, dass der tatsächlich durch V4 erzeugte E sie für alle Schritte erfüllt.

Außerdem gilt dieser Beweis zunächst für die Produktinterpretation B_C=∇c. Ob D_cov c in den Quellen eine solche Operatorverkettung oder eine kovariante Ableitung des Operatorfeldes c bezeichnet, muss separat geklärt werden. Beispielsweise ist bei einer induzierten Verbindung auf Endomorphismen D_cov(c) im Allgemeinen nicht dasselbe wie die Komposition ∇∘c. Die Bezeichnung „kovariant“ allein liefert keine Typdefinition.

## 3. Zustandsvervollständigung ist keine interne Auswahlregel

∇,W,L,R als primitive Daten aufzunehmen kann eine unterbestimmte Modellbeschreibung vervollständigen. Das ist ein sinnvoller Modellvorschlag. Es beweist nicht, dass diese Daten aus den bisherigen BFG-Größen folgen, und auch nicht, dass alle ihre Wahlfreiheiten reine Gauge-Freiheiten sind.

Die Identität Y'=UYU* beweist Kovarianz für Daten, die tatsächlich durch dieselbe unitäre Transformation zusammenhängen. Sie beweist nicht, dass beliebige zulässige Verbindungen unitär äquivalent sind. Bereits eindimensional können unter der Produktinterpretation c=W=L=1 und ∇=1 beziehungsweise ∇=2 die unterschiedlichen Gram-Werte 1 beziehungsweise 4 ergeben; unitäre Konjugation identifiziert diese nicht.

Der behauptete Unmöglichkeitsbeweis für den reduzierten Zustand ist deshalb nur bedingt: Er benötigt zwei nach sämtlichen Originalaxiomen zulässige Erweiterungen desselben reduzierten Zustands mit verschiedenen Ergebnissen. Die Schreibweise ∇'=∇+A allein weist deren gemeinsame Zulässigkeit nicht nach.

N_R wird später als ebenfalls zu transportierende primitive Größe verwendet, fehlt aber im anfangs als vollständig bezeichneten Zustand. Entweder ergänzen oder explizit ableiten. Auch D_next, sämtliche Gates und gegebenenfalls Kontrollsignale müssen eindeutig festgelegt werden.

## 4. Der skalare Fluss ist nur lokal abgesichert

Die algebraische Auflösung I_B=A/(1-B) ist korrekt für B≠1. Lokale Lipschitz-Stetigkeit und Abstand vom Nennernullpunkt liefern für eine passend definierte endlichdimensionale ODE lokale Existenz und Eindeutigkeit. Sie liefern nicht automatisch einen Fluss für jedes fest vorgegebene Zeitintervall.

Gegenbeispiel zur allgemeinen Schlussregel: β=δ=0, F_Phi=Phi², F_I=0. Dann ist B=0 überall sicher und das Vektorfeld lokal Lipschitz. Trotzdem divergiert die Lösung mit Phi(0)>0 nach endlicher Zeit. Dieses Beispiel widerlegt den allgemeinen Fortsetzungsschluss, nicht speziell die konkrete Engine-PDE.

Zusätzlich erforderlich sind ein Fortsetzungskriterium, etwa ein geeignetes invariantes kompaktes Gebiet oder hinreichende Wachstumsabschätzungen, sowie die Bedingungen an Positivität und sonstige Zustandsgrenzen. Eine Randableitungsprüfung braucht die entsprechenden Regularitäts- und Tangentialvoraussetzungen. Für die PDE mit Laplaceoperator ist außerdem eine eigene Funktionalraumanalyse nötig; ein ODE-Verweis genügt nicht.

V4 S. 11, Abschnitt 5.5, behandelt skalare Carrier-Ordnung als Readout und nicht als Generatorinput. Der vorgeschaltete skalare Fluss ist daher als zusätzliche Kopplung oder als unabhängiger Begleitsektor zu deklarieren; seine Vereinbarkeit mit V4 ist nicht gezeigt.

## 5. Rekursionsmediator und Quadratwurzel

Eine Kompression erfüllt im Allgemeinen nicht sqrt(E N E)|EH = E sqrt(N) E|EH. Beispiel:

    N = [[2,1],[1,2]],  E = diag(1,0).

Links ergibt sich auf EH sqrt(2), rechts (sqrt(3)+1)/2. Gleichheit folgt unter passenden Reduktionsannahmen für N, nicht allein daraus, dass J auf seinem Support eine Isometrie ist.

Der Satz zum vermittelten Rekursionsoperator benötigt daher ausdrücklich die richtige Kompression und Reduktion aller beteiligten Faktoren, insbesondere N_R und R. Für den Potenztransport braucht man die entsprechende Invarianz/Reduktion des vollständigen Operators. Ein Eigenvektor wird nur dann zu einem nichtnulligen persistenten Eigenvektor transportiert, wenn der korrekt typisierte Vektor im erhaltenen Support liegt. Ein verworfener Eigenvektor kann auf null abgebildet werden.

## 6. Keine bewiesene globale Stabilität aus lokaler Paketabschätzung

Der zentrale Übergang in P6 ist nicht bewiesen: Eine Abschätzung des aktuellen Dual-Order-Pakets ist keine Operatorungleichung für jeden Vektor des vollständigen Schrittop­erators.

Einfaches Gegenbeispiel für diese Schlussform: K=diag(1/2,2), aktueller Vektor x=(1,0). Dieser Vektor wird kontrahiert, während auf (0,1) Wachstum auftritt. Auch eine bewiesene Operatorabschätzung für einen Teiloperator kontrolliert nicht ohne Weiteres die nachgeschaltete vollständige Dynamik.

Zu liefern ist eine exakte Definition von K_n und ein Beweis von

    K_n* G_(n+1) K_n ≤ q² G_n

für alle Vektoren des jeweils behaupteten Teilraums, einschließlich der stateabhängigen Gewichte und aller nachgeschalteten Operationen. Die Kompressionsidentität der Gram-Geometrie allein liefert diesen Beweis nicht.

Wenn die Ungleichung zusätzlich vorausgesetzt wird, sind die geometrische Produktabschätzung und die angegebene Eingangsfaltung korrekt. Sie bilden dann einen bedingten Stabilitätssatz, keine aus dem CTC-Transport bereits abgeleitete Eigenschaft. Die persistente/stabile Zerlegung benötigt zudem mittransportierte Invarianz und Kontrolle der Kreuzkopplungen sowie passend typisierte und normierte Eingangsbedingungen.

Der Jordanblock [[1,1],[0,1]] ist nicht potenzbeschränkt auf dem gesamten Raum, besitzt aber den nichtnulligen persistenten Vektor (1,0). Er fällt daher nicht automatisch durch jedes Gate, das nur einen bounded-non-decay-Witness verlangt. Witness-Persistenz und globale Operatorbeschränktheit sind zu unterscheiden.

## 7. Unendliche Dimension: brauchbarer lokaler Formensatz, unvollständiger Gesamtübergang

Unter den angegebenen beschränkten und beschränkt invertierbaren Gewichten ist folgende Aussage tragfähig: Für geschlossenes dicht definiertes ∇ ist B=∇c mit Dom(B)=c^(-1)Dom(∇) geschlossen und dicht definiert. Auch T=W^(1/2)BL ist geschlossen und dicht definiert; daher definiert T*T einen positiven selbstadjungierten Gram-Operator und den zugehörigen vollständigen Graphformraum.

Das löst einen wichtigen Teil der Definitionsbereichsfrage für die Produktinterpretation. Zum vollständigen Iterationssatz fehlen weiterhin die korrekt typisierte Reduktion E auf den verdoppelten Räumen und die Analyse des tatsächlichen polaren Analyseoperators: Auf welchem Hilbertraum wird polar zerlegt? Ist der G-orthogonale Witnessprojektor dort beschränkt? Welche Adjungierte werden verwendet? Wie gehen Support und Formdomäne ineinander über?

Die in P6 angegebene Schranke G_n ≤ (1+||Y_0||)I steht nur bei beschränktem Y_0 zur Verfügung. Für den ausdrücklich zugelassenen unbeschränkten Gram-Operator ist ||Y_0|| keine endliche Konstante. Beispiel auf l²: ∇e_k=k e_k, c=W=L=I. Dann Ye_k=k²e_k und ||e_k||_G²=1+k². Eine uniforme obere Normäquivalenz mit der ursprünglichen Hilbertnorm existiert nicht. Eine Stabilitätsaussage im Graphraum bleibt möglich, muss aber eigenständig formuliert und bewiesen werden.

## 8. Abbruch und Informationsverlust

Ein absorbierender Zustand ⊥ kann eine bereits wohldefinierte partielle Abbildung totalisieren. Er ersetzt weder die Definition der erfolgreichen Schritte noch einen Nachweis nichtterminaler Fortsetzung. Die Annahme „alle benötigten Bedingungen gelten bei jedem n“ ist eine bedingte Aussage, keine aus Anfangsdaten bewiesene Invarianz.

Reduktion bedeutet fehlende Kopplung zwischen zwei Sektoren für die geprüften Operatoren. Sie bedeutet nicht, dass der verworfene Sektor keine eigenen Observablen, Kapazitäten oder künftigen Beiträge zur zustandsabhängigen Auswahl besitzt. Future-null-Eigenschaft beziehungsweise Verhaltensäquivalenz muss separat bewiesen werden. Auch die Nichtleere einer interessanten, über mehrere Schritte nichtterminalen Klasse unter allen zusätzlichen Gates ist noch vorzuführen.

## Korrigiertes Statusledger

| Punkt | Status nach Gegenprüfung |
|---|---|
| P1 State Update | Lokaler skalarer Ansatz plausibel; vollständiges globales Update offen |
| P2 Rekonstruktion | Explizite Zustandsvervollständigung vorgeschlagen; Transport falsch typisiert, interne Auswahl offen |
| P3 Gram-Rebuild | Bedingter Reduktionssatz reparierbar und algebraisch beweisbar; Anwendung auf V4-Support offen |
| P4 Rekursion | Zusätzliche Transportregel; Typen und Mediatorreduktion nachzubessern |
| P5 Iteration | Totalisierung prinzipiell möglich; vollständige Schrittdefinition und nichtterminale Invarianz nicht bewiesen |
| P6 Nichtnormalität | Produkt-/Inputsatz korrekt unter zusätzlich bewiesener Cross-Step-Ungleichung; diese fehlt |
| P7 Unendliche Dimension | Lokaler geschlossener Formaufbau tragfähig; gesamter Transport und Stabilitätsanschluss offen |

## Nächste konkrete Reparatur

1. H, H⊕H, S H und E(H⊕H) in jeder Formel getrennt ausweisen; den V4-Transport korrekt übernehmen.
2. Bedeutung und Typ von D_cov c festlegen, einschließlich eventueller Leibniz- und Verbindungseigenschaften.
3. Den beschränkten Gram-Reduktionssatz als eigenständiges Lemma beweisen und sein Gate am tatsächlich erzeugten E prüfen.
4. Eine vollständig spezifizierte nichttriviale Mehrschritt-Konstruktion angeben, die sämtliche Gates erfüllt.
5. Den vollständigen K_n definieren und seine Cross-Step-Ungleichung beweisen; andernfalls Stabilität explizit als Zusatzannahme markieren.
6. Erst anschließend globale skalare Fortsetzung und unbeschränkte Operator-/Formdomänen hinzufügen.

Urteil: brauchbarer Entwurf einer neuen bedingten Erweiterung, jedoch kein bereits gültiger Seven-Problem Closure Theorem. Die Bezeichnungen „kleinste“ oder „minimale“ gemeinsame Lösung sind ohne definiertes Minimalitätskriterium und Beweis ebenfalls nicht begründet.
