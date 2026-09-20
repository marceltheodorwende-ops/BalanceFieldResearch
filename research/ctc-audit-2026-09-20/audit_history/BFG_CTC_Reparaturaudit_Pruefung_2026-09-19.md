> Historische Reviewnotiz. Der aktuelle konsolidierte Stand steht im übergeordneten README; spätere Korrekturen sind dort ausgewiesen.

# Prüfung des korrigierten BFG-CTC-Reparaturaudits

## Urteil und Umfang

Der neue Entwurf verbessert die mathematische Lage wesentlich: Die falschen Transporttypen sind korrigiert, die bedingten Sätze werden überwiegend sauber von interner Rekonstruktion getrennt, und die frühere Gesamtschließung wird zurückgenommen. Der beschränkte Transport-/Gram-Satz ist unter seinen Voraussetzungen tragfähig.

Allerdings besitzt das Mehrschrittbeispiel eine bisher übersehene Quellenabhängigkeit: Die ausgeschriebene Witnessdefinition in V4 ist nicht mit ihrer dort behaupteten spektralen Charakterisierung gleichwertig. Auch meine vorherigen Gegenprüfungen hatten diesen Fehler noch nicht erkannt. Das Beispiel ist unter einer ausdrücklich korrigierten spektralen Definition nachvollziehbar, nicht unter beiden widersprüchlichen V4-Definitionen zugleich.

Gelesen: der eingereichte Reparaturaudit einschließlich seiner Beweise und Abschnitte 21–27; erneut abgeglichen: V4-Gleichungen 27–29 und die zuvor geprüfte Analyse-/Kompressionsarchitektur. Gleichung 27 wurde zusätzlich auf der gerenderten Originalseite 7 visuell kontrolliert. Die drei Übergänge wurden mit exakter rationaler Arithmetik nachgerechnet. Keine neue Vollprüfung aller Quellen und keine empirische Validierung.

## Bestätigte Teile

- Satz 1: Range-/Supportdarstellung sind durch J eingeschränkt auf seinen Initialraum unitär äquivalent. Die korrigierten Typen stimmen.
- Satz 2: Bei beschränkten Faktoren und gemeinsam reduzierendem Range stimmen Faktor-Rebuild und Gram-Kompression überein. Die Positivitätsargumente stimmen. Untergrenzen für B und L sowie ein positives Gewicht liefern die angegebenen unteren Gram-Schranken.
- Sätze 3 und 4: Im beschränkten Rahmen sind Quadratwurzel- und Rekursions-/Potenztransport unter den angegebenen Reduktionsannahmen korrekt. Die zusätzliche Reduktion von R_C ist bereits eine Folge gemeinsamer Reduktion von N_R und R; sie ist unschädlich, aber redundant.
- Satz 5: Die Paketabschätzung für den gewichterzeugenden Vektor ist korrekt. Sie ist von der allgemeinen Operatorabschätzung zu unterscheiden.
- Satz 6: Das kompakte vorwärtsinvariante Gebiet innerhalb des offenen Definitionsgebiets liefert das angegebene ODE-Fortsetzungskriterium. Dessen Anwendung auf die konkrete BFG-Dynamik bleibt offen.
- Satz 7: Geschlossenheit und Dichtheit von T unter den genannten invertierbaren beschränkten Faktoren sind korrekt; der positive selbstadjungierte Gram-Operator und der Graphraum sind ein gültiger bedingter Baustein.

## Neuer blockierender Quellenbefund: Witnessdefinition

V4 S. 7, Gleichung 27, definiert den Witnessraum als abgeschlossenen linearen Spann aller Vektoren, deren Vorwärtsorbit beschränkt ist und deren Norm nicht asymptotisch verschwindet. Danach wird dieser Raum mit der Summe der Eigenräume zum Einheitskreis gleichgesetzt.

Diese Gleichheit ist falsch, sogar bei einer diagonalen, normalen, potenzbeschränkten Matrix:

    R = diag(1,1/2),  G=I.

Sowohl e1 als auch e1+e2 haben einen beschränkten nichtverschwindenden Orbit:

    R^k e1=e1,
    R^k(e1+e2)=e1+2^(-k)e2.

Daher gehört auch e2=(e1+e2)−e1 zum linearen Spann dieser Witnessvektoren. Die linke Seite der V4-Definition liefert somit den ganzen zweidimensionalen Raum. Der periphere Eigenraum auf der rechten Seite ist dagegen nur span(e1).

Allgemeiner enthält dieser Spann bei globaler Potenzbeschränktheit und einem nichtnulligen persistenten Vektor auch jede rein abklingende Richtung: Addiere sie zum persistenten Vektor und subtrahiere anschließend den persistenten Vektor.

### Auswirkung auf das neue Beispiel

Für R_d=diag(1,…,1,1/2) liefert die wörtliche Spann-Definition W_d=R^d, nicht span(e1,…,e_(d−1)). Dann ist P_d=I. Der polare Range behält Dimension d; die beanspruchte Folge 5→4→3→2 entsteht so nicht.

Bereits die erste Energie unterscheidet sich: Mit dem wörtlichen P=I und sonst unveränderten neutralen Faktoren ergibt sich D_1=(1/4)(1,1,1,1,1) und ||D_1||²_G=5/8 statt 1/2.

Die spektrale Charakterisierung beziehungsweise der Rieszraum aus Gleichung 28 liefert hingegen genau den im Audit verwendeten Projektor. Beide Quellenaussagen können nicht zugleich beibehalten werden. Ein Erratum beziehungsweise eine explizite Wahl der spektralen Definition ist erforderlich.

