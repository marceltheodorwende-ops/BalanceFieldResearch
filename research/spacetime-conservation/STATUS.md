# Geprüfter Stand: erste BFG-Untersuchungsrunde

Datum: 23. Oktober 2026. Auftrag: [verbindlicher Prompt](MANDATE.de.md).
**Erste Runde abgeschlossen; physikalische Herleitung weiterhin offen.** Exakte Aussagen betreffen die angegebenen mathematischen Klassen. Keine neue empirische Bestätigung, kein unabhängiges Peer Review.

| Frage | Ergebnis | Evidenz / Grenze |
|---|---|---|
| Bestehender vollständiger Update reproduziert? | PASS im geprüften Sektor | 32 komplexe Vollpersistenzfälle in n=2,3,4,5; 12 zusätzliche unitäre Kovarianzkontrollen. Unabhängige ausgerichtete Form stimmt bis <4e-15 überein. |
| Gibt es einen erhaltenen Kernel-Skalar? | BFG-abgeleitet, sektoriell | tr K bleibt bei P=I und 0<Y<I erhalten. Einheiten sind keine nachgewiesenen Joule. |
| Welche linearen K-Ladungen bleiben erhalten? | Exakt charakterisiert | Für fest transportiertes A und alle K genau dann, wenn [A,Y]=0. Keine Auswahl physikalischer Energie/Impulsgewichte. |
| Bleibt tr K über alle Ereignisse erhalten? | In dieser Verallgemeinerung widerlegt | Exakte Rangverlust- und Seed-Gegenbeispiele. |
| Gibt es eine vollständige skalare Kernelbilanz? | BFG-abgeleitet für nichtterminale Ereignisse | Delta tr K=tr[K(D-I)], D aus den beiden Blöcken des echten Analyse-Isometrie-U. 24 partielle Trägerfälle bestätigt; größter normierter Rest <5e-16. |
| Ist tr(FK) eine universelle Energie? | Kandidat widerlegt | Nach einem Ereignis 1 -> sqrt(1152/1295)~0.943173. Bei [F,Y]=0 wird die gewichtete Ladung hingegen erhalten. |
| Reichen skalare Zusammenfassungen als Zustand? | Konkrete Projektion nicht geschlossen | Gleiche (n,tr K,tr F,tr W,tr Y,tr FK), verschiedene nächste tr FK. Vollständiger Zustand nicht widerlegt. |
| Nichtkonstante stetige skalare y-Energie? | Im genannten Bereich ausgeschlossen | Eine stetig bis zum Attraktor fortsetzbare erste Integrale ist konstant, übrige skalare Konstanten festgehalten. |
| Lorentz-Signatur durch positives internes G? | Direkter injektiver Pullback ausgeschlossen | Positive Kongruenz bleibt positiv; Aussage nur über diesen Ansatz. |
| BFG-interner algebraischer Lorentz-Träger? | Konstruktive Standardmathematik | Herm(C^2) besitzt reelle Dimension 4, det X=x0^2-|x|^2 und positiven Zukunftskegel. Zwei-Moden-Auswahl und physikalische Interpretation offen. |
| Ist der geprüfte Update eine Lorentz-Transformation? | Für die unveränderte Determinantenmetrik widerlegt | Null -> zeitartig mit exaktem Defekt 143/1295. Kein generelles No-Go für Lorentz-kovariante Dynamik mit weiteren Feldern. |
| Ist die Y-Dynamik im selben Lift Lorentz-konform? | Geprüfte Identifikation widerlegt | Vollständige endogene Ableitung: Zeit-/Raumfaktor 14/5 am Skalarpunkt; exakter Null-Defekt 4864/50625. |
| Gemeinsame physikalische Wirkung, Stress und Einstein? | OPEN | Raumzeit-/Uhr-/Stromabbildung, Symmetrie, physikalische Normierung und Wirkungsherleitung fehlen. |

## Frische Ausführung
- python audit.py: Exit 0, alle endlichen Kontrollassertionen erfüllt.
- python -m unittest -v test_audit: 7 Tests bestanden.
- 19 zusätzliche exakte rationale Skalarkontrollen; 16 Positivkegelkontrollen; symbolische Determinanten-/Hesse-Matrix und algebraische Gegenbeispiele.
- Quellcode vor Import gegen ursprüngliche Git-Blob-ID geprüft. [Maschinenlesbare Resultate](results.json), [Quellenmanifest](SOURCE_MANIFEST.json), [Herleitungen](DERIVATION.md).
- Ein zusätzlicher sechsfacher Trajektorienversuch ist **PARTIAL**: fünf nichtterminale Schritte geprüft, dann bestehender numerischer Analyse-Rangabbruch im sechsten Schritt bei maximalem Y-Eigenwert etwa 3.87e-14. Die Bilanz der fünf abgeschlossenen Schritte hat Rest etwa 3.55e-15. Dieser Abbruch ist keine exakte BFG-Terminalitätsaussage; Grundcode und Toleranz wurden nicht geändert.
- GitHub-CI ist separat zu prüfen; lokale Resultate bedeuten nicht automatisch einen erfolgreichen Actions-Lauf.

