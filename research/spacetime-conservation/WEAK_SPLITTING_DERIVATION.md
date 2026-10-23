# Schwache Lastaufspaltung: Kernelgrenze und endlicher Geometriesprung

## Quellenbereich
[BFG-abgeleitet] Unveränderte gepinnte Vollpersistenzquelle mit F>0, 0<Y<I. Betrachte Y_epsilon=yI+epsilon A für festes 0<y<1 und festes hermitesches A. Für hinreichend kleines epsilon bleibt der Bereich zulässig. Die numerischen Präparationen liegen zusätzlich auf C. F,W,K werden festgehalten; alpha ist weiterhin die vollständige endogene Formationslastfunktion.

## Exakte symmetrische Zwei-Unitär-Darstellung
Aus den bereits hergeleiteten Operatoren T_C=cos Theta, T_B=sin Theta, Theta=atan(sqrt(beta/alpha)Y) folgt mit U=exp(iTheta)

    Phi_Y(K) = (U K U†+U† K U)/2
             = cos(ad_Theta)(K).

Beweis: Multipliziere U=cos Theta+i sin Theta aus; die gemischten Terme heben sich in der Mittelung auf. Der Kanal ist damit ein symmetrisches Mittel zweier unitärer Konjugationen. Dies ist eine exakte algebraische Darstellung desselben BFG-Ereignisses. Sie behauptet keine physikalische Hamiltonfunktion, zufällige Zeitentwicklung oder neu hinzugefügte Quelle.

## Zweiter Koeffizient bei fast gleichen Lasten
Am Skalarpunkt ist alpha_0=y²/(1+y²) und sqrt(beta_0/alpha_0)=1/y. In einer A-Eigenbasis mit Eigenwerten a_i schreibe q(epsilon)=sqrt(beta_epsilon/alpha_epsilon)=1/y+c epsilon+O(epsilon²). Die vollständige endogene alpha-Änderung steckt in dem für alle i gemeinsamen c. Dann

    theta_i(epsilon)=atan[q(epsilon)(y+epsilon a_i)]
                   =pi/4+epsilon(a_i/(2y)+cy/2)+O(epsilon²),
    theta_i-theta_j=epsilon(a_i-a_j)/(2y)+O(epsilon²).

Der gemeinsame alpha-Beitrag verschwindet in der ersten Winkeldifferenz, ohne alpha im tatsächlichen Update einzufrieren. Deshalb

    Phi_epsilon(K)=K+epsilon² G_y,A(K)+O(epsilon³),
    G_y,A(K)= -[A,[A,K]]/(8y²).

Der Rest gilt bei festem endlichem Zustand und festem y>0; keine Uniformität für y->0 oder unbeschränkte A wird beansprucht. Die Formel gilt auch für nichtkommutierendes F. G ist dissipativ für das Hilbert-Schmidt-Produkt, erhält tr K und jede feste mit A kommutierende lineare Ladung. Es ist ein mathematischer Dephasierungsgenerator; eine Identifikation mit Energie oder räumlichem Impuls folgt nicht.

[Standardmathematik] Mit L=A/(2y) gilt G(K)=LKL-(L²K+KL²)/2. Daher erzeugt G eine vollständig positive, unital-spurtreue Semigruppe. Alternativ ist ihre Schur-Matrix exp[-t(a_i-a_j)²/(8y²)] die Gram-Matrix komplexer Phasen unter einer Gaußverteilung. Dies ist eine Aussage über den hergeleiteten Grenzgenerator und kein als Prämisse eingesetztes physikalisches Gesetz.

## Eingefrorene Vergleichsiteration
Wendet man für jedes epsilon denselben Phi_epsilon insgesamt N_epsilon=floor(t/epsilon²) Mal an, so folgt in endlicher Dimension

    (Phi_epsilon)^N_epsilon -> exp(t G_y,A).

Beweis: Für jedes Paar i,j ist h_ij(epsilon)=1-epsilon²(a_i-a_j)²/(8y²)+O(epsilon³). Logarithmieren nahe eins und Multiplikation mit N_epsilon liefert den angegebenen Exponenten; endlich viele Matrixelemente geben Normkonvergenz.

Diese integerzahlige wiederholte Anwendung vollständig positiver Kanäle widerspricht dem vorigen Halbpotenz-Gegenzeugen nicht: Hier ändert sich der Kanal mit epsilon und nur ganzzahlige positive Potenzen werden iteriert. Es wird keine beliebige fraktionale Potenz eines festen Drei-Moden-Kanals als positiv vorausgesetzt.

