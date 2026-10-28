# Runde58: Informationsgrenze der Instrumente des unveränderten Witness-Kanals

Präregistrierung PROTOCOL.md, Commit 783eda3730090d5a18ced2475b12f70f26365bf9; Auswertung 2026-10-24. Ausschließlich BFG: vollständiges Dynamic Order vom 8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370, PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498, durch audit.load_update geprüft.

## Ergebnis und physikalischer Status

Manuskript§26 benennt Quantenoperationen und Instrumente als zu prüfende zusätzliche Brücke. Unter der zusätzlichen Identifikation rho_Q=W ist der tatsächliche Witness-Transport bei festem F/Y/K/P und gemeinsamer Retention ein isometrischer, mathematisch energieerhaltender Quantenkanal. Jede vollständig positive Instrumentzerlegung, deren unbeobachteter Kanal mit ihm für alle unterstützten W übereinstimmt, hat auf diesem Träger nur von W unabhängige Ergebniswahrscheinlichkeiten.

Das ist eine präzise Grenze für informative Messungen innerhalb des unveränderten universellen Witness-Kanals. Es verbietet weder externe Messungen mit Rückwirkung noch eine Quantenbrücke mit eingeschränkten Präparationen, anderen Zuständen oder zusätzlichen Kopplungen. Es identifiziert auch keine physikalische Energieeinheit, Uhr oder räumlichen Impuls.

## Tatsächlicher Witness-Kanal statt K-C/B-Kanal

Die BFG-Quelle liefert auf dem gemeinsamen nichtterminalen Retentionszweig

    E(W)=V W V†, V†V=P, W=PWP, trW=1.

Hier ist V=T4 Tsel. F,Y,K,P werden während der Kanalbetrachtung festgehalten. Wegen der Retentionsbedingungen sind beide Witness-Normierungen exakt1 und der geometrisch bestimmte V ist von W unabhängig. Das gilt auch bei einem nichtterminalen Seed und bei wechselnder Hilbert-Dimension; der Seed trägt keine Witnessmasse.

Dieser Kanal ist nicht der C/B-Kompressionskanal des Kernels K aus früheren Runden. Eine Krausdarstellung der K-Transformation darf nicht als physikalisches Instrument für W eingesetzt werden, ohne dass ihre Wirkung auf W mit dem Originalupdate übereinstimmt.

Als positiver mathematischer Befund gilt zudem

    V† F_out V=F auf ranP,
    tr[E(W) F_out]=tr(WF).

Daher erfüllt dieser konkrete isometrische Kanal die F-Erwartungsbilanz für alle unterstützten W. Eine energieerhaltende Quantenoperation ist jedoch noch kein kontinuierlicher Hamiltonianfluss; die Generatorgrenze aus Runde57 wird dadurch nicht aufgehoben.

## Exakter Instrumentsatz (Standard-CP-Matrixalgebra)

Sei Z eine orthonormale Basis von ranP, J=VZ und J†J=I_r. Betrachte ein endliches vollständig positives Instrument I_a mit

    sum_a I_a(rho)=J rho J†

für alle positiven normierten r-dimensionalen Eingabedichten rho. Die Instrumentvorschrift ist fest, darf also nicht vom unbekannten rho selbst abhängen.

Der unnormierte Choioperator des Gesamkanals ist

    C_E=|vec J><vec J|.

Er hat Rang1 und Spur r. Für jedes a ist C_a>=0 und Sum C_a=C_E. Jeder Vektor orthogonal zu vecJ hat daher Erwartung0 in jedem C_a; Positivität erzwingt dessen vollständige Annihilation. Somit liegt jedes C_a im selben eindimensionalen Träger:

    C_a=p_a |vec J><vec J|, p_a>=0, sum p_a=1,
    I_a(rho)=p_a J rho J†.

Äquivalent sind sämtliche Krausoperatoren auf dem aktiven Input proportional zu J. Zurück im ursprünglichen Träger:

    I_a(W)=p_a V W V†,
    E_a=p_a P,
    Prob(a|W)=p_a.

Bei p_a>0 ist auch der normierte bedingte Witnesszustand derselbe E(W). Es entsteht keine W-abhängige Ergebnisinformation durch eine solche Instrumentzerlegung. Randfälle r=1 sowie isometrische Dimensionsvergrößerung ändern den Rang1-Beweis nicht.

Die Wahrscheinlichkeiten dürfen von den festgehaltenen Hintergrunddaten F/Y/K/P und der gewählten Instrumentvorschrift abhängen. Ausgeschlossen ist allein Information über eine unbekannte Witness-Präparation bei demselben Hintergrund und unverändertem universellem Gesamtkanal. Dies ist keine Aussage, dass der vollständige BFG-Zustand keinerlei Informationen trägt.

