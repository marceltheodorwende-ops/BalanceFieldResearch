# Runde76: Identifizierbarkeit aus der autonomen Überlebenshistorie

Vorabcommit 9abc7e9ef37af8bc72672995f01cd04800cfb6bd, Ausgangshead fa012644926d9de940a604323c8568e9a43845cd. Gepinnte BFG-Quelle und bestehende Originalimplementierung unverändert. Quellen I5/6 (Selektion), I10/I17 (Gram-Nachfolger), I11/I32 (separate Originalmasse/Transportgeschichte), II89 (Projektionsabschluss); kombiniert mit dem vollständigen Abhängigkeitssatz aus Runde75.

## Präzise Datensatzgrenze

Untersucht wird der projizierte Datensatz aus strukturellen Feldern B=(K,F,Y,P), Transportpfeilen, Seedhistorie, lokalen Überlebensmassen und gespeicherter skalarer Originalmasse. **Der gespeicherte Witness selbst ist aus diesem Datensatz ausgeschlossen.** Eine vollständige Xi-Historie enthält W bereits; dafür wird keinerlei Nichtrekonstruierbarkeit behauptet. Die Untersuchung fragt, ob die unabhängig vom gespeicherten W ausgegebenen autonomen Strukturdaten und Massen den Witness oder eine physikalische Zustandswahl bestimmen.

## 1. Allgemeiner Informationsbefund

**Aus vorhandenen BFG-Regeln abgeleitet:** Für feste strukturelle Anfangsdaten bestimmt S0=Tsel0†Tsel0 die erste Witnessabfrage m0=tr(S0W0). Auf dem Zweig m0>0 entwickeln sich sämtliche strukturellen Daten unabhängig vonW (Runde75).

Nach dem ersten erfolgreichen autonomen Ereignis gilt der Quellen-Gramsatz0<Y_+<I. Daher sind alle späteren autonomen Selektoren auf dem aktiven Träger voll, Tsel=P und m_sel=1. Auch m4=1. Bis zu einer strukturellen Terminalentscheidung lautet der gesamte lokale Massenverlauf somit (m0,1,1,...), die gespeicherte Originalmasse bleibt m0. Endet die strukturelle Folge, ist dieses Ende auf den verglichenen positiven-Massen-Zweigen ebenso unabhängig vonW.

Der projizierte strukturelle/Massen-Datensatz erhält überW0 also nur die eine skalare Abfrage tr(S0W0). Dies ist eine mathematische interne Abfrage, keine neu angenommene physikalische Bornmessung. Historienlänge allein macht daraus keine Folge verschiedener tomographischer Effekte.

## 2. Lineares Identifizierbarkeitskriterium

**Standardmathematik:** Auf einem d-dimensionalen Anfangsträger ist ein allgemeiner hermitescher Zustand durch lineare Erwartungswerte nur eindeutig bestimmt, wenn die abgefragten hermiteschen Operatoren zusammen mitI den gesamten reellen hermiteschen Operatorraum aufspannen. Dieser hat Dimensiond²; normierte Zustände bilden eine affine Menge der Dimensiond²-1.

Hier ist der Abfragespan höchstens span(I,S0), Dimension<=2. Für d>=2 ist2<d². Es gibt daher nichtnull tracelose Hermitesche D mit tr(S0D)=0. Um einen strikt positiven Zustand herum bleiben W±epsilon D für ausreichend kleines epsilon positiv und liefern dieselben Daten. Bei S0=I ist der Informationsgehalt sogar nur die bereits bekannte Normierung.

Das schließt Identifizierbarkeit auf speziell eingeschränkten Präparationsfamilien nicht aus. Auch zusätzliche unabhängig spezifizierte Messungen oder eine nichtautonome Dynamik mit Eingriffen sind andere Datensätze. Falls rankS0=1, kann der erfolgreiche konditionierte Witness bereits auf einen eindimensionalen Zustand kollabieren; der allgemeine Anfangs-Witness bleibt dennoch nicht bestimmt. Der neue Gegenzeuge benutzt rankS0=2 und lässt auch den konditionierten Zustand mehrdeutig.

## 3. Neuer gleicher-Massen-Gegenzeuge

Runde75s vorab festgelegte strukturelle n4-Daten bleiben gleich, aber nun:

W_A=(3/5)uu†+(2/5)e4e4†,
W_B=(3/5)J/2+(2/5)e4e4†,

mit dem dort definierten rank2-Projektor J und u inJ. Die echte erste Selektion ist Tsel=J; beide Massen sind3/5. Beide erfolgreichen strukturellen Nachfolger einschließlich tatsächlichem Seed und Folgeereignis sind gleich. Auch alle gespeicherten Originalmassen stimmen überein. Trotzdem lauten die konditionierten Witness uu† und J/2: Reinheiten1 und1/2, Hilbert-Schmidt-Abstand1/sqrt2. Dieser Unterschied bleibt beim nächsten autonomen Ereignis erhalten.

Unabhängige exakte Diagonalkontrolle auf einem dreidimensionalen Anfangsträger: S=diag(1,1,0), W_a=diag(3/5,0,2/5), W_b=diag(3/10,3/10,2/5). Beide positiv/normiert, beide tr(SW)=3/5, aber unterschiedliche konditionierte Zustände. Der exakte Operator-Abfragespan hat Rang2 statt benötigtem Rang9; die Zustandsmenge hat affine Dimension8.

## Schluss für die Brückenfrage

Die autonome Überlebenshistorie ist eine echte Quelleninformation und darf nicht mit bloßer Normierung verwechselt werden. Sie ergänzt jedoch den strukturellen Verlauf nicht zu einem allgemeinen Witness-Bestimmungskriterium. Damit schließt auch diese naheliegende historische Ergänzung die in Runde75 präzisierte Zustandswahl nicht.

Dies ist **kein** Beweis, dass keine physikalische BFG-Brücke möglich wäre, und keine Aussage gegen die intern vorgegebene Witnessrolle. Selbst ein vollständig bekannter W würde die zusätzliche physikalische Bedeutung eines Energieoperators nicht allein aus der Speicherung erhalten. Es wird keine neue Auswahlregel, Messapparatur oder Energiegleichung eingeführt. Weiterer Fortschritt benötigt ein konkret vorhandenes zusätzliches Auswahl-/Kompatibilitätsargument oder unabhängig spezifizierte zusätzliche Messdaten, nicht bloß mehr autonome Ereignisindizes.

## Prüfungen und CI

Ein frischer lokaler PASS,4 Originalereignisse, keine Fehlvorläufe/Korrektur. Gleiche Massen3/5, danach1; gleiche historische Massen3/5; Reinheiten1 vs1/2, Abstand1/sqrt2. Maximaler aufgezeichneter Rest1.12e-16, Toleranz1e-10. Allgemeiner Gramsatz und Spanargument algebraisch, nicht aus zwei numerischen Ereignissen extrapoliert. [Vollständiger Prüftext/Rohdaten](AUTONOMOUS_SURVIVAL_IDENTIFIABILITY_CHECKS.md). Keine Original-/Audit-/Workflowänderung.

Am Ausgangsheadfa012644926d9de940a604323c8568e9a43845cd sind Actions40192012078/40192009876 beide completed/success. Sie prüfen die bestehende Pipeline; neue eingebettete mathematische Reproduktionen bleiben separate lokale Evidenz.