**Entscheidende Grenze:** Die eingefrorene Vergleichsiteration ist nicht die autonome BFG-Ereignisfolge. Letztere aktualisiert Y und damit den Folgekanal nach jedem Ereignis. Ein Rücksetzen von Y auf seinen Anfangswert wäre eine zusätzliche Steuerregel. Eine solche Rücksetzung wurde nicht als Quelle eingeführt und die hohen Vergleichs-Iterationszahlen sind keine entsprechenden Quellaufrufe.

## Vollständiger Zustand: regulärer Euler-Grenzfall bei festem y scheitert
Die tatsächliche Geometrie erfüllt schon bei epsilon=0

    Y_+=f(y)I, f(y)=2y²/[(1+y)²(1+y²)].

Für 0<y<1 ist f(y)<y. Bei y=1/4 ist f(y)=32/425 und f(y)-y=-297/1700. Somit

    lim_(epsilon->0) ||Y_+(epsilon)-Y_epsilon||_F
        =sqrt(n)*297/1700 >0.

Ein regulärer gemeinsamer Euler-Ansatz mit delta t=epsilon² und endlichem Geometrievektorfeld müsste dagegen einen gegen null gehenden Zustandssprung besitzen. Sein Geometrie-Differenzenquotient divergiert hier bereits in einem Ereignis. Eine andere feste, stetige und lokal invertierbare Zustandskarte kann die zwei verschiedenen Grenzzustände nicht identifizieren.

Damit ist nur der **feste positive Skalarhintergrund in dieser Kleinschrittskalierung** ausgeschlossen. Kein allgemeines No-Go für diskrete physikalische Zeit, singuläre/renormierte Koordinaten, Randgrenzen y_epsilon->0, getriebene Vervollständigungen oder andere gemeinsame Skalierungen. Solche Alternativen brauchen eigene quellengebundene Hypothesen und Kontrollen.

## Frische Evidenz und Grenzen
[Vorabprotokoll](WEAK_SPLITTING_PROTOCOL.md), [Prüfcode](weak_splitting_audit.py), [Resultate](weak_splitting_results.json).

Symbolische Winkeldifferenzrechnung einschließlich beliebigem gemeinsamen q-Ableitungsbeitrag bestätigt exakt (a-b)/(2y) und den Koeffizienten -(a-b)²/(8y²). Drei komplexe Präparationen in n=2,3,4, je vier epsilon-Werte und je eine zusätzliche unitäre Kontrolle: **15 vollständige Quellaufrufe**. Die symmetrische Unitärform stimmt mit der Quelle bis <1.5e-15 überein, Kovarianz bis <1.9e-15.

Beim Halbieren von epsilon nähern sich die skalierten Kernelreste und die eingefrorenen Vergleichsfehler wie vorab gefordert an. Zwischen epsilon=0.01 und 0.00125 sinken die Kernel-Generatorfehler ungefähr um Faktor acht; die letzten Fehler sind ca. 0.00313,0.00156,0.00293. Die eingefrorenen Vergleichsfehler bei t=0.1 enden bei ca. 0.000159,0.000123,0.000207. Alle vorab festgelegten Konvergenzgrenzen bestanden.

Die Geometriesprünge bleiben dagegen nahe ihren strikt positiven Grenzwerten von ca. 0.2471,0.3026,0.3494. Die eingefrorenen 1000 bis 64000 Kanalpotenzen wurden direkt spektral ausgewertet; sie sind ausdrücklich keine erfolgreich gerechneten autonomen Quelltrajektorien. Keine Quelle, Präparation oder Toleranz wurde nachträglich angepasst. CI wird getrennt vom lokalen Lauf geprüft.

## Nächste Abhängigkeit
Ein gemeinsamer BFG-Grenzbereich müsste die Geometrieentwicklung mitführen und eine ausgewählte Zeitregel begründen. Der jetzt nachgewiesene dissipative Kernelkoeffizient allein genügt dafür nicht. Als konkrete nächste Alternative ist eine quellengebundene gemeinsame Rand-/relative-Last-Skalierung prüfbar; ihre Closure und Uhr müssten vor physikalischen Viererstrom- oder Einstein-Aussagen geklärt werden. Raummaß, kalibrierte Zeit, vollständige Energie-Impuls-Erhaltung und Wirkung bleiben offen.
