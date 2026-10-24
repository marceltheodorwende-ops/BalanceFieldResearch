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

CI-Nachprüfung der relationalen Rahmen: Beide Actions-Jobs zu Codecommit 1392c40e0e5bf13e83b7af93df6cb181ec8b42a9 erfolgreich. Manuskript-Prüfsumme, alle sechs Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Codecommit und späterer Dokumentationsstand sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.

## Fortsetzung: endlicher Eintritt aus dem gesamten positiven Vollpersistenzsektor

[Herleitung](EVENTUAL_CLASS_DERIVATION.md), [vorab festgelegtes Protokoll](EVENTUAL_CLASS_PROTOCOL.md), [Prüfcode](eventual_class_audit.py), [Resultate](eventual_class_results.json).

Für P=I, F>0 und 0<Y<I ist jetzt ohne anfängliche C-Einschränkung bewiesen: M_k<=2^-k M_0. Mit delta=lambda_min(F)/tr(F)>0 folgen m_+>=delta M²/16 und M_+<=2M². Sobald M²<=delta/128, liegt der Folgezustand in C; eine explizite endliche Ereignisschranke ist angegeben. Der stabile Bereich ist damit für diesen ganzen autonomen Vollpersistenzsektor nach endlich vielen Ereignissen erreichbar.

Die einfache Spektralstruktur folgt daraus ausdrücklich NICHT: Ein exakter anfangs einfacher n=3-Zeuge kollidiert an der Grenze der Zwei-Moden-Auswahl, obwohl der Folgezustand schon in C liegt. Ein Y-only-Rang-zwei-Selektor ist dort mehrdeutig. Die Formation löst diesen konkreten Gleichstand auf; eine allgemeine Y/F/W-Auswahlregel ist als nächster Kandidat zu prüfen. Symmetrische Gegenfälle bleiben erhalten.

Ein weiterer exakter Zeuge erhöht tr(Y) um ca. 0.168954 trotz Halbierungsschranke für M. Der bisherige positive Trace-Log-Uhrkandidat gilt daher weiterhin nur auf seinem bewiesenen C-Bereich, nicht allgemein. Die summierbare Lastdauer tr(Y)/n hat dagegen auf dem größeren Sektor die Schranke 2M_0.

Frische Evidenz: 12 exakte Präparationen mit insgesamt 20 rationalen Ereignissen bis zum C-Eintritt; 24 komplexe und zwei vorgeschriebene vollständige Quellaufrufe bestanden. Ein nachträglicher algebraischer Diagnoseschritt prüft die Formationsauflösung des einzelnen Kollisionszeugen, ohne ihn als vorab geplantes allgemeines Auswahltheorem auszugeben. CI separat prüfen. Physikalische Lokalität, Uhrkalibrierung, vollständiger Viererstrom und Einstein bleiben offen.

CI-Nachprüfung des Eintrittssatzes: Beide Actions-Jobs zu Codecommit b972c74aa61fcc57304ccbe3856544e6e8edac82 erfolgreich. Manuskript-Prüfsumme, alle sieben Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und späterer Dokumentationsstand sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.

## Fortsetzung: Y/F/W-Gleichstandsauflösung und vier erhaltene Paar-Koordinaten

[Herleitung](LEX_SELECTOR_DERIVATION.md), [vorab festgelegtes Protokoll](LEX_SELECTOR_PROTOCOL.md), [Prüfcode](lex_selector_audit.py), [Resultate](lex_selector_results.json).

Die deklarierte lexikografische Auswahl verfeinert Y-Eigenräume zunächst durch komprimierte Formation, danach durch komprimierten Witness. Sie ist kovariant und auf C erhalten, sofern kein verbleibender unaufgelöster Block die Rang-zwei-Grenze schneidet. Der Paar-/Spektralumgebungsfaktor bleibt dabei exakt geschlossen; einfaches Y-Spektrum ist nicht mehr nötig. Sowohl der vorige Kollisionszeuge als auch ein eigener Witness-Ausweichfall werden aufgelöst.

Die Auswahl ist ausdrücklich partiell: Vollsymmetrie bleibt unaufgelöst, und ein exakter Pfad zeigt einen Sprung beim Übergang zu einer Spektralentartung. Keine globale glatte oder physikalisch eindeutige Auswahl wird behauptet.

Konstruktiver Sonderfall: Liegt das ausgewählte Paar in EINEM Y-Eigenraum, gilt K_S,+=K_S. Mit stabilen Formations-Eigenlinien und nichtverschwindender Witness-Referenz sind damit vier quotient-invariante relationale Kernelkoordinaten erhalten, ohne inverse Historiengewichte. Ein nichttrivialer vollständiger n=4-Zeuge erhält alle vier lokalen Komponenten, während sich der globale Kernel um ca. 0.01548 ändert. Das widerspricht der früheren Dämpfung bei ungleichen Paarlasten nicht und liefert allein keinen physikalischen Viererstrom.

31 vollständige Quellaufrufe im finalen Audit, exakte Auswahl-/Positivitäts-/Entartungskontrollen und Basiswechseltests bestanden; größter Rest <2e-13. Numerische Gruppierungsschwellen sind von exakter Entartung getrennt, aufgelöste Testlücken liegen mehr als 2.3 Millionen Schwellen auseinander. CI separat prüfen. Nächste physikalische Abhängigkeit: eine BFG-interne Ereignisnachbarschaft oder räumliche Observable samt geprüfter Transport-/Kontinuitätsregel. Auswahl/Seed und Kartenwechsel bleiben zusätzliche mathematische Grenzen.

CI-Nachprüfung der Y/F/W-Auswahl: Beide Actions-Jobs zu Codecommit f6a00b8fa6d388dd5b9eb0afb209f31fb7545a97 erfolgreich. Manuskript-Prüfsumme, alle acht Audits, sieben Grenztests und Artefakt-Upload bestanden. Der spätere Dokumentationscommit ist vom geprüften Codestand in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.

## Fortsetzung: interne Graphen und exakter kanalbasierter Kernelstrom

[Herleitung](MODE_GRAPH_DERIVATION.md), [vorab festgelegtes Protokoll](MODE_GRAPH_PROTOCOL.md), [Prüfcode](mode_graph_audit.py), [Resultate](mode_graph_results.json).

Ein Graph aus normierten Formations-/Witness-Kanten und Kernel-Kohärenzbeträgen besitzt auf den erhaltenen Y-Moden eine geschlossene Abschwächungsdynamik. Die Knotenbestände bleiben dort fest. Die naheliegende Formel 2 Im tr(Q_i R Q_j K) ist dagegen kein universeller Kontinuitätsstrom: Ein exakter +/-Zeuge hat identische Graphdaten, entgegengesetzte Ströme und Bilanzdefekte +/-1/2. Auch eine anfangs geschlossene Dreieckszirkulation wird nicht allgemein erhalten.

Konstruktive Alternative direkt aus denselben Quelloperatoren:
J^Phi_ij=sum_a Re tr(P_i T_a P_j [T_a,K]).
Dieser Strom ist antisymmetrisch und erfüllt exakt Delta tr(P_i K)+sum_j J^Phi_ij=0 für erhaltene orthogonale Knotenprojektoren. Auf Y-Knoten verschwindet er; auf nichtkommutierenden Formationseigenknoten kann er einen nichtverschwindenden Bestandsaustausch tragen. Ein exakter positiver Zwei-Knoten-Zeuge hat den Fluss 1-31/sqrt(1001)≈0.0201837, ohne erfundene Reservoirvariable.

33 vollständige Quellaufrufe im finalen Audit bestanden; größter Strom-Bilanzrest <7.6e-15, übrige Identitätsreste <9e-14. Algebraische Ketten-/Zyklusgrenzen, Phasen-Faserverlust und die negativen Stromkandidaten bleiben sichtbar. CI separat prüfen.

Dies ist eine interne Kernel-Kontinuitätsgleichung, noch keine physikalische Energie-Impuls-Erhaltung im Raum. Formationseigenmoden sind bislang keine belegten räumlichen Orte. Nächste Abhängigkeit: notwendige Kohärenzdaten für die Geschlossenheit des Formation-Knotenstroms und eine quellenbasierte, auf Lokalität geprüfte Kanal-Nachbarschaft; physikalische Kalibrierung, Viererstrom und Einstein bleiben offen.

CI-Nachprüfung der Kanal-Kontinuität: Beide Actions-Jobs zu Codecommit c51eb79911c9818002115d8ef5455d38b79dae37 erfolgreich. Manuskript-Prüfsumme, alle neun Audits, sieben Grenztests und Artefakt-Upload bestanden. Die Dokumentationsschranke für den maximalen Normbudget-Rest ist auf <9e-14 präzisiert (final ca. 8.04e-14), unverändert unter 1e-10. Geprüfter Code und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.

## Fortsetzung: Populations-Geschlossenheit und exaktes Kohärenzgedächtnis

[Herleitung](POPULATION_CLOSURE_DERIVATION.md), [vorab festgelegtes Protokoll](POPULATION_CLOSURE_PROTOCOL.md), [Prüfcode](population_closure_audit.py), [Resultate](population_closure_results.json).

Die positiven symmetrischen Kanalgewichte P_ij=sum_a |(T_a)_ij|² bilden eine doppelt-stochastische Matrix. Für diagonalen Kernel gilt q_+=Pq und der vorige Quellenstrom reduziert sich auf P_ij(q_i-q_j). Allgemein tritt jedoch diag Phi(O K) hinzu. Exakte Geschlossenheit für alle K erfordert D Phi O=0, äquivalent zur Invarianz der Formation-Diagonalalgebra. Populations-Geschlossenheit allein entscheidet auf Graphen mit Zyklen noch nicht jeden Kantenstrom.

