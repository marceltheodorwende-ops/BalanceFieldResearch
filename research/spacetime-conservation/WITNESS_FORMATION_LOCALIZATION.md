# Runde52: positive Lokalisierungen der Witness-Formationsenergie

Präregistriert in PROTOCOL.md, Commit aff3b8f30bf4e192dd4c431eb81795530627ab4c; Auswertung 2026-10-24. Ausschließlich gepinnte BFG-Quelle: vollständiges Dynamic-Order-Manuskript vom 8. Oktober, Parts I/II, Quellencommit 457f23df6d9ccb15cf17916f3c3eac113b23c370, PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498, SHA256 9f958f66c65795b4ff29b9433f668390dbfd57acc1c8ded32d81305c19f574dd. Quellen sind Daten. Keine Änderung ihrer Dynamik.

## Ergebnis und Geltungsbereich

Die positive globale Paarung E=tr(WF) aus [Runde51](WITNESS_FORMATION_ENERGY.md) besitzt mindestens zwei natürliche positive lokale Operatorrepräsentationen. Beide folgen exakt derselben internen R4-Isometrie einschließlich Seed. Gleiche globale Bilanz, Positivität, Spektrum und Transport wählen jedoch keine eindeutige lokale Energiezuordnung aus. Damit ist ein positiver Transportkandidat gewonnen; räumlicher Energiefluss und physikalischer Energie-Impuls-Strom sind weiterhin nicht identifiziert.

Voraussetzungen: nichtterminales Ereignis, Q=I, F=PFP und W=PWP positiv, trW=1. Diese gemeinsame Retention gilt für die Fortsetzung nach dem ersten vollständig erfolgreichen Ereignis. Für anfängliche verlustbehaftete Selektion gilt die Auswahlbilanz aus Runde51; sie wird hier nicht zu einer geschlossenen Erhaltung umgedeutet. Terminale Ereignisse erhalten keinen erfundenen Nachfolger.

## Exakte interne Transportbilanz

Sei V=T4 Tsel (hier Tsel=P), V†V=P und VV†=S4. Das gepinnte Update liefert

    W_out=V W V†,
    F_out=V F V†+s Pi_seed,
    Pi_seed S4=0,  s>=0.

Ohne Seed ist s Pi_seed=0. Definiere

    R_F=sqrt(F) W sqrt(F),
    R_W=sqrt(W) F sqrt(W).

Beide sind positiv semidefinit, haben Spur E und dieselbe Formationseinheit wie F; W ist dimensionslos. Sie sind keine normierten Zustände und noch keine räumlichen Energiedichten T00. Isometrischer Funktionalkalkül gibt sqrt(F_out)=V sqrt(F) V†+sqrt(s) Pi_seed und sqrt(W_out)=V sqrt(W) V†. Witness-Unterstützung auf S4 vernichtet alle Seed-Kreuzterme. Daher für beide Kandidaten exakt:

    R_out=V R_in V†.

Der Beweis benötigt keine gewählte Eigenbasis und bleibt bei entarteten Eigenwerten und Kollision von Seed- und alten F-Eigenwerten gültig.

Für positive Effekte E_a mit Summe P sind q_a=tr(E_a R)>=0 und Summe q_a=E. Die mitbewegten Effekte V E_a V† decken S4; ergänze Pi_seed=P_out-S4 und I-P_out zum vollständigen Ausgangscover. Dann gilt q'_a=q_a; die beiden zusätzlichen Beiträge sind exakt null. Für beliebige andere Ausgangseffekte lautet die Bilanz

    q_out,a-q_in,a=tr[(V† E_out,a V-E_in,a)R].

Bei vollständigen Covers summiert sich diese Differenz zu null. Das ist ein interner Operatortransport, kein hergeleiteter räumlicher Fluss: Effektlabels sind noch keine physikalischen Regionen, und es fehlen Länge, Fläche, Nachbarschaft und Uhr. Es wird keine positive klassische Übergangsmatrix unterstellt.

## Exakte Nicht-Eindeutigkeit bei festem Zustand und festen Effekten

