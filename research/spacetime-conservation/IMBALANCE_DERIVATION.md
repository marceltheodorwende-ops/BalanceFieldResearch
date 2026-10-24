# Formations-Ungleichgewicht und kritische relative Skala

## Zustand und Koordinaten
[BFG-abgeleitet] Behalte den Zwei-Niveau-Lastsektor A=A†, A²=I und definiere das erhaltene Ungleichgewicht delta=tr(FA)/trF, |delta|<1. In der ausgerichteten Vollpersistenzrepräsentation bleiben F,A erhalten. F darf nicht mit A kommutieren; seine beiden Blockgewichte sind (1±delta)/2.

Schreibe Y=s(I+rA), 0<r<1. **Hier ist s der spektrale Mittelpunkt** (y_++y_-)/2. Bei delta!=0 unterscheidet er sich von der früheren formationsgewichteten Normierung: <Y>_F=s(1+delta r). Diese neue Parametrisierung fügt keine Quelle oder Dynamik hinzu.

## Exakte endliche Rekurrenz und Randkarte
Aus derselben vollständigen Formationslastformel folgt exakt

    q=alpha/[(1-alpha)s²]
     =[1+r²+2delta r+s(1-r²)(1+delta r)]/[1+s-delta sr],
    G_±=[q+(1±r)²]/[(1+s(1±r))²(1+s²q)],
    s_+=s²(G_++G_-)/2,
    r_+=(G_+-G_-)/(G_++G_-),
    h(s,r,delta)=[q+1-r²]
                  /sqrt[(q+(1-r)²)(q+(1+r)²)].

Der Kernel besitzt unveränderte A-Diagonalblöcke und den gemeinsamen Faktor h auf den Querverbindungen. Keine Rücksetzung von Y oder formationsunabhängige Gewichtung wird eingesetzt.

Für s->0 ergibt sich in diesen Mittelpunktkoordinaten

    r_+=b_delta(r)=r/(1+delta r+r²),
    h_delta(r)=(1+delta r)
                /sqrt[(1+delta r+r²)²-r²].

Die folgenden Langzeitaussagen betreffen ausdrücklich diese aus BFG abgeleitete Randkarte. Der vorige uniforme positive-s-Beweis setzte delta=0 voraus und wird hier nicht ungeprüft auf delta!=0 erweitert. Die endlichen exakten Rekurrenzen werden zusätzlich an kurzen vollständigen Quellereignissen geprüft.

## Drei relative Randregime
Exakt gilt

    b_delta(r)-r=-r²(delta+r)/(1+delta r+r²),
    1/b_delta(r)-1/r=delta+r.

- delta=0: die bereits bewiesene langsame Kontrastabnahme mit r_j~1/sqrt(2j).
- delta>0: r_j fällt gegen null und r_j<=1/(1/r0+delta j). Ein festes positives Ungleichgewicht erzeugt somit eine andere Skala als die ausgeglichene Grenze.
- delta=-a<0: der positive Fixpunkt ist r*=a. Für 0<r0<a wächst die Folge monoton zu a; für a<r0<1 fällt sie monoton zu a. Es gibt keinen Überschwinger, denn
  a-b_(-a)(r)=(a-r)(1-ar)/(1-ar+r²).
  Am Fixpunkt gilt h_(-a)(a)=sqrt(1-a²)<1. Die Randform bleibt nichtisotrop und der Quer-Kernel wird bei jedem weiteren Randereignis gedämpft.

Dies ist eine mathematische Regimeklassifikation des ausgewiesenen Randsektors; es sind keine beobachteten physikalischen Phasen.

Eine zusätzliche präzise Robustheitsgrenze folgt schon für festes 0<delta<=1/4 und r0=epsilon<=1/4. Setze D=(1+delta r+r²)²-r²>=1. Dann
1-h_delta(r)²=r²(1+2delta r+r²)/D<=(19/16)r² und h²>=237/256. Aus -log x<= (1-x)/x folgt -log h<=r². Daher für jedes N

    -log d_N<=sum_j r_j²<=epsilon²+epsilon/delta.

Bei festem delta>0 und epsilon->0 geht somit der kumulative Randkanal sogar für beliebig viele Schritte gegen die Identität. Für N=floor(t/epsilon²) und festes t>0 folgt zugleich r_N/epsilon->0 aus der obigen Kehrwertschranke. Dieser punktweise t>0-Befund ist kein gleichmäßiger Formgrenzwert am Anfang t=0 und unterscheidet sich vom ausgeglichenen nichttrivialen Dämpfungsverlauf.

## Kritisches Ungleichgewicht delta=kappa epsilon
Setze r0=epsilon, delta=kappa epsilon und t=j epsilon². Für die geprüfte kompakte Familie -1/2<=kappa<=1/2 gilt exakt

    u_j=r_j/epsilon,
    u_(j+1)=u_j/[1+epsilon²(kappa u_j+u_j²)].

