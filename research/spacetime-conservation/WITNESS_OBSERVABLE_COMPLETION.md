# Runde56: minimaler gemeinsamer Anfangs-/Zukunftsraum der Witness-Ablesungen

Präregistrierung PROTOCOL.md, Commit 2343831640875bc31bdeeb40035c5ce9b8b8fe02; Auswertung 2026-10-24. Nur BFG: vollständiges Dynamic Order vom 8. Oktober2026, Parts I/II; Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370, PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Gepinntes Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498; Identitätsprüfung durch audit.load_update.

## Konstruktives Ergebnis und genaue Reichweite

Am festen rationalen F/Y/K/P-Hintergrund aus [Runde55](WITNESS_POPULATION_CERTIFICATE.md) hat der gemeinsame Observablenraum für anfängliche Y-Spektralbestände und sämtliche späteren Y-Spektralbestände exakt Dimension6. Die vier anfänglichen Momentobservablen werden durch genau zwei zusätzliche affine Witness-Ablesungen vervollständigt. Die Ergänzung ist ausreichend für beliebig viele mathematisch exakte nichtterminale Folgeereignisse dieses Hintergrunds, weil nach dem ersten Ereignis keine neuen Spektralachsen entstehen.

Minimalität meint eine lineare/affine Observablenbeschreibung, die die anfänglichen Bestände behält und alle zukünftigen Bestände vorhersagen soll. Sie meint weder die Anzahl beliebiger nichtlinearer Kodierungen noch Raumzeitdimensionen oder physikalische Energie-/Impulskomponenten. Normierung ist eine der sechs linearen Größen: bei trW=1 bleiben fünf frei variierende reelle Erwartungswerte.

Der Hintergrund und seine exakte erste Seed-/Rangbilanz bleiben wie in Runde55:

    P=F=diag(1,1,1,0), K=-I4,
    Y=(1/100)*[[20,3,1,8],[3,35,2,7],[1,2,55,6],[8,7,6,70]],
    G=I+Y, C=G^(-1), B=YC,
    PG=Z(Z†GZ)^(-1)Z†G, Z=(e1,e2,e3),
    alpha=4019981/31875481,
    H=A†A=alpha C PG†PG C+(1-alpha)B PG†PG B.

Die Quelle bestimmt H ohne Witness-Abhängigkeit. Es wird keine neue Kopplung eingeführt.

## Exakter Rang und konstruktive Ergänzung

Komprimiere alle Ablesungen auf den ursprünglichen aktiven Träger:

    A_k=P Y^k P, k=0,1,2,3,
    B_k=P H^k P, k=1,2,3.

Für ein hermitesches W=PWP sind tr(W A_k) die Eingangsmomente; tr(W B_k) die Momente des ersten Ausgangs-Y nach dem vollständigen R4-Transport. Diese Identität einschließlich F_out=I und W_out=V_svd† W V_svd wurde in Runde55 exakt bewiesen.

Die rationale Rangrechnung ergibt in der festen Reihenfolge:

    span{A_0,...,A_3}: Rang4,
    plus B_1: Rang5,
    plus B_2: Rang6,
    plus B_3: weiterhin Rang6.

Damit genügt als Basis O=(A_0,A_1,A_2,A_3,B_1,B_2). Die unabhängigen zusätzlichen Ablesungen sind tr(W P H P) und tr(W P H² P). Sie sind positiv, weil H>0; sie sind trotzdem keine unabhängig identifizierten physikalischen Ströme.

Verwendet wird die reell symmetrische aktive Matrixbasis

    D=(e11,e22,e33,e12+e21,e13+e31,e23+e32),
    M_ij=tr(O_i D_j).

Das exakt berechnete Zertifikat lautet

    det M =
    50039509481554182681062527277403475 /
    17825502216487046980221686777068840575409321698 !=0.

M ist daher invertierbar, und alle reell symmetrischen aktiven Observablen liegen im Span dieser sechs Größen. Insbesondere liefert M^T c=coords(P H³ P) eine exakte rationale Darstellung von B_3. Alle Koeffizienten werden in [WITNESS_OBSERVABLE_COMPLETION_CHECKS.md](WITNESS_OBSERVABLE_COMPLETION_CHECKS.md) vollständig ausgegeben und als Matrixidentität geprüft.

Die vier Eingangsmomente und die ersten vier Ausgangsmomente spannen folglich genau diesen Rang6-Raum auf. Der Rang6-Gegenstand ist ein gemeinsamer Retrospektiv-/Vorhersageraum am Anfang, keine Behauptung, dass im späteren vollen Träger stets sechs unabhängige momentane Populationswerte existieren.

Minimalität: Ein linearer Observablenraum, der sämtliche A_k und B_k auswerten soll, muss deren gemeinsamen Span enthalten, also mindestens Dimension6 haben. Daher kann eine einzelne zusätzliche affine Erwartungsgröße zum Rang4-Anfangsraum nicht alle ersten Ausgangspopulationen bestimmen. Die zwei angegebenen Ergänzungen erreichen die Schranke. Ohne Verpflichtung, die anfänglichen Populationen weiter mitzuführen, können die vier ersten Ausgangs-Spektralgewichte allein als zukünftige Buchführung verwendet werden; das ist eine andere, kleinere Aufgabe.

## Exakte Zukunftsgrenze: keine weiteren Witness-Richtungen in diesem Verlauf

Nach dem ersten zertifizierten Ereignis gelten F=P_out=I4, K=-I4 und Y_1 unitär äquivalent zu H. Runde55 bewies H>0. Hier wird zusätzlich I-H>0 rational über alle vier positiven führenden Hauptminoren nachgewiesen; die vollständigen Brüche stehen im Kontrollprotokoll. Damit 0<Y_1<I.

