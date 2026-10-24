# Formationsabhängige Schranke des lokalen Kohärenzverlusts

## Quelle und Gegenstand

Unter genannten BFG-Annahmen abgeleitet, Standardmathematik aus demselben gepinnten vollen positiven Persistenzupdate, keine neue Dynamik oder physikalische Prämisse. F>0, Y>0, aktuelle Mischung alpha=L_B/(L_C+L_B), L_C=tr[F(I+Y)^(-1)], L_B=tr[FY²(I+Y)^(-1)]. Für die geordnete untere Paarlast u=y_1<v=y_2 definiere ell²=alpha/(1-alpha)=L_B/L_C>0 und chi=(v-u)/ell. Die Größe ist dimensionslos im bestehenden mathematischen Lastchart, keine physikalisch kalibrierte Energie oder Länge.

## Exakte Einzelschrittabschätzung

Der bereits hergeleitete Schurfaktor ist

h=(ell²+uv)/sqrt[(ell²+u²)(ell²+v²)].

Exakt gilt (ell²+u²)(ell²+v²)-(ell²+uv)²=ell²(v-u)². Deshalb h=(1+x)^(-1/2) mit x=ell²(v-u)²/(ell²+uv)²>=0. Aus 1-(1+x)^(-1/2)<=x/2 und ell²+uv>=ell² folgt

0<=1-h<=ell²(v-u)²/[2(ell²+uv)²]<=chi²/2.

Dies ist keine neue Erhaltung; es kontrolliert den exakten Defekt durch die aktuelle formationsabhängige Mischung. Das Paar allein bestimmt ell nicht: die erforderliche Umgebung bleibt enthalten.

## Explizite Formationskondition als ausreichende Zusatzvoraussetzung

Sei n die volle persistierende Dimension, f_min>0 und f_max die extremen Eigenwerte von F, kappa=f_max/f_min. Im Eigenrahmen von Y liegen alle F_ii zwischen f_min und f_max. Sei M=max Y und M<=1/2. Der Term zur größten Last liefert L_B>=f_min M²/(1+M). Dagegen L_C<=tr F<=n f_max. Also

ell²>=M²/[n kappa(1+M)].

Für ein drittes geordnetes y_3>y_2 und eta=(y_2-y_1)/(y_3-y_1) gilt v-u=eta(y_3-y_1)<=eta M. Damit

1-h<=chi²/2<=n kappa(1+M) eta²/2<=3n kappa eta²/4.

Die Rechnung gilt für komplexes, mit Y nicht kommutierendes F. Gleichmäßige Elliptizität wird nicht als Gesetz der Quelle ausgegeben. Für eine Klasse von Anfangsdaten mit beschränktem n und kappa liefert sie eine uniforme kleine Einzelschrittschranke bei kleinem eta. Im vollen ausgerichteten Persistenzsektor bleibt F und damit kappa erhalten; bei Auswahl-, Seed- oder Rangereignissen darf dies nicht ohne zusätzliche Bilanz globalisiert werden.

## Präzise endliche Historie und verbleibende Lücke

Für d_N=product(j<N)h_j gilt weiterhin 1-d_N<=sum(j<N)(1-h_j). Somit

1-d_N<=min[1, (1/2)sum(j<N)chi_j²],
1-d_N<=min[1, (3n kappa/4)sum(j<N)eta_j²]

im festen Persistenzsektor mit obigen Voraussetzungen. Der lokale Kerneldefekt ist diese Zahl mal der anfänglichen Offdiagonalnorm; beide diagonalen Komponenten bleiben konstant. Eine entsprechende Restschranke ab N benötigt die Restreihe ab N. Konvergenz und Kleinheit von sum chi_j² oder sum eta_j² sind zusätzliche mathematische Aufgaben, hier nicht als Quellresultat behauptet.

Die bekannte strikte Kontraktion eta_+<eta allein beweist keine Summierbarkeit ihrer Quadrate. Der neue Befund schließt die Einzelschrittbrücke mit Formationsdaten, nicht die gesamte Nach-dem-Austritt-Langzeitlücke. Keine inverse Historienkalibrierung oder nachträglich eingebaute Erhaltung wird vorgenommen.

## Erhaltener Gegenzeuge und Verträglichkeit

In der Gegenfamilie aus Runde 29, Y=diag(2epsilon²,4epsilon²,epsilon),F=diag(1,1,epsilon^6), gilt ell²/epsilon^4->10. Daher chi²->2/5 und die neue obere Verlustschranke chi²/2->1/5. Sie behauptet also gerade keinen verschwindenden Defekt, im Einklang mit 1-h->1-9/sqrt(91)>0. Die alternative konditionierte Schranke enthält kappa=epsilon^(-6), das nicht uniform beschränkt ist. Der alte Gegenzeuge bleibt vollständig gültig und wird nicht durch eine stillschweigende Konditionsannahme gelöscht.

## Frische Evidenz

FORMATION_BOUND_PROTOCOL.md wurde vor Auswertung auf GitHub gespeichert. Symbolisch geprüft: exakte Faktoridentität und chi²-Grenzwert der alten Gegenfamilie. Der allgemeine Konditionsvergleich beruht auf den expliziten positiven Spurabschätzungen oben. Neun frische Original-Quellaufrufe: n=3,4 mit nichtkommutierendem komplexem F und vorgegebenen Konditionszahlen 1,4,16; sechs Basisfälle und drei komplexe simultane unitäre Eichkontrollen. Positive K und W=I/n, feste im Protokoll angegebene Lasten. Jeder Basisfall prüft ell-Untergrenze, chi-Verlustschranke und konditionierte eta-Verlustschranke.

Kernelrest 6.557897197895601e-16, Lastrest 2.3507910043935894e-17, Eichrest 1.0309476579756622e-15; vorab Schwelle 1e-10, Ungleichungsslack 1e-12. Keine numerische Langtrajektorie oder allzeitliche Summierbarkeit geprüft. CI separat in CI_VALIDATION.md.

Nächster konkreter Schritt: eine aus der vollen Quelle abgeleitete quantitative Abnahme für die formationsabhängige Defektreihe oder ein Gegenbeispiel gegen deren gewünschte uniforme Kontrolle. Allgemeine Auswahl des lokalen Trägers, räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein bleiben offen. Auch eine formationsabhängig kleine lokale Kerneländerung identifiziert die vier Komponenten noch nicht mit physikalischem Energie-Impuls.
