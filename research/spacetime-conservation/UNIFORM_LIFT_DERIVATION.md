# Uniforme Übertragung auf die positive-Last-Dynamik

## Aussage und Bereich
[BFG-abgeleitet mit Standardmathematik] Betrachte die exakte mathematische Vollpersistenz-Dynamik im ausgeglichenen Zwei-Niveau-Sektor

    A=A†, A²=I, <A>_F=0, F>0,
    Y=s(I+rA), 0<s<=1/100, 0<r<=1/4.

A und F werden in der ausgerichteten Quotientenrepräsentation mitgeführt. F muss nicht mit A kommutieren: Nur die gleichen Formationsgewichte beider A-Eigenblöcke werden benötigt. Diese Annahmen wählen einen konkreten mathematischen Sektor, keine physikalischen Orte, zwei komplexen Moden oder vier Raumzeitdimensionen.

Die vorher offene [Rand-zu-Quelle-Brücke](RELATIVE_SLOW_DERIVATION.md) kann auf diesem Sektor mit einer uniformen Abschätzung geschlossen werden. Der Satz betrifft die exakte mathematische Ereignisregel, nicht eine Behauptung unbegrenzt erfolgreicher Gleitkomma-Aufrufe des Originalcodes mit seiner numerischen Rangtoleranz.

## Exakte positive-Last-Rekurrenzen
Setze

    q(s,r)=1+r²(1-s)/(1+s),
    G_±=[q+(1±r)²]/[(1+s(1±r))²(1+s²q)].

Aus der vollständigen Formationslastformel und dem Y-Update folgen exakt

    s_+=s²(G_++G_-)/2,
    r_+=(G_+-G_-)/(G_++G_-),
    h(s,r)=[q+1-r²]/sqrt[(q+(1-r)²)(q+(1+r)²)].

Der Kernel entwickelt sich blockweise als D_A(K_+)=D_A(K) und O_A(K_+)=h(s,r)O_A(K). Die Folgewerte s,r sind die tatsächlich aktualisierten Werte; es gibt kein Geometrie-Reset und keine eingefrorene alpha-Folge.

Für die Abschätzungen ist die äquivalente rationale Form nützlich:

    D=(1+s)³+r²(1-2s²-s³)+r^4 s²,
    r_+=r(1+s)[1-s²+r²(s²-2s)]/D,
    b(r)=r/(1+r²),
    b(r)-r_+=rs P/[(1+r²)D],
    P=2(1+s)²+r²(1-s²)+r^4(2+2s-s²).

Auf dem deklarierten Bereich sind D>=1, 0<P<3 und der Zähler von r_+ strikt positiv. Für die P-Obergrenze genügt die exakte rationale Zahl
2(101/100)²+1/16+(1/256)(2+2/100)=675389/320000<3.
Damit

    0<r_+<=b(r)<=r,
    |r_+-b(r)|<=3sr.

Die Gesamtlast erfüllt unabhängig davon s_+<=M_+<=2M² mit M=s(1+r). Dies folgt direkt aus alpha<=M²/(1+M²) und Y_+<=alpha I+(1-alpha)M² I. Daher

    0<s_+<=(25/8)s²<=s/32,
    sum_(j>=0) s_j <=(32/31)s0.

s und r bleiben also im angegebenen positiven Bereich. Alle endlichen exakten mathematischen Ereignisse haben positive Lasten; eine numerische Fortsetzbarkeit unter fester Rangschwelle wird nicht daraus abgeleitet.

## Uniformer relativer Formfehler
Seien r0=rbar0=epsilon<=1/4, r_j die tatsächliche positive-s-Folge und rbar_(j+1)=b(rbar_j) die Randfolge. Auf [0,1/4] ist b steigend mit 0<=b'<=1. Daher induktiv r_j<=rbar_j<=epsilon und

    delta_(j+1)<=delta_j+3epsilon s_j,
    delta_j=rbar_j-r_j.

Summieren gibt für **alle** j, ohne Faktor j,

    |r_j-rbar_j|/epsilon
        <=3 sum_l s_l <=(96/31)s0 <4s0.

Die schnell schrumpfende Gesamtlast verhindert hier die unkontrollierte Aufsummierung eines bloßen pauschalen Einereignisfehlers.

## Kumulativer Kernel-Fehler
Seien d_N=Produkt_(j<N) h(s_j,r_j) und dbar_N=Produkt_(j<N) h(0,rbar_j), beide in (0,1]. Schreibe h über q wie oben. Weil q>=1 und r<=1/4, sind die drei Nenner in

    partial_q log h
      =1/(q+1-r²)-1/[2(q+(1-r)²)]-1/[2(q+(1+r)²)]

größer als eins. Somit |partial_q log h|<=2. Mit |partial_s q|<=2r² folgt

    |log h(s,r)-log h(0,r)|<=4sr².

Weiter ist h(0,r)=(1+r²+r^4)^(-1/2) und
|partial_r log h(0,r)|=(r+2r³)/(1+r²+r^4)<=2r.
Mit der uniformen Formschranke erhält man für N epsilon²<=T

    |log d_N-log dbar_N|
      <=4epsilon² sum_j s_j
        +sum_(j<N) 2epsilon |r_j-rbar_j|
      <=(8T+5epsilon²)s0.