Für volle Persistenz mit F=I liefert dieselbe Quelle, nach Rückführung in den vorigen Rahmen,

    W_next=W, F_next=I, P_next=I, K_next=-I,
    Y_next=g_alpha(Y),
    g_alpha(y)=(alpha+(1-alpha)y²)/(1+y)².

Die Rückführung ist eine Darstellungsidentifikation, keine Änderung des Originalupdates. Für 0<y<1 sind LC,LB und alpha,1-alpha positiv sowie 0<g_alpha(y)<1. Daher bleibt dieser genaue Verlauf im vollen, nichtterminalen Persistenzsektor. Die Trägerdimension bleibt4, ein neuer orthogonaler Seed ist nicht nötig.

Jedes spätere Y ist nach Verkettung der Quellrahmen eine skalare Funktion von H. Deshalb sind seine Spektralprojektoren Summen von Spektralprojektoren von H: zuvor verschiedene Eigenwerte können verschmelzen, keine neue Richtung entsteht und eine bereits erfolgte Verschmelzung kann in einer späteren gemeinsamen Funktionsanwendung nicht aufgespalten werden. Diese bereits in Runde49 verwendete Struktur wird hier auf den Witness-Observablenraum angewandt.

Jeder H-Spektralprojektor ist als Interpolationspolynom vom Grad höchstens3 in H darstellbar. Somit sind sämtliche zukünftigen Witness-Spektralablesungen bereits durch P H^k P,k0..3, bestimmt. Zusammen mit den Eingangsmomenten ist der Rang6-Raum also für die gesamte mathematisch exakte Zukunft dieses festgehaltenen Hintergrunds hinreichend. Der Beweis setzt keinen konstant eingefrorenen alpha-Wert voraus: alpha wird bei jedem Quellereignis neu aus der aktuellen Geometrie berechnet.

Das ist eine Beobachtungsschließung für diese Covers samt bekannter Hintergrunddynamik. Sie ist kein autonomes universelles Sechs-Komponenten-BFG-Gesetz, wenn F/Y/K/P beliebig variieren, und kein physikalisch ausgewählter Raum-/Zeit-/Impulsansatz.

## Komplexe Witness-Zustände und unsichtbare Richtungen

Im gewählten rationalen reellen Hintergrund sind alle auf den Eingang zurückgezogenen Observablen reell symmetrisch. Für W=R+iT mit R reell symmetrisch und T reell antisymmetrisch gilt tr(W O)=tr(R O). Die drei imaginär-antisymmetrischen aktiven Richtungen werden von diesen Covers weder am Anfang noch in der beschriebenen Zukunft gelesen. Sie sind damit nicht verschwunden oder dynamisch verboten. Andere Observablen oder andere Hintergrundgeometrien könnten sie erkennen.

Die sechs Messwerte bestimmen R aus M und damit alle hier geprüften Ablesungen, nicht das vollständige komplexe W mit neun reellen hermiteschen Komponenten. Eine simultane komplexe Eichtransformation transportiert den sichtbaren Observablenraum mit; sie macht die ursprünglichen reellen Koordinaten nicht zu einer physikalisch bevorzugten Basis.

## Frische Evidenz und Grenzen

[WITNESS_OBSERVABLE_COMPLETION_CHECKS.md](WITNESS_OBSERVABLE_COMPLETION_CHECKS.md) enthält exakte Ränge, Determinante, Darstellungskoeffizienten sowie vollständige frische Mehrschritt-Reproduktion und Rohdaten.

Ein lokaler vollständiger Lauf mit6 Originalereignissen PASS ohne Fehler: neue allgemeine komplexe positive Witness-Präparation, Zufallsseed20261106, und ihre komplexe simultane Eichversion; je3 Ereignisse einschließlich erstem Seed. Danach wurde der zusätzliche exakte I-H-Positivitätsguard eingefügt und der gesamte vorgelagerte rationale/Rekonstruktionsabschnitt frisch separat bestanden (0 weitere Originalaufrufe). Diese Ergänzung schließt die Voraussetzung des allgemeinen Zukunftsarguments explizit, ohne den bereits bestandenen numerischen Verlauf als Beweis unendlicher Gleitkommafortsetzung auszugeben.

Die Rekonstruktion des sichtbaren R-Anteils hat Rest6.15e-14; der nicht rekonstruierte imaginäre Anteil hat Norm0.3459 und wurde absichtlich nicht zu null erklärt. Kleinster aktiver Witness-Eigenwert0.1407. Alle Y-Momente k0..3 der beiden3-Ereignisfolgen stimmen mit den aus H-Spektralgewichten und den jeweils frisch berechneten Quell-alphas vorhergesagten Werten bis2.23e-16 überein; Eichmomentrest2.23e-16. Numerische Konditionierung bleibt eine praktische Grenze; der exakte Rang folgt aus der rationalen Determinante. Bei sehr langen Gleitkommafolgen gelten die Quellschwellen und mögliche numerische Terminalentscheidungen; der Zukunftssatz betrifft die exakte Mathematik.

## Nächste physikalische Abhängigkeit

Die BFG-Quelle trägt die fehlende Kohärenzinformation bereits in W; im konkreten Beispiel lässt sich ein minimaler affiner Ergänzungsraum bestimmen. Noch offen ist, welche dieser Ablesungen physikalische Orts-/Transportobservablen darstellen und ob eine unabhängig begründete Uhr und Generatorstruktur sie mit Energie und Impuls verbindet. Die zwei zusätzlichen Werte werden hier nicht als Impulskomponenten umbenannt.

Nur Forschungsdokumentation; keine Quell-/Audit-/Workflowänderung, kein neuer Remote-CI-Pass.
