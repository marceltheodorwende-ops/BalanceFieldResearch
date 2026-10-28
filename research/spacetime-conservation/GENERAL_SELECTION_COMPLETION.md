# Runde62: allgemeine CP-Auswahlergänzung und kohärente Alternative

Präregistrierung PROTOCOL.md, Commit ca635ba21755f1cae160c73d5c12fd925d546489; Auswertung 2026-10-24. Nur BFG: vollständiges Dynamic Order vom 8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370. PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498, von audit.load_update geprüft.

## Ergebnis und Zusatzannahmen

Das Kreuzblockhindernis aus [Runde61](SELECTION_ENERGY_COMPLETION.md) liegt nicht nur am dort gewählten Lüders-Komplement. Es betrifft jede vollständig positive Instrumentergänzung desselben scharfen behaltenen Quellzweigs, wenn Ergebnisse klassisch getrennt und ihre Energie blockadditiv zugeordnet werden. Universelle F-Erwartungserhaltung verlangt dann [S,F]=0.

Eine kohärente isometrische Erweiterung mit Kreuzenergie kann dagegen mathematisch konstruiert werden. Sie reproduziert den behaltenen Quellenzweig und erhält die F-Erwartung. Diese Konstruktion ist ausdrücklich KEINE von BFG ausgewählte physikalische Umgebung, Wechselwirkung, Uhr oder Energie-Impuls-Herleitung. Eine zu einem beliebigen Auswahlprozess passend konstruierte Erhaltung identifiziert allein noch keine physikalische Energie.

Geprüfte Klasse: rho_Q=W als zusätzliche Zustandsbrücke; feste F/Y/K/P und damit festes nichtterminales Quellereignis; unveränderte unnormierte behaltene Operation; vollständig positive, eingangszustandsunabhängige Vergleichs-Instrumente; additive Energieobservablen in getrennten Ergebnisblöcken. Andere Zustands-/Auswahlbrücken und interbranch-kohärente Observablen sind nicht ausgeschlossen.

## Exakter Satz für beliebige verworfene CP-Operationen

Die unnormierte behaltene Quelloperation ist

    I_S(W)=V W V†, V†V=S,
    V† F_out V=SFS.

Der normierte Ausgang ist I_S(W)/tr(SW), wie in der Originalquelle. Orthogonale Seedanteile tragen zum Energie-Pullback nicht bei.

Ergänze beliebige verworfene Krausoperatoren K_b mit zusammen vollständigem Instrument:

    sum_b K_b†K_b=R=I-S.

Für jeden x in ranS gilt Sum_b ||K_b x||²=<x,Rx>=0. Also K_b S=0 für alle b und damit K_b=K_b R. Diese Trägeraussage gilt unabhängig von Feedback, Ausgangsdimension oder Anzahl der verworfenen Operationen.

Bei beliebigen festen hermiteschen verworfenen Energieobservablen H_b ist der gesamte Pullback

    G_R=sum_b K_b† H_b K_b=R G_R R.

Universelle Erwartungserhaltung bei blockadditiver Ausgangsenergie würde erfordern

    F=SFS+G_R.

Die rechte Seite hat keine S/R-Kreuzblöcke. Somit notwendig SFR=RFS=0, also [S,F]=0. Dieses Hindernis benötigt nicht einmal Positivität der H_b. Erhaltung für alle positiven normierten W ist zur Operatoridentität äquivalent; eine Kompensation für nur einen einzelnen bekannten W genügt nicht.

Umgekehrt existiert bei [S,F]=0 eine solche mathematische Ergänzung: K_R=R und H_R=F liefern G_R=RFR und SFS+RFR=F. Das ist eine Existenzaussage, nicht die Behauptung, jedes beliebig gewählte H_b erhalte Energie. Sie spezifiziert auch keinen tatsächlichen BFG-Nachfolger des verworfenen Zweigs.

Allgemein bleibt für jeden Kandidaten der feste Offdiagonalrest

    S(F-SFS-G_R)R=SFR.

Daher kann kein klassisch getrennter verworfener CP-Kanal innerhalb dieser Klasse die fehlende Kreuzenergie universell ergänzen.

## Positive kohärente Vergleichskonstruktion

Setze auf dem direkten Summenraum des behaltenen Ausgangs und einer mathematischen Komplementkopie

    J=[V; R], J†J=S+R=I.

Für W ist omega=J W J† eine positive normierte Gesamtdichte. Ihr behaltenes diagonales Teilstück ist V W V†, sodass die Konditionierung genau die ursprüngliche Witness-Quelle reproduziert.

Mit dem ursprünglichen Quellen-Seedterm N=F_out-V F V†>=0, N V=0, definiere

    H_ext=J F J†+diag(N,0)
         =[[F_out, V F R],
           [R F V†, R F R]].