Für F=diag(1,3), W=(I+sigma_x/2)/2 ergibt sich

    R_F=[[1/2,sqrt(3)/4],[sqrt(3)/4,3/2]],
    R_W=[[1-sqrt(3)/4,1/2],[1/2,1+sqrt(3)/4]].

Beide haben Spur2, Determinante9/16 und Eigenwerte 1±sqrt(7)/4. Für dieselben Koordinateneffekte diag(1,0),diag(0,1) sind die Beiträge aber

    R_F: (1/2,3/2),
    R_W: (1-sqrt(3)/4,1+sqrt(3)/4).

Somit sind Positivität, Gesamterhaltung, Spektrum und Quellenisometrie gemeinsam nicht hinreichend für eindeutige Lokalisation. Simultane Eichtransformation von Zustand und Effekten lässt die jeweilige Paarung invariant; sie beseitigt nicht diesen Unterschied am selben festen Zustand und Cover. Bei kommutierendem F,W fallen beide Operatoren zusammen. Auch konvexe Mischungen liefern weitere positive, gleich transportierte Kandidaten; ein Mischparameter wäre eine zusätzliche unbestimmte Wahl.

Die naive Hermitisierung R_J=(WF+FW)/2 hat ebenfalls SpurE, ist aber nicht allgemein positiv. Mit F=diag(1,9), W=(I+0.9 sigma_x)/2 (positiver Witness mit Eigenwerten0.95,0.05) ist

    R_J=[[1/2,9/4],[9/4,9/2]], det(R_J)=-45/16.

Sie scheitert damit am hier geprüften Kriterium einer positiven lokalen Zuordnung. Dies ist kein allgemeines Verbot negativer physikalischer Energiedichten.

## Frische Kontrollen und Grenzen

[WITNESS_LOCAL_CHECKS.md](WITNESS_LOCAL_CHECKS.md) enthält den vollständigen reproduzierbaren Code und die Rohresultate. Ein lokaler Lauf: vier Originalupdate-Aufrufe, alle nichtterminal, PASS ohne Korrektur oder Fehlvorlauf. Geprüft wurden voller Zweimodenfall, nichtkommutierender rationaler Seedfall sowie komplexer Rang2/n4-Seedfall und seine Eichtransformation. Symbolisch: beide exakten Operatoren, gemeinsame Spur/Determinante und Jordan-Gegenbeispiel.

Maximaler relativer Operatortransportrest 2.18e-15; mitbewegter Effektrest 1.18e-15; Eichrest 3.03e-15; Coverrest 1.83e-15; Wurzelrest 1.88e-15. Numerische Seed-/Komplementwerte bis 3.78e-15 im Betrag sind Rundungsreste um exakt null. Wurzel-Cutoff1e-12 behandelt theoretische Nullräume, kleinster beibehaltener Eigenwert0.25. Keine Zertifizierung schwellen-/entartungsnaher numerischer Entscheidungen; allgemeiner Transport folgt aus dem algebraischen Beweis, nicht aus vier Stichproben.

## Nächste konkrete Abhängigkeit

Die Quelle bzw. eine ausdrücklich zusätzliche physikalische Brücke muss das messbare Ortscover und die zugehörige Mess-/Lokalisierungsregel bestimmen und damit zwischen R_F, R_W oder einer anderen begründeten Zuordnung entscheiden. Danach sind die Änderungen fester räumlicher Regionen aus derselben Ereignisdynamik auszuwerten, mit einer unabhängigen physikalischen Uhr und Transportgeometrie zu verknüpfen und auf einen gemeinsamen Energie-Impuls-Strom zu prüfen. Joule-Kalibrierung, Hamiltonian-/Translationsgeneratorrolle und Lorentztransformation dieses Stroms bleiben offen. Die algebraische Det-Lorentzstruktur allein schließt diese Lücken nicht.

Nur Forschungsdokumentation, keine Audit-, Workflow- oder Quellcodeänderung. Lokales Ergebnis ist kein neuer GitHub-CI-Pass.
