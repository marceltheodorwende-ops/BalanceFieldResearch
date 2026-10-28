# Kontinuierliche Interpolation des eingefrorenen Kernelkanals

## Frage und Geltungsbereich
[BFG-abgeleitete Kanalform, anschließend Standardmathematik] Für ein einzelnes Vollpersistenz-Ereignis ist K_+=Phi(K) in der Y-Eigenbasis der Schur-Kanal H o K. H_ab=cos(theta_a-theta_b), theta_a=atan(sqrt(beta/alpha)y_a). Die source-endogenen Werte F,Y,alpha bestimmen hier einen **eingefrorenen linearen Kernelkanal**. Eine Interpolation dieses Kanals ist keine kontinuierliche Gleichung für das gesamte BFG-Tupel.

Nach den endlichen Graphreichweitenschranken ist für eine physikalische Geschwindigkeit weiterhin eine begründete Zeit notwendig. Hier wird die engere vorgeschaltete Frage geprüft: Legt ein vorhandener Kanal bereits eine positive homogene Zwischenzeitabbildung fest?

## Eintragsweise Potenz: exakter Gegenzeuge auf C
[Kandidat, im angegebenen Bereich widerlegt] Setze Phi_t(K)=H^[t] o K mit eintragsweisen positiven reellen Potenzen (H^[t])_ab=H_ab^t. Diese Formel erfüllt die homogene Semigruppengleichung und die Endpunkte. Für t=0 ist H^[0] die Einsmatrix und damit der Identitätskanal. Positivität ist jedoch gesondert notwendig.

Der vorab festgelegte positive Vollpersistenzzeuge lautet

    Y=diag(3/20,1/5,4/15),
    F=diag(1,1,57/92), W=I/3, K=ones(3,3)/3.

m=3/20, M=4/15 erfüllen 0<m<=M<=1/2 und m>=2M²; der Zeuge liegt in C. Die Formationslastformel liefert exakt alpha=1/26, beta=25/26. Daher sqrt(beta/alpha)y=(3/4,1,4/3) und

    H = [[1,a,b],[a,1,a],[b,a,1]],
    a=7/(5 sqrt(2)), b=24/25.

Die eintragsweise Halbpotenz hat

    det H^[1/2]=(1-sqrt(b))(1+sqrt(b)-2a)
              =(1-2sqrt(6)/5)(5+2sqrt(6)-7sqrt(2))/5 < 0.

Beweis des strikten Vorzeichens ohne Gleitkomma: Der erste Faktor ist positiv. 49²=2401>2400=20²*6 impliziert 49>20sqrt(6), damit 98>49+20sqrt(6)=(5+2sqrt(6))² und 7sqrt(2)>5+2sqrt(6). Der zweite Faktor ist negativ.

Ein Schur-Multiplikator ist bei positiv semidefinitem Multiplikator vollständig positiv (Gram-/Kraus-Darstellung). Umgekehrt muss schon Positivität H^[t]>=0 erzwingen: Das positive Eingangskernel ones/3 wird auf H^[t]/3 abgebildet. Der Halbpotenzansatz verletzt also sogar Positivität. Numerisch det≈-2.08285e-6, kleinster Eigenwert≈-3.45960e-5; die negative Eigenrichtung ist kein Rundungsartefakt.

Dies widerlegt den benannten homogenen Ansatz mit positiven reellen Schur-Faktoren. Es ist **kein** allgemeines No-Go für andere kontinuierliche Einbettungen, zusätzliche Freiheitsgrade, andere Generatoren oder eine physikalische BFG-Zeit.

## Zwei positive Alternativen mit denselben Endpunkten
[Standardmathematische Konstruktionen, keine ausgewählte BFG-Zeit] Für 0<=s<=1:

1. Konvexer Pfad C_s=(1-s)Id+s Phi. Sein Schur-Multiplikator ist (1-s)ones+sH, eine positive semidefinite Matrix mit Diagonale eins.
2. Winkelpfad A_s mit Multiplikator cos[s(theta_a-theta_b)]. Dieser ist die Gram-Matrix der normierten reellen Vektoren (cos(s theta_a),sin(s theta_a)). Krausoperatoren sind cos(s Theta), sin(s Theta) für Theta=atan(sqrt(beta/alpha)Y).

Beide Pfade sind vollständig positiv, unital, spurtreu, stetig und kovariant unter simultaner unitärer Basistransformation. Beide beginnen bei Id und enden exakt bei Phi. Beide benötigen keine nachträgliche Änderung des BFG-Endpunkts. Sie sind aber unterschiedliche zusätzliche Zwischenzeitregeln.

Am Zeugen beträgt der Frobeniusabstand ihrer Halbzeitmultiplikatoren etwa 0.0149390. Beide verletzen dort die Halbzeit-Semigruppengleichung: ||C_1/2 o C_1/2-Phi|| auf Ebene der Schur-Multiplikatoren≈0.000567936, analog beim Winkelpfad≈0.0300169. Die verwendete Norm ist die Frobeniusnorm der Multiplikatormatrizen, keine behauptete physikalische Distanz oder Norm des Superoperators.

Damit sind positive Interpolationen vorhanden, während der ungeprüfte logarithmische Ansatz scheitert und diese zwei Alternativen keine homogene Semigruppe liefern. Eine reelle Intervallkoordinate s ist außerdem noch keine kalibrierte Dauer. Beliebige stetige monotone Umparametrisierungen mit festen Endpunkten vergrößern die Zwischenzeitmehrdeutigkeit.

## Frische Kontrollen
[Vorabprotokoll](INTERPOLATION_PROTOCOL.md), [Prüfcode](interpolation_audit.py), [Resultate](interpolation_results.json).

Exakte Formations-alpha- und Determinantenrechnung, ein vollständiger Quellenzeuge, zwölf komplexe Präparationen (vier je n=3,4,5) auf C und drei unitäre Quellkontrollen: 16 vollständige Aufrufe. Die alternativen Gram-Matrizen wurden für s=1/4,1/2,3/4 geprüft. Größter Quellrest <3.5e-15, Kovarianzrest <1.2e-15. Kleine negative alternative Gram-Eigenwerte bis ca. -8.9e-16 liegen innerhalb der vorab festgelegten absoluten Toleranz 1e-10; exakte Positivität folgt aus den angegebenen Gram-Beweisen.

Der negative Halbpotenzwert ist ein erfolgreich geprüfter Gegenzeuge und kein fehlgeschlagener Audit. Keine Präparation, Quelle oder Schwelle wurde angepasst. Keine allgemeine Behauptung über die Halbpotenz aller Präparationen. GitHub-CI wird getrennt dokumentiert; Manuskript, Grundgleichungen, Lizenzen und empirische Ergebnisse bleiben unverändert.

## Nächste notwendige Abhängigkeit
Eine kontinuierliche physikalische Zeit darf weder durch ein ungeprüftes Kanal-Logarithmieren noch durch freie Wahl einer positiven Interpolation als bereits hergeleitet gelten. Nötig ist eine BFG-interne Auswahl und gegebenenfalls ein kontrollierter gemeinsamer Grenzübergang für Kernel **und** Geometrie samt Dauerregel. Alternativ kann die Theorie diskrete Ereignisse behalten; dann muss die physikalische Zeit-/Strominterpretation auf dieser Ebene begründet werden. Langfristige Reichweitenschranken, räumliches Maß, vollständiger Energie-Impuls-Strom, Wirkung und Einstein bleiben offen.
