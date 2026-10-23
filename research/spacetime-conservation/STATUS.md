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

- **Auswahlgrenze:** Das jeweils neu gewählte Paar der zwei kleinsten Y-Eigenwerte kann nach einem BFG-Ereignis ein anderes sein. Ein exakter einfacher-Spektrum-Zeuge zeigt den Wechsel {1,2}->{2,3}.
- **Lokales Paar allein nicht geschlossen:** Identische komprimierte K,F,W,Y können verschiedene Folgewertе liefern, weil die globalen Formationslasten das Mischgewicht alpha bestimmen. Exakter Unterschied der ersten lokalen Folge-Y-Komponente: 18396/788237.
- **Paar plus aktuelles alpha ebenfalls nicht autonom:** Ein zweiter rationaler Zeuge hat identisches Paar und alpha=169/723, aber unterschiedliche nächste alpha-Werte und unterschiedliche lokale Y nach zwei Ereignissen.
- **Konstruktiver Fortschritt:** Paar plus die formationsgewichtete Spektralverteilung des Komplements besitzt eine exakt aus dem vorhandenen BFG-Update abgeleitete geschlossene Folgedynamik auf dem Vollpersistenz-/Historienbereich. Nichtdiagonale Kopplungen von K,F,W zwischen Paar und Rest dürfen dabei vorhanden sein. Die Verteilung liefert alpha und wird durch dieselbe g_alpha-Abbildung fortgeschoben.
- **Frische Kontrolle:** 12 komplexe Präparationen, 36 Folgeereignisse, vier unitäre Projektionskontrollen; größter Rest <3e-15. Beide Faser-Gegenbeispiele gegen das vollständige Quell-Update geprüft.
- **Retained correction:** Eine anfänglich zu starke Erwartung an die vollständige Eigenwertreihenfolge wurde durch exakte Rechnung verworfen; die festgelegten Eingaben blieben gleich. Die tatsächlich bewiesene Paarwechsel-Aussage ist in der Herleitung abgegrenzt.

Damit ist ein konkreter umgebungsabhängiger Zwei-Moden-Faktor vorhanden. Die eindeutige physikalische Auswahl, Uhr, räumlicher Transport und lokale vollständige Energie-Impuls-Erhaltung bleiben offen. Nächster Schritt ist eine begründete, dynamisch erhaltene Paar-/Historienklasse oder eine Herleitung der Übergangs-/Stromregeln für diesen konkreten Faktor. GitHub-CI dieses neuen Codes ist getrennt vom bisherigen ersten Rundencode zu prüfen.



CI-Nachprüfung der Fortsetzung: Beide Actions-Jobs für Codecommit 73c4035e4e8da390e99f65463596f286a3b8a8b8 erfolgreich; PDF-Prüfsumme, beide Audits und sieben Tests bestanden. Details in [CI_VALIDATION.md](CI_VALIDATION.md).

## Fortsetzung: invariant gewählte Zwei-Moden-Klasse

[Neue Herleitung](STABLE_PAIR_DERIVATION.md), [vorab festgelegtes Protokoll samt offener Korrektur](STABLE_PAIR_PROTOCOL.md), [Prüfcode](stable_pair_audit.py), [Resultate](stable_pair_results.json).

Für Vollpersistenz und spektrale Extrema m,M mit **0<m<=M<=1/2 und m>=2M²** wurde eine nichtleere invariant erhaltene BFG-Klasse bewiesen. Bei einfachem Spektrum bleibt die Reihenfolge aller Y-Moden erhalten. Deshalb ist das Paar der zwei kleinsten Eigenwerte dort aus dem aktuellen Zustand wiedergewinnbar; die zusätzliche Paar-Historienmarkierung des vorigen allgemeinen Faktors ist auf dieser Klasse nicht mehr nötig. Die Wahl dieser Klasse und der Zwei-Moden-Ausleseregel ist weiterhin kein physikalisches Auswahltheorem.

Die positive Schranke jedes endlichen Spektrallückenschritts ist explizit bewiesen. Eine gleichmäßige unendliche numerische Lücke wird nicht behauptet: die Spektren konvergieren gegen null. Der geschlossene Paar-/Spektralumgebungsfaktor bleibt gültig. Nur Masse und erster Moment der Umgebung reichen nach einem weiteren exakten Gegenbeispiel auch hier nicht.

**Wichtige Dokumentkorrektur:** Die allgemeine Ableitungsformel in DERIVATION.md Abschnitt 8 war falsch gedruckt. Richtig ist g'_alpha(y)=2[(1-alpha)y-alpha]/(1+y)^3 und damit a(y)=2y(1-y)/[(1+y²)(1+y)^3]. Die zuvor numerisch geprüften Spezialwerte bei y=1/2 bleiben richtig. Die Formel und die neue Lückenschranke wurden korrigiert; zusätzliche symbolische und Drei-Punkt-Quellkontrollen bestanden. Anfangs passende numerische Stichproben allein hätten den Formeldefekt nicht aufgedeckt.