Ein positiver Zwei-Moden-Faserzeuge mit identischen Populationen, Kohärenzbeträgen und Kanalgewichten liefert unterschiedliche Folgebestände (erste Komponentendifferenz ca. 0.00542986). Auch anfangs diagonale Zustände erzeugen Kohärenz; die Quelle weicht im zweiten Schritt um ca. +/-5.21695e-6 vom wiederholt dephasierten Markovmodell ab. Eine exakte, aus der Quelle eliminierte Gedächtnisformel beschreibt diesen Beitrag ohne neue Reservoirvariable.

Konstruktive Ausnahme: Ein zur Y-Basis unvoreingenommener Formation-Zwei-Moden-Sektor besitzt trotz [F,Y]!=0 eine geschlossene Population-/Lastdynamik mit nichtverschwindendem Kanalstrom. Die Y-Eigenwerte müssen als Geometriedaten mitgeführt werden; q allein bestimmt den zeitabhängigen Kanal nicht. Keine physikalische Auswahl oder Robustheit dieses Sonderbereichs wird behauptet.

36 vollständige Quellaufrufe im finalen Audit bestanden; Populations-/Gedächtnisreste <8.3e-15. Der erste Lauf scheiterte erst beim JSON-Export symbolischer Brüche; nach Stringserialisierung frisch wiederholt, ohne veränderte Gleichung oder Schranke. CI separat prüfen. Nächste Abhängigkeit: Kanal-Nachbarschaft, Reichweite und räumliche Lokalität samt physikalischer Auswahl/Kalibrierung. Vollständiger Energie-Impuls-Strom, Raumzeitwirkung und Einstein bleiben offen.

CI-Nachprüfung der Populations-Geschlossenheit: Beide Actions-Jobs zu Codecommit 4bbdc990e264721bbd03333f895f4ddc963fac4a erfolgreich. Manuskript-Prüfsumme, alle zehn Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Codecommit und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.

## Fortsetzung: Kanalreichweite auf einer deklarierten internen Kette

[Herleitung](CHANNEL_RANGE_DERIVATION.md), [vorab festgelegtes Protokoll](CHANNEL_RANGE_PROTOCOL.md), [Prüfcode](channel_range_audit.py), [Resultate](channel_range_results.json).

Die echten Kanaloperatoren sind T_C=sqrt(alpha)(alpha I+beta Y²)^-1/2 und T_B=sqrt(beta)Y(alpha I+beta Y²)^-1/2. Eine tridiagonale Y-Kette erzwingt daher keinen strikt nächsten-Nachbar-Kanal. Ein exakter positiver Drei-Knoten-Zeuge hat Y13=0, aber einen direkten Übergang P31≈7.76536e-6 im vollständigen Quellereignis. Strikte Positivität ist durch ein Konvexitätszertifikat bewiesen, nicht nur numerisch geschätzt.

Konstruktiv liefert eine normkonvergente Binomialentwicklung kontrollierte endliche Bandapproximationen und eine geometrische, zustandsabhängige Abschätzung entfernter Kanalgewichte. Sie wird nicht als veränderte Quellendynamik eingesetzt. Vollständig getrennte Y-reduzierende Blöcke besitzen dagegen exakt keine kreuzenden Kanalströme; ihre Kernelbestände bleiben erhalten. Globales alpha verhindert dennoch die unbegründete Behauptung autonomer Teilsysteme.

20 vollständige Quellaufrufe im finalen Audit bestanden, einschließlich vier Basiswechsel- und vier Blockkontrollen; größte Identitätsreste <2.6e-15. Sehr kleine Ferngewichte (~2.69e-19) sind als Matrixfunktionsschätzungen ohne relative Positivitätszertifizierung durch den Quellcode gekennzeichnet. CI separat prüfen.

Dies widerlegt nur die geprüfte strikte Ein-Kanten-Regel auf der gewählten internen Nachbarschaft. Keine Aussage über eine verletzte physikalische Lorentz-Kausalität oder universell ausgeschlossene endliche Reichweiten. Nächste Abhängigkeit: Erhaltung/Veränderung der Lokalitätsbeschreibung unter wiederholten Y-Ereignissen und globalem alpha-Rückkopplung; räumliche Auswahl, Kalibrierung, Viererstrom und Einstein bleiben offen.

CI-Nachprüfung der Kanalreichweite: Beide Actions-Jobs zu Codecommit 37d45d42422ccf8b704410519f2a1eb6eee2ea19 erfolgreich. Manuskript-Prüfsumme, alle elf Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und späterer Dokumentationsstand sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.

## Fortsetzung: wiederholte Veränderung der aktuellen Y-Nachbarschaft

[Herleitung](ADJACENCY_EVOLUTION_DERIVATION.md), [vorab festgelegtes Protokoll](ADJACENCY_EVOLUTION_PROTOCOL.md), [Prüfcode](adjacency_evolution_audit.py), [Resultate](adjacency_evolution_results.json).

Nicht nur der Kernelkanal reicht über die anfängliche Kette hinaus: Das echte Y-Update erzeugt selbst eine neue direkte Kante. Für den Drei-Knoten-Zeugen ist Y1,13=413979576/2486758594075≈0.000166474 exakt positiv. Ein neuer Beweis über die tatsächliche endogene alpha-Folge zeigt: Diese Kante bleibt nach JEDEM endlichen weiteren Ereignis strikt vorhanden. Die beiden ursprünglichen Kanten bleiben ebenfalls positiv; die Kette wird zum Dreieck.

Dabei bleiben alle Spektralprojektoren fest, weil Y_k=phi_k(Y0). Feste Spektralalgebra ist also keine feste dünn besetzte Formation-Knoten-Nachbarschaft. Gewichte schrumpfen gegen null; eine endliche physikalische Zeit oder unbegrenzt fortsetzbare Gleitkommarechnung folgt daraus nicht. Die Konvexitätsrechnung friert alpha nur im Hilfsargument der einzelnen spektralen Funktion ein und variiert nicht die vollständige endogene Zustandsableitung.

Neun exakte rationale Ereignisse sowie zwölf vollständige Quellaufrufe inklusive Basiswechselkontrollen bestanden; größter Rest <7.7e-16. C-Mitgliedschaft wurde mit rationalen Gershgorin-Schranken kontrolliert. CI separat prüfen.

Ein initialer Referenzgraph kann als deklarierte Historienauslese geprüft werden; das Löschen neu erzeugter Y-Kanten wäre dagegen eine Modelländerung. Nächste Abhängigkeit: kontrollierte mehrfache Kanal-Komposition relativ zu einem solchen Referenzgraphen, ohne aktuelle Matrixsparsamkeit als physikalische Lokalität auszugeben. Raumzeit, physikalischer Viererstrom und Einstein bleiben offen.

CI-Nachprüfung der wiederholten Nachbarschaftsentwicklung: Beide Actions-Jobs zu Codecommit 1c6bb478a2070018e34938ce2309aec6bb119603 erfolgreich. Manuskript-Prüfsumme, alle zwölf Audits, sieben Grenztests und Artefakt-Upload bestanden. Der geprüfte Codestand ist vom späteren Dokumentationscommit in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: exakte mehrfache Kanal-Komposition

[Herleitung](COMPOSITION_DERIVATION.md), [Vorabprotokoll](COMPOSITION_PROTOCOL.md), [Prüfcode](composition_audit.py), [Resultate](composition_results.json).

Im erhaltenen anfänglichen Y-Spektralrahmen ist der vollständige N-Ereignis-Kanal exakt ein Schur-Multiplikator mit H_ab=Produkt_k h_ab(k). Eine Tensorprodukt-Gram-Darstellung beweist vollständige Positivität, Unitalität und Spurtreue. Die tatsächliche endogene Geometriefolge wird unverändert mitgeführt; keine Umordnung der nichtlinearen Ereignisse wird behauptet.

Für anfangs diagonale Formation-Populationen ist die ganze effektive Übergangsmatrix aus dieser Form oder sämtlichen Kraus-Wörtern berechenbar, symmetrisch und doppelt-stochastisch. Sie weicht entlang der neuen geprüften Pfadfolgen vom Produkt einzelner Populationsmatrizen ab: Kohärenzen dürfen nicht zwischen den Ereignissen gelöscht werden. Nach drei Ereignissen liegen die vier Matrixabweichungen zwischen 1.31e-5 und 3.36e-5.

28 vollständige Quellaufrufe in n=3,4,5,6 einschließlich vier Basiswechselkontrollen bestanden; sämtliche Identitätsreste <9.1e-15. Sehr kleine Ferngewichte sind nur absolut kontrolliert. Keine unendliche numerische Fortsetzung oder physikalische Lokalität wird behauptet. CI separat prüfen.

Nächster Schritt: kontrollierte mehrschrittige Reichweite gegenüber dem anfänglichen Referenzgraphen oder eine quellenbegründete räumliche Auswahl. Physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein bleiben offen.


CI-Nachprüfung der Kanal-Komposition: Beide Actions-Jobs zu Codecommit 5aa2bdf8f1f590dda52abd7876a611118c04bbaa erfolgreich. Manuskript-Prüfsumme, alle dreizehn Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und nachfolgende Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: bewiesener Mehrereignis-Tail im anfänglichen Graphen

[Herleitung](MULTIEVENT_RANGE_DERIVATION.md), [Vorabprotokoll](MULTIEVENT_RANGE_PROTOCOL.md), [Prüfcode](multievent_range_audit.py), [Resultate](multievent_range_results.json).

Eine Vektor-Bernsteinapproximation des vollständigen Kraus-Tensorprodukts liefert jetzt die kontrollierte Schranke tr(Q_außerhalb K_N)<=min(1,L_N²(M0-m0)²/(4d)) tr(K0) jenseits des d-Balls im anfänglichen Y0-Graphen. Sie gilt für positive, anfangs auf S unterstützte Kernel einschließlich Kohärenzen. L_N ist explizit aus den tatsächlichen endogenen alpha- und Spektralintervallfolgen beschränkt. Weder wiederholte Dephasierung noch Kantentrunkierung wird eingesetzt.

