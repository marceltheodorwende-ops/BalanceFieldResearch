# Auswahl des Load-Gesetzes: Grenzen der Herleitung und unabhängiger Prüfplan

Stand: 21. September 2026. Fortsetzung des [Rebuild-Eingabevertrags](../rebuild-input-contract-2026-09-21/README.md). Status: mathematische Prüfung und prospektiver Prüfentwurf. Keine Messung, keine empirische Bestätigung und keine Änderung des Referenzgesetzes.

## 1. Die vorhandenen Prinzipien liefern keine eindeutige Auswahl

Im skalaren endlichen SA-Zweig ist q=||p||²/||D_old||², 0<q<1/4, und der nächste Load lautet g=h(q). Die drei Vergleichsgesetze sind H1: h(q)=q, H2: h(q)=q², H3: h(q)=q/2.

Gezielt erneut geprüft wurden Unified V4, insbesondere S. 8 (reziproke Balance), S. 9 (Kontrastnormalisierung), S. 31 (Schließungsannahmen und physikalische Energieinterpretation), sowie Strong Form V2, Abschnitte zur neutralen Elimination, lokalen physikalischen Schließung und zum terminalen Energiebudget. Quellenidentität und Grenzen des extrahierten Textkorpus sind in der [vorherigen Quellenprüfung](../next-gram-identifiability-2026-09-21/README.md) dokumentiert. Diese Recherche ist keine vollständige Abwesenheitsprüfung in allen BFG-Schriften.

| Prinzip | Konsequenz | Keine daraus belegte Konsequenz |
|---|---|---|
| Reziproke Balance, V4 Gl. (32)–(34) | Gewichte der beiden alten persistenten Lasten | Numerischer Wert des nächsten Gram-Loads |
| Exakte neutrale Elimination | C(Y)=(I+Y)^(-1), sobald Y feststeht | Auswahl von Y oder h aus der Minimierung über den neutralen Hilfswert |
| Kontrastnormalisierung, V4 BFG-C4 | z=(1-y)/(1+y) kodiert den gegebenen Load | Identifikation von y_next mit dem alten Paketgewinn |
| No-Retuning | Ein gewähltes Gesetz bleibt stufen- und zielunabhängig fest | Eindeutige Auswahl zwischen drei jeweils festen Gesetzen |
| Physikalische Erhaltungssätze | Zusätzliche Realisierungs- und Bilanzanforderungen in den betreffenden physikalischen Sektoren | Gleichsetzung der strukturellen Graphnorm mit Joule-Energie oder allgemeine Normerhaltung beim Reclosure |

Insbesondere wäre die Zusatzforderung E_next=E_old im hier definierten dissipativen Schritt mit jeder positiven Wahl g unvereinbar: E_next/E_old=q/((1+g)(1+eta_old))<1/4. Sie kann deshalb keine der drei Regeln auswählen. Das ist keine Widerlegung physikalischer Energieerhaltung: Für diese fehlen eine validierte Energieabbildung und die Bilanz weiterer Kanäle.

Die schon konstruierten Gegenmodelle beweisen Nicht-Eindeutigkeit relativ zu den explizit geprüften Bedingungen. Ein zusätzliches Originalaxiom könnte sie ausschließen, müsste aber als zusätzliche Prämisse genau belegt werden.

## 2. Warum einfache Reparaturaxiome noch keine interne Herleitung sind

Auch Glattheit, Monotonie, Positivität und h(0)=0 unterscheiden H1–H3 nicht. Die zusätzliche Normierung h'(0)=1 würde H2 und H3 ausschließen, lässt aber etwa h(q)=q+q² zu. Diese Alternative ist weiterhin positiv, glatt, monoton und hat dieselbe Ableitung am Ursprung; der bisherige Schließungs- und Dissipationsbeweis gilt auch für sie.

Additivität h(x+y)=h(x)+h(y) für positive x,y mit x+y<1/4 zusammen mit Positivität erzwingt auf diesem Intervall h(q)=c q: Positivität liefert Monotonie, rationale Unterteilungen liefern Linearität auf rationalen Vielfachen, und monotone Approximation erweitert sie auf alle Werte. Erst eine unabhängige Normierung legt c=1 fest. In den geprüften Quellen wurde weder diese Additivität des neuen Loads noch die benötigte Normierung hergeleitet.

Auch eine postulierte Kompositionsregel h(xy)=h(x)h(y) wählt H1 nicht allein: H2 erfüllt sie ebenfalls. Zudem muss erst begründet werden, weshalb zwei aufeinanderfolgende Reclosure-Schritte mit wechselnden Räumen und neuem Resolventen überhaupt durch die Multiplikation ihrer Paketgewinne beschrieben werden dürfen. Die Annahme ist kein automatischer Inhalt der vorhandenen Iteration.

**Entscheidung:** Keine neue Zusatzbedingung wird hier als ursprünglicher BFG-Satz ausgegeben. Das Referenzgesetz bleibt eine deklarierte Modellergänzung.

## 3. Unabhängig beobachtbare Größe

Für den skalaren nächsten Gramoperator Y_next=gI ist die neutrale Response

    C_next=sI,  s=1/(1+g).

