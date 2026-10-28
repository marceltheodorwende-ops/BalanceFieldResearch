# Runde54: Witness-Energiepopulationen sind nicht automatisch eine geschlossene lokale Dynamik

Präregistrierung PROTOCOL.md, Commit 9e63c32e3777063fe5348865e90d3bd92f611d53; Auswertung 2026-10-24. Nur gepinnte BFG-Quelle: vollständiges Dynamic Order vom 8. Oktober 2026, Parts I/II, Quellencommit 457f23df6d9ccb15cf17916f3c3eac113b23c370, PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498; Identitätsprüfung durch audit.load_update.

## Ergebnisstatus

Exakt bewiesen wird ein lineares Faser-Kriterium für energieaffine Populationsablesungen bei festem, Witness-unabhängigem Ereignistransport. Ein konkreter, frisch numerisch geprüfter BFG-Fall zeigt danach eine robuste Nichtgeschlossenheit des momentanen Y-Spektralcovers: gleiche eingehende Populationen und Gesamtenergie bei gleichen F,Y,K,P, verschiedene ausgehende Populationen. Der konkrete Zeuge ist ein Gleitkommaresultat ohne Intervallzertifikat; nicht als exakter algebraischer Gegenbeweis ausgeben.

Die Spektralcovers sind ein BFG-interner Kandidat für Labels, noch keine physikalisch identifizierten Ortsregionen. Die zusätzliche Energieinterpretation von W und F aus Runde51–53 bleibt eine Hypothese.

## Exaktes Kriterium (Standardmatrixalgebra)

Fixiere auf einem aktiven Träger P alle anderen Zustandsdaten, den gemeinsamen Retentionszweig und die Covers. Der Quellen-R4-Transport V ist dort unabhängig von W; keine W-abhängige Anfangskonditionierung wird einbezogen. Für den R_F-Kandidaten schreibe die Eingangsablesungen als

    q_i(W)=tr(W A_i),  A_i=P sqrt(F) E_i sqrt(F) P.

Die Ausgangsablesung ist ebenfalls linear,

    q'_j(W)=tr(W B_j),
    B_j=V† sqrt(F_out) E'_j sqrt(F_out) V.

Dann sind alle q'_j für sämtliche positiven normierten W auf P allein durch die q_i bestimmt genau dann, wenn

    B_j in span_R{P,A_1,...,A_n} für jedes j.

Das Kriterium betrifft auch beliebige deterministische, nicht nur lineare vorgeschlagene Populationsupdates. Beweis: Liegt B_j im Span, ist seine Erwartung eine affine Funktion der Eingangswerte. Andernfalls existiert ein hermitesches L im Hilbert-Schmidt-Orthogonalkomplement mit trL=0, tr(L A_i)=0 und tr(L B_j)!=0. Für hinreichend kleines epsilon>0 sind W±=P/r±epsilon L positive normierte Zustände, r=rankP. Sie haben dieselben q_i und verschiedene q'_j. Damit scheitert das Faser-Kriterium aus dem Manuskriptabschnitt89 für diese reduzierte Beschreibung. Das Argument benötigt ein ganzes zulässiges Witness-Umfeld um P/r; beschränkte physikalische Präparationen können den Schluss verändern.

Für F=P ist R_F=W. Bei dem folgenden K=-I-Zeugen und vollem Ausgangsraum hat K_out=-I, genau einen ergänzten Seed mit Stärke1 und F_out=I. Somit sind A_i=P E_i(Y)P und B_j=V† E_j(Y_out)V. Die Populationsberechnung mit W ist hier exakt dieselbe Kandidaten-Energieberechnung, keine neue Energiedefinition. Alle übrigen Daten und die Gesamtenergie1 sind für beide Witness-Präparationen identisch.

## Präregistrierter numerischer Originalfall

    P=F=diag(1,1,1,0), K=-I4,
    Y=[[.2,.03,.01,.08],
       [.03,.35,.02,.07],
       [.01,.02,.55,.06],
       [.08,.07,.06,.7]].

Eingangs-/Ausgangseffekte sind die nach Eigenwert sortierten einfachen Y-Spektralprojektoren. Der Originalschritt mit W=P/3 bestimmt V und die Ausgangseffekte; keine Änderung der Quellgleichungen und keine nachträgliche Anpassung an einen Einstein-Wert.

