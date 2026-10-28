# Runde60: Anfangsselektion kann den kommutierenden Energiesektor verlassen

Präregistrierung PROTOCOL.md, Commit 5baa53d51ad1f305f38a3d0f3e8d92be306d944b; Auswertung 2026-10-24. Nur BFG: vollständiges Dynamic Order vom 8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370, PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Gepinntes Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498, von audit.load_update geprüft.

## Ergebnis und Einordnung

Der in [Runde59](COMMUTING_FORMATION_SECTOR.md) exakt stabile kommutierende Witness-/F-Sektor ist eine Retentionsaussage. Eine echte anfängliche BFG-Selektion kann ihn verlassen: Ein vollständig kommutierender positiver Eingang W=F²/14 wird durch die originale oblique Q-Selektion in einen nichtkommutierenden Nachfolger mit exakt ||[W_out,F_out]||_F²=1/294 überführt.

Damit ist die positive messbare Präparationsklasse nicht automatisch unter beliebigen vollständigen Anfangsupdates abgeschlossen. Eine geschützte Selektion bleibt als natürliche Alternative erhalten. Auch diese kann jedoch die bedingte Energie ändern; Schutz der Kommutation ist nicht gleich vollständige Energieerhaltung.

Die Aussagen betreffen die BFG-Matrizen und ihre zusätzlichen Energie-/Quantenkandidaten. Es wird keine physikalische Messkopplung eingeführt und keine verlorene Witnessmasse als erfundenes Reservoir verbucht.

## Allgemeine Auswahlformel des Kommutators

Für ein nichtterminales vollständiges Ereignis seien

    S=Tsel† Tsel,
    m=tr(SW)>0,
    V=T4 Tsel, V†V=S,
    W_out=V W V†/m,
    F_out=V F V†+s Pi_seed.

Die orthogonale Seedrichtung hat Witnessgewicht0. Mit A=SWS/m und B=SFS gilt daher exakt

    [W_out,F_out]=V[A,B]V†.

Die Isometrie bewahrt die Norm des bereits komprimierten Kommutators, nicht die des ursprünglichen [W,F]. Wenn der Eingang [W,F]=0 erfüllt, liefert Standardmatrixalgebra

    [SWS,SFS]
       =S(F(I-S)W-W(I-S)F)S.

Die verworfenen Kreuzblöcke bestimmen also die mögliche neu entstehende Nichtkommutation. Eine hinreichende Schutzbedingung ist [S,F]=0: dann ist die rechte Seite0. Sie ist nicht notwendig; beispielsweise W proportionalF oder besondere Kompressionen können auch bei [S,F]!=0 kommutieren. Das exakte Ereigniskriterium ist [SWS,SFS]=0.

Für P=I ist eine weitere leicht prüfbare hinreichende Anfangsbedingung [Y,F]=0, weil Q der ganze unterhalb1 liegende Y-Spektralraum und damit S=Q dann mit F kommutiert. Dies ist eine zusätzliche Einschränkung der erlaubten Hintergrund-/Präparationsklasse, keine allgemeine Eigenschaft der BFG-Quelle.

## Exakter zulässiger Drei-Moden-Zeuge

    P=I3, F=diag(1,2,3),
    W=F²/14=diag(1,4,9)/14,
    K=-I3,
    S=I3-ones3/3,
    Y=S/2+2(I3-S).

S ist ein rationaler orthogonaler Rang2-Projektor. Y hat Eigenwerte1/2 auf ranS und2 auf seinem Komplement, also ist der Originalselektor Q=S und Tsel=S. F und W sind strikt positiv und kommutieren am Eingang. Die ausgewählte Witnessmasse ist exakt m=2/3.

Die normalisierte Witnesskompression und F-Kompression haben den rationalen Kommutator

    [SWS/m,SFS]=(1/42)*
        [[0,1,-1],[-1,0,1],[1,-1,0]].

Damit beträgt seine Frobeniusnorm²6/42²=1/294. Da das weitere R4 auf dem ausgewählten Träger isometrisch ist, gilt derselbe Wert für den tatsächlichen Ausgangskommutator.

Die selektierte Y-Geometrie ist skalar1/2. Weil S und Y kommutieren, bleibt der Analyseoperator auf ranS, sein Rang ist2, ein ergänzender Seed ist nicht nötig. Beide Lasten sind positiv; alpha=(1/2)²/(1+(1/2)²)=1/5. Das vollständige Ereignis ist nichtterminal und liefert

    output_dimension=2,
    Y_out=(8/45)I2.

