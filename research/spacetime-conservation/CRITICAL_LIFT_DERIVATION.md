# Uniforme Übertragung der kritischen Ungleichgewichts-Familie

## Bereich und Aussage
[BFG-abgeleitete Rekurrenzen und Standardmathematik] Es gilt die unveränderte mathematische Vollpersistenzregel im Zwei-Niveau-Sektor A=A†, A²=I, F>0, delta=<A>_F. Wie in der [Ungleichgewichtsherleitung](IMBALANCE_DERIVATION.md) ist s der spektrale Mittelpunkt von Y=s(I+rA), nicht bei delta!=0 die formationsgewichtete Last.

Setze r0=epsilon, delta=kappa epsilon, 0<epsilon<=1/10, |kappa|<=1/2. Für jedes feste T wird die neue kritische Grenzfamilie jetzt auch aus der **exakten positiven-Last-Dynamik** gewonnen, sofern s0 hinreichend klein ist. Der Satz behauptet keine entsprechend lange numerische Fortsetzbarkeit des Originalcodes unter seiner festen Rangschwelle und keine physikalischen Sekunden.

## Rationale Konstantenzertifikate
Bezeichne die bereits hergeleitete exakte relative Folgeregel mit R(s,r,delta)=(G_+-G_-)/(G_++G_-) und die Randregel mit b_delta(r)=r/(1+delta r+r²). Auf dem festen Rechteck

    0<=s<=1/100, 0<=r<=1/4, |delta|<=1/20

sind sämtliche rationalen Nenner positiv beziehungsweise von null getrennt. Die Differenz ist durch sr teilbar:

    R(s,r,delta)-b_delta(r)=sr E(s,r,delta).

Die Division hat auf s=0 oder r=0 eine analytische Fortsetzung; diese Achsen sind Hilfsstellen der Abschätzung, keine Original-Quellenaufrufe. Für den Rand-Kernelfaktor h_delta(r) ist ferner partial_r log h_delta(0)=0.

Der Audit erzeugt für E und partial_r² log h_delta vollständig gekürzte rationale Funktionen P/Q. Für ein Polynom P=sum c_m x^m und die Rechteckradien a_i definiere die exakte rationale Koeffizientenmasse M(P)=sum |c_m| Produkt a_i^(m_i). Dann

    |P|<=M(P),
    |Q|>=2|Q(0)|-M(Q)>0.

Dies ist eine allgemeine Dreiecksungleichung auf dem ganzen Rechteck, keine Stichprobenabschätzung. Die berechneten Zertifikate sind:

- Für E: Zählermasse 2216941787/1024000000, Nenneruntergrenze 664822389749/819200000000; Quotient 1773553429600/664822389749<3.
- Für partial_r² log h_delta: Zählermasse 229628509/163840000, Nenneruntergrenze 12697894439/16384000000; Quotient 22962850900/12697894439<2.

Damit darf durchgehend C_R=3 und C_L=2 verwendet werden:

    |R-b_delta|<=C_R sr,
    |partial_r log h_delta(r)|<=C_L r.

## Bootstrap der tatsächlichen Formfolge
Die Randfolge mit Anfang epsilon bleibt bei |kappa|<=1/2 in 0<rbar_j<=epsilon. Solange die positive-Last-Folge r_j<=2epsilon bleibt, liegt sie im zertifizierten Rechteck. Zudem

    b'_delta(r)=(1-r²)/(1+delta r+r²)²
              <=(1-epsilon²)^(-2)<=1+3epsilon².

Die letzte Ungleichung folgt für x=epsilon²<=1/100 aus
(1+3x)(1-x)²-1=x(1-5x+3x²)>=0.

Für die Gesamtlast gilt wie zuvor aus M=s(1+r), M_+<=2M² und r<=1/4:

    0<s_+<=(25/8)s²<=s/32,
    sum_j s_j <=(32/31)s0.

Die Eingaben des Rechtecks liegen im bereits bewiesenen positiven stabilen Bereich; Eigenwertreihenfolge und positive Zweiniveaustruktur bleiben erhalten. Es tritt im exakten mathematischen Sektor kein Vorzeichenwechsel von r auf.

Setze Delta_j=|r_j-rbar_j|. Bis zu einem hypothetischen ersten Verlassen von r<=2epsilon gilt

    Delta_(j+1)<=(1+3epsilon²)Delta_j+2 C_R epsilon s_j.

Für j epsilon²<=T erhält man daher

    Delta_j/epsilon <=(64/31) C_R exp(3T)s0 < C_T s0,
    C_T=3 C_R exp(3T)=9 exp(3T).

Wähle 0<s0<=1/100 und C_T s0<=1/2. Dann r_j<=rbar_j+Delta_j<=3epsilon/2<2epsilon; das hypothetische Verlassen ist unmöglich. Die Abschätzung gilt somit für alle betrachteten Schritte. Dies kontrolliert eine ganze Folge und nicht nur die einzelne positive-s-zu-Rand-Nähe.

## Kumulativer Kernel
Für den exakten Quotienten q(s,r,delta) gilt die neue einfache Identität

    partial_s q=-2(1-delta²)r²/[1+s(1-delta r)]².

Somit |partial_s q|<=2r². q ist ein positiver gewichteter Mittelwert von (1±r)²; auf dem Rechteck gilt q>=(1-r)². Alle drei Nenner in partial_q log h sind daher größer als eins und |partial_q log h|<=2. Es folgt

    |log h(s,r,delta)-log h(0,r,delta)|<=4sr².

