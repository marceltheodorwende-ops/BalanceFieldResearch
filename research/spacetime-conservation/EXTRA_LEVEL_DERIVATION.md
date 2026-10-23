# Zusätzliche Lastniveaus: transversale Empfindlichkeit

## Bereich und konkrete zusätzliche Richtungen
[BFG-abgeleitete Tangentenrechnung] Untersuche den ausgeglichenen Zwei-Niveau-Unterbereich der zuvor kontrollierten Dynamik: A=A†, A²=I, <A>_F=0, Y=sZ, Z=I+rA. Hier s=<Y>_F ist zugleich der spektrale Mittelpunkt. Die neue Aussage wird nicht ohne Rechnung auf sämtliche kritischen Ungleichgewichte erweitert.

Zusätzliche innere Lastaufspaltungen sind Hermitesche Richtungen B innerhalb eines A-Eigenblocks, mit tr B=tr(FB)=0. Ein expliziter zulässiger n=4-Zeuge lautet

    A=diag(1,1,-1,-1),
    B_+=diag(1,-1,0,0),
    B_-=diag(0,0,1,-1),
    F=I+kleine hermitesche Kreuzblockkopplung.

F ist positiv und muss nicht mit A kommutieren. Beide B-Richtungen sind auch formationszentriert. Eine Störung Z+eta B erzeugt zusätzliche Lastniveaus, die bei einer Reduktion auf zwei gemeinsame Lastwerte verlorengingen. Bei eindimensionalem jeweiligem Eigenblock gibt es diese innere spurfreie Richtung nicht; insbesondere wird kein universelles Hindernis für einen bereits ausgewählten nichtdegenerierten Zwei-Moden-Träger behauptet.

## Exakte Randableitung und relative Verstärkung
Weil <B>_F=<ZB>_F=0, hat mu2=<Z²>_F bei eta=0 keine erste Variation. Aus R_F(Z)=(mu2 I+Z²)/(2mu2) folgt deshalb

    D R_Z[B_±]=(1±r)B_±/(1+r²).

Die Basisaufspaltung entwickelt sich gleichzeitig als r_+=r/(1+r²). Bezeichne die infinitesimale innere Amplitude mit eta. Relativ zur Basisamplitude ist der exakte linearisierte Faktor daher

    (eta_+/r_+)/(eta/r)=1±r.

Im höheren Lastblock wächst die relative Tangentenstörung; im niedrigeren wird sie gedämpft. Die Richtungen bleiben entlang der ungestörten Basisfolge parallel zu demselben B, sodass ihre Faktoren tatsächlich multipliziert werden können. Es handelt sich um Ableitungen der vollständigen Formabbildung an der Basisfolge, nicht um eine willkürlich angesetzte Störgleichung.

## Exakte positive-Last-Faktoren
Für die unveränderte positive-s-Quelle gilt an derselben Basis Y=s(I+rA), y_±=s(1±r), alpha aus der vollständigen Formation:

    H_±(s,r)= (y_+-y_-) g'_alpha(y_±)
              /[g_alpha(y_+)-g_alpha(y_-)].

Die formationsgewichteten Lasten und die Folgeskalierung besitzen in diesen B-Richtungen keine erste Variation. Daher ist diese Formel die exakte relative Tangentenantwort des ausgerichteten Quellenupdates, einschließlich der endogenen alpha-Abhängigkeit.

Auf C ist g' positiv und
g''=2[(1-alpha)(1-2y)+3alpha]/(1+y)^4>0.
Die Sekantensteigung liegt somit strikt zwischen beiden Randableitungen. Exakt folgt für jedes solche positive Ereignis

    H_+>1, 0<H_-<1.

Dies ist bereits eine Aussage über die positive-Last-Regel und nicht nur den Grenzkanal. Sie betrifft relative innere Breiten; absolute Lasten können gleichzeitig stark schrumpfen.

Nach rationalem Kürzen sind H_± auf 0<=s<=1/100, 0<=r<=1/4 analytisch fortsetzbar, mit H_±(0,r)=1±r. Der Audit zertifiziert durch exakte gewichtete Koeffizientenmassen für beide Vorzeichen

    |partial_s log H_±|<=1,
    |log H_±(s,r)-log(1±r)|<=s.

Die Zählermasse des rationalen logarithmischen Ableitungsausdrucks ist 3411425438039/5120000000000, die Nenneruntergrenze 289799743064696487/409600000000000000. Ihr Quotient 272914035043120000/289799743064696487 ist kleiner als eins. Der ganze Rechteckbereich ist damit kontrolliert; keine Stichprobe wird als globale Schranke ausgegeben.

## Langsame Skala: exponentielle Tangentenempfindlichkeit
Auf der Randbasis r0=epsilon, N epsilon²->T>0 sind die kumulativen relativen Tangentenfaktoren

    G_±,N=Produkt_(j<N)(1±r_j).