## Fehler und Korrekturen bleiben sichtbar
Das erste lokale Starten des Audits scheiterte an einem zusätzlich angehängten Zeilenumbruch der lokalen Quellkopie. Die Kopie wurde auf die exakten gepinnten Bytes zurückgesetzt; der Grundcode wurde nicht geändert.
Die ursprüngliche Protokollerwartung eines nichtleeren Seed-Komplements im skalaren Rangverlustfall C3 war falsch. Das wurde durch algebraische Ranganalyse vor dem ersten numerischen Lauf korrigiert; C3 blieb erhalten und ein eigener nichtskalarer Seed-Fall C3b kam hinzu.
Der C10-Trajektorienversuch stoppte zunächst mit dem unveränderten ArithmeticError. Danach wurde nur der neue Prüfbericht um die explizite Aufzeichnung dieses numerischen Abbruchs erweitert; keine sechsfach erfolgreiche Fortsetzung wird behauptet.

## Nächste notwendige Abhängigkeit
Ein aus BFG ausgewählter **lokaler Zwei-Moden-Ereignisträger mit räumlichem Transport, Uhr und einer Interpretation des vorzeichenbehafteten Kernelflusses**. Vor einer Einstein-Gleichung sind zu spezifizieren und zu prüfen:
1. Auswahlregel aus Xi oder ausdrücklich benötigter Historie, Definitions-/Zielraum, Quotientenkovarianz und Verhalten bei Rang-/Seed-Ereignissen.
2. Geschlossene Folgedynamik nach Abschnitt 89; eine skalare Traceliste reicht nachweislich nicht.
3. Quelle und Austausch aller vier Stromkomponenten aus derselben Dynamik; globale Trace-Buchführung allein liefert keinen lokalen Spannung-Energie-Tensor.
4. Erst danach eine ausgewählte Wirkung/Symmetrie, physikalische Normierung und ein kontrollierter Raumzeit-Grenzfall.

Der BFG-Quelltext bestimmt bislang keine eindeutige solche Regel. Eine eingesetzte Lorentz-Signatur, eine per Definition ausgleichende Reservoirvariable oder eine Wirkung mit frei gewählten Zwangsmultiplikatoren schließt diese Lücke nicht. Eine spätere Quelle oder konkrete Auswahlregel kann gezielt gegen die hier veröffentlichten Zeugen geprüft werden.

## Fortsetzung: Zwei-Moden-Träger und geschlossener Umgebungsfaktor

Geprüfte Fortsetzung vom 23. Oktober 2026: [Herleitung](PAIR_DERIVATION.md), [vorab festgelegtes Protokoll](PAIR_PROTOCOL.md), [Prüfcode](pair_audit.py), [Resultate](pair_results.json).

- **Auswahlgrenze:** Das jeweils neu gewählte Paar der zwei kleinsten Y-Eigenwerte muss nach einem BFG-Ereignis ein anderes sein. Ein exakter einfacher-Spektrum-Zeuge zeigt den Wechsel {1,2}->{2,3}.
- **Lokales Paar allein nicht geschlossen:** Identische komprimierte K,F,W,Y können verschiedene Folgewertе liefern, weil die globalen Formationslasten das Mischgewicht alpha bestimmen. Exakter Unterschied der ersten lokalen Folge-Y-Komponente: 18396/788237.
- **Paar plus aktuelles alpha ebenfalls nicht autonom:** Ein zweiter rationaler Zeuge hat identisches Paar und alpha=169/723, aber unterschiedliche nächste alpha-Werte und unterschiedliche lokale Y nach zwei Ereignissen.
- **Konstruktiver Fortschritt:** Paar plus die formationsgewichtete Spektralverteilung des Komplements besitzt eine exakt aus dem vorhandenen BFG-Update abgeleitete geschlossene Folgedynamik auf dem Vollpersistenz-/Historienbereich. Nichtdiagonale Kopplungen von K,F,W zwischen Paar und Rest dürfen dabei vorhanden sein. Die Verteilung liefert alpha und wird durch dieselbe g_alpha-Abbildung fortgeschoben.
- **Frische Kontrolle:** 12 komplexe Präparationen, 36 Folgeereignisse, vier unitäre Projektionskontrollen; größter Rest <3e-15. Beide Faser-Gegenbeispiele gegen das vollständige Quell-Update geprüft.
- **Retained correction:** Eine anfänglich zu starke Erwartung an die vollständige Eigenwertreihenfolge wurde durch exakte Rechnung verworfen; die festgelegten Eingaben blieben gleich. Die tatsächlich bewiesene Paarwechsel-Aussage ist in der Herleitung abgegrenzt.

Damit ist ein konkreter umgebungsabhängiger Zwei-Moden-Faktor vorhanden. Die eindeutige physikalische Auswahl, Uhr, räumlicher Transport und lokale vollständige Energie-Impuls-Erhaltung bleiben offen. Nächster Schritt ist eine begründete, dynamisch erhaltene Paar-/Historienklasse oder eine Herleitung der Übergangs-/Stromregeln für diesen konkreten Faktor. GitHub-CI dieses neuen Codes ist getrennt vom bisherigen ersten Rundencode zu prüfen.