Die Folge bleibt zwischen max(0,-kappa) und eins. Ein Euler-/Grönwall-Argument wie beim ausgeglichenen Fall ergibt auf festen Zeitintervallen mit Fehler O_T(epsilon²)

    du/dt=-u²(kappa+u), u(0)=1,
    d(log d)/dt=-u²/2, d(0)=1.

Beweis des zweiten Koeffizienten: Setze delta=kappa epsilon und r=epsilon u in h_delta² ein; die rationale Entwicklung ist 1-epsilon²u²+O(epsilon^4), uniform auf dem kompakten u/kappa-Bereich. Logarithmieren und Riemannsummen liefern die Dämpfung mit demselben Fehlergrad. Die Formgleichung hat einen glatten Lipschitz-Vektorfluss auf diesem invarianten Bereich; lokale Fehler sind O(epsilon^4), daher global O_T(epsilon²).

Für kappa!=0 wird u unabhängig über

    P_k(v)=log[(kappa+v)/v]/kappa²-1/(kappa v),
    t=P_k(1)-P_k(u(t))

bestimmt; P'_k(v)=1/[v²(kappa+v)]. Die Dämpfung ist exakt

    d(t)=sqrt[(kappa+u(t))/(kappa+1)].

Für kappa=0 ergeben sich u=(1+2t)^(-1/2) und d=(1+2t)^(-1/4). Auf der Randkarte erhält delta=o(epsilon) damit den ausgeglichenen Grenzwert, während delta~kappa epsilon eine andere, kontrollierte Grenzfamilie liefert. Eine kleine feste Störung ist auf dieser Skala nicht automatisch vernachlässigbar.

Die Aussagen liefern eine quantitative Robustheitsfrage und deren Randantwort. Sie wählen weder physikalische Sekunden noch einen räumlichen Impuls oder eine Formation, die den kritischen Zusammenhang von selbst erfüllt.

## Frische Evidenz
[Vorabprotokoll](IMBALANCE_PROTOCOL.md), [Prüfcode](imbalance_audit.py), [Resultate](imbalance_results.json).

Symbolisch geprüft: vollständige q-Formel, Randrekurrenz, Kehrwertidentität, negative Fixpunktfaktorisierung, h*²=1-delta² und kritischer Dämpfungskoeffizient. Numerische kritische Folgen wurden für kappa=-1/2,0,1/2 und vier epsilon-Werte bis T=1/2 berechnet, mit bis zu 3200 **Randschritten**. Die Grenzreferenz wurde unabhängig durch die implizite Integralformel gelöst.

Am kleinsten epsilon liegen die Formfehler je nach kappa zwischen ca. 7.36e-6 und 9.75e-6, die Dämpfungsfehler zwischen ca. 1.88e-5 und 2.48e-5. Alle vorab festgelegten Konvergenzgrenzen bestanden. Bei festem delta=1/20 wurden die Kehrwertschranken ebenfalls eingehalten; die endlichen Daten werden nicht als schon erreichte asymptotische Werte ausgegeben.

Zusätzlich **12 vollständige Original-Quellaufrufe** in n=2,4, komplex gedrehtes A, positives nichtkommutierendes F mit den vier vorab festgelegten Ungleichgewichten, positives K, jeweils s=1/1000 und r=1/20. Der delta=1/40-Fall umfasst jeweils zwei tatsächliche Ereignisse; zwei weitere Aufrufe prüfen unitäre Kovarianz. Maximaler Quell-/Rekurrenzrest ca. 1.66e-12, Kovarianzrest <4.4e-15, unter vorab unverändertem 1e-10. Der größere Zweitereignisrest bleibt ausgewiesen und wird nicht auf die früheren 1e-14-Werte gerundet.

Keine Fälle verworfen oder Kriterien angepasst. Die allgemeine Regime-/Grenzaussage beruht auf der angegebenen Algebra und Fehleranalyse, nicht auf den endlichen Kontrollen. Manuskript, Grundgleichungen, Lizenzen und empirische Ergebnisse unverändert. CI separat ausgewiesen.

## Nächste offene Abhängigkeit
Die Empfindlichkeit und die kritische Ungleichgewichtsskala der Randkarte sind geklärt. Für die neue kappa-Familie fehlt noch die uniforme positive-s-Übertragung, die bisher nur bei delta=0 bewiesen ist. Ebenso fehlt eine BFG-interne Auswahl oder Stabilisierung der nötigen Formations-/Lastrelation. Physikalische Uhr und räumliche Auslese, vollständige Energie-Impuls-Erhaltung, Wirkung und Einstein bleiben offen.
