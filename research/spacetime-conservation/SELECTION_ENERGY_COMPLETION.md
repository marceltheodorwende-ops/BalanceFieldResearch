# Runde61: Auswahlenergie braucht mehr als die verworfene Witnessmasse

Präregistrierung PROTOCOL.md, Commit 27afafc4fb0e4c0fedaf735477d5296ecdefc618; Auswertung 2026-10-24. Nur gepinnte BFG-Quelle: vollständiges Dynamic Order vom 8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370. PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498, durch audit.load_update geprüft.

## Status: explizite mathematische Vergleichsergänzung

Die Originalquelle liefert bei Anfangsselektion einen normalisierten behaltenen Witness-Nachfolger. In [Runde60](COMMUTING_SECTOR_SELECTION.md) änderte sich dessen bedingte Energie. Hier wird geprüft, ob ein zusätzlich mitgerechneter komplementärer Projektionszweig bereits eine geschlossene F-Erwartungsbilanz ergeben würde.

Dieser komplementäre Zweig ist KEIN von der BFG-Quelle spezifizierter physikalischer Nachfolger, kein nachgewiesenes Reservoir und keine Änderung des Originalupdates. Das binäre Lüders-Instrument dient ausschließlich als offen deklarierter mathematischer Vergleich. Frische Originalaufrufe prüfen nur den tatsächlich behaltenen Quellzweig.

Ergebnis: Auch dieser Vergleich schließt bei obliquer Auswahl die Energie nicht allgemein. Neben den beiden gewichteten Zweigenergien steht ein exakter Kreuzblockterm. Universelle Erhaltung durch diese besondere Zweigergänzung gilt genau dann, wenn der Selektor mit F kommutiert. Für einzelne geeignete Präparationen kann der Kreuzterm auch ohne diese universelle Bedingung verschwinden.

## Exakte Bilanzidentität

Fixiere einen orthogonalen Selektor S und R=I-S sowie positive F,W mit trW=1 und 0<m=tr(SW)<1. Definiere die komprimierten Vergleichsenergien

    E_S=tr(W S F S)/m,
    E_R=tr(W R F R)/(1-m).

Für den nichtterminalen behaltenen BFG-Zweig ist E_S genau die Quellenenergie tr(W_out F_out) aus der Auswahlformel von Runde51; der orthogonale Seed trägt kein Witnessgewicht.

Die Vergleichsergänzung besitzt die gewichtete Summe

    E_comp=m E_S+(1-m)E_R
          =tr[W(SFS+RFR)].

Aus I=S+R folgt dagegen

    E_in=tr(WF)
        =E_comp+X,
    X=tr[W(SFR+RFS)]
     =2 Re tr(W S F R).

Die Identität ist Standardmatrixalgebra. X ist ein reeller Erwartungs-Kreuzterm in Formationseinheiten; er wird hier nicht als physikalische Arbeit, Strahlung, Energie eines Apparats oder Impuls umbenannt. Sein Vorzeichen ist im Allgemeinen nicht festgelegt.

Für alle positiven normierten W gilt E_comp=E_in genau dann, wenn

    SFR+RFS=0.

Denn solche Dichten trennen hermitesche Operatoren. Multiplikation mit S von links und R von rechts liefert daraus SFR=0; mit Hermiteschheit von F auch RFS=0. Äquivalent ist [S,F]=0. Umgekehrt verschwinden die Kreuzblöcke bei [S,F]=0 unmittelbar.

Das klassifiziert allein das betrachtete binäre Projektionsinstrument. Andere Instrumente, Rückwirkungen und physikalische Energieablesungen werden dadurch nicht allgemein ausgeschlossen.

## Exakter obliquer Quellenzeuge

Wie in Runde60:

    P=I3, F=diag(1,2,3), W=F²/14,
    S=I3-ones3/3,
    K=-I3, Y=S/2+2(I3-S).

Die originale Q-Selektion ist S, der behaltene Schritt ist nichtterminal und hat Ausgangsdimension2. Exakt gilt

    m=2/3, 1-m=1/3,
    E_in=18/7,
    E_S=16/7,
    E_R=2,
    E_comp=(2/3)(16/7)+(1/3)2=46/21,
    X=8/21.

