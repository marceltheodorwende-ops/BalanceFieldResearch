# Runde55: exaktes rationales Zertifikat der Populations-Nichtgeschlossenheit

Präregistrierung PROTOCOL.md, Commit aa47a8e9bb157cf62021e6f71dcd9b67001f7a59; Auswertung 2026-10-24. Ausschließlich gepinnte BFG-Quelle: vollständiges Dynamic Order, 8. Oktober 2026, Parts I/II, Quellencommit 457f23df6d9ccb15cf17916f3c3eac113b23c370; PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498, durch audit.load_update geprüft. Standardmatrixalgebra und exakte rationale Rechnung werden von den zusätzlichen physikalischen Interpretationen getrennt.

## Ergebnis

Der Populationsverlust aus [Runde54](WITNESS_POPULATION_CLOSURE.md) besitzt jetzt einen eigenständigen exakten rationalen Gegenzeugen am selben F/Y/K/P-Grundzustand. Er benötigt keine numerisch bestimmten Eigenvektoren und kein Intervallargument. Zwei strikt positive aktive Witness-Zustände haben exakt dieselben Eingangs-Y-Spektralpopulationen und Gesamtenergie1, aber nach dem vollständigen BFG-Update ein exakt unterschiedliches erstes Y-Ausgangsmoment. Deshalb können ihre Ausgangs-Y-Spektralpopulationen nicht alle gleich sein.

Das ist ein exakter Gegenbeweis gegen ein autonomes Populationsupdate für diesen Kandidaten und alle zulässigen Witness-Präparationen. Er identifiziert noch keine physikalischen Ortsregionen oder Energie-Impuls-Ströme. Der konkrete Zahlenzeuge von Runde54 bleibt ein numerischer Zeuge; hier wird ein anderer rationaler Witness-Paar konstruiert und zertifiziert.

## Rationaler Grundzustand und vollständiges Quellenereignis

    P=F=diag(1,1,1,0), K=-I4,
    Y=(1/100)*[[20,3,1,8],[3,35,2,7],[1,2,55,6],[8,7,6,70]].

Setze G=I+Y, C=G^(-1), B=YC, Z=(e1,e2,e3) und den originalen metrischen Projektor

    PG=Z(Z†GZ)^(-1)Z†G,
    LC=tr(G PG C P C PG†),
    LB=tr(G PG B P B PG†),
    alpha=LB/(LC+LB)=4019981/31875481,
    H=alpha C PG†PG C+(1-alpha)B PG†PG B=A†A.

Alle Matrizen bis hier sind rational. LC und LB sind exakt positiv. Die führenden Hauptminoren von Y sind

    1/5, 691/10000, 18951/500000, 2475617/100000000,

und von I-Y

    4/5, 5191/10000, 116599/500000, 6409917/100000000.

Damit 0<Y<I und Q=I. Alle vier führenden Hauptminoren von H sind ebenfalls exakt positiv; vollständige rationale Werte im Zertifikat. Folglich rankA=4 und die dünne Quellen-SVD besitzt unitäres rechtes V_svd. Für beide unterstützten normierten W gilt

    Tsel=P, T4=V_svd†P, S4=V_svd† P V_svd,
    W_out=V_svd† W V_svd,
    Y_out=V_svd† H V_svd.

K_out=-I, weil U†U=I. Das Komplement von S4 ist eindimensional, sein komprimierter Kernelwert ist exakt-1. Der Seed ist deshalb eindeutig, zulässig und nichtterminal, Stärke1. Es folgt F_out=P_out=I. Die gemeinsame Retention und Witnessmassen1 sind exakt erfüllt; es gibt keine versteckte selektive Renormierung zwischen den beiden Präparationen. Die globale Kandidatenenergie ist tr(WF)=trW=1 und bleibt1.

## Explizite rationale Kohärenzfaser

Definiere

    L=(1/38391229)*
      [[-5383726,-21363972,11643531,0],
       [-21363972,4176682,0,0],
       [11643531,0,1207044,0],
       [0,0,0,0]],
    W±=P/3±L/6.

Exakte Zertifikatsidentitäten:

    L=L†=PLP,
    tr(L P Y^k P)=0, k=0,1,2,3,
    max_i sum_j |L_ij|=1.

Da L hermitesch ist, gilt ||L||_op<=1 über die absolute Zeilensummen-Norm. Deshalb W±>=P/6 auf ranP, trW±=1 und W± sind gültige unterstützte Witness-Zustände. Ihre Gleichheit aller vier Momente ist keine Toleranzaussage:

    tr[(W+-W-)Y^k]=0, k=0,1,2,3.