Für F>=0 ist H_ext>=0. Zudem J† H_ext J=F, also

    tr(omega H_ext)=tr(WF).

Die positive Energiekonstruktion stimmt im behaltenen Diagonalblock mit dem Quellen-F_out überein. Der Preis sind kohärente Kreuzblöcke zwischen den beiden Ergebnisräumen. Für [S,F]!=0 kommutiert H_ext nicht mit dem klassischen Ergebnisprojektor. Die Gesamtdichte besitzt zugleich Kreuzblöcke V W R, solange der Eingang solche Auswahlkohärenzen trägt.

Wird der Ergebnisraum klassisch dephasiert, verschwinden diese Dichte-Kreuzblöcke und es bleibt

    tr(D_outcome(omega) H_ext)=tr[W(SFS+RFR)].

Genau die Kreuzerwartung aus Runde61 geht verloren. Die universelle CP-Ergänzungsgrenze und die kohärente Konstruktion widersprechen einander nicht: sie haben verschiedene Anforderungen an die Bedeutung des Ergebnisregisters und der Gesamtenergie.

J und H_ext wurden nach dem gewünschten Pullback konstruiert. Das beweist mathematische Konsistenz einer kohärenten Erweiterung, aber weder ihre physikalische Existenz noch eine unabhängige BFG-Auswahlregel, einen Hamiltonianfluss oder eine lokale Energie-Impuls-Bilanz.

## Exakter Quellenzeuge und frische Kontrollen

Am bisherigen rationalen Grundzustand

    F=diag(1,2,3), W=F²/14,
    S=I-ones/3, R=I-S, P=I,
    Y=S/2+2R, K=-I

ist der Kreuzoperator

    SFR+RFS=[[-2/3,-1/3,0],
             [-1/3,0,1/3],
             [0,1/3,2/3]],

mit Frobeniusnorm²4/3 und Witness-Erwartung8/21. Insbesondere ||SFR||_F=sqrt(2/3)>0. Jeder klassisch blockadditive CP-Komplementansatz hat diesen Offdiagonalrest unabhängig vom gewählten G_R.

Die kohärente Konstruktion hat hier Dimension5, reproduziert die behaltene zweidimensionale Quelle und hält E_in18/7. Nach klassischer Ergebnisdephasierung bleibt dagegen46/21, genau wie Runde61. Bei der geschützten Kontrollauswahl S0=diag(1,1,0) ist der Kreuzoperator null, und kohärente/dephasierte Energien stimmen überein.

[GENERAL_SELECTION_COMPLETION_CHECKS.md](GENERAL_SELECTION_COMPLETION_CHECKS.md) enthält Code und Rohdaten. Ein frischer lokaler Lauf PASS ohne Fehlvorlauf/Korrektur mit drei Originalereignissen: obliquer Hauptfall, geschützter Fall, komplexe simultane Eichversion (Seed20261112). Diese Originalaufrufe betreffen nur den behaltenen Quellzweig.

Pro Fall wurden zusätzlich zwei mathematische verworfene Krausoperatoren K_b=sqrt(p_b)U_b R,p=(.25,.75), mit zufälligen komplexen unitären U_b geprüft. Ihre Effektsumme ist R; beliebige feste positive Vergleichsenergie diag(4,5,6) liefert einen auf R gestützten Pullback. Sie wird nicht auf erfolgreiche Kompensation eines einzelnen Erwartungswerts nachkalibriert.

Numerische Maximalreste: Erweiterungsisometrie5.36e-16, behaltene konditionierte Dichte5.30e-16, verworfene Effektsumme2.62e-16 und Pullbackstützung9.66e-16. Unvermeidbare Offdiagonalnorm0.8164965809 im obliquen Fall,0 im geschützten. Zugehöriger Identitätsrest1.06e-15, Cross-Eichrest5.56e-17. Die allgemeine Aussage folgt aus dem exakten Stützraumbeweis, nicht aus drei Zufallsinstrumenten.

## Nächste Abhängigkeit

Eine universelle Auswahlbilanz mit unveränderter scharfer Quelle muss entweder energiekompatible Selektoren begründen oder eine unabhängig bestimmte zusätzliche physikalische Struktur enthalten, die über klassisch additive Ergebnisenergien hinausgeht. Die explizite kohärente Alternative zeigt, welche Kreuzdaten eine solche Erweiterung tragen müsste; sie ersetzt deren Herleitung nicht. Physikalische Orts-/Uhr-/Generator-/Impulsabbildung bleibt offen.

Nur Forschungsdokumentation; ursprüngliche Manuskripte, Grundgleichungen, Lizenzen und empirische Ergebnisse unverändert, keine Audit-/Workflowänderung und kein neuer Remote-CI-Pass.
