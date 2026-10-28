# Gekoppelte langsame relative Randdynamik

## Abhängigkeit und Bereich
[BFG-abgeleitete Randkarte, anschließend Standardmathematik] Grundlage ist die [relative Kleinlast-Randkarte](SMALL_LOAD_DERIVATION.md): R_F(Z)=(mu2 I+Z²)/(2mu2), mu2=<Z²>_F, <Z>_F=1, samt gleichzeitigem Kernelkanal Psi_Z. Sie wurde als s->0-Grenze des tatsächlichen Vollpersistenz-Updates gewonnen.

Hier wird die **autonome relative Randkarte** iteriert, wobei Form und Kernel bei jedem Randschritt gemeinsam aktualisiert werden. Eine uniforme Approximation entsprechend langer positiver-s-Quelltrajektorien ist damit noch nicht bewiesen. Keine Null-Last-Quelle wird ausgeführt; t bezeichnet zunächst eine mathematische Skalierungskoordinate.

## Allgemeine nahezu isotrope Normalform
Sei Z=I+rA, A hermitesch, <A>_F=0 und m2=<A²>_F. Direktes Ausmultiplizieren liefert exakt

    R_F(Z)-I = [rA+(r²/2)(A²-m2 I)]/(1+r²m2).

Für allgemeines A entsteht damit eine quadratische Formrichtung Q=A²-m2 I. In den festen skalierten Koordinaten B=(Z-I)/epsilon mit anfänglich r=epsilon gilt

    B_+-B=(epsilon/2)Q+O(epsilon²).

Falls Q nicht verschwindet, hat diese erste relative Formänderung auf der Kernel-Zeitskala delta t=epsilon² einen divergierenden Anfangsdifferenzenquotienten. Dies verwirft nur einen regulären gemeinsamen Euler-Ansatz in diesen Koordinaten für allgemeine Formen; andere Skalen, Grenzschichten oder besondere Sektoren sind nicht ausgeschlossen.

Exakter Drei-Niveau-Zeuge: A=diag(-1,0,1), F=I3, m2=2/3 und Q=diag(1/3,-2/3,1/3)!=0.

## Invarianter ausgeglichener Zwei-Niveau-Sektor
Nehme zusätzlich A²=I und <A>_F=0 an. Beide A-Eigenräume haben damit dieselbe Formationsgewichtung. Ihre Dimensionen müssen nicht eins sein; dies ist kein Auswahltheorem für zwei komplexe Moden oder vier physikalische Dimensionen. Für 0<r<1 ist Z=I+rA positiv.

Die Randform bleibt exakt in derselben Familie:

    Z_+=I+r_+ A, r_+=r/(1+r²).

Innerhalb eines A-Eigenblocks ist der Kernel unverändert. Zwischen den beiden Eigenblöcken gilt mit mu2=1+r²

    h(r)=(mu2+(1-r)(1+r))
          /sqrt[(mu2+(1-r)²)(mu2+(1+r)²)]
        =1/sqrt(1+r²+r^4).

Dies sind gekoppelte quellenabgeleitete Randschritte: Das nächste h wird aus dem tatsächlich fortgeschobenen r berechnet. Es wird kein konstantes h oder unabhängiges Form-Reset verwendet.

## Gemeinsamer langsamer Grenzwert der Randkarte
Starte r_0=epsilon und setze h_step=epsilon², u_j=r_j/epsilon. Dann exakt

    u_(j+1)=u_j/(1+h_step u_j²),
    (u_(j+1)-u_j)/h_step=-u_j³/(1+h_step u_j²).

Auf jedem festen t-Intervall [0,T], t=j h_step, konvergiert die interpolierte Folge gegen

    du/dt=-u³, u(0)=1,
    u(t)=(1+2t)^(-1/2).

Beweis mit Fehlerkontrolle: 0<u_j<=1; der Unterschied zum Euler-Schritt für f(u)=-u³ ist höchstens h_step². Auf [0,1] ist f Lipschitz mit Konstante 3, und für die exakte Lösung gilt |u''|<=3. Einschließlich exaktem lokalem Zeitschrittfehler ist der Fehler pro Schritt höchstens (5/2)h_step². Diskretes Grönwall liefert an Gitterpunkten zum Beispiel

    |u_j-u(t_j)| <= (5/6)(exp(3T)-1) h_step.