Frische Kontrollen: 48 exakte rationale Ereignisse, 36 komplexe Quellereignisse und drei zusätzliche Ableitungsvergleiche. Projektorrest <3e-13, lokaler Kernelrest <4e-15, Momentgegenbeispielrest ~1.1e-17. Physikalische Uhr, räumlicher Transport, vollständiger lokaler Viererstrom und Einstein bleiben offen. Der nächste konkrete Ansatz ist die quellenbasierte komponentenweise Austauschbilanz dieses nun aktuell auswählbaren Faktors. CI für den neuen Code ist separat zu prüfen.

CI-Nachprüfung der invarianten Klasse: Beide Actions-Jobs zu Codecommit fb034641f3e0c0344d24b66fee03cfa215b23bd2 erfolgreich; PDF-Prüfsumme, alle drei Audits und sieben Tests bestanden. Die frühere Formulierung zur allgemeinen Auswahlgrenze wurde präzisiert: Das Paar *kann* wechseln, nicht *muss* wechseln; die neu bewiesene invariante Klasse ist damit vereinbar. Details in [CI_VALIDATION.md](CI_VALIDATION.md).

## Fortsetzung: Komponentenbilanz und Grenzen einer Ausgleichsladung

[Herleitung](COMPONENT_EXCHANGE_DERIVATION.md), [Protokoll](COMPONENT_EXCHANGE_PROTOCOL.md), [Prüfcode](component_exchange_audit.py), [Resultate](component_exchange_results.json).

Im stabilen Zwei-Moden-Eigenrahmen gilt exakt **(p0,p1,p2,p3)_+=(p0,h p1,h p2,p3), 0<h<1**. Zwei feste lineare Ladungsrichtungen bleiben erhalten, zwei werden gedämpft. Der Defekt ist als Doppelkommutator aus den vorhandenen Kanaloperatoren hergeleitet; er besitzt eine ereignisweise mathematische Gradientenform, keine nachgewiesene physikalische Energie oder Lorentz-Wirkung.

Für jede additive Kandidatenladung aus fester linearer Paarladung plus beliebiger Funktion der übrigen aktuellen BFG-Daten gilt ein begrenztes Hindernis: Die übrigen Daten entwickeln sich unabhängig vom Paar-Kernelblock. Ein exakter +/-Zeuge hat identische Umgebungsfolgen, aber entgegengesetzte erforderliche Ausgleichsterme. Auch die reine Zweig-Marginale der beiden Quelle-Analysekanäle unterscheidet diese Eingaben nicht. Gemeinsame, gemischte Ladungen und andere physikalische Ergänzungen sind damit nicht allgemein widerlegt.

Die Ereignisabbildung bleibt als reelle lineare Abbildung invertierbar, ihre Inverse erhält aber nicht den gesamten positiven Kegel. Mit **historisch invers mitgeführten Observablen** lassen sich vier konstante mathematische Größen konstruieren. Dieser formale Ausweg und eine mittransportierte quadratische Form sind explizit dokumentiert; sie liefern ohne quellenbasierte Auswahl, Uhr und räumliche Interpretation keinen physikalischen Viererstrom.

Frische Prüfung: exakte algebraische Zertifikate sowie 24 gepaarte Ereignisse aus 12 komplexen Präparationen (48 vollständige Quellaufrufe); alle Reste <4e-15 bei vorab festgelegtem 1e-10. Grundcode und Manuskript unverändert. Nächste Abhängigkeit ist die quellenbasierte Auswahl einer relationalen Observablen-/Transport-/Uhrregel oder einer gemeinsamen Wechselwirkungsfunktion, nicht ein nachträglich passend gewählter Kompensator. CI des neuen Codes wird separat geprüft.

CI-Nachprüfung der Komponentenbilanz: Beide Actions-Jobs zu Codecommit 1e9d068e12c2ff371bbad3afc34aa329f67b2d82 erfolgreich. PDF-Prüfsumme, alle vier Audits, sieben Grenztests und Artefakt-Upload bestanden. Lokale Resultate und GitHub-Prüfung sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt belegt. Die physikalischen Abhängigkeiten bleiben offen.

## Fortsetzung: Zustandsuhren und exakte skalare Ereigniskoordinate

[Herleitung](CLOCK_DERIVATION.md), [vorab festgelegtes Protokoll](CLOCK_PROTOCOL.md), [Prüfcode](clock_audit.py), [Resultate](clock_results.json).