Die Gleichheit nur auf einer kommutierenden Präparationsfamilie genügt nicht für den Satz; dann müssen die Instrument-Choioperatoren nicht dieselbe universelle Kanalzerlegung darstellen.

## Informative F-Messung: gleiche Energie ist schwächer als gleiches Update

Seien Pi_l die Spektralprojektoren von F auf dem aktiven Träger. Die natürliche projektive Energieablesung vor dem Quellen-R4-Transport hat unbeobachtete Wirkung

    D_F(W)=sum_l Pi_l W Pi_l,
    W_meas,out=V D_F(W) V†.

Sie erhält tr(WF), weil F mit jedem Pi_l kommutiert. Im Allgemeinen gilt aber D_F(W)!=W, also stimmt der vollständige Witness-Nachfolger nicht mit dem Originalupdate überein. Eine zusätzliche Messkopplung müsste diese Rückwirkung ausdrücklich als physikalische Erweiterung erklären.

Exakt für

    F=diag(1,3),
    W=[[1/2,1/4],[1/4,1/2]]

ist D_F(W)=I/2 und

    tr(WF)=tr[D_F(W)F]=2,
    ||W-D_F(W)||_F²=1/8.

Die Energie bleibt2, die verlorene Kohärenz ist jedoch nicht null. Das Quadrat des Defekts ist rational exakt; sein Quellen-Ausgangsdefekt ist wegen der Isometrie gleich groß. Somit ist dieses informative Messinstrument kein Instrument des unveränderten Witness-Gesamtkanals auf allen Zuständen.

## Positive eingeschränkte Alternative

Für in F blockdiagonale W gilt D_F(W)=W. Auf dieser eingeschränkten Präparationsfamilie kann eine projektive F-Messung informativ sein und gleichzeitig den unbeobachteten Witness-Zustand unverändert lassen. Beispiel:

    W_A=diag(3/4,1/4), Energie3/2, Prob_F=(3/4,1/4),
    W_B=diag(1/4,3/4), Energie5/2, Prob_F=(1/4,3/4).

Das ist eine echte mathematisch verträgliche Alternative für diese Zustandsfamilie. Die BFG-Quelle erlaubt aber auch kohärente W; eine physikalische Einschränkung auf kommutierende Präparationen wäre separat zu begründen und darf nicht stillschweigend eingesetzt werden.

Ein von W unabhängiges Zufallslabelinstrument p=(0.3,0.7) ist dagegen auf allen Witness-Zuständen mit dem unveränderten Kanal kompatibel. Es bestätigt die zulässige Rang1-Klasse, liefert jedoch keine Information zur Unterscheidung der unbekannten W-Präparationen.

## Frische Kontrollen

[WITNESS_INSTRUMENT_CHECKS.md](WITNESS_INSTRUMENT_CHECKS.md) enthält vollständigen Code und Rohdaten. Ein frischer lokaler Lauf PASS ohne Fehlvorläufe/Korrektur, fünf vollständige Originalereignisse: voller Kohärenzzeuge, beide diagonalen Präparationen, rationaler Rang2/n3-Seedzeuge mit nichtkommutierendem W und dessen komplexe Eichversion (Seed20261108).

Bei allen fünf Fällen numerischer Choi-Rang1 mit unnormiertem Spektrum(r,0,...), r=2. Maximaler Choi-Spektrumrest1.42e-15, Isometrierest1.18e-15, Witness-Quellrest6.03e-16 und Zufallsinstrumentrest5.57e-16. Kohärenz-Pinchingdefekt0.3535533906, Seedfall0.1414213562, komplexer Eichrest1.12e-16. Beide diagonalen Präparationen haben Pinchingdefekt0 und die unterschiedlichen oben angegebenen Messwahrscheinlichkeiten. Sämtliche Pinching-Erwartungsenergien bleiben bis Rundung erhalten.

Der allgemeine Instrumentsatz folgt aus der exakten Rang1-/Positivitätsargumentation; fünf Choi-Spektren ersetzen diesen Beweis nicht. Die Kontrollen betreffen nur den festgelegten Retentionszweig, nicht terminale oder Witness-konditionierende Anfangsereignisse.

## Nächste konkrete Abhängigkeit

Eine informative physikalische Messbrücke muss festlegen, ob und wie sie den Witness verändert, die physikalischen Präparationen beschränkt oder andere BFG-Daten/Zustände ausliest. Ein zusätzliches verborgenes informatives Ergebnis bei universell unverändertem Witness-Gesamtkanal reicht nicht aus. Für eine räumliche Energie-Impuls-Bilanz bleiben die unabhängige Orts-/Transport-/Uhr-/Generatoridentifikation offen. Es wird kein solcher Mechanismus zur Anpassung an ein gewünschtes Einstein-Ergebnis ergänzt.

Nur Forschungsdokumentation; Manuskript, Grundgleichungen, empirische Ergebnisse, Audit und Workflow unverändert. Kein neuer Remote-CI-Pass.