Der Beweis verbindet Polynome in Y0 mit Graphdistanz und kontrolliert den gesamten entfernten Bestand, nicht nur einzelne Übergänge. Die Schranke ist konservativ und zustands-/folgenabhängig; keine universelle Geschwindigkeit oder strikte endliche Reichweite wird behauptet. Physikalische Orte und Sekunden sind weiterhin nicht ausgewählt.

21 vollständige Quellaufrufe auf Pfaden n=6,10,14, symbolische Tensornormkontrolle und 27 Grad-/Tail-Kontrollen bestanden. Quellrest <6.5e-15, Kovarianzrest <3.1e-15, kein Schrankenverstoß. Für n=14,N=3,d=3 liegt die Schranke bei ca. 0.01016, die gemessene entfernte Punktmassenpopulation bei ca. 1.65e-10; die konservative Lücke bleibt sichtbar. CI separat prüfen.

Nächste Abhängigkeit: langfristiges Wachstum der Schranken und BFG-interne Auswahl von Raummaß und physikalischer Uhr. Vollständiger Energie-Impuls-Strom, Lorentz-Dynamik und Einstein bleiben offen.


CI-Nachprüfung der Mehrereignis-Reichweite: Beide Actions-Jobs zu Codecommit 8d4e1ba9c3efab03749ed06d1fe3414e25dde559 erfolgreich. Manuskript-Prüfsumme, alle vierzehn Audits, sieben Grenztests und Artefakt-Upload bestanden. Der geprüfte Codestand und die spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: kontinuierliche Kanal-Interpolation und Zeitmehrdeutigkeit

[Herleitung](INTERPOLATION_DERIVATION.md), [Vorabprotokoll](INTERPOLATION_PROTOCOL.md), [Prüfcode](interpolation_audit.py), [Resultate](interpolation_results.json).

Der homogene Schur-Ansatz h_ab(t)=h_ab^t ist nicht allgemein positiv: Ein exakt vorab benannter Drei-Moden-Zeuge auf C mit alpha=1/26 hat für den Halbzeitschritt det≈-2.08285e-6 und kleinsten Eigenwert≈-3.45960e-5. Ein positiver Kernel wird damit auf einen indefiniten Kernel abgebildet. Nur dieser Ansatz ist widerlegt, keine allgemeine kontinuierliche BFG-Einbettung.

Zwei explizite positive Alternativen — konvexer Kanalpfad und Winkel-Gram-Pfad — besitzen denselben BFG-Endpunkt, unterscheiden sich aber zu Zwischenzeiten und erfüllen am Zeugen keine homogene Semigruppengleichung. Eine diskrete Kernelabbildung bestimmt dadurch noch keine eindeutige physikalische Zeitinterpolation; keine Alternative wird als zusätzliche Grundgleichung ausgewählt.

Exakte algebraische Zertifikate, 16 vollständige Quellaufrufe und Zwischenzeit-PSD-Kontrollen bestanden; Quellrest <3.5e-15, Kovarianzrest <1.2e-15. CI separat prüfen. Die gemeinsame kontinuierliche Entwicklung von Geometrie und Kernel, die physikalische Uhrkalibrierung und räumliche Interpretation bleiben offen. Nächster konstruktiver Ansatz ist ein begründeter gemeinsamer Grenzbereich oder eine direkte diskrete Zeit-/Stromauswahl aus BFG; eine frei eingesetzte Interpolation schließt diese Lücke nicht.


CI-Nachprüfung der Kanal-Interpolation: Beide Actions-Jobs zu Codecommit d137dfc1654acde0b7bf0b45c8872b706faf264d erfolgreich. Manuskript-Prüfsumme, alle fünfzehn Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und nachfolgende Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: schwache Aufspaltung und gemeinsame Kleinschrittgrenze

[Herleitung](WEAK_SPLITTING_DERIVATION.md), [Vorabprotokoll](WEAK_SPLITTING_PROTOCOL.md), [Prüfcode](weak_splitting_audit.py), [Resultate](weak_splitting_results.json).

Der echte Kernelkanal ist exakt das symmetrische Mittel zweier unitärer Konjugationen. Für Y=yI+epsilon A ergibt die vollständige endogene Rechnung den zweiten Koeffizienten -[A,[A,K]]/(8y²). Wiederholte Anwendung DESSELBEN eingefrorenen Kanals besitzt einen mathematischen dissipativen Grenzwert; sie wird ausdrücklich nicht als autonome BFG-Trajektorie ausgegeben.

Die gemeinsame Euler-Skalierung delta t=epsilon² scheitert dagegen bei festem y>0 an einem endlichen Geometriesprung. Am geprüften y=1/4 ist y_+=32/425, also y_+-y=-297/1700 auch im Grenzfall verschwindender Aufspaltung. Der kleine Kerneldefekt allein liefert somit keine kleine vollständige Zustandsänderung und keine kontinuierliche BFG-Zeit.

Symbolische Koeffizientenrechnung und 15 vollständige Quellaufrufe bestanden; exakter Zwei-Unitär-Rest <1.5e-15, Kovarianzrest <1.9e-15. Die vorab festgelegten Generator-/Vergleichs-Konvergenzkontrollen bestanden. Bis 64000 eingefrorene Kanalpotenzen sind analytisch-spektrale Vergleichsauswertungen, keine entsprechend vielen Quellereignisse. CI separat prüfen.

Der Gegenbefund betrifft diese feste-Hintergrund-Skalierung. Gemeinsame Rand-/relative-Last-Grenzen oder eine direkte diskrete Zeitregel bleiben konkrete nächste Alternativen. Physikalisches Raummaß, Uhr, vollständiger Energie-Impuls-Strom, Wirkung und Einstein bleiben offen.


CI-Nachprüfung der schwachen Lastaufspaltung: Beide Actions-Jobs zu Codecommit 865d7f3b909676714d4404907c573e1105f64fbc erfolgreich. Manuskript-Prüfsumme, alle sechzehn Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: gemeinsame Kleinlastgrenze und relative Randdynamik

[Herleitung](SMALL_LOAD_DERIVATION.md), [Vorabprotokoll](SMALL_LOAD_PROTOCOL.md), [Prüfcode](small_load_audit.py), [Resultate](small_load_results.json).

Mit s=tr(FY)/trF und Z=Y/s liefert der unveränderte BFG-Update eine exakte endliche Koordinatenform. Für s->0 bei fester relativer Form folgt s_+~2mu2 s² und Z_+->(mu2 I+Z²)/(2mu2), mu2=tr(FZ²)/trF. Gleichzeitig besitzt der Kernel einen expliziten positiven spurtreuen Grenzkanal, der im Allgemeinen NICHT die Identität ist.

Ein exakter Zwei-Moden-Zeuge hat Grenz-h12=4/sqrt(21) und Kernelsprung≈0.0898934. Ein anderer Pfad mit demselben F,W,K und ebenfalls Y->0 hat dagegen den Identitätskanal. Der rohe Null-Lastpunkt allein bestimmt deshalb keine eindeutige stetige Kernel-Fortsetzung; die relative Form muss mitgeführt werden. s=0 wird nur als mathematische Randkarte behandelt, nie als Quellenaufruf.

19 vollständige Quellaufrufe im finalen Audit sowie exakte rationale Grenzrechnungen bestanden. Endliche Quell-/Koordinatenreste <3e-15, Kovarianzrest <1.6e-15. Asymptotikfehler bleiben ausdrücklich größer: beim kleinsten Zeugen-s etwa 0.04021 für den skalierten Folgelastwert und 0.00669 für die relative Form. CI separat prüfen.

Die gemeinsame Randkarte ist konstruktiv gewonnen; ein physikalischer Kleinschritt folgt daraus noch nicht. Nächste konkrete Prüfung ist die gekoppelte nahezu isotrope relative Formdynamik, einschließlich verbleibender Kernelwirkung. Physikalische Uhr, Raummaß, vollständiger Energie-Impuls-Strom und Einstein bleiben offen.


CI-Nachprüfung der relativen Kleinlast-Randkarte: Beide Actions-Jobs zu Codecommit e80f76593b32439454df5887e375700eaab3c1fa erfolgreich. Manuskript-Prüfsumme, alle siebzehn Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: gekoppelter langsamer Grenzwert im ausgeglichenen Randsektor

[Herleitung](RELATIVE_SLOW_DERIVATION.md), [Vorabprotokoll](RELATIVE_SLOW_PROTOCOL.md), [Prüfcode](relative_slow_audit.py), [Resultate](relative_slow_results.json).

Die allgemeine relative Randkarte erzeugt für Z=I+rA einen quadratischen Formterm A²-<A²>_F I. Ein exakter Drei-Niveau-Zeuge zeigt, dass dieser Term nicht allgemein verschwindet und die reguläre epsilon²-Zeitskalierung in den gewählten relativen Koordinaten behindert.

Konstruktiver Sondersektor: A²=I und <A>_F=0 bleiben auf der Randkarte exakt erhalten; r_+=r/(1+r²), h(r)=1/sqrt(1+r²+r^4). Für r0=epsilon und t=N epsilon² folgen gemeinsam u(t)=(1+2t)^(-1/2) und blockübergreifende Kerneldämpfung d(t)=(1+2t)^(-1/4). Ein expliziter Euler-/Grönwall-Beweis kontrolliert die feste-T-Grenze mit O_T(epsilon²). Die Randform wird dabei tatsächlich mitgeführt.

Symbolische Identitäten, Randschritt-Konvergenzkontrollen und 14 vollständige einereignisweise Quellaufrufe bestanden; exakter Quellrest <3.4e-15, Kovarianzrest <4.2e-15, endlicher Quellen-/Randformabstand bis ca. 0.00039374. Bis 3200 Randschritte sind ausdrücklich keine 3200 vollständigen Quellevents. CI separat prüfen.