Auf der invarianten Klasse C gilt die neue gleichmäßige Schranke M_k <= (4/9)^k M_0. Daraus folgen drei konkrete positive, quotient-invariante Dauerkandidaten: konstante Dauer hat unendliche Summe, tr(Y)/n eine endliche Summe <=9M_0/5, und ln[tr(Y)/tr(Y_+)] eine teleskopisch unendliche Summe. Die gleiche BFG-Ereignisfolge bestimmt damit noch keine eindeutige physikalische Zeit oder Zeno-Aussage.

Konstruktiv existiert auf dem skalaren Zweig 0<y<=3/10 eine stetige Zustandskoordinate tau(y)=log_2 A(y), mit A(f(y))=2A(y), also exakt einem Tick je Ereignis. Eine konvergente Reihe samt expliziter Restschranke wurde hergeleitet. Periodische monotone Umparametrisierungen erhalten die Tickgleichung; eine zusätzliche asymptotische Normierung wählt diese mathematische Koordinate eindeutig, liefert aber noch keine physikalischen Sekunden oder räumlichen Fluss.

Frische Prüfung: 24 komplexe und drei skalare vollständige Quellereignisse. Alle Kriterien bestanden; skalare Quellreste <1e-16, Tickreste <3e-16. Die 48 analytischen Log-Rekurrenzen sind ausdrücklich keine 48 erfolgreichen Quellereignisse. Ein anfänglicher struktureller SymPy-Vergleich wurde durch exakte rationale Differenzprüfung berichtigt; die mathematische Identität blieb unverändert. CI des neuen Codes separat prüfen. Nächste eigenständige Abhängigkeit: geschlossene relationale Raumobservablen und ihr Transport aus den vorhandenen Paar-/Formations-/Witness-Daten.

CI-Nachprüfung der Uhrenkonstruktion: Beide Actions-Jobs zu Codecommit fe718cde8e7d0eca5eb70cfa82b663a9bcfe2a63 erfolgreich. Manuskript-Prüfsumme, alle fünf Audits, sieben Grenztests und Artefakt-Upload bestanden. Der spätere Dokumentationscommit beansprucht keine zusätzliche geprüfte Codeänderung; Details in [CI_VALIDATION.md](CI_VALIDATION.md).

## Fortsetzung: relationaler Paarrahmen und quotient-invariante Koordinaten

[Herleitung](RELATIONAL_FRAME_DERIVATION.md), [vorab festgelegtes Protokoll](RELATIONAL_FRAME_PROTOCOL.md), [Prüfcode](relational_frame_audit.py), [Resultate](relational_frame_results.json).

Eine nichtverschwindende Formations-Querverbindung zwischen den stabil ausgewählten Eigenlinien definiert einen kovarianten Pauli-Rahmen. Seine Kernelkoordinaten sind unter den zulässigen Basiswechseln invariant. Rahmen und Referenzamplitude bleiben unter dem vollständigen Vollpersistenz-Update erhalten. Zusammen mit den bisherigen Paar-/Umgebungsdaten entsteht ein explizit geschlossener reeller Koordinatenfaktor auf dem Quotienten.

Der Witness liefert eine alternative Referenz, auch bei verschwindender Formations-Querverbindung. Auf der Überlappung unterscheiden sich beide durch eine exakt berechnete konstante SO(2)-Drehung. An vollständig diagonalen symmetrischen Zuständen verbietet der Phasenstabilisator einen natürlichen transversalen Pauli-Rahmen; die Formationskarte lässt sich dort nicht stetig fortsetzen. Diese Grenze widerlegt keine anderen Referenzen an unsymmetrischen Zuständen.

34 vollständige Quellaufrufe, einschließlich acht Basiswechselkontrollen und eines Witness-Ausweichfalls, bestanden. Größter Rest <1.5e-13 bei vorgegebenem 1e-10. Ein struktureller symbolischer Hermitizitätsvergleich wurde durch exakte Differenzvereinfachung korrigiert; keine mathematische Formel oder Schwelle wurde angepasst. CI separat prüfen.

Damit ist die interne relationale Referenz konstruktiv geklärt, räumliche Bewegung und physikalischer Viererstrom bleiben offen. Die Dämpfung der zwei transversalen Komponenten bleibt auch in den quotient-invarianten Koordinaten bestehen. Nächste mathematische Reichweitenfrage: Eintritt allgemeinerer Vollpersistenzdaten in die stabile Klasse und Verhalten der Referenzkarten bei Auswahl/Seed; für physikalischen Transport fehlen weiterhin Ereignisnachbarschaft und eine quellenbegründete Verschiebungs-/Stromabbildung.
