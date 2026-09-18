# Gleicher BFG-Ausgangszustand, zwei zulässige lokale Rebuilds

Ausgangspunkt: Commit 22fceab04fd852e390c63d2b1de9d379b73c35d1.
Diese Stufe prüft die offene Rekonstruktion nach Anwendung von Split,
Polartransport und Formation-Gate. Sie ergänzt den vorherigen abstrakten
Gramvergleich um einen vollständig ausgerechneten lokalen Kandidaten.

## Behauptung und Reichweite

Die numerischen Bedingungen von V4 Gl.37–41 bestimmen für den unten angegebenen
Zustand die Faktoren in Gl.40 nicht eindeutig. Zwei positive Rebuilds liefern
verschiedene neutrale Folgezustandsvektoren. Das ist ein Gegenbeispiel gegen
Eindeutigkeit **aus diesen lokalen Bedingungen allein**, kein Nachweis zweier
vollständiger Modelle aller BFG-Axiome und keine Widerlegung einer zusätzlich
spezifizierten vorgelagerten Rekonstruktionsfunktion.

## Ausgangszustand

Auf dem eindimensionalen reellen Träger seien

    d=1, Y=1, G=2, R=1,
    Differenzkapazität=3, Kohärenzkapazität=1, Neutralkapazität=1.

Der ganze Träger ist persistent; P_G=1. Hier stimmen die gedruckte
Nichtabkling-Span-Definition und die vorgeschlagene periphere Definition überein.
Das Beispiel hängt deshalb nicht vom bisherigen Persistenzdefinitionsfehler ab.
Für das leere stabile Komplement verwenden wir die im Labor dokumentierte
Konvention gamma=1. Die eindimensionale minimale Mode ist einfach und isoliert.

## Split und Polartransport

Es gilt C_N=B_N=1/2. Die metrischen Lasten sind jeweils 2(1/2)^2=1/2;
die reziproken Gewichte sind ebenfalls je 1/2. Daher

    A = (1,1)^T/(2 sqrt(2)),
    Q = sqrt(A†A)=1/2,
    J = (1,1)^T/sqrt(2).

In der orthonormalen Trägerbasis u=J ist das Kreuzpaket
z=u†Ad=1/2. Die Kapazitätskompression ergibt wieder 3,1,1; folglich K=-1.
Positive duale Lasten, positiver Persistenzabstand sowie einfache isolierte
negative Formation sind erfüllt. Der gemeinsame Gate-Entscheid ist positiv.

## Zwei Rebuilds auf demselben neuen Träger

Wir geben die folgenden Faktoren in der Basis u an:

| Lokale Fortsetzung | B_C | W_N | L_C | H_C | Y_next | d_next=(1+Y_next)^-1 z |
| --- | --- | --- | --- | --- | --- | --- |
| A | 1 | 1 | 1 | 1 | 1 | 1/4 |
| B | 2 | 1 | 1 | 4 | 4 | 1/10 |

Beide erfüllen die positive Gram-Bauform Gl.40 und verwenden denselben Split,
denselben Polartransport und dasselbe erfolgreiche Gate. Die unterschiedlichen
Lastspektren 1 und 4 sind nicht durch einen unitären Basiswechsel verbunden.
Es handelt sich deshalb nicht bloß um verschiedene Faktorisierungen desselben Y.
Auch Basis-Kovarianz allein beseitigt diese Freiheit nicht: skalare Vielfache
der Identität transformieren kovariant. Die Forderung nach einer *bestimmten*
vorgelagerten Funktion kann die Freiheit beseitigen; diese Funktion muss dazu
aber definiert und ihre Eindeutigkeit hergeleitet werden.

Die Tabelle ist kein Vorschlag, A oder B zum universellen Modell zu erklären.
Insbesondere sind hier keine vollständigen Funktionen für alle Zustände oder
rekursiven Transportgesetze konstruiert. Falls weitere BFG-Annahmen einen der
beiden Faktoren ausschließen sollen, sind genau diese Annahmen und ihre
Anwendung auf diesen Zustand die nächste zu prüfende Beweispflicht.

## Konsequenz für die sieben Probleme

Der erste offene Schritt ist weiterhin die Rekonstruktion, nicht die Anzahl
weiterer Iterationen. Ein eindeutiger Satz müsste aus demselben vollständigen
Input genau eine Last Y_next (gegebenenfalls modulo erklärter Äquivalenz)
erzwingen. Anschließend ist ein R_next zu definieren, das die erforderliche
Persistenzklasse erhält. Erst darauf kann der vollständige Iterationsbeweis
aufbauen. Der bestehende Gram-Rebuild kann die Faktoren beider lokalen
Fortsetzungen bereits verarbeiten; er entscheidet nicht, welche BFG auswählt.

## Audit und Verifikation

Complete Edition: eng abgegrenzter Claim und konstruktive Gegenprüfung.
Workflow Master: negative Erkenntnis erhalten, keine Gleichsetzung eines
lokalen Beispiels mit einem globalen Modell. Context Recovery: V4 Gl.37–41
und V2 §24 bleiben Quellen; keine hinzugefügte Closure wird ihnen zugeschrieben.
Die drei Originalquellen sind im
[Auditquellenregister](../prediction-audit-2026-09-18/sources.json) identifiziert.

Am 18.9. wurden Lasten, Gewichte, Paketnormquadrat und beide Folgezustandswerte
mit Python `fractions.Fraction` in exakter rationaler Arithmetik nachgerechnet:
Lasten 1/2, Gewichte 1/2, Paketnormquadrat 1/4, Folgezustände 1/4 und 1/10;
alle Assertions bestanden, Exit 0. Die Wurzelfaktoren in J kürzen sich in
den angegebenen Produkten analytisch. Dies ist eine algebraische Kontrolle,
kein empirischer Test und keine vollständige unabhängige Begutachtung.

Status: lokaler Nicht-Eindeutigkeitsnachweis fertig; universelle Rekonstruktion
weiter offen. Originalpaper, Produktionscode und historische Resultate unverändert.