Offen bleibt die uniforme Übertragung auf lange autonome positive-s-Quellfolgen, die Auswahl des ausgeglichenen Sektors und physikalische Uhr-/Raumkalibrierung. Der konstruktive Randgrenzwert liefert allein keine vollständige Energie-Impuls- oder Einstein-Herleitung.


CI-Nachprüfung der langsamen relativen Randdynamik: Beide Actions-Jobs zu Codecommit ddc022162009f033161e3825db49d6215e4cf8f4 erfolgreich. Manuskript-Prüfsumme, alle achtzehn Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und nachfolgende Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: uniforme positive-Last-Übertragung im ausgeglichenen Sektor

[Herleitung](UNIFORM_LIFT_DERIVATION.md), [Vorabprotokoll](UNIFORM_LIFT_PROTOCOL.md), [Prüfcode](uniform_lift_audit.py), [Resultate](uniform_lift_results.json).

Die bislang offene Übertragung des Randgrenzwerts ist im exakten ausgeglichenen Zwei-Niveau-Sektor jetzt analytisch kontrolliert. Für 0<s0<=1/100, r0=epsilon<=1/4 liefern die unveränderten mathematischen Quellrekurrenzen s_+<=s/32 und |r_j-rbar_j|/epsilon<4s0 für alle j. Der kumulative Log-Kernelfehler ist bei N epsilon²<=T höchstens (8T+5epsilon²)s0.

Damit folgt bei gemeinsamem s0(epsilon)->0 der vorherige gekoppelte langsame Grenzwert nun aus der exakten positiven-Last-Vollpersistenzregel, mit Fehler O_T(s0+epsilon²). Keine Geometrie-Rücksetzung oder erfundene Zeitgleichung. Die Aussage bleibt auf diesen mathematischen Sektor und feste skalierte Zeitintervalle begrenzt.

Symbolische Faktorisierungen, exakte Bereichsabschätzungen, Mehrpräzisions-Präfixe und analytisch begrenzte lange Rekurrenzfortsetzungen sowie 12 vollständige kurze Original-Quellaufrufe bestanden. Größter Originalquell-/Rekurrenzrest <1.3e-14, Kovarianzrest <1.4e-15. Lange reduzierte Folgen bis 3200 Schritte sind keine entsprechenden Original-Quellaufrufe; mathematische Tailgrenzen sind kein Intervall-Rundungszertifikat. CI separat prüfen.

Offen bleiben Auswahl und Robustheit des ausgeglichenen Sektors, physikalische Uhr, Raummaß und Energie-Impuls-Zuordnung. Nächster konkreter Test ist ein kleines Formations-Ungleichgewicht auf derselben gemeinsamen Skala. Eine vollständige physikalische Lorentz-/Einstein-Herleitung bleibt offen.


CI-Nachprüfung der uniformen Übertragung: Beide Actions-Jobs zu Codecommit e7584d66a1e24ca6631479b1b2809ee060849d42 erfolgreich. Manuskript-Prüfsumme, alle neunzehn Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: Formations-Ungleichgewicht und Robustheitsgrenze

[Herleitung](IMBALANCE_DERIVATION.md), [Vorabprotokoll](IMBALANCE_PROTOCOL.md), [Prüfcode](imbalance_audit.py), [Resultate](imbalance_results.json).

Die exakte Zwei-Niveau-Formel ist jetzt für delta=tr(FA)/trF!=0 hergeleitet; s bezeichnet hier ausdrücklich den spektralen Mittelpunkt. Auf der Randkarte gilt r_+=r/(1+delta r+r²). Ein festes positives delta führt zu schnellerem Kontrastabbau und einem bei epsilon->0 trivialen kumulativen Rand-Kernel; negatives delta hat den stabilen relativen Fixpunkt r*=-delta mit h*=sqrt(1-delta²). Kleine feste Ungleichgewichte sind somit auf der bisherigen langsamen Skala nicht allgemein vernachlässigbar.

Die kritische Skala delta=kappa epsilon besitzt eine kontrollierte Randgrenzfamilie u'=-u²(kappa+u), (log d)'=-u²/2. Der bisherige ausgeglichene Verlauf ist kappa=0; delta=o(epsilon) erhält diesen Randgrenzwert. Die uniforme positive-s-Übertragung wurde bisher nur bei delta=0 bewiesen und wird hier nicht ungeprüft erweitert.

Symbolische Identitäten, zwölf kritische Rand-Konvergenzfolgen und feste-delta-Schranken sowie 12 vollständige kurze Original-Quellaufrufe bestanden. Maximaler Quell-/Rekurrenzrest ca. 1.66e-12, Kovarianzrest <4.4e-15, unverändert unter 1e-10. Bis 3200 Randschritte bleiben von den Originalaufrufen getrennt. CI separat prüfen.

Nächste Abhängigkeit: uniforme positive-s-Übertragung der kritischen Familie und BFG-interne Auswahl/Stabilisierung der Formations-/Lastrelation. Physikalische Uhr, Raummaß, vollständiger Energie-Impuls-Strom und Einstein bleiben offen.


CI-Nachprüfung des Formations-Ungleichgewichts: Beide Actions-Jobs zu finalem Codecommit 9db5364c87d760c1b9cbf262ae0a268988fe1341 erfolgreich. Manuskript-Prüfsumme, alle zwanzig Audits, sieben Grenztests und Artefakt-Upload bestanden. Die Zweitereigniskontrolle reicht die tatsächlich zurückgegebene Quellenlast weiter. Geprüfter Code und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: uniforme positive-Last-Übertragung der kritischen Familie

[Herleitung](CRITICAL_LIFT_DERIVATION.md), [Vorabprotokoll](CRITICAL_LIFT_PROTOCOL.md), [Prüfcode](critical_lift_audit.py), [Resultate](critical_lift_results.json).

Die zuvor offene Übertragung für delta=kappa epsilon ist jetzt für |kappa|<=1/2 kontrolliert. Exakte rationale Rechteckzertifikate liefern C_R=3 und C_L=2. Ein Bootstrap ergibt |r_j-rbar_j|/epsilon<=C_T s0, C_T=9 exp(3T), sofern C_T s0<=1/2; der kumulative Log-Kernelfehler ist durch [17epsilon²+2 C_L C_T T]s0 begrenzt.

Damit folgt die kritische gekoppelte Familie u'=-u²(kappa+u), (log d)'=-u²/2 aus der exakten mathematischen positiven-Last-Quelle im ausgewiesenen Zwei-Niveau-Sektor, mit Fehler O_T(s0+epsilon²). Eine unbegrenzt numerisch erfolgreiche Originaltrajektorie oder physikalische Uhr wird nicht behauptet.

Symbolische Zertifikate, zwölf analytisch begrenzte lange Rekurrenzfolgen und 14 vollständige kurze Original-Quellaufrufe bestanden. Original-Quellrest <1.9e-13, Kovarianzrest <2.3e-14, unter unverändertem 1e-10. Die Bootstrapbedingung ist in allen Präparationen erfüllt; Mehrpräzisionswerte und analytische Tailgrenzen bleiben getrennt. CI separat prüfen.

Offen bleiben Auswahl und Stabilität gegenüber zusätzlichen Lastniveaus, physikalische Uhr-/Raumauslese und vollständiger Energie-Impuls-Strom. Nächster konkreter Reichweitentest ist eine zusätzliche Lastaufspaltung innerhalb der beiden Blöcke. Keine vollständige physikalische Lorentz-/Einstein-Herleitung.


CI-Nachprüfung der kritischen positiven-Last-Übertragung: Beide Actions-Jobs zu Codecommit 2bd809551e10ef0ac2436fd8a7417523e2882b48 erfolgreich. Manuskript-Prüfsumme, alle einundzwanzig Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: zusätzliche Lastniveaus und transversale Empfindlichkeit

[Herleitung](EXTRA_LEVEL_DERIVATION.md), [Vorabprotokoll](EXTRA_LEVEL_PROTOCOL.md), [Prüfcode](extra_level_audit.py), [Resultate](extra_level_results.json).

Im ausgeglichenen Zwei-Niveau-Unterbereich besitzen innere formationszentrierte Lastaufspaltungen relative Tangentenfaktoren 1+r im höheren und 1-r im niedrigeren Block. Die exakte positive-Last-Quelle hat entsprechende Faktoren H_+>1 und 0<H_-<1; rationale Zertifikate kontrollieren ihren Abstand zur Randform.

Auf N epsilon²->T folgt epsilon log G_±->±(sqrt(1+2T)-1), auch für die exakte mathematische positive-Last-Basis bei s0(epsilon)->0. Damit wächst die obere relative Tangentenverstärkung wie exp(c(T)/epsilon). Es besteht keine epsilon-uniform begrenzte lineare Empfindlichkeit in dieser Richtung, sofern der jeweilige Block innere Dimension hat. Das widerlegt weder den exakten Sektorgrenzwert noch beweist es schon eine nichtlineare Flucht endlicher Störungen.

Symbolische Richtungs-/Quotientenzertifikate, vier lange Randfolgen und 38 vollständige Original-Quellaufrufe bestanden. Basisrest <1.3e-14, Last-Kovarianzrest <1e-18; schlechtester bester zentraler Ableitungsfehler ca. 2.28e-8 unter vorab 1e-6. Alle Schrittweiten und größere Rundungsreste bleiben sichtbar. CI separat prüfen.

Nächste Abhängigkeit: nichtlineare Störungsreichweite und BFG-interne Auswahl/Isolierung des Ereignisträgers. Physikalische Uhr, Raummaß, vollständiger Energie-Impuls-Strom und Einstein bleiben offen.


CI-Nachprüfung zusätzlicher Lastniveaus: Beide Actions-Jobs zu Codecommit 6404d74f3cb7533bf4a2e1c60ede8098c8d0b72d erfolgreich. Manuskript-Prüfsumme, alle zweiundzwanzig Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Fortsetzung: endliche zusätzliche Aufspaltung und nichtlineare relative Grenze