Y ist hermitesch; seine Spektralprojektoren sind Interpolationspolynome in Y vom Grad höchstens3. Daher ist die Erwartung jedes Eingangs-Y-Spektralprojektors exakt gleich. Zusätzlich bestätigt der rationale Code die Quadratfreiheit der charakteristischen Y-Polynomfunktion; die vier Inputlabels sind also einfach. Die Gleichheit der Populationen selbst würde auch für zusammengefasste entartete Spektralprojektoren aus der Polynomialdarstellung folgen.

Für das erste Ausgangsmoment liefert hingegen der vollständige Quellentransport

    tr(W_out Y_out)=tr(W H),
    Delta=tr[(W+-W-)H]=tr(LH)/3
         =432029868515685052375000 /
          1925886930087373395035647149
         >0.

Numerisch ist Delta ungefähr0.00022432774311214874, aber sein positives Vorzeichen wird durch die rationalen ganzen Zahlen bewiesen. Gleiche Ausgangsspektralpopulationen würden dasselbe Ausgangsmoment erzwingen, Widerspruch. Dies beweist exakt die Faser-Nichtgeschlossenheit ohne Bestimmung eines einzigen Ausgangseigenvektors.

Auch bei F_out=I ist R_F,out=W_out. Das Spektralpopulationsargument betrifft daher dieselben lokalen Kandidaten-Energiebestände wie in Runde54. Das Moment ist ein Trennobservable für die Populationen, nicht ein neu eingeführtes physikalisches Energiegesetz.

## Was mindestens zusätzlich behalten werden muss

Die vier komprimierten Eingangs-Momentobservablen P Y^k P haben exakt Rang4 im reell symmetrischen aktiven3x3-Raum. PH P liegt nicht in ihrem Span, denn L annihiliert alle vier, aber tr(LH)!=0. Für die Vorhersage mindestens dieses Ausgangsmoments ist somit mindestens eine weitere linear unabhängige Witness-Ablesung nötig. Ein entsprechender Ein-Schritt-Raum hat Dimension mindestens5; das ist keine Behauptung, dass fünf Größen bereits über beliebig viele Ereignisse schließen oder physikalische Raumzeitdimensionen darstellen. Vollständiges W trägt die benötigte Information bereits, ohne dass die BFG-Grundgleichung ergänzt werden müsste.

Mitbewegte Covers bleiben die exakte geschlossene Alternative aus Runde52. Ihre Buchführung bestimmt aber weiterhin keinen räumlichen Fluss. Auch kann eine physikalische Präparationsbeschränkung die hier universal über alle W formulierte Kandidatenklasse einschränken; das wäre separat zu belegen.

## Frische Prüfung, Evidenz und nächste Abhängigkeit

[WITNESS_POPULATION_CERTIFICATE_CHECKS.md](WITNESS_POPULATION_CERTIFICATE_CHECKS.md) enthält das vollständige ausführbare rationale Zertifikat, alle Positivitätsminoren, Nullmomente, L und Delta sowie numerische Originalkontrollen. Ein lokaler Lauf PASS ohne Fehler oder Korrektur, vier neue Originalaufrufe: rationales W± und komplexe simultane Eichversionen, Seed20261105. Keine Wiederholung des alten numerischen L-Zeugen.

Numerische Zusatzkontrollen: Eingangs-Populationsgap1.67e-16, Ausgangs-Populationsgap0.05500560922; Ausgangsmomentgap0.00022432774311215153 gegenüber exakter Vorhersage. F_out-I-Rest1.25e-15 im angezeigten rationalen Paar; Populations-/Momenteichrest9.44e-16. Diese Gleitkommazahlen sind Plausibilitätskontrollen; der Nichtgeschlossenheitsbeweis beruht auf rationalen Identitäten und exakter Positivität.

Nächste konstruktive Abhängigkeit ist der unter tatsächlichen Coverwechseln benötigte Witness-Observablenraum: Ein zusätzlicher kohärenzsensitiver Observable genügt als Trenninformation dieses Moments, ein dauerhaft geschlossener Raum ist noch zu prüfen. Eine physikalische Orts-/Präparationsbrücke, Uhr und Impuls-/Translationsgeneratoridentifikation bleiben erforderlich. Populations-Nichtgeschlossenheit widerlegt keine Kontinuitätsgleichung mit zusätzlichen Strom- oder Wechselwirkungsgrößen.

Nur Forschungsdokumentation; Manuskript, Grundgleichungen, empirische Ergebnisse, Audit und Workflow unverändert. Lokale Zertifikatsprüfung ist kein neuer Remote-CI-Pass.