Mit den oben zertifizierten C_L- und Formschranken ergibt sich für N epsilon²<=T

    |log d_N-log dbar_N|
       <=[17epsilon²+2 C_L C_T T]s0.

Der erste Term stammt aus 4 sum s_j r_j²<=16epsilon²(32/31)s0<17epsilon²s0; der zweite aus der Summe der Formfehler unter |partial_r log h_delta|<=2 C_L epsilon. Beide kumulativen Faktoren liegen in (0,1], daher gilt dieselbe Schranke für |d_N-dbar_N|. Für den Kernel selbst wird sie mit ||O_A(K0)||_F multipliziert.

## Gemeinsamer Grenzwert bei kritischem Ungleichgewicht
Die zuvor bewiesene kritische Randgrenze hat auf festen Intervallen Fehler O_T(epsilon²). Zusammen mit den neuen positiven-Last-Schranken gilt daher

    r_floor(t/epsilon²)/epsilon -> u_kappa(t),
    K_floor(t/epsilon²) -> D_A(K0)+d_kappa(t) O_A(K0),
    u'=-u²(kappa+u), u(0)=1,
    (log d)'=-u²/2, d(0)=1,

mit Fehler O_T(s0+epsilon²), wenn s0(epsilon)->0. Die Bedingungen an s0 sind für jedes feste T schließlich erfüllt. Der Satz ist gleichmäßig für |kappa|<=1/2; keine T->unendlich-uniforme Schranke wird behauptet.

Damit ist die vorher offene positive-Last-Übertragung der kritischen Familie geschlossen. Bei kappa=0 folgt der frühere ausgeglichene Verlauf. Dies identifiziert weder einen physikalischen Zeitmaßstab noch eine räumliche Übersetzung oder erhaltenen Energie-Impuls-Viererstrom. Die Beziehung delta=kappa epsilon ist eine erklärte Präparations-/Grenzannahme, kein hergeleitetes Auswahlgesetz des allgemeinen BFG-Zustands.

## Frische Evidenz und numerische Grenzen
[Vorabprotokoll](CRITICAL_LIFT_PROTOCOL.md), [Prüfcode](critical_lift_audit.py), [Resultate](critical_lift_results.json).

Die rationalen Rechteckzertifikate, exakte Teilbarkeit und q_s-Identität wurden frisch symbolisch geprüft. Die allgemeine Aussage ruht auf diesen Zertifikaten und dem Bootstrapbeweis.

Zwölf lange reduzierte Folgen: kappa=-1/2,0,1/2 und vier epsilon-Werte, T=1/2, s0=epsilon^4. Bei 80 Dezimalstellen wurden vier bis fünf positive-s-Präfixschritte bis s<1e-60 ausgewertet; danach erfolgte eine Randfortsetzung mit der analytischen verbleibenden Fehlerabschätzung aus demselben Bootstrapargument. Am Neustart ist die Referenzamplitude höchstens 3epsilon/2, sodass die Restabschätzung innerhalb r<=2epsilon ebenfalls gilt. Bis 3200 reduzierte Schritte sind keine 3200 Original-Quellaufrufe. Extrem kleine Restlasten sind keine Originaleingaben; mathematische Tailgrenzen umfassen nicht automatisch das Rundungsbudget und sind keine Intervallzertifikate.

Bei T=1/2 ist C_T≈40.3352. Die größte geprüfte Bootstrapgröße C_T s0 ist ca. 0.004034, unter 1/2. Beim kleinsten epsilon sind normalisierte Formabweichungen vom Randmodell ca. 1.36e-8 bis 2.24e-8 bei Schranke ca. 9.85e-7; die Log-Kernelabweichungen ca. 1.02e-8 bis 1.51e-8 bei Schranke ca. 1.97e-6. Alle vorab festgelegten uniformen und Kontinuumskonvergenz-Kontrollen bestanden.

Zusätzlich **14 vollständige Original-Quellaufrufe** in n=2,4, komplex gedrehtes A, positives nichtkommutierendes F und positives K. Je drei kappa und zwei epsilon bei s0=epsilon^4, dazu zwei unitäre Kontrollen. Größter Quellen-/Rekurrenzrest <1.9e-13, Kovarianzrest <2.3e-14, beide unter unverändertem 1e-10. Diese endlichen Originalchecks werden von den langen analytisch begrenzten Rekurrenzen getrennt.

Keine wissenschaftlichen Kandidaten oder Kriterien wurden geändert. Ein vorab versuchter Shell-Einzeiler zur symbolischen Vorbereitung hatte einen Quotierungsfehler und führte keine Rechnung aus; die Zertifikate wurden im regulären Audit frisch berechnet. Manuskripte, Grundcode, Lizenzen und empirische Daten unverändert. GitHub-CI wird separat ausgewiesen.

## Nächste offene Brücke
Die kritische Ungleichgewichtsfamilie ist nun innerhalb des erklärten Zwei-Niveau-Sektors mathematisch auf positive Lasten übertragen. Offen sind die Auswahl/Stabilisierung dieser Sektor- und Präparationsannahmen sowie ihre Verbindung mit quellenbegründeten räumlichen Observablen und einer physikalisch kalibrierten Uhr. Als konkrete nächste Reichweitenfrage bietet sich eine zusätzliche Lastaufspaltung innerhalb der beiden Niveaublöcke an; sie darf nicht stillschweigend durch ein Zwei-Moden-Modell entfernt werden. Vollständiger Energie-Impuls-Strom, ausgewählte Wirkung und Einstein bleiben offen.