[Herleitung](FINITE_SPLITTING_DERIVATION.md), [Vorabprotokoll](FINITE_SPLITTING_PROTOCOL.md), [Prüfcode](finite_splitting_audit.py), [Resultate](finite_splitting_results.json).

Eine erklärte n=4-Dreiniveau-Familie besitzt exakte endliche Randrekurrenzen für Hauptaufspaltung r und innere Breite b. Oberhalb wächst q=b/r; unterhalb bildet r<=1/4,q<=1/2 einen invarianten relativen Kontraktionsbereich. Für obere Anfangsdaten r0=epsilon,q0=epsilon² (b0=epsilon³) ist ein nichtlinearer Austritt aus r<1/4,q<1/2 spätestens nach O(epsilon^-1 log(1/epsilon)) Randschritten bewiesen. Der Austritt ist relativ und behauptet keine rohe Y-Abweichung von Ordnung eins.

Für die vollständige positive-Last-Quelle auf C liefern geordnete Lücken und strikte Konvexität exakt q_+>q im oberen und q_+<q im unteren Fall. Eine quantitative lange Quellen-Austrittszeit bleibt ohne zusätzliche uniforme nichtlineare Fehlerkontrolle offen.

Symbolische Identitäten, vier obere Austrittskontrollen, vier untere lange Kontraktionskontrollen und 18 vollständige Original-Quellaufrufe bestanden. Obere Austritte nach 50,124,295,684 Randschritten liegen unter den bewiesenen Schranken 120,321,806,1942. Original-Lastrest <1.4e-18, normierter r/b-Rest <7.2e-13. Sehr kleine untere Randbreiten sind nicht als entsprechend aufgelöste Original-Matrixtrajektorien ausgegeben. CI separat prüfen.

Nächste Abhängigkeit: quantitative nichtlineare positive-s-Übertragung und quellenbasierte Auswahl/Isolierung des lokalen Trägers, einschließlich des konstruktiven unteren Kontraktionsbereichs. Physikalische Uhr, Raummaß, vollständiger Viererstrom und Einstein bleiben offen.


CI-Nachprüfung der endlichen Aufspaltung: Beide Actions-Jobs zu Codecommit bbecf2ed3a0f3563cd271a61eea3d3a543311121 erfolgreich. Manuskript-Prüfsumme, alle dreiundzwanzig Audits, sieben Grenztests und Artefakt-Upload bestanden. Geprüfter Code und spätere Dokumentation sind in [CI_VALIDATION.md](CI_VALIDATION.md) getrennt ausgewiesen.


## Runde 24: unteres Paar mit uniformem Rand-Gedächtnis

[LOWER_PAIR_MEMORY_DERIVATION.md](LOWER_PAIR_MEMORY_DERIVATION.md): V=b²/r liefert am unteren relativen Rand V-V_+>=b² und damit sum b_j²<=b_0²/r_0. Der exakte Paarfaktor erfüllt auch bei positiver Last 1-h<=32b²/35. Zusammen ergibt sich am Rand für beliebig viele Ereignisse ein lokaler transversaler Kerneldefekt <=(32/35)b_0²/r_0, insbesondere O(epsilon^5) bei b_0=epsilon³,r_0=epsilon. Zwei diagonale Komponenten bleiben exakt, zwei transversale nur näherungsweise erhalten.

Vier frische Randkontrollen à 2000 Ereignisse und zehn Original-Quellaufrufe bestanden; Kernelrest <1.5e-14, Eichrest <4.6e-14. Positiv-Last-Summierbarkeit und vollständiger physikalischer Strom bleiben offen. Nächster Schritt ist die positive-s-Lyapunov-Abschätzung des unteren Kegels. CI dieses Codecommits separat prüfen.


CI Runde 24: Beide Remote-Läufe zu Codecommit 7ff76ae4e2bf37d85dd1b1271fa8c3e4e1d44b7a vollständig erfolgreich, einschließlich aller 24 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte. Siehe CI_VALIDATION.md für exakte Runs und Trennung von geprüftem Code und späterer Dokumentation.


## Runde 25: untere Gedächtnisschranke auf volle positive Last übertragen

[LOWER_PAIR_LIFT_DERIVATION.md](LOWER_PAIR_LIFT_DERIVATION.md), [Vorabprotokoll](LOWER_PAIR_LIFT_PROTOCOL.md), lower_pair_lift_audit.py und lower_pair_lift_results.json.

In der erklärten n=4-Familie (obere Zweifachentartung, ausgeglichene F-Diagonalblöcke) ist der Bereich s<=1/100,r<=1/4,q=b/r<=1/2 unter der vollständigen positiven-Last-Quelle invariant. Konvexität liefert r_+<=r; ein exaktes rationales Rechteckzertifikat liefert q_+<=q(1-r/2). Damit V=b²/r, V-V_+>=b²/2 und sum b_j²<=2b_0²/r_0. Die lokale transversale Kerneländerung bleibt für alle Ereigniszahlen durch (64/35)b_0²/r_0 mal anfänglichen Offdiagonalnorm beschränkt. Zwei Diagonalkomponenten sind exakt, zwei transversale näherungsweise erhalten.

Vier positive-s-Präfixe mit je sechs Ereignissen bei 500 Dezimalstellen ohne Randersetzung und zehn Original-Quellaufrufe bestanden. Kernelrest <2e-14, Eichrest <1.8e-14, normierter Lastrest <3.7e-12. Hochpräzise skalare Lasten unter dem Original-Rangcutoff sind keine aufgelösten Original-Matrixtrajektorien. Die unendliche Restschranke stammt aus dem exakten Beweis.

Die offene positive-s-Summierbarkeit aus Runde 24 ist für diese Familie geschlossen. Nächste Abhängigkeit: quellenbasierte Auswahl/Isolierung und Robustheit ohne obere Entartung bzw. ausgeglichene F-Blöcke. Frühere obere Verstärkung bleibt gültig. Räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen. CI dieses neuen Codecommits separat prüfen.


CI Runde 25: Beide Actions-Läufe zu Codecommit b9a916f73d539bbc1342c89f46d4905b8d3468b8 vollständig erfolgreich, einschließlich aller 25 Audits, sieben Grenztests, Prüfsumme und Artefakte. Exakte Runs und Trennung von Code-/Dokumentationsstand in CI_VALIDATION.md.


## Runde 26: einseitig ungleiche Formationsgewichte

[LOWER_PAIR_FORMATION_DERIVATION.md](LOWER_PAIR_FORMATION_DERIVATION.md) erweitert die positive-Last-Gedächtnisschranke auf F-Diagonalblöcke (1+delta)I und (1-delta)I, 0<=delta<=1/2, bei beibehaltener oberer Lastentartung. Ein rho-unabhängiges rationales Zertifikat liefert q_+<=q(1-r/2); alpha-Monotonie liefert r_+(delta)<=r_+(0)<=r. Der gesamte lokale transversale Defekt bleibt <=(64/35)b_0²/r_0 mal Anfangs-Offdiagonalnorm. Keine beliebige F-Robustheit oder generische Quellenauswahl behauptet.

Exakte signed Randrekurrenz zeigt die Grenze: r=1/20,q=1/10,delta=-1/2 ergibt r_+=15998/312805>r. Die alte Hauptkontrast-Monotonie lässt sich nicht pauschal auf negative Gewichtsverschiebung übertragen; andere Lyapunov-Kandidaten bleiben offen.

Sechs 500-stellige positive-s-Präfixe à sechs Ereignisse, rationales Zertifikat und 14 Original-Quellaufrufe bestanden. Kernelrest <2.2e-15, Eichrest <3e-15, normierte Last <2.4e-13. Nächste Abhängigkeit: zusätzliche obere Aufspaltung und allgemeinere Formation; räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom bleiben offen. CI separat prüfen.


CI Runde 26: Beide Actions-Läufe zum Codecommit 7d160a7e9e804d413cbc24e4d97e343a24ad2319 vollständig erfolgreich. Alle 26 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Laufnachweise in CI_VALIDATION.md.


## Runde 27: negative Gewichtsrichtung ohne Hauptkontrast-Monotonie

[LOWER_PAIR_SIGNED_DERIVATION.md](LOWER_PAIR_SIGNED_DERIVATION.md) schließt die bisher offene kleine negative Formationsrichtung -1/8<=delta<=0 in derselben oberen-entarteten Familie. Ein exaktes positives rationales Zweiniveau-Vergleichszertifikat hält r<=1/4 invariant, obwohl r wachsen darf. Die alternative Funktion U=q² liefert U-U_+>=2b² und damit sum b_j²<=q_0²/2. Der lokale transversale Kerneldefekt bleibt für alle Ereigniszahlen <=(16/35)q_0² mal Anfangs-Offdiagonalnorm. Diese Schranke ist schwächer, benötigt aber keine r-Monotonie; die engere nichtnegative Schranke bleibt erhalten.

Vier neue 500-stellige positive-s-Präfixe und acht vollständige Original-Quellaufrufe bestanden. Kernelrest <7.1e-16, Eichrest <2e-15, normierte Last <2.9e-13. Im Originalfall r=.05,delta=-.125,q=.1,s=.001 wächst r auf .05008176369701517, während q fällt. Das alte Gegenbeispiel bleibt bestehen; es wird durch die andere Lyapunov-Funktion umgangen.

Zusammen gilt nun eine uniforme lokale Gedächtnisschranke für delta in [-1/8,1/2] unter den erklärten F-Block- und oberen Entartungsannahmen. Nächste Abhängigkeit: endliche obere Lastaufspaltung und Trägerauswahl. Allgemeines F, Raumtransport, physikalische Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 27: Beide Actions-Läufe zu Codecommit 1497d48857398607074527a4c2593628f46ffbde vollständig erfolgreich; alle 27 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden. Exakte Nachweise und Trennung Code/Dokumentation in CI_VALIDATION.md.


## Runde 28: endliche obere Aufspaltung, gestoppte untere Kontrolle

