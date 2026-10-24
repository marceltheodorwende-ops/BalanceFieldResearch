# Kontrollierte Mehrereignis-Reichweite im anfänglichen Graphen

## Voraussetzungen und Quellenbezug
[BFG-abgeleitet mit Standardmathematik] Gepinnter vollständiger Quellupdate, Vollpersistenz, F>0, 0<Y<I und endliche Ereignisfolge auf C. Behalte die Formationseigenknoten als deklarierte orthogonale Rang-eins-Projektoren und den anfänglichen Trägergraphen von Y0. Dieser interne Graph ist keine bereits hergeleitete physikalische Raumgeometrie. Keine Kante wird aus der tatsächlichen Dynamik entfernt.

Die [Kompositionsherleitung](COMPOSITION_DERIVATION.md) gibt Y_k=phi_k(Y0) und den normierten reellen Krausvektor

    v_N(t) = Tensorprodukt_(k<N) (cos theta_k(t), sin theta_k(t)),
    theta_k(t) = atan(sqrt(beta_k/alpha_k) phi_k(t)),
    phi_0(t)=t, phi_(k+1)(t)=g_(alpha_k)(phi_k(t)).

Hier ist die tatsächliche endogene alpha-Folge festgehalten, während nur das skalare Hilfsargument t variiert. Diese Ableitung ist nicht die vollständige endogene Zustandsableitung und keine Behauptung autonomer Teilsysteme.

## Endliche explizite Lipschitzschranke
Sei [m0,M0] das anfängliche Spektralintervall mit m0<M0. Auf C sind die skalaren Spektralfunktionen steigend. Daher m_k=phi_k(m0), M_k=phi_k(M0) die Intervallenden. Setze D0=1 und

    ell_k = 2(beta_k M_k-alpha_k)/(1+m_k)^3,
    D_(k+1)=ell_k D_k,
    b_k = sqrt(alpha_k beta_k) D_k/(alpha_k+beta_k m_k²),
    L_N² = sum_(k<N) b_k².

Aus 0<g'_alpha(t)=2(beta t-alpha)/(1+t)^3<=ell_k folgt 0<phi'_k<=D_k, anschließend |theta'_k|<=b_k. Alle Größen sind für jedes endliche N endlich, ohne globale alpha-Rückkopplung zu ignorieren.

Die Ableitung eines Tensorprodukts ist die Summe der nach jeweils einem Faktor abgeleiteten Terme. Verschiedene Terme sind orthogonal, weil jeder normierte reelle Zweigvektor zu seiner eigenen Ableitung orthogonal ist. Somit

    ||v'_N(t)||²=sum_(k<N) |theta'_k(t)|² <= L_N².

Dies vermeidet einen pauschalen Faktor 2^N aus der Zahl der Kraus-Wörter. Eine N-unabhängige Schranke oder eine lineare physikalische Lichtkegelschranke wird nicht behauptet. Bei skalarem Y0 ist der Kanal die Identität; dieser triviale Fall benötigt keine Intervallapproximation.

## Bernsteinapproximation und Graphdistanz
Für ganzzahliges d>=1 bilde das vektorwertige Bernsteinpolynom p_d(t) auf [m0,M0]:

    p_d(t)=sum_(j=0,...,d) binom(d,j) x^j(1-x)^(d-j)
                              v_N(m0+(M0-m0)j/d),
    x=(t-m0)/(M0-m0).

[Standardmathematik, expliziter Beweis] Interpretiere die Gewichte als Binomialwahrscheinlichkeit J~Bin(d,x). Dann

    ||v_N(t)-p_d(t)||
       <= L_N (M0-m0) E|J/d-x|
       <= L_N (M0-m0) sqrt[x(1-x)/d]
       <= epsilon_N,d := L_N (M0-m0)/(2 sqrt(d)).

Jede Komponente von p_d ist ein Polynom in t vom Grad <=d. Die zugehörigen approximierten Krausoperatoren sind deshalb Polynome in Y0 und haben keine Einträge zwischen Knoten mit anfänglicher Graphdistanz >d: In jedem Produkt von höchstens d Faktoren Y0 können nur höchstens d ursprüngliche Kanten überquert werden. Diagonale Faktoren sind stationäre Schritte. Der Beweis gilt für jeden endlichen deklarierten Y0-Trägergraphen, nicht nur Pfade.