Die punktweise lineare Interpolation behält damit Konvergenz auf festen Zeitintervallen. Eine uniforme T->unendlich-Fehlerschranke wird nicht behauptet.

Schreibe die A-Blockanteile von K als D_A(K)=(K+AKA)/2 und O_A(K)=(K-AKA)/2. Nach j Randschritten

    K_j=D_A(K0)+d_j O_A(K0),
    d_j=Produkt_(l<j) (1+r_l²+r_l^4)^(-1/2).

Uniform für u_l in [0,1] gilt
log h(r_l)=-(h_step/2)u_l²+O(h_step²).
Die obige O(h_step)-Approximation der u-Folge und eine Riemannsumme liefern auf festen Intervallen

    log d(t)=-1/2 Integral_0^t u(v)² dv=-1/4 log(1+2t),
    d(t)=(1+2t)^(-1/4),
    K(t)=D_A(K0)+(1+2t)^(-1/4) O_A(K0).

Auch hier ist der Gitterfehler O_T(epsilon²). Äquivalent

    dK/dt= -u(t)² [A,[A,K]]/8.

Die Dynamik bleibt vollständig positiv, unital und spurtreu, weil 0<d(t)<=1 ein positiver Zwei-Block-Dephasierungskanal ist. In einem nichtdegenerierten Zwei-Moden-Träger bleiben die zwei blockdiagonalen Komponenten konstant, die zwei transversalen werden gedämpft. Daraus folgt kein erhaltener physikalischer Viererstrom.

Dies ist ein expliziter gemeinsamer Form-/Kernel-Grenzwert der abgeleiteten Randkarte. Er wählt keine physikalischen Sekunden, räumlichen Orte oder Lorentz-Boosts. Ein weiterer Maßstabsfaktor für t wäre ohne Kalibrierung weiterhin frei.

## Frische Evidenz
[Vorabprotokoll](RELATIVE_SLOW_PROTOCOL.md), [Prüfcode](relative_slow_audit.py), [Resultate](relative_slow_results.json).

Symbolisch geprüft: allgemeine Normalform, nichtverschwindender Drei-Niveau-Q-Term, exakte r-Rekurrenz und h²=1/(1+r²+r^4). Für T=1/2 wurden 50,200,800,3200 **Randschritte** bei epsilon=1/10,1/20,1/40,1/80 berechnet. Der Amplitudenfehler fällt von ca. 0.0006156 auf 9.58e-6, der Kernel-Dämpfungsfehler von ca. 0.0014219 auf 2.22e-5; die vorab festgelegten Grenzen sind erfüllt. Diese Rechnungen bestätigen die bewiesene feste-T-Konvergenz, ersetzen sie aber nicht.

Zusätzlich 14 vollständige, jeweils einereignisweise Quellaufrufe: komplex gedrehte ausgeglichene Sektoren n=2,4, ein komplex gedrehter Drei-Niveau-Zeuge, jeweils vier r-Werte, sowie zwei unitäre Zusatzkontrollen; s=1/1000. Maximaler exakter Quellrest <3.4e-15, Kovarianzrest <4.2e-15. Der endliche Quellen-/Randformabstand ist deutlich größer, maximal ca. 0.00039374, unter der vorab festgelegten 0.01. Identitätsfehler, Randapproximation und viele Randschritte bleiben getrennt.

Keine Kriterien-, Quellen- oder Rangtoleranzänderung. Keine 3200 vollständigen Quellenereignisse behauptet. Manuskripte, Grundgleichungen, Lizenzen und empirische Daten unverändert; CI separat ausgewiesen.

## Genau nächste offene Brücke
Vor einer Übertragung auf die vollständige autonome positive-s-Dynamik ist eine uniforme Fehlerabschätzung für N~epsilon^-2 nötig, während s unter derselben Quelle schnell schrumpft. Einereignisweise O(s)-Nähe allein beweist diese lange Grenzfolge nicht. Zusätzlich sind die BFG-interne Auswahl des ausgeglichenen Sektors, eine physikalische Uhr und räumliches Maß offen. Vollständiger Energie-Impuls-Strom, Wirkung und Einstein bleiben offen.