[TWO_SIDED_PAIR_DERIVATION.md](TWO_SIDED_PAIR_DERIVATION.md) lockert die obere Lastentartung: vier Lasten 1+r±a und 1-r±b. Für s<=.01,r<=.25,p=a/r<=.5,q=b/r<=.5 zertifiziert eine exakte rationale rho-Hülle auch bei beliebigem F>0 die untere Kontraktion q_+<=q(1-r/2). U=q² kontrolliert sum b_j²<=q_0²/2 und den lokalen Kohärenzverlust <=16q_0²/35 bis einschließlich des ersten Bereichsaustritts. Keine allzeitliche Schranke nach Austritt behauptet.

Exakte volle positive-Last-Quelle r=.1,p=.5,q=.1,s=.001 liefert p_+=.5466189288623009>.5; der Bereich ist nicht invariant. Zwei von vier gestoppten 500-stelligen Präfixen verlassen ihn nach einem Ereignis, zwei bleiben sechs geprüfte Ereignisse darin. Zehn frische Original-Quellaufrufe bestanden: Kernelrest <4.1e-15, Eichrest <3.5e-15, normierter Lastrest <3.5e-13. Allgemeines F stammt aus dem symbolischen rho-Beweis, Originalkontrollen nutzen ausdrücklich die erklärte Kreuzblockfamilie.

Nächste Abhängigkeit: untere Kontrolle nach oberem Bereichsaustritt bzw. andere spektral-geometrische Schranke. Allgemeine Trägerauswahl, Raumtransport, physikalische Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 28: Beide Actions-Läufe zum Codecommit 128633e95ca2169c86afa285893b9c43259b5ac6 vollständig erfolgreich. Alle 28 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 29: geordnete Spektrallücke und formationsabhängige Grenze

[SPECTRAL_GAP_DERIVATION.md](SPECTRAL_GAP_DERIVATION.md) beweist für drei geordnete Lasten in C die allzeitliche geometrische Monotonie eta_+<eta, eta=(y_2-y_1)/(y_3-y_1), ohne obere Blockbreitengrenze. Die erhoffte Gedächtnisbrücke aus eta allein scheitert jedoch bei beliebigem F>0: Y=diag(2epsilon²,4epsilon²,epsilon), F=diag(1,1,epsilon^6) liegt in C mit m=2M²; eta->0, aber h_12->9/sqrt(91)<1. Ein nicht verschwindender Einzelschrittverlust widerlegt jede uniforme Verlustschranke phi(eta_0)->0 in dieser Allgemeinheit.

Sechs frische Original-Quellaufrufe und exakte rationale Grenzwerte bestanden. Kernelrest <2.1e-15, Eichrest <8.4e-15, Lückenrest <5.7e-16. Der Gegenzeuge nutzt variierende, nicht gleichmäßig konditionierte Formation; keine Widerlegung formationsabhängiger oder gleichmäßig elliptischer Abschätzungen. Frühere Spezial-/Stoppresultate bleiben gültig.

Nächste Abhängigkeit: nach-dem-Austritt-Kontrolle muss Mischung alpha, interne Paarbreite oder explizite Formationskondition einbeziehen. Allgemeine Trägerauswahl, Raumtransport, physikalische Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 29: Beide Actions-Läufe zum Codecommit 661e2131935ec6a23597747a131f126677813d2c vollständig erfolgreich. Alle 29 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; negatives Forschungsresultat innerhalb des bestandenen Audits ausdrücklich beibehalten. Nachweise in CI_VALIDATION.md.


## Runde 30: formationsabhängige Einzelschrittbrücke

[FORMATION_BOUND_DERIVATION.md](FORMATION_BOUND_DERIVATION.md) leitet mit ell²=alpha/(1-alpha),chi=(y_2-y_1)/ell exakt 1-h<=chi²/2 her. Für F>0, Konditionszahl kappa und volle Dimension n gilt ell²>=M²/[n kappa(1+M)], folglich bei M<=1/2 auch 1-h<=3n kappa eta²/4. Komplexe nichtkommutierende Formation ist eingeschlossen; eine uniforme Konditionsannahme wird nicht als Quellgesetz eingeführt.

Endliche Historien sind durch die entsprechenden Defektsummen begrenzt. Deren allgemeine Summierbarkeit ist weiterhin offen und folgt nicht aus eta-Monotonie allein. Der Gegenzeuge aus Runde 29 bleibt erhalten: chi²->2/5 statt null, kappa ist unbeschränkt.

Neun frische Original-Quellaufrufe n=3,4, kappa=1,4,16 einschließlich drei Eichkontrollen bestanden. Kernelrest <6.6e-16, Eichrest <1.1e-15, Lastrest <2.4e-17. Nächste Abhängigkeit: quantitative Kontrolle der formationsabhängigen Defektreihe aus der vollen Dynamik. Trägerauswahl, Raumtransport, physikalische Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 30: Beide Actions-Läufe zu Codecommit a4f2c299fbfff1aea0cc71d9b709e4ecde83228b vollständig erfolgreich. Alle 30 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 31: allzeitliche konditionierte Paar-Kontrolle durch Teleskopieren

[TELESCOPING_MEMORY_DERIVATION.md](TELESCOPING_MEMORY_DERIVATION.md) schließt die formationsabhängige Defektsumme im festen vollen Persistenzsektor: n>=3, F>0 mit kappa, Y in C mit M<=1/4 und y_1<y_2<y_3. Explizite Quellkrümmung liefert 1-eta_+/eta>=64(y_3-y_2)/(625M). Damit chi_j²/2<=C_0(eta_j²-eta_(j+1)²), C_0=3125 n kappa/[512(1-eta_0)]. Die Summe ist endlich, der lokale transversale Gesamtdefekt bleibt für alle Ereignisse <=min(1,C_0 eta_0²) mal Anfangs-Offdiagonalnorm. Das positive Kohärenzprodukt hat einen nichtverschwindenden Grenzwert.

Keine obere Blockentartung oder obere Breiten-Stoppgrenze nötig. Der frühere formationsfreie Gegenzeuge bleibt gültig, da seine Kondition unbeschränkt wird. Die Schranke kann bei großem kappa nur den trivialen Wert 1 liefern. Keine Endlichkeit von sum eta_j² behauptet; die gewichtete chi-Defektreihe wird direkt kontrolliert.

Neun frische Original-Quellaufrufe sowie sechs 500-stellige positive-s-Präfixe à sechs Ereignisse mit expliziter Restabschätzung bestanden. Kernelrest <9.8e-16, Eichrest <1.7e-15, Lastrest <5.2e-17. Die unendliche Kontrolle folgt aus dem Beweis. Nächste Abhängigkeit: quellenbasierte lokale Auswahl und Fortsetzung über Auswahl-/Rangereignisse sowie räumlicher Transport. Physikalische Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 31: Beide Actions-Läufe zu Codecommit 0a5361ac15ccafb25100eef9c049407767c11397 vollständig erfolgreich. Alle 31 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Trennung von geprüftem Code und Dokumentation in CI_VALIDATION.md.


## Runde 32: lückenabhängige Stabilität der spektralen Trägerwahl

[SELECTOR_STABILITY_DERIVATION.md](SELECTOR_STABILITY_DERIVATION.md) beweist für P_2(Y) bei äußerer Lücke g=lambda_3-lambda_2 und epsilon=||E||_2<g/2 die Schranke ||P_2(Y+E)-P_2(Y)||_F<=2epsilon/(g-epsilon). Innere Paarentartung ist zulässig; kritisch ist die äußere Lücke. Die exakte BFG-Familie Y_t=diag(.1,.1+t,.1+2t), F=I,W=K=I/3 und feste Rotation pi/12 in Moden 2,3 zeigt ||Delta Y||_2->0 bei konstantem Projektorabstand (sqrt(3)-1)/2. Diese Grenze bleibt unter einem vollständigen Quellereignis sichtbar.

Am vollständig isotropen Grenzzustand existiert kein einzelner aus dem gesamten Zustand unitär kovariant bestimmter Rang-zwei-Projektor. Dies betrifft weder Auswahl mit tatsächlich nichtisotropen Zusatzdaten noch mengenwertige Beschreibungen. Die feste-Sektor-Gedächtnisschranke aus Runde 31 bleibt gültig.

Sechs unabhängige Hermitesche Störungskontrollen und acht frische Original-Quellaufrufe bestanden. Projektorrest <1.7e-14, Eichrest <4.6e-14, Last-Kovarianzrest <3e-17. Nächste Abhängigkeit: vorhandene Witness-/Formationsdaten bei lückenschließender Wahl und dynamische Geschlossenheit; räumlicher Transport, physikalische Uhr und vollständiger Viererstrom bleiben offen. CI separat prüfen.


CI Runde 32: Beide Actions-Läufe zu Codecommit 7be75f5b6898aaf13dc5e34e810574ed4ad7b6dc vollständig erfolgreich. Alle 32 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 33: konkurrierende Auflösung mit vorhandenen F-/W-Daten

[TIE_AMBIGUITY_DERIVATION.md](TIE_AMBIGUITY_DERIVATION.md) zeigt am vollständig positiven skalaren Lastsektor Y=yI,F=diag(1,2,4), W mit nichtkommutierendem 2/3-Block, K=diag(1,2,3)/6: Formation zuerst und Witness zuerst bestimmen verschiedene kovariante Rang-zwei-Beobachtungsflächen. Beide Flächen und beide komprimierten Kernel bleiben exakt konstant; lokale Spuren 1/2 bzw. 7/12. Kovarianz, Persistenz und vier konstante lokale Komponenten allein wählen daher keinen eindeutigen Träger.

Eine kontinuierliche mathematische Kandidatenfamilie aus F+tau W interpoliert zwischen ihnen; tau ist ausdrücklich zusätzliche Selektorwahl, kein Quellgesetz. Der originale BFG-Träger bleibt Rang drei. Frühere lexikographische Konstruktion, Stabilitäts- und Gedächtnissätze bleiben gültig; kein allgemeines Selektor-No-Go behauptet.