Im reell symmetrischen aktiven3x3-Raum wird jeder B_j orthogonal zum Span der A_i und P projiziert. Der größte Rest bestimmt den normierten L-Zeugen; das ist eine explizite Faser-Konstruktion aus dem vorab benannten Kriterium. Das Outputlabel j=2 zählt ab0, also das dritte Spektrallabel. W±=P/3±0.1L.

Frische Resultate:

- Eingangs-Spanrang4, kleinster nichtverschwindender Singulärwert0.1276258; redundanter fünfter Singulärwert2.95e-16.
- Gewählter Ausgangs-Spanrest0.2279948351.
- Kleinster aktiver Witness-Eigenwert0.2612725968, also strikt positiv auf P.
- Maximaler Eingangspopulationsunterschied1.11e-16.
- Maximaler Ausgangspopulationsunterschied0.04559896703, entsprechend 2*0.1*Spanrest.
- Gesamtenergie beider Zustände1, Ausgang0.9999999999999993; Ausgangsrang4.
- Kleinster Abstand verschiedener Y-Eigenwerte über Input/Output0.0177365691; keine nahezu entartete Spektralwahl.
- Komplexe simultane Eichkontrollen beider Präparationen: Populationsrest2.78e-16.

Die Originalausgangspopulationen sind etwa

    W+: (.008372199,.316558600,.352645096,.322424105),
    W-: (.006996025,.347354063,.307046129,.338603783).

Die Quelllasten wurden zusätzlich rational kontrolliert. Wichtig bei partiellem P: G=I+Y, Z eine Basis von ranP,

    PG=Z(Z†GZ)^(-1)Z†G, C=(I+Y)^(-1), B=YC,
    LC=tr(G PG C P C PG†),
    LB=tr(G PG B P B PG†),
    alpha=LB/(LC+LB)=4019981/31875481.

Die Vollträgervereinfachung tr(F C),tr(F Y² C) ist hier nicht zulässig.

## Prüfverlauf und Grenzen

[WITNESS_POPULATION_CHECKS.md](WITNESS_POPULATION_CHECKS.md) enthält Code und vollständige Rohdaten. Erster lokaler Lauf: alle fünf Originalereignisse, Populationsfaser und Eichkontrollen bestanden; danach scheiterte die zusätzliche symbolische alpha-Kontrolle, weil versehentlich die Vollträger-Lastformel verwendet wurde. Der Kontrollcode wurde auf den originalen G-Projektor korrigiert. Danach frischer vollständiger Lauf PASS mit fünf Originalereignissen. Insgesamt10 Originalaufrufe auf fünf Präparationen, final5; kein Fehler in der Originaldynamik geändert.

Die sichtbaren Abstände sind groß gegenüber den Residuen. Gleichwohl sind L, Spanrang und Spektralprojektoren hier numerisch bestimmt. Ein rigoroses Intervall-/algebraisches Zertifikat dieses konkreten Zeugen ist offen. Der allgemeine lineare Spansatz ist davon unabhängig exakt. Keine allgemeine Aussage, dass jedes BFG-Spektralcover oder jeder physikalische Zustand diese Nichtgeschlossenheit aufweist.

## Natürliche Alternative und nächste Abhängigkeit

Mitbewegte Effekte E'_i=V E_i V† liefern weiterhin exakt q'_i=q_i (plus orthogonale Nullbeiträge) gemäß Runde52. Sie sind eine geschlossene interne Buchführung, bestimmen aber keinen räumlichen Energiefluss. Das momentane Y-Spektralcover ist eichkovariant, doch seine Populationsablesung verliert die für das nächste Cover relevante Witnesskohärenz.

Ein autonomes Gesetz allein für diese momentanen lokalen Energiebestände, auch ergänzt um die gemeinsame Gesamtenergie, ist im numerisch geprüften Fall nicht möglich. Ein physikalischer Kontinuitätsansatz darf Kohärenzen bzw. Strom-/Wechselwirkungsdaten als zusätzliche Zustandsgrößen behalten; Nichtgeschlossenheit der Dichte allein widerlegt keine solche Kontinuitätsgleichung. Nächster konstruktiver Schritt: den notwendigen Witness-Observablenraum unter rückgezogenen Coverwechseln bestimmen und prüfen, welche dieser zusätzlichen Daten die BFG-Quelle bereits trägt. Physikalische Präparations-/Ortsbrücke, Uhr, Impuls und Generatorrolle bleiben offen.

Nur Forschungsdokumentation, keine Quell-/Audit-/Workflowänderung und kein neuer Remote-CI-Pass.