E_in=54/21 ist also trotz vollständiger Vergleichs-Witnessmasse um8/21 größer als die bloße Summe der komprimierten Zweigenergien. Das Defizit ist nicht einfach die Energie des verworfenen Drittels; die Auswahlbasis hat die F/W-Kreuzinformation zwischen S und R entfernt. Der Eingang erfüllt sogar [W,F]=0. Diese Kommutation allein macht die Mess-/Auswahlbasis nicht energieverträglich.

Die Source-Energie E_S bleibt dieselbe wie zuvor; die neue Rechnung untersucht eine andere Fragestellung, nämlich die ausdrücklich hypothetische unbedingte Zweigergänzung.

## Zwei positive Alternativen mit verschiedenen Voraussetzungen

1. Geschützte Hintergrundselektion S0=diag(1,1,0) beim selben F,W:

       m=5/14, E_S=9/5,
       1-m=9/14, E_R=3,
       E_comp=18/7=E_in, X=0.

   Weil [S0,F]=0, gilt diese Vergleichs-Erhaltung für ALLE W. Die einzelne behaltene bedingte Energie bleibt dennoch9/5 statt18/7. Eine konditionierte Erwartungsänderung und eine gewichtete unbedingte Erhaltung dürfen nicht verwechselt werden.

2. Gleiche oblique Hintergrundselektion S, aber W=I3/3:

       m=2/3, E_S=E_R=2,
       E_comp=E_in=2, X=0.

   Hier kommutiert W mit S und hat deshalb keine Auswahl-Kreuzkohärenz. Das ist eine Einzelpräparationsalternative, keine universelle Eigenschaft des obliquen S/F-Paars. Allgemein reicht [W,S]=0 für X=0, während [W,F]=0 allein nach dem Hauptzeugen nicht ausreicht.

Diese Alternativen sind mathematisch positiv beschrieben; weder der verworfene Vergleichszweig noch eine Kopplung, die ihn physikalisch realisiert, sind damit aus BFG hergeleitet.

## Frische Kontrolle und genaue Grenzen

[SELECTION_ENERGY_COMPLETION_CHECKS.md](SELECTION_ENERGY_COMPLETION_CHECKS.md) enthält vollständigen Reproduktionscode und Rohdaten. Ein frischer lokaler Lauf PASS ohne Fehlvorlauf/Korrektur, vier Originalaufrufe: obliquer Hauptfall, geschützter Fall, obliquer gemischter Witness und komplexe simultane Eichversion des Hauptfalls (Seed20261111).

Die drei Vergleichsfälle wurden unabhängig rational berechnet. Original-Quellenergie und E_S stimmen bis8.89e-16 überein; vollständige Vergleichsbilanz bis5.00e-16, Kreuzterm-Eichrest2.23e-16. Der Quellcode wurde nicht um einen verworfenen Zweig ergänzt. Die Vergleichsenergien E_R sind direkte Matrixkompressionen, keine aus einer beobachteten BFG-Fortsetzung des Komplements gewonnenen Resultate.

Die Identität und die universelle Kommutantenbedingung sind exakt, die Zahlenkontrollen sind Implementierungsevidenz. Es werden keine empirische Energieeinheit, kein neuer physikalischer Speicher und keine vollständige Energie-Impuls-Erhaltung behauptet.

## Nächste Abhängigkeit

Eine physikalische Auswahlbilanz muss erklären, wie die behaltene Konditionierung, verworfene Information und gegebenenfalls der Kreuzterm mit unabhängig bestimmten messbaren Trägern zusammenhängen. Allein eine zusätzliche Liste verworfener Zweigenergien reicht außerhalb des energiekompatiblen Selektionssektors nicht. Das liefert ein konkretes Prüfkriterium für spätere Brücken, aber kein Recht, den Kreuzterm nachträglich als beliebige fehlende Energie zu deklarieren. Physikalische Orts-, Uhr-, Generator- und Impulsabbildungen bleiben offen.

Nur Forschungsdokumentation; Manuskript, Grundgleichungen, Lizenzen, empirische Ergebnisse, Audit und Workflow unverändert. Kein neuer Remote-CI-Pass.