Sechs frische Original-Quellaufrufe und exakte Block-/Spuridentitäten bestanden. Feldrest <1.7e-16, Kompressionsrest <1.3e-16, Eichrest <3.7e-15. Nächste Abhängigkeit: quellengestütztes Auswahlkriterium oder mengenwertige Sektorbeschreibung statt willkürlicher Priorität; echte Auswahl-/Rangbilanz und räumlicher Transport offen. Physikalische Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 33: Beide Actions-Läufe zu Codecommit 7c8cf8a1f2250d73407df3772796c10d0c28a9be vollständig erfolgreich. Alle 33 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 34: Informationsdimension beschrifteter Paarfamilien

[PAIR_FAMILY_DERIVATION.md](PAIR_FAMILY_DERIVATION.md) untersucht die Alternative, konkurrierende F-/W-Paarsektoren gemeinsam zu behalten. Die beschriftete P_tau-Kompressionsfamilie aus Runde 33 hat auf Herm(C³) exakt reellen Rang 8 und Kern J=i(|2><3|-|3><2|); drei rationale Mitglieder genügen. Bei Spur eins sind sieben sichtbare affine Parameter vorhanden. Eine positive Faser K±=I/3±J/12 besitzt gleiche Familienbilder; im skalaren Lastsektor bleiben sie auch künftig gleich, daher hier ausdrücklich kein Faser-Geschlossenheitsgegenbeispiel.

Alle beschrifteten Rang-zwei-Flächen zusammen bestimmen hingegen den gesamten Herm(C^n)-Kernel mit n² reellen Parametern. Das bloße Sammeln der Paarsektoren erzeugt deshalb keinen automatisch vierdimensionalen lokalen Träger. Labels werden nicht stillschweigend wegquotientiert; physikalische Raumzeitdimension wird nicht aus diesem Rang abgelesen.

Exakte Ränge/Nullraum/Positivität und acht frische Original-Quellaufrufe bestanden. Kompressionsrest <1.8e-16, verborgener Kernelrest <2e-16, Eichrest <5.7e-16. Nächste Abhängigkeit: quellengestützte geschlossene Reduktion und Bilanz über überlappende/wechselnde Sektoren. Trägerauswahl, Raumtransport, physikalische Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 34: Beide Actions-Läufe zu Codecommit b07c18e54dbe7d29f783d5be5fe84a28b8612ad2 vollständig erfolgreich. Alle 34 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 35: echte Faser-Nichtgeschlossenheit der Paarfamilie

[PAIR_CLOSURE_DERIVATION.md](PAIR_CLOSURE_DERIVATION.md) erweitert den vorigen skalaren Test auf Y mit Kopplung zwischen Moden 1/2. Dieselben positiven K±-Fasermitglieder haben identische behaltene Y,F,W und sämtliche P_tau-Bilder, aber nach dem vollständigen Quellereignis verschiedene Witness-Paarbilder. Exakt Phi(J)=(h_plus-h_minus)J13/2+(h_plus+h_minus)J23/2; Ausgangstrennung (h_plus-h_minus)/12>0. Dies verletzt II89 für diese Reduktion außerhalb skalarer Last, nicht BFG oder jede Reduktion.

Eine native Ergänzung ist i[F,W]=(2/9)J. Der zusätzliche Skalar tr(i[F,W]K) löst die Faser auf und erhöht den Bildrang von 8 auf 9, stellt also den ganzen Kernel wieder her statt vier physikalische Komponenten zu liefern. Er ist keine erhaltene Energie-/Impulsgröße. Der alte skalare Geschlossenheitsbefund bleibt ausdrücklich gültig.

Exakte rationale Kanal-/Kommutator-/Rangidentitäten und acht Original-Quellaufrufe bestanden. Kernelrest <3.1e-16, Feldrest <7.5e-16, Eichrest <6.3e-16. Nächste Abhängigkeit: quellengestützte geschlossene Reduktion oder vollständige Mehrsektor-Bilanz mit Kohärenzen, Überlappungen und Wechseln. Raumtransport, physikalische Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 35: Beide Actions-Läufe zu Codecommit f8277d33b8dce8c98006327b92f205aaf7ee3aad vollständig erfolgreich. Alle 35 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 36: normierte Überlappungsbilanz

[OVERLAP_BALANCE_DERIVATION.md](OVERLAP_BALANCE_DERIVATION.md) erweitert die frühere orthogonale Modenkontinuität auf beliebige feste positive Effekte E_a mit sum E_a=I. Aus demselben Hermiteschen BFG-Krauskanal folgt J_ab=sum Re tr(E_a T E_b[T,K]), J_ab=-J_ba und Delta tr(E_aK)+sum_b J_ab=0. Kohärenzen bleiben im Strom enthalten; keine q-Allein-Geschlossenheit oder physikalische Energie-Deutung behauptet.

Die frühere P_tau-common-line-Familie lässt sich nicht mit endlichen skalaren Gewichten zu I normieren: e1-Erwartung verlangt Gewichtssumme1, Spur verlangt3/2. Alternative Koordinatenpaare erfüllen sum P_ij=(n-1)I und nach Normierung korrekte Gesamtspur; unnormiert würden Bestände n-1-fach gezählt.

Exakte Cover-/Stromidentitäten, nichtkommutierender Effekt-Kontrollfall und acht Original-Quellaufrufe bestanden. Kontinuitätsrest <2.8e-16, Antisymmetrierest <3.7e-17, Eichrest <1.3e-15. Nächste Abhängigkeit: Zuordnung bei wechselnden Effekten und echte Auswahl-/Rangereignisse, anschließend räumliche/zeitliche Deutung. Vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 36: Beide Actions-Läufe zu Codecommit c669138d11d44992d1ec519ffac7cefa3842ae8f vollständig erfolgreich. Alle 36 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 37: wechselnde Sektoren und Zuordnungsbilanz

