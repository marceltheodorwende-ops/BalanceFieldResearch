# Gegenprüfung der mathematischen Referenzreparatur

Datum: 15. September 2026. Bezug: BFG_Mathematischer_Audit_2026-09-15.md.
Erneute KI-gestützte Prüfung; keine unabhängige externe Begutachtung.

## Abschließendes Urteil

Die mathematischen Kernaussagen des Auditberichts sind unter den dort genannten
Voraussetzungen richtig. Die Ausschlusslogik, die Integralidentität und die
konservative Fehlergrenze wurden nachgerechnet. Es wurde kein Gegenbeispiel
innerhalb dieser Voraussetzungen gefunden. Ein numerisch zertifizierter
Entscheider ist damit noch nicht implementiert. Die vorhandene Software besitzt
diese neue Absicherung weiterhin nicht.

| Prüfgegenstand | Urteil | Evidenz |
| --- | --- | --- |
| Ein gemeinsamer gesunder Parameter erklärt alle Zeiten | Korrekte Definition | Quantorenprüfung |
| Kein Ausschluss einer enthaltenen wahren gesunden Referenz | Bedingt bewiesen | Wahres Parameter-Zustands-Paar ist zulässiger Zeuge |
| Duhamel-Identität bei nichtkommutierenden Matrizen | Korrekt | Ableitung des Matrixprodukts, kein Vertauschen der Faktoren nötig |
| Operatorfehler <= t eta | Korrekt für t>=0 und symmetrische PSD-Laplacematrizen | Kontraktivität und Integralabschätzung |
| Zentrierter Zustandsfehler | Korrekt | Zerlegung in Anfangsfehler und Operatorfehler |
| Kantengewichtsgrenze eta=2 max_i sum_j b_ij | Korrekte konservative Grenze | Absolute Zeilensumme und Symmetrie |
| Fehlerfreiheit der numerischen Umsetzung | Nicht nachgewiesen | Keine zertifizierten Rundungs- oder Optimierungsgrenzen implementiert |
| Eindeutige Ausfalldiagnose | Nicht allgemein möglich | Überlappende Modellfamilien und Gleichgewichtsgegenbeispiel |

## Vollständiger Kernbeweis

Alle Matrizen wirken auf denselben endlichdimensionalen Knotenraum; t>=0.
L und L0 sind reelle symmetrische Laplacematrizen nichtnegativer ungerichteter
Gewichte. Zusammenhang des Graphen ist für die folgende Grenze nicht nötig.

Setze Q(s)=exp(-(t-s)L) exp(-sL0). Dann ist

`Q'(s)=exp(-(t-s)L)(L-L0)exp(-sL0)`.

Aus Q(t)=exp(-tL0) und Q(0)=exp(-tL) folgt die im Audit angegebene
Integralidentität mit negativem Vorzeichen. Da beide Matrizen PSD sind, haben
ihre Exponentialoperatoren für nichtnegative Zeiten euklidische Operatornorm
höchstens eins. Integration liefert `||exp(-tL)-exp(-tL0)||_2 <= t||L-L0||_2`.
Kommutativität von L und L0 wird nicht vorausgesetzt.

Mit E=exp(-tL), E0=exp(-tL0) gilt

`Ex0-E0*xhat0 = E(x0-xhat0)+(E-E0)xhat0`.

Weil L1=L0*1=0, gilt (E-E0)1=0. Daher darf xhat0 im zweiten Term durch
`P*xhat0`, P=I-11^T/n, ersetzt werden. Daraus folgt

`||Ex0-E0*xhat0||_2 <= epsilon_x + t eta ||P*xhat0||_2`.

Für Messungen y=SEx0+v mit `||v||_2<=epsilon_y` ist die vollständige Messgrenze

`||y-S E0*xhat0||_2 <= ||S||_2 (epsilon_x+t eta ||P*xhat0||_2)+epsilon_y`.

Für einen einzelnen Knotensensor ist ||S||_2=1. Bei mehreren Sensoren müssen
die Norm des Fehlervektors und komponentenweise Fehlerbudgets sauber getrennt
werden: Ein skalares Budget e pro Sensor ergibt etwa sqrt(m)e als 2-Normgrenze
bei m Sensoren, nicht automatisch e. Für n Anfangswerte mit jeweils Fehler e0
kann epsilon_x=sqrt(n)e0 verwendet werden. Diese Präzisierung war im ursprünglichen
Audit bei allgemeinem S nur verkürzt formuliert.

Für Delta L=L-L0 gilt zeilenweise

`sum_j |Delta L_ij| <= 2 sum_{j!=i}|Delta w_ij| <= 2 sum_{j!=i} b_ij`.

Da Delta L symmetrisch ist, ist ihre 2-Norm durch die maximale absolute
Zeilensumme beschränkt. Diese Grenze umfasst auch Gewichte null und getrennte
Komponenten, sofern ihre Änderungen von den b_ij tatsächlich abgedeckt werden.

## Mengenlogik und zertifizierte Entscheidung