Mit log(1±r)=±r+O(r²), r_j=epsilon u(t_j)+O_T(epsilon³) und u(t)=(1+2t)^(-1/2) folgt

    epsilon log G_±,N
       -> ±Integral_0^T u(t)dt
        = ±[sqrt(1+2T)-1].

Der Rest in dieser skalierten Logarithmusform ist O_T(epsilon). Der obere Faktor wächst somit wie exp([sqrt(1+2T)-1+o(1)]/epsilon), der untere fällt entsprechend.

Auch diese Aussage lässt sich auf die exakte positive-Last-Basis übertragen. Aus der schon bewiesenen ausgeglichenen Quellenabschätzung gelten sum s_j<=(32/31)s0 und |r_j-rbar_j|<=4epsilon s0. Daher

    |epsilon sum log H_±(s_j,r_j)
      -epsilon sum log(1±rbar_j)|
      <=[(32/31)epsilon+(16/3)T]s0.

Hier wurde |d log(1±r)/dr|<=4/3 auf r<=1/4 verwendet. Bei gemeinsamem s0(epsilon)->0 besitzt also auch die exakte mathematische positive-Last-Dynamik denselben skalierten logarithmischen Tangentenbefund. Es wurden keine langen Gleitkomma-Originaltrajektorien unter ihrer Ranggrenze verlangt.

## Präzise Bedeutung der Grenze
Der zuvor bewiesene Zwei-Niveau-Grenzwert bleibt im exakt deklarierten Sektor gültig. Seine Einbettung in einen höheren Rang besitzt jedoch keine epsilon-uniform begrenzte lineare Empfindlichkeit gegenüber den genannten inneren Aufspaltungen des höheren Lastblocks.

Dies ist eine **variationale Aussage am ungestörten Sektor**. Aus ihr folgt hier keine bereits bewiesene nichtlineare Flucht für beliebige endliche Störungen, keine allgemeine physikalische Instabilität und keine universelle Widerlegung von BFG. Wie lange eine konkrete endliche Störung der Tangentenrechnung folgt und welche epsilon-abhängige Umgebung benötigt wird, bleibt separat zu kontrollieren. Die gleichzeitige untere Kontraktion und das Fehlen dieser Richtung bei Blockdimension eins werden ausdrücklich erhalten.

## Frische Evidenz
[Vorabprotokoll](EXTRA_LEVEL_PROTOCOL.md), [Prüfcode](extra_level_audit.py), [Resultate](extra_level_results.json).

Symbolisch geprüft: beide vollständigen Randrichtungsableitungen, exakte positive-s-Tangentenquotienten und s=0-Grenzen; rationale Rechteckzertifikate für beide logarithmischen Ableitungen. Die beiden skalierten Rand-Logarithmen wurden für vier epsilon-Werte bis T=1/2 mit bis zu 3200 Randschritten berechnet. Sie nähern sich ±(sqrt(2)-1)≈±0.414214. Beim kleinsten epsilon sind die Fehler ca. 0.002132 und 0.002201; beide vorab festgelegten Konvergenzkriterien bestanden.

Zusätzlich **38 vollständige Original-Quellaufrufe**: vier komplex gedrehte n=4-Präparationen bei zwei r- und zwei s-Werten, je Basisereignis und zentrale ±eta-Variationen in beiden Blockrichtungen für eta=1e-4,1e-5, dazu zwei unitäre Basischecks. Größter Basis-Identitätsrest <1.3e-14, Last-Kovarianzrest <1e-18. Der schlechteste beste zentrale Richtungsfehler ist ca. 2.28e-8 bei vorgegebener 1e-6-Grenze. Alle Schrittweitenfehler bleiben im JSON; kleinere eta geben teilweise größere Rundungsfehler bis ca. 1.43e-7 und werden nicht verschwiegen.

Die endlichen Quellkontrollen bestätigen die lokal abgeleitete Tangentenform; die lange logarithmische Aussage folgt aus dem Beweis und der uniformen Quellenabschätzung. Keine Quellen-/Rangtoleranz-/Kriterienänderung. Manuskripte, Grundgleichungen, Lizenzen und empirische Daten unverändert. CI separat ausgewiesen.

## Nächste Abhängigkeit
Die lineare Empfindlichkeit gegenüber zusätzlichen inneren Lastniveaus ist nun präzise erfasst. Vor einer robusten physikalischen Sektorauswahl bleiben die nichtlineare Störungsreichweite und eine BFG-interne Isolierung/Selektion des gewünschten Ereignisträgers zu prüfen. Das Verstärkungsresultat darf weder durch Entfernen zusätzlicher Niveaus noch durch eine erfundene Stabilisierung verdeckt werden. Physikalische Uhr, räumliche Observable, vollständiger Energie-Impuls-Strom, ausgewählte Wirkung und Einstein bleiben offen.