[MOVING_COVER_DERIVATION.md](MOVING_COVER_DERIVATION.md) ergänzt die feste-Effekt-Kontinuität um R_after,a=tr[(E'_a-E_a)K_+]: Delta q_a+sum_b J_ab(E,K)=R_after,a, sum R_after=0. Die alternative cover-first-Zerlegung verwendet R_before=tr[(E'-E)K]; ihre Differenz ist der exakt berechnete Kreuzterm tr[(E'-E)(K_+-K)]. Keine physikalische Zeitordnung oder neue Reserve wird daraus behauptet.

Ein exakter Originalzeuge hat K_+=K und dynamischen Strom0, aber durch manuelle Coverrotation lokale Änderung (0,1/40,-1/40). Eine lokale Bestandsänderung allein belegt daher keinen dynamischen Transport. Allgemeine numerische Kontrollen nutzen wohldefinierte eigenwertgeordnete K-/K_+-Paarcovers mit geprüften Lücken; keine globale Kollisionsfortsetzung unterstellt.

Neun Original-Quellaufrufe und exakte Spur-/Rotationsidentitäten bestanden. Bilanzrest <9.7e-16, Eichrest <1.7e-15, reiner Zuordnungsrest <1.4e-16. Nächste Abhängigkeit: echte Auswahl-/Seed-/Rangereignisse mit wechselnden Trägerräumen. Physikalische Raum-/Zeitdeutung, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 37: Beide Actions-Läufe zu Codecommit 4c1cab945632a740157890ba15067a2320ebf8c6 vollständig erfolgreich. Alle 37 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 38: lokale Bilanz über echte Auswahl-/Seed-/Rangereignisse

[RANK_LOCAL_BALANCE_DERIVATION.md](RANK_LOCAL_BALANCE_DERIVATION.md) leitet aus den tatsächlichen rechteckigen Analyseblöcken U_C,U_B den positiven Beobachtungsrückzug B_a=sum U_r Eout_a U_r† und Delta q_a=tr[K(B_a-Ein_a)] her. Ganze Raumüberdeckungen ergeben die bekannte signed Spurdefektbilanz tr K(D-I); aktive Trägerüberdeckungen dagegen tr K(sum U_r P_+ U_r†-P). Diese Bestände dürfen außerhalb voller Persistenz nicht gleichgesetzt werden.

Ein exakter Seedzeuge hat Dimension3->2 und aktiven Rang1->2, D=2P. Seine ambiente Kernelspur ändert sich um11/2, der aktive Bestand um-9/4; I-D besitzt Eigenwerte(-1,1,1). Das ist keine positive Export-/Energiereserve. Terminale Nachfolger werden nicht erfunden.

Zehn frische Original-Quellaufrufe einschließlich sechs nichtterminaler Teilträgerfälle und drei Eichkontrollen bestanden. Normierter lokaler Rest <1.5e-16, Eichrest <5.4e-14, Zeugenrest <1.8e-15. Ein vor Auswertung abgebrochener Syntaxlauf ist in der Herleitung erhalten. Nächste Abhängigkeit: physikalische Identifikation von Bestand, Zuordnung und Transport samt signed Seed-/Auswahltermen. Raumrelation, Uhr, vollständiger Viererstrom und Einstein bleiben offen. CI separat prüfen.


CI Runde 38: Beide Actions-Läufe zu Codecommit 7d0cc91bf7d1023a9c3cd32f127e52ef5d8722f9 vollständig erfolgreich. Alle 38 Audits, sieben Grenztests, Manuskript-Prüfsumme und Artefakte bestanden; exakte Nachweise und Code/Dokumentations-Trennung in CI_VALIDATION.md.


## Runde 39: konkrete physikalische Energie-/Impulsidentifikation

[PHYSICAL_IDENTIFICATION.md](PHYSICAL_IDENTIFICATION.md) prüft die bisherigen Bestände ausdrücklich gegen die eigenen physikalischen Messanforderungen I41/I55–56/I68/I70/II86. Ergebnis: noch keine hergeleitete physikalische Identifikation; Formationseinheit EF, interne Austauschbilanz und algebraischer Lorentzträger reichen nicht aus. M_E, Uhr-/Raum-/Quantenabbildung und unabhängig kalibrierte Messprüfung bleiben notwendig.

Neue exakte Aussage: Für den natürlichen Kandidaten E_act=tr(PK)+tr F heben sich explizite Seedterme auf, aber Delta E_act=tr[K(B4-P)]-ell_F bleibt, B4=sum U_r S4 U_r†. Beim einfachen Rang-eins-Zeugen null, in zwei neuen Originalfällen numerisch -0.01348060647 und +0.02959852861. Diese Gegenkontrollen sind nicht intervallzertifiziert. Der ambiente Kandidat tr K+tr F hat bereits am exakten bisherigen Seedzeugen Defekt31/4. Keine allgemeine Energie-No-Go-Behauptung.

Gemeinsame positive Skalierung von K,F kommutiert exakt mit dem mathematischen Update einschließlich Seed; vier frische Originalaufrufe bestätigen dies bis6.7e-16. Dies zeigt keine vom Kernel gewählte Joule/EF-Kalibrierung, keine physikalische Unmöglichkeit einer Kalibrierung. Insgesamt sieben unterschiedliche neue Quellaufrufe; Fixture-Erfassungswiederholungen getrennt. Nächster physikalischer Schritt: konkrete, vorab festgelegte Energie-/Impuls-Messbrücke und vollständige Bilanz der Auswahl-/Transportreste; mathematisch kann B4-P weiter exakt untersucht werden.

Reine Dokumentationsrunde; kein Audit-/Workflow-/Quellcode verändert und kein neuer Remote-Pass behauptet. CI-Stand des bisherigen Codes bleibt Runde38, separat in CI_VALIDATION.md.


## Runde 40: rational zertifizierter Defekt des kombinierten aktiven Bestands

[ACTIVE_STOCK_DEFECT.md](ACTIVE_STOCK_DEFECT.md) liefert einen einfachen rationalen zulässigen n=3-Zustand mit aktivem Rang2->3 und eindeutigem Seed. Alpha=1/10, ell_F=0. Die expliziten Seedbeiträge kompensieren exakt, dennoch gilt 6599430384017/10^15 < Delta[tr(PK)+tr F] < 6599430384019/10^15. Allgemeine Erhaltung dieses ungewichteten Kandidaten damit durch rationales Zertifikat widerlegt; keine allgemeine Widerlegung physikalischer BFG-Brücken.

Exakte Residuen und positive Sylvester-Abschätzung zertifizieren die inverse Gramwurzel unabhängig von numerischer SVD. Zwei Originalkontrollen im finalen Lauf, einschließlich komplexer Eichkontrolle, bestätigen den Defekt; zuvor ein explorativer Originalaufruf. Eichrest<2e-15. Ein anfangs fehlerhafter symbolischer Last-Hilfsterm (Y² statt Y P Y) wurde nach Assertion-Abbruch korrigiert; danach frischer vollständiger Pass. Quellgleichung unverändert.

Nächste mathematische Abhängigkeit: Bedingungen für B4=P bzw. quelleninterne Struktur des aktiven Transportrests. Energieablesung, räumliche Relation, Uhr und physikalischer Viererstrom bleiben offen. Reine Dokumentations-/Zertifikatsrunde, keine Code-/Workflowänderung und kein neuer Remote-Pass behauptet.


## Runde41: feste lineare Bestandsgewichte und erhaltene Teilklassen

[LINEAR_STOCK_LIMIT.md](LINEAR_STOCK_LIMIT.md) zeigt: Kein nichttriviales festes reelles a,b macht a tr(PK)+b tr F auf allen zulässigen nichtterminalen Ereignissen erhalten. Exakter Rang1-Zeuge erzwingt a=b; rational zertifizierter Rang2-Defekt d!=0 erzwingt dann a=b=0. Det der Änderungsmatrix=-9d/4. Keine Verallgemeinerung auf jede physikalische Energieabbildung.

Positiv abgegrenzt: Bei Q_selection=I, unterstütztem F/W und Rang r gilt B4>=0, B4<=2P, supp B4<=P und tr B4=r; X=B4-P ist spurfrei. Rang1, skalares PKP oder reduzierender P-Y-Sektor geben hinreichende Einzelschritt-Erhaltung. Am selben Rang2-Kanal kehrt Vertauschen der ersten zwei K-Eigenwerte das Defektvorzeichen exakt um; K=-I hat Defekt0 trotz X!=0. Kein allgemeiner Dissipationsterm.

Vier vorab bestimmte frische Originalaufrufe bestanden; exakte symbolische Gewichtselimination bestätigt. Dokumentationsrunde, Quell-/Audit-/Workflowdateien unverändert, kein neuer Remote-Pass. Nächste Abhängigkeit: source-selected Zusatzbestand oder unabhängig begründete geschlossene Zustandsklasse; M_E, Raumrelation, Uhr und Impulsstrom weiter offen.


## Runde42: gleiche Bestände und gleicher Seed, verschiedene Ausgänge

[SEED_STOCK_CLOSURE.md](SEED_STOCK_CLOSURE.md) konstruiert zwei zulässige K± bei identischen vollen Y,F,W,P, tr K=-6, tr(PK)=-4, Rangdaten und exakt gleichem Seedwert-2. Auch die vollen Nicht-Kernel-Ausgangsfelder sind gleich, die aktiven Ausgangsbestände unterscheiden sich jedoch um4w. Neues rationales Zertifikat: 6541042265093/10^15<w<6541042265096/10^15. Damit scheitert II89-Geschlossenheit dieser konkreten Bestandsreduktion selbst bei bekanntem aktuellem Seedbetrag.

Folgerung: Eine universelle additive Korrektur R(Y,F,W,P) zu tr(PK)+tr F kann die entgegengesetzten Reste±2w nicht ausgleichen; ebenso wenig eine direkte Gegenbuchung allein aus gleichem aktuellem Seedbetrag und gleichen Ereignisrängen. Zusätzliche K-abhängige Richtungsinformation bleibt notwendig für diese Reduktion; keine allgemeine physikalische Energie-No-Go-Behauptung.

Zwei frische Originalaufrufe bestanden; Nicht-Kernel-Feldrest<4.7e-16. Zertifikat/Prüftext vollständig dokumentiert. Keine Quell-/Audit-/Workflowänderung, kein neuer Remote-Pass behauptet. Nächste Abhängigkeit: quellengestützte Auswahl und Geschlossenheit zusätzlicher K-Matrixinformation; Raum/Uhr/physikalischer Viererstrom bleiben offen.


## Runde43: konstruktiv geschlossene aktive Kernelreduktion

[ACTIVE_KERNEL_QUOTIENT.md](ACTIVE_KERNEL_QUOTIENT.md) beweist auf Q_selection=I mit unterstütztem F/W: Pi_act=(PKP,F,W,Y,P) bestimmt den kompletten nächsten BFG-Nachfolger einschließlich Seed/Terminalstatus; K-Komplement-/Kreuzblöcke sind irrelevant. Nach nichtterminalen Ereignissen gilt diese Klasse weiter. Keine Aussage für beliebige initiale Q!=I-Selektion.

Bei festgehaltener Geometrie ist k->vollständiges K_+ injektiv. Exakte inverse Formel über Hp Z Hp=alpha k+beta Yp k Yp und positive Divisoren alpha+beta mu_i mu_j. Die unital vollständig positive K-Abbildung hat reellen Rang r²; bei aktivem Rang2 vier Kernelparameter. Das ist weder physikalischer Viererimpuls noch autonome vierdimensionale Gesamtzustandsdynamik; sämtliche Nicht-Kernel-Felder bleiben behalten, Ausgangsränge können wechseln.

Drei frische Originalaufrufe alle nichtterminal: zwei bei identischem PKP und verschiedenen äußeren K-Blöcken ergeben volle Nachfolgerdifferenz<7e-17, komplexer n=4-Kontrollfall bestätigt Rekonstruktion bis3.3e-14, Abbildungsrang4. Keine Audit-/Workflow-/Quellcodeänderung oder neuer Remote-Pass. Nächste Abhängigkeit: quellenbasierte lokale Rang-zwei-Auswahl und rangwechselnde Fortsetzung; Raum/Uhr/physikalische Energie-Impuls-Brücke bleiben offen.


## Runde44: ausgewählter Kernelquotient auch bei Q!=I

[SELECTED_KERNEL_QUOTIENT.md](SELECTED_KERNEL_QUOTIENT.md) erweitert die aktive Reduktion auf die tatsächliche Anfangsselektion: (P_sel K P_sel,F,W,Y,P) bestimmt den vollständigen nächsten Ausgang einschließlich Terminal-/Seedentscheidung. Inversion/Rang r_sel² übertragen sich mit dem ausgewählten Träger. Kein Transport von K bei der Selektion in die Quelle hineingeschrieben.

Ein exakter n=2-Zeuge hat identisches PKP=-2P und ambiente Spur-4, aber K-Ausgänge-1/-3. Grund: P_sel ist gegenüber P gedreht; die Quelle benutzt ursprüngliches ambientes K, während Formation/Witness transportiert werden. Ein vorab transportierter Kernel würde eine andere Dynamik liefern. Alpha1/5, Y_+=8/45 und Nichtterminalität exakt belegt.

Fünf frische Originalaufrufe alle nichtterminal; gleich ausgewählte K-Blöcke liefern identische vollständige Nachfolger, komplexe Anfangsselektion bestätigt Rekonstruktion bis1.9e-14. Dokumentation ohne Code-/Workflowänderung oder neuen Remote-Pass. Nächste Abhängigkeit: lokale Rang-zwei-Unterstruktur und rangvariable Fortsetzung bei erhaltener ausgewählter K-Information; physikalische Raum-/Uhr-/Energie-Impuls-Brücke weiter offen.