Die doppelte Ausgangseigenwertentartung ist Teil des exakten Zustands; das Kommutator-/Energieresultat hängt von keiner willkürlichen Basiswahl in diesem Eigenraum ab.

Die Witness-Formationsenergie wird entsprechend der allgemeinen Auswahlformel aus Runde51 konditioniert:

    E_in=tr(WF)=18/7,
    E_out=tr(S W S F)/m=16/7.

Die Änderung ist kein Defekt einer behaupteten geschlossenen Retentionsbilanz: ein Drittel der Witnessmasse wird bei der Anfangsauswahl verworfen, und das Originalupdate normiert den selektierten Witness. Die Quelle liefert hier keinen zusätzlichen physikalischen Energie-Impuls-Träger, der diese bedingte Änderung schon zu einer Gesamtbilanz vervollständigt.

Ein folgendes vollständiges Retentionsereignis erhält den entstandenen Wert1/294 und die Energie16/7, wie Runde59 vorhersagt. Anfangsselektion und spätere Retention haben somit klar unterschiedliche Rollen.

## Positive Kontrollselektion und getrennte Energiegrenze

Beim selben F,W,K,P, aber

    S0=diag(1,1,0), Y0=diag(1/2,1/2,2)

gilt [S0,F]=0. Der komplette Anfangsschritt bleibt nichtterminal, liefert ebenfalls Y_out=(8/45)I2 und bewahrt die Kommutation. Die ausgewählte Witnessmasse ist5/14; W_out hat in der passenden Energieeigenbasis Gewichte(1/5,4/5), F-Ausgangswerte(1,2). Deshalb

    E_out=9/5 !=18/7.

Die Schutzbedingung macht die eingeschränkte informative F-Messklasse stabil, sie hebt jedoch die Konditionierung nicht auf und beweist keine universelle Energieerhaltung. Die benötigte physikalische Anfangs-/Austauschbilanz bleibt eigenständig zu konstruieren.

## Frische Kontrollen und Grenzen

[COMMUTING_SECTOR_SELECTION_CHECKS.md](COMMUTING_SECTOR_SELECTION_CHECKS.md) enthält vollständige exakte Rechnung, Reproduktionscode und Rohdaten. Ein frischer lokaler Lauf PASS ohne Fehlvorlauf/Korrektur, vier Originalereignisse: oblique Anfangsselektion, deren Retentionsnachfolger, schützende Anfangsselektion und komplexe simultane Eichversion des obliquen Eingangs (Seed20261110).

Rationale Symbolrechnung bestätigt die allgemeine Kreuzblockidentität, Eingangskommutator0, m=2/3, Norm²1/294 und E_out16/7 sowie den geschützten Fall m5/14, Norm²0, E_out9/5. Numerisch stimmt die Original-Norm² mit0.0034013605442177 überein und bleibt im nächsten Ereignis erhalten. Maximaler Kommutatortransportrest4.09e-16, komplexer Eichrest der Norm²2.00e-17. Beide ursprünglichen Auswahlfälle liefern die erwartete degenerierte Y-Ausgangsgeometrie.

Die allgemeine Kreuzblockidentität und der konkrete rationale Gegenzeuge sind exakt. Die Gleitkommakontrollen bestätigen die Zuordnung zur gepinnten Implementierung; sie sind keine unabhängige physikalische Bestätigung. Es werden keine terminalen Fortsetzungen oder universellen Aussagen über beliebige alternative Zustandsbrücken behauptet.

## Nächste Abhängigkeit

Eine physikalisch ausgewählte kommutierende Messklasse müsste nicht nur die Präparation [W,F]=0 begründen, sondern auch die Verträglichkeit ihrer Anfangsselektion bzw. die genaue komprimierte Kommutationsbedingung sichern. Zusätzlich muss eine geschlossene Energie-Impuls-Bilanz die Auswahl-/Normierungsschritte erklären. Die Retentionsinvarianten allein schließen diese Lücke nicht. Uhr, Orts-/Transportabbildung und Impulsgenerator bleiben offen.

Nur Forschungsdokumentation; Manuskript, Grundgleichungen, Lizenzen, empirische Ergebnisse, Audit und Workflow unverändert. Kein neuer Remote-CI-Pass.