Da die Exponentialfunktion auf nichtpositiven Argumenten Lipschitz mit Konstante eins ist, gilt dieselbe rechte Seite für |d_N-dbar_N|. Für beliebiges hermitesches Anfangskernel folgt der Frobeniusfehler höchstens diese Schranke mal ||O_A(K0)||_F. Positivität ist für diese lineare Fehlerabschätzung nicht erforderlich.

## Gemeinsamer Grenzwert der mathematischen positiven Quelle
Die vorige feste-T-Randkonvergenz hat Fehler O_T(epsilon²). Kombiniert mit den neuen Schranken ergibt sich für jede gemeinsame Wahl s0(epsilon)->0:

    r_floor(t/epsilon²)/epsilon -> (1+2t)^(-1/2),
    d_floor(t/epsilon²) -> (1+2t)^(-1/4),

uniform auf festen t-Intervallen in den skalierten Form- und Kernelkoordinaten. Eine explizite Gesamtfehlerordnung ist O_T(s0+epsilon²). Die Wahl s0=epsilon² erfüllt dies mit O_T(epsilon²).

Dies ist nun eine kontrollierte gemeinsame relative Form-/Kernelgrenze der **exakten positiven-Last-Vollpersistenzregel** in dem ausgewiesenen Sektor. Die rohe Gesamtlast verschwindet in dieser Grenzfamilie. Ein frei als Sekunden interpretierter t-Parameter, eine quellenbegründete Sektorauswahl und räumliche Translationsstruktur sind damit weiterhin nicht gegeben. Der Grenzkanal dämpft transversale Kernelkomponenten; er ist kein erhaltener physikalischer Viererstrom.

## Frische Evidenz
[Vorabprotokoll](UNIFORM_LIFT_PROTOCOL.md), [Prüfcode](uniform_lift_audit.py), [Resultate](uniform_lift_results.json).

Symbolisch geprüft: vollständige Formations-q-Identität, rationale r-Rekurrenz und positive Differenzfaktorisierung. Die Konstantenschranken oben verwenden exakte rationale Ungleichungen; Stichproben tragen den allgemeinen Satz nicht.

Für epsilon=1/10,1/20,1/40,1/80 und s0=epsilon² wurden die reduzierten, exakt aus der Quelle hergeleiteten Rekurrenzen mit 80 Dezimalstellen zunächst für fünf bis sechs positive-s-Schritte ausgewertet. Nach s<1e-60 wurde die verbleibende Folge bis N=50,200,800,3200 mit der Randregel und der **analytischen verbleibenden Fehlerschranke** fortgesetzt. Kein Quellenaufruf bei auf null unterlaufender Last, kein Ändern der numerischen Rangtoleranz. Die im JSON angegebenen extrem kleinen Restgrenzen betreffen den mathematischen Tail, nicht das gesamte Mehrpräzisions-Rundungsbudget: Mehrpräzision ist keine Intervallarithmetik.

Beim kleinsten epsilon ist der normalisierte Formunterschied zur Randfolge ca. 0.00011055 bei bewiesener Schranke 0.000625; der Log-Kernelunterschied ca. 0.00007813 bei Schranke ca. 0.00062512. Der Fehler zur gemeinsamen Kontinuumsformel fällt bis ca. 0.00012012 für die Form und 0.00004359 für die Kerneldämpfung. Alle vorab festgelegten Kontrollen bestanden.

Zusätzlich **12 vollständige Original-Quellaufrufe** in n=2,4 mit komplex gedrehtem A, positivem nichtkommutierendem ausgeglichenem F und positivem K. Der größte epsilon-Fall wurde jeweils über zwei tatsächliche Ereignisse geprüft; weitere Präparationen und unitäre Kontrollen blieben kurz und numerisch aufgelöst. Größter Quell-/Rekurrenzrest <1.3e-14, Kovarianzrest <1.4e-15. Die langen reduzierten Folgen sind ausdrücklich keine 3200 erfolgreichen Aufrufe des numerischen Originalupdates.

Keine Kriterien-, Quellen- oder Rangtoleranzänderung. Manuskripte, Grundgleichungen, Lizenzen und empirische Ergebnisse unverändert; CI separat ausgewiesen.

## Nächste Abhängigkeit
Die uniforme mathematische Übertragung ist für den exakt ausgeglichenen Zwei-Niveau-Sektor geschlossen. Offen sind seine Auswahl und Stabilität gegenüber Formations-Ungleichgewicht/weiteren Lastniveaus, physikalische Zeitkalibrierung, räumliche Observable und Energie-Impuls-Zuordnung. Als nächste konkrete Reichweitenfrage bietet sich die Wirkung eines kleinen Formations-Ungleichgewichts auf diese gemeinsame Skala an. Ein solcher Stabilitätstest darf keine fehlenden physikalischen Gesetze ersetzen. Vollständiger Viererstrom, Wirkung und Einstein bleiben offen.