### Eng begrenzte Reparatur

Für die endlichdimensionale potenzbeschränkte Klasse mit isoliertem peripherem Spektrum definiere W ausdrücklich als Summe der Eigenräume mit |lambda|=1, äquivalent zum entsprechenden Rieszraum. Verwende dann den G-orthogonalen Projektor auf diesen Raum; er ist im Allgemeinen nicht identisch mit dem Rieszprojektor selbst.

Diese Reparatur stellt die intendierte spektrale Fassung her. Sie ist als Korrektur der früheren falschen Gleichsetzung zu dokumentieren. Die unendlichdimensionale Verallgemeinerung benötigt eigene Annahmen und einen eigenen Satz.

## Rechenprüfung des Beispiels unter der spektralen Reparatur

| Übergang | beide Loads | Produkt der Loads | Energie vorher | Energie nachher |
|---|---:|---:|---:|---:|
| 5→4 | 2 | 4 | 10 | 1/2 |
| 4→3 | 3/32 | 9/1024 | 1/2 | 3/128 |
| 3→2 | 1/256 | 1/65536 | 3/128 | 1/1024 |

Die Bruchwerte, polaren Faktoren und diagonalen Gram-Faktoren stimmen. Die im Text angegebenen spektralen Formationgates gelten bei dieser Interpretation.

Die neue Regel R_d=I−P_max(K_d)/2 wird in jedem Schritt neu angewendet. Sie ist ausdrücklich keine bloße Kompression des alten R_d: Dessen Kompression wäre auf dem erhaltenen alten peripheren Raum die Identität. Der Entwurf benennt diese neue Regel korrekt als Modellentscheidung. Das Beispiel bestätigt eine eingeschränkte Beispielklasse, keine interne eindeutige Rekonstruktion von R.

## Zusätzlich ableitbar: bedingte Abschätzung der tatsächlichen Folge

Im beschränkten, gemeinsam reduzierenden Gram-Zweig gilt auf dem neuen Range

    Y_next=(Y⊕Y)|Range,
    G_next=(G⊕G)|Range.

Setze v=A_D D im neuen Range und D_next=(I+Y_next)^(-1)v. Durch Funktionalkalkül ist der Resolvent in der G_next-Norm kontraktiv. Deshalb folgt aus der V4-Paketabschätzung:

    ||D_next||_(G_next) ≤ ||v||_(G⊕G) ≤ 2^(-1/2)||D||_G.

Falls jeder der betrachteten Schritte existiert und erneut dieselben Voraussetzungen erfüllt, folgt induktiv

    ||D_n||_(G_n) ≤ 2^(-n/2)||D_0||_(G_0).

Dies ist eine bedingte Abschätzung der tatsächlichen ungestörten Folge. Es beweist weder, dass die Gates unbegrenzt bestehen, noch Störungsrobustheit, eine Lipschitz-Abschätzung zwischen zwei verschiedenen Zuständen oder den allgemeinen linearen Switching-/Inputsatz. Bei wechselnden Räumen ist außerdem keine Konvergenzbehauptung in einem gemeinsamen Raum ohne Identifikationen enthalten.

## Weitere begrenzte Präzisierungen

- In Abschnitt 10 ist E v nur für v im verdoppelten alten Raum definiert. Für einen ursprünglichen Vektor in H muss zuerst seine konkrete Einbettung angegeben werden.
- Die Formel J=AQ^+ ist in unendlicher Dimension bei nichtgeschlossenem Bild mit Vorsicht zu lesen: Q^+ kann unbeschränkt sein. J ist der kanonische beschränkte polare Anteil; eine Produktdarstellung benötigt Definitionsbereich und gegebenenfalls stetige Fortsetzung.
- Abschnitt 6 zeigt fehlende Reduktion eines beliebigen Faktors F. Eine konsistente Gram-Faktorisierung des dort gewählten Y lässt sich ergänzen, etwa c=L=I, ∇=F und W=F Y F. Dann ist ∇*W∇=Y. Das ist ein Gegencheck im abstrakten Produktzweig, weiterhin kein Nachweis aller Originalgates.
- Die PDE in Abschnitt 17 enthält im negativen Gradiententerm der I-Gleichung keinen Faktor I. Die lokal verfügbare Engine v1.0 verwendet dort −gamma I |grad Phi|². Falls eine andere historische Variante gemeint ist, braucht sie eine genaue Quellenstelle; beide Varianten dürfen nicht vermischt werden.
- Die Aussage, eine eigenständige V3-Datei sei in der anderen File Library verfügbar, ist hier nicht überprüfbar. Sie wird nicht als verifizierter Quellenfund übernommen.

## Schlussstatus

Der korrigierte Audit liefert einen brauchbaren beschränkten Transport-/Gram-Satz und ein rechnerisch stimmiges Mehrschrittmodell unter einer expliziten spektralen Witnessdefinition. Seine zurückhaltende Sieben-Punkte-Statusmatrix ist grundsätzlich angemessen. Vor einer Veröffentlichung des Beispiels als V4-konform muss die widersprüchliche Witnessdefinition korrigiert und der Modellstatus des neuen R-Updates erhalten werden.

Nächste Priorität: ein dokumentiertes Witness-Erratum mit dem zweidimensionalen Gegenbeispiel und der begrenzten spektralen Ersatzdefinition; danach die Beispielrechnung und den bedingten Folgensatz daran anschließen. Keine Behauptung einer abgeschlossenen universellen Weltformel.
