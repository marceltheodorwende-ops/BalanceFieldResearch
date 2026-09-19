# M3: explizites endliches Verbindungsmodell

Ausgangsstand: 58018b747e12c21e403de46922a5c67525778e5e.
**Status: zusätzlicher Modellvorschlag, keine interne Herleitung der universellen
BFG aus den fünf Originalpapern.** Der Nutzer hat die Fortsetzung nach dem
Abschluss der internen Ableitungsrunde verlangt. Diese Stufe erprobt deshalb
eine vollständig ausgewiesene Modellergänzung. Frühere Negativbefunde bleiben gültig.

## Zusätzliche Annahmen

Der endlichdimensionale dimensionslose Zustand ist X=(A,D,c,N,d), mit
A†=-A, positiven hermiteschen Kapazitäten D,c,N und nichtverschwindendem d.

1. Die kovariante Ableitung in dieser homogenen Matrixrealisierung ist die
   innere Ableitung D_cov(c)=[A,c]. Ein unabhängiger partieller Ableitungsterm
   wird hier nicht modelliert. [A,.] erfüllt die Leibnizregel und erhält für
   schiefhermitesches A die Hermitizität von c.
2. B_C=[A,c], W_N=I und L_C=I, also Y=B_C†B_C.
3. Der rekursive Transport ist R=(I-A)^-1(I+A), die Cayley-Abbildung von A.
   Der dimensionslose Schritt ist auf eins festgelegt. Das ist eine Modellwahl.
4. Nach dem BFG-Split und Gate werden D,c,N wie in V4 Gl.39 komprimiert.
   Zusätzlich wird A nach derselben Vorschrift A'=U†(A⊕A)U komprimiert.
5. Aus A',c' werden B'_C,Y',R' vollständig neu berechnet.
   Der Paketupdate ist d'=(I+Y')^-1 U†A_DO d. Keine nachträgliche Normierung.

U ist eine orthonormale Basis des aktiven Polarträgers. Die Verwendung dieser
Zusatzregeln ist verbindlich für M3, nicht für die ursprüngliche BFG. Sie liefert
ein bestimmtes Modell innerhalb der algebraischen Bauformen, keine Auswahl
dieses Modells durch die vorhandenen Axiome.

## Bedingter Wohldefiniertheitssatz für M3

Für schiefhermitesches A ist I-A invertierbar: seine Eigenwerte haben Realteil
eins. Die Cayley-Abbildung ist unitär, weil die kommutierenden Polynome I±A
einander adjungiert sind. R ist daher normal und potenzbeschränkt. Alle Modi
sind persistent; das Modell besitzt hier keinen abklingenden R-Komplementraum.
Der Laborwert gamma=1 für ein leeres stabiles Komplement ist ausdrücklich übernommen.