## Gesamter Bestand außerhalb des Balls — einschließlich Kohärenzen
Schreibe den exakten Kompositions-Stinespringoperator als V_N= sum_s L_s tensor |s> und die Polynomialapproximation entsprechend als Vtilde. Durch die gemeinsame Spektralbasis gilt

    ||V_N-Vtilde|| = max_(lambda in spec Y0) ||v_N(lambda)-p_d(lambda)||
                   <= epsilon_N,d.

V_N ist eine Isometrie. Sei K0>=0 auf einem Knotenbereich S unterstützt und Q der Projektor außerhalb des d-Balls B_d(S) im anfänglichen Graphen. Dann (Q tensor I)Vtilde P_S=0 und

    tr(Q K_N)
      = ||(Q tensor I)V_N sqrt(K0)||_HS²
      <= min(1,epsilon_N,d²) tr(K0).

Die Eins-Schranke folgt separat aus Positivität und Spurtreue des echten Kanals. Es wird kein approximierter Kanal als Quelle eingesetzt, und Vtilde braucht weder exakt isometrisch noch eine neue physikalische Dynamik zu sein. Positive Kohärenzen innerhalb S sind ausdrücklich erlaubt; eine wiederholte Dephasierung wird nicht verwendet. Für indefinite K gilt diese positive Bestandsaussage nicht unverändert.

Für eine Anfangspunktmasse erhält man insbesondere sum_(dist(i,j)>d) P^(N)_ij <= min(1,L_N²(M0-m0)²/(4d)). Dies ist eine kontrollierte, konservative algebraische Tail-Schranke für die gesamte entfernte Population. Sie bedeutet keine exakt verschwindenden Fernübergänge. Für abgetrennte Komponenten bleibt die frühere exakte Blockaussage stärker. Ein Graph- oder Uhrmaßstab in Metern/Sekunden folgt daraus nicht.

## Vorab festgelegte frische Prüfung
[Protokoll](MULTIEVENT_RANGE_PROTOCOL.md), [Prüfcode](multievent_range_audit.py), [Resultate](multievent_range_results.json).

Symbolische Zwei-Faktor-Tensornormidentität exakt null. Pfade n=6,10,14, Y0=I/4+A/40, F=diag(1,...,n), W=I/n. Je drei vollständige Ereignisse an Punktmasse und positivem kohärentem Rang-eins-Kernel auf den ersten zwei Knoten; drei Basiswechselkontrollen: **21 vollständige Quellaufrufe**. Grade d=1,2,3, somit 27 Vektor-/Polynom-/Tail-Kontrollen. Die Komponenten der exakten Krausvektoren repräsentieren sämtliche bis zu acht Wörter.

Maximaler Quellrest 6.48e-15, Kovarianzrest 3.10e-15. Kein Schrankenverstoß bei unverändertem absolutem Zuschlag 1e-10. Polynome zeigen außerhalb der Grad-Reichweite nur Rundungsreste <1e-15. Die Schranken sind sichtbar konservativ: für n=14,N=3,d=3 ist die bewiesene normierte Tail-Schranke ca. 0.0101585, die Punktmassen-Quellpopulation dort ca. 1.65e-10. Kleine Tails sind ausschließlich absolut numerisch kontrolliert; dieser Vergleich ist kein relatives Präzisionszertifikat.

Keine angepasste Schwelle, kein verworfener Fall, kein Quellabbruch. Die endliche Rechnung bestätigt den allgemeinen Beweis, ersetzt ihn aber nicht. GitHub-CI wird separat vom lokalen Lauf ausgewiesen. Originalmanuskript, Grundcode, Lizenzen und empirische Ergebnisse bleiben unverändert.

## Offene nächste Abhängigkeit
Der bisher offene kontrollierte endliche Mehrereignis-Tail im anfänglichen Referenzgraphen liegt damit vor. Offen sind insbesondere die Wachstumsrate dieser Schranken bei langen tatsächlichen Ereignisfolgen, eine BFG-ausgewählte räumliche Metrik und die physikalische Zeitkalibrierung. Ohne diese Auswahl ergibt sich weder eine physikalische Geschwindigkeit noch Lorentz-Dynamik. Vollständiger Energie-Impuls-Strom, translations-/diffeomorphismusbezogene Wirkung und Einstein bleiben offen.