Die Hypothese ist `es existiert (theta,x0), so dass für alle k die Messbedingung gilt`.
Sie darf nicht durch `für alle k existiert ein eventuell anderes (theta_k,x0_k)`
ersetzt werden. Die gesunde Parametermenge muss außerdem vor der Entscheidung
feststehen und den wahren gesunden Fall enthalten.

Bei kontinuierlicher Vorhersage und nichtleerer kompakter Suchmenge K lässt
sich für komponentenweise Fehlerbudgets e_ki die Funktion

`g(theta,x0)=max_{k,i} (|y_ki-[S f(theta,x0,t_k)]_i|-e_ki)`

verwenden. Es existiert ein gemeinsamer verträglicher Zeuge genau dann, wenn
`min_K g <= 0`. Kompaktheit sorgt dafür, dass das Minimum angenommen wird.
Ohne diese Voraussetzung darf ein nur asymptotisch erreichter Wert null nicht
als vorhandener Zeuge ausgegeben werden.

Für eine numerische Implementierung ergeben sich drei zulässige Entscheidungen:

1. **Gesunde Familie ausgeschlossen:** Eine nachweislich gültige globale
   Untergrenze für min_K g ist strikt positiv.
2. **Verträglicher Zeuge:** Ein konkretes Paar erfüllt nachweislich sämtliche
   Bedingungen einschließlich der numerischen Fehlergrenzen.
3. **Ungeklärt:** Beides wurde nicht nachgewiesen; etwa bei Zeitlimit, zu weiter
   Intervallhülle oder unzureichender numerischer Genauigkeit.

Ein lokal gefundenes positives Minimum, Nichtkonvergenz oder ein Gitter ohne
Treffer erfüllt Fall 1 nicht. Eine äußere Hülle kann Ausschluss beweisen, wenn
eine Messung außerhalb liegt; Überlappung beweist keinen gemeinsamen Zeugen.
Ein exakt auf dem Rand liegender Zeuge kann numerisch ungeklärt bleiben.

## Konkrete Gegenprüfungen

**Gitterlücke:** Bei Zwei-Knoten-Diffusion und wahrem Gewicht 1 ist die
normierte Abweichung bei t=1 gleich 0.1353352832. Die gesunden Gittergewichte
0.9 und 1.1 liefern 0.1652988882 und 0.1108031584. Kein Treffer in diesem Gitter
beweist also keine Unverträglichkeit mit dem Intervall [0.9,1.1].

**Falsche Zeitquantoren:** Die Werte q(1)=exp(-1.8) und q(2)=exp(-4.4) liegen
jeweils in den zulässigen Zeitpunkthüllen für dasselbe Gewichtsintervall.
Der erste erzwingt aber Gewicht 0.9, der zweite Gewicht 1.1. Bei festem Gewicht
und normiertem Anfangskontrast gibt es keinen gemeinsamen Zeugen.

**Fehlende PSD-Annahme:** Für L=-1, L0=0, t=1 wäre die Operatorabweichung
e-1=1.7182818285 größer als t|L-L0|=1. Dieser Fall ist kein zulässiger
Graph-Laplacian; er zeigt, weshalb die Kontraktivitätsannahme wesentlich ist.

**Gleichgewicht:** Für x0=c1 verlaufen alle ungestörten Graphen identisch.
Gesunde und defekte Hypothesen bleiben hier selbst mit perfekten Vollmessungen
ununterscheidbar. Eine zusätzliche Anregung kann diese Situation ändern,
garantiert aber nicht jede gewünschte Unterscheidung. Das ist keine numerische Schwäche.

## Numerische Plausibilitätsprüfung

Zusätzlich zum Beweis wurden 720 Kombinationen geprüft: n=2,4,8,12;
jeweils 30 zufällige Laplacian-Paare und Zeiten 0, 1e-6, 0.2, 2, 50, 10000.
Seed 20260918; NumPy über den vorhandenen Python-Runtime. Enthalten waren
getrennte Referenzgraphen, nichtnegative Gewichte nach Störung und ein
Anfangsfehler mit 2-Norm 0.03. 90 der 120 Matrixpaare kommutierten nicht.

Keine Verletzung der Kanten-, Operator- oder Zustandsgrenze oberhalb 1e-10
wurde gefunden; größter positiver Rundungsüberschuss 4.00e-15. Der Lauf endete
mit Exitcode 0. Diese Prüfungen verwenden Gleitkomma-Eigendecomposition und
sind keine zertifizierte Intervallrechnung. Sie stützen die Implementierbarkeit
des Beweises, ersetzen ihn aber nicht und liefern keine zusätzlichen 720
bestandenen Repository-Unit-Tests.

## Abschluss und verbleibender Auftrag

Die verlangte Gegenprüfung ist abgeschlossen. Die bedingte mathematische
Herleitung ist in dieser Prüfung als korrekt beurteilt. Ein einsatzfertiger
Monitor oder eine externe wissenschaftliche Begutachtung folgt daraus nicht.
Für die Umsetzung fehlen noch eine begründete gesunde
Parametermenge, eine garantierte numerische Hülle beziehungsweise ein
zertifizierter Entscheider und getrennte Messgrößen für Ausschluss, Zeugen
und Enthaltung. Produktionscode und historische Ergebnisdateien wurden bei
dieser Gegenprüfung nicht verändert.