Y>=0 folgt aus der Gramform. Bei positiven dualen Lasten hat A_DO vollen
Spaltenrang, da P_G=I, C_N invertierbar und das Keep-Gewicht positiv ist.
Somit hat der neue Träger dieselbe endliche Dimension wie der alte.
Kompression erhält Positivität der Kapazitäten und Schiefhermitizität von A.
Der neu berechnete Gram ist positiv, die neue Cayley-Abbildung unitär.
Außerdem ist d' nicht null: A_DO ist injektiv, U† ist auf seinem Bild
isometrisch, und (I+Y')^-1 ist invertierbar.

Jeder Gate-erfolgreiche Schritt liefert daher wieder einen zulässigen M3-Zustand.
Ein Gate-fehlgeschlagener Schritt führt zum absorbierenden Terminalzustand.
So ist die Iteration in exakter Arithmetik für jeden endlichen Schritt definiert,
bis gegebenenfalls Terminalität eintritt. Basiswechsel U→UV ändern die
Operatoren nur durch unitäre Konjugation und den Paketvektor durch V†.
Es wird keine bevorzugte SVD-Basis zu einem physikalischen Freiheitsgrad erklärt.

Diese Argumente beweisen einen Satz über **M3 unter seinen neuen Annahmen**.
Sie beweisen weder allgemeine BFG-Universalität noch Konvergenz oder Naturgültigkeit.

## Verhältnis zu den Gegenbeispielen

M3 rekonstruiert B'_C aus A',c', statt die vollständige frühere Gramform
zu erben. Im Allgemeinen gilt

    [U†A2U,U†c2U] != U†[A2,c2]U,
    Y'_M3 != U†(Y⊕Y)U.

Außerhalb des neuen Trägers liegende Verbindungsinformationen werden bewusst
nicht weitergeführt. M3 ist deshalb **keine verlustfreie Lösung** des früheren
Kanalproblems und keine Bestätigung von G1. Beide Abweichungen werden vom
Code als Frobeniusnormen ausgegeben. Der Verlust wird nicht durch neue Gewichte
oder nachträgliche Retuning-Faktoren versteckt.

Der Gegenfall mit D_cov=∂_t fällt nicht unter den homogenen Ansatz [A,.].
Damit ist er hier ausgeschlossen, nicht widerlegt. Der M3-Ansatz ersetzt die
fehlende allgemeine Entwicklungsregel durch eine ausdrücklich eingeschränkte
Regel. Reelle Naturdaten und unendlichdimensionale Felder sind nicht einbezogen.

## Analytische Referenz

Für A=[[0,-1],[1,0]], c=diag(1,2), D=5I, N=I und d=(1,1) gilt
B_C=[[0,-1],[-1,0]], Y=I, R=A. Der Split ist skalar in den beiden
direkten Summenblöcken. Bis auf unitäre Trägerkoordinaten bleiben A,D,c,N
unverändert und d wird je Schritt durch vier geteilt. Die Formation hat
die einfachen Eigenwerte -3 und -2 und besteht das exakte Gate.
Damit gilt ||d_n||=sqrt(2)/4^n. Dies ist ein nichtterminaler exakter Referenzlauf
mit schrumpfender Amplitude, keine Entstehung wachsender Komplexität.

Bei sehr kleinen Amplituden kann die feste numerische Lasttoleranz das Gate
ablehnen. Das ist nicht dasselbe wie exakte physikalische Terminalität.
Die derzeitige Numerik wird deshalb nicht für unendlich viele Schritte zertifiziert.

## Implementierung und Befunde

`bfg_lab.connection_model.operators` erzeugt die abgeleiteten Größen;
`advance` gibt vollständigen Folgezustand und Diagnostik zurück. None ist
absorbierend. Der Eingabezustand wird nicht verändert. `seed` liefert die
analytische Referenz. Die ursprünglichen M1/M2-Modelle bleiben unverändert.

Ein zusätzlicher dreidimensionaler Fall mit nichtkommutierenden Matrizen
besteht drei Kandidatenschritte. Schon im ersten Schritt beträgt die G1-
Abweichung etwa 3.834, die Ableitungsabweichung etwa 1.503. Dies ist ein
Negativbefund für die Identifikation von M3 mit G1, kein numerisches Rauschen.
Das Ergebnis wird in results.json reproduzierbar festgehalten.

## Audit und Status der sieben Probleme

Complete Edition: Modellannahme, bedingter Satz und numerische Demonstration
getrennt. Workflow Master: alle negativen Befunde erhalten; keine Änderung
der Originalpaper. Context Recovery: B_C=[A,c] ist die besondere neue
Realisierung, nicht der nachträglich behauptete universelle Inhalt von V2.
Die drei Auditdateien bleiben durch das bestehende
[Register](../prediction-audit-2026-09-18/sources.json) identifiziert.

Für M3 sind State Update, konkrete Gramfaktoren, Rebuild, R_next und endliche
Iteration vollständig spezifiziert. Die entsprechenden **universellen**
Probleme bleiben offen. M3 behandelt weder allgemeinen nichtnormalen Transport
noch unendlichdimensionale Realisierung. Es enthält nur unitären Transport.

Nächster sinnvoller Prüfgegenstand: Verhalten bei nichtkommutierenden Matrizen
und Empfindlichkeit gegenüber der Verbindungsannahme. Vor einem physikalischen
Anspruch wäre eine unabhängige Begründung dieser Annahme erforderlich.
Die pausierte Hintergrundautomatisierung wird durch diesen einzelnen Lauf
nicht stillschweigend neu gestartet.