Operationaler Prüfentwurf: An einem für den Messvorgang festgehaltenen nächsten Zustand wird eine unabhängig kalibrierte Eingabe u und ihre neutrale Ausgabe v erfasst. Das Modell sagt v=s u voraus. Bei mehreren Anregungsrichtungen müssen Linearität und die skalare Wirkung zusätzlich geprüft werden; eine einzelne Richtung beweist keine Isotropie des Operators. Messung darf den zugrunde gelegten Zustand nicht unmodelliert verändern.

Die physikalische Bedeutung von u und v, ihre gemeinsame Skalierung, die Präparation und der Messapparat sind derzeit nicht festgelegt. Deshalb ist dies eine mathematische Schnittstelle für einen späteren Versuch, kein bereits realisierbares universelles BFG-Messgerät.

Insbesondere ist v=(1+h(q))^(-1)u aus dem Referenzcode keine unabhängige Ausgabe. Ebenso wäre es zirkulär, eta_next durch dieselbe Regel zu erzeugen und die Übereinstimmung anschließend als Bestätigung zu zählen. q muss aus getrennt bestimmten alten Zustands-/Paketdaten stammen, ohne s zur Anpassung seiner Skalierung zu verwenden.

## 4. Exakte Vorhersagen und erforderliche Trennschärfe

Für q=1/5 lauten die Vorhersagen:

| Hypothese | g | s |
|---|---:|---:|
| H1 | 1/5 | 5/6 = 0,833333… |
| H2 | 1/25 | 25/26 = 0,961538… |
| H3 | 1/10 | 10/11 = 0,909091… |

Der kleinste Abstand ist 15/286. Bei exakt bekanntem q und einer vorab abgesicherten absoluten Gesamtfehlergrenze epsilon für s sind die drei zulässigen Messwertbänder paarweise disjunkt, wenn

    epsilon < 15/572 = 0,026223776… .

Dies ist eine deterministische hinreichende Trennbedingung für diese drei Punktvorhersagen, keine Aussage über Teststärke, Konfidenz oder vorhandene Instrumentengenauigkeit. Fehlergrenzen müssen alle relevanten Kalibrier-, Mess- und vereinbarten Abbildungsfehler umfassen und unabhängig begründet werden.

Ist q nur im vorab bestimmten Intervall [0,19;0,21] bekannt, ergeben sich stattdessen:

    H1: s in [100/121, 100/119],
    H2: s in [10000/10441, 10000/10361],
    H3: s in [200/221, 200/219].

Der kleinste Zwischenraum dieser Intervalle ist 101800/2286579. Nach Erweiterung jedes Intervalls um +/-epsilon bleiben sie disjunkt für

    epsilon < 50900/2286579 = 0,022260329… .

Die rationalen Rechnungen stehen in [PREDICTIONS.json](PREDICTIONS.json). Beide q-Szenarien sind Entwurfsbeispiele und keine bereits gemessenen Zustände. Allgemein werden aus [q_low,q_high] die Responseintervalle [1/(1+h(q_high)),1/(1+h(q_low))] gebildet, da alle drei h monoton wachsen. Für q nahe null nähern sich die Vorhersagen an; es gibt keine positive einheitliche Trennschwelle auf dem gesamten offenen SA-Bereich.

## 5. Vorab festzulegende Entscheidung

1. Reales System, Rolle der Variablen, Eingabe/Ausgabe, Skalierung, Präparation und SA-Zulässigkeit definieren. Ein fehlendes Abbildungsverfahren wird nicht durch Simulation ersetzt.
2. H1–H3, q-Bestimmung, Fehlerbudget und Auswertungsregel vor Ergebnisinspektion einfrieren. Keine anschließende individuelle Normierung je Hypothese.
3. Für einen gemessenen Wert s_hat ist eine Hypothese kompatibel, wenn s_hat im um epsilon erweiterten Vorhersageintervall liegt. Andernfalls ist sie unter den deklarierten Abbildungs- und Fehlerannahmen ausgeschlossen.
4. Kein kompatibles Modell: Abbildung, SA-Annahmen oder die gesamte Kandidatenfamilie scheitern; keine Regel nachträglich passend machen. Mehrere kompatible Modelle: Ergebnis unentscheidend. Genau eines: dieses Modell überlebt den vorab festgelegten Vergleich an diesem Zustand, ohne dadurch universell bewiesen zu sein.
5. Mehrere vorab ausgewählte Zustände und unabhängige Wiederholungen benötigen denselben festen h-Verlauf. Bei statistischen statt garantierten Fehlergrenzen ist zusätzlich ein eigener vorab festgelegter statistischer Prüfplan erforderlich.

## 6. Arbeitsstand und konkrete Grenze

Die theoretische Auswahl ist mit den geprüften Prinzipien nicht erreicht. Der unabhängige Vergleich ist nun mit Vorhersagen, Fehlerschwellen und Auswertungsregeln spezifiziert. Seine Ausführung benötigt ein konkretes Trägersystem und unabhängig gewonnene Zustands-/Response-Daten; solche Daten wurden in dieser Stufe nicht erzeugt oder vorgelegt.

Dies folgt den Auditkriterien Claim-State, Unterscheidbarkeit, Redescription, Quellenhierarchie und Erhalt negativer Ergebnisse. Der Entwurf ist noch keine registrierte empirische Präregistrierung. Weitere Konsistenztests desselben Referenzcodes würden diese fehlende Evidenz nicht liefern. Die sieben universellen Probleme bleiben offen, soweit ihre bisherigen bedingten Teilresultate sie nicht abdecken.
