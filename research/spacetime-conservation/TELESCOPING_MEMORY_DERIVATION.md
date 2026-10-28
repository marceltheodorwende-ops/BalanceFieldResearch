# Konditioniertes unteres Paar: allzeitliche Kontrolle durch Teleskopieren

## Geltungsbereich und Quelle

Unter erklärten BFG-Annahmen abgeleitet mit Standardmathematik aus derselben gepinnten vollständigen positiven Persistenzquelle. F>0 beliebig komplex, n>=3 fest, kappa=lambda_max(F)/lambda_min(F)<infty. Y in der bereits bewiesenen invarianten Klasse C, maximaler Eigenwert M<=1/4; drei kleinste Eigenwerte strikt geordnet 0<u=y_1<v=y_2<w=y_3. Weitere Eigenwerte sind beliebig oberhalb w. Keine obere Zweifachentartung, ausgeglichenen F-Blöcke oder obere Breitenkegel werden angenommen.

Im ausgerichteten vollen Persistenzsektor bleibt F erhalten, ebenso n und kappa. C und die Ordnung sind invariant; die bekannte M-Kontraktion hält M<=1/4 für jedes endliche Ereignis. Die Aussage gilt innerhalb dieses Sektors, nicht über Auswahl-/Seed-/Rangwechsel hinweg. Ein C-Zustand mit 1/4<M<=1/2 kann nach der bekannten Lastkontraktion separat behandelt werden; sein erster Defekt muss dann zusätzlich bilanziert werden.

Setze eta=(v-u)/(w-u) in (0,1), U=eta², ell²=alpha/(1-alpha), chi=(v-u)/ell, beta=1-alpha>0. alpha wird in jedem Schritt aus dem vollständigen Zustand berechnet. Paarsektor und notwendige Umgebung werden nicht zu einer fälschlich autonomen Zwei-Moden-Dynamik verkürzt.

## Quantitative Sekantenabnahme aus derselben Quelle

Das Spektralupdate ist g(y)=(alpha+beta y²)/(1+y)². Exakt

g'(y)=2(beta y-alpha)/(1+y)³,
g''(y)=2[beta(1-2y)+3alpha]/(1+y)^4.

In C gilt g'>0. Für 0<y<=M<=1/4 liefern dieselben Formeln

0<g'(y)<=2beta M,
g''(y)>=256beta/625=:k.

Die Konstante ist rational: 1/(5/4)^4=256/625. Subtrahiere k y²/2 von g. Die verbleibende Funktion ist konvex. Für die beiden geschachtelten Sekanten folgt daher

S_13-S_12 >= k(w-v)/2,
S_13=[g(w)-g(u)]/(w-u)<=2beta M.

Wie in Runde 29 ist eta_+/eta=S_12/S_13. Also exakt

1-eta_+/eta >=64(w-v)/(625M).

Es wurde keine positive Abnahmegeschwindigkeit erfunden: Sie folgt aus der expliziten Krümmung derselben BFG-Lastabbildung. Mit t=w-u und w-v=(1-eta)t ergibt sich

U-U_+ >= eta²(1-eta_+/eta)
          >=(64/625)eta²(1-eta)t/M.

## Vergleich mit dem formationsabhängigen Defekt

Die Spurabschätzung aus Runde 30 gibt ell²>=M²/[n kappa(1+M)]. Damit

1-h<=chi²/2 <=n kappa(1+M)eta²(t/M)²/2
                  <=(5n kappa/8)eta²(t/M)².

Weil t/M<=1 und eta_j<=eta_0<1, folgt an jedem Ereignis

1-h_j <= chi_j²/2 <= C_0(U_j-U_(j+1)),
C_0=3125 n kappa/[512(1-eta_0)].

Der rationale Faktor ist (5/8)/(64/625)=3125/512. Er ist konservativ; seine Größe wird nicht auf ein gewünschtes Ergebnis kalibriert.

## Allzeitliche Summe, Paar-Gedächtnis und Rest

Teleskopieren liefert für jedes endliche N

sum(j<N)chi_j²/2 <= C_0(eta_0²-eta_N²)<=C_0 eta_0²,
sum(j>=N)chi_j²/2 <= C_0 eta_N².

Damit ist die formationsabhängige Defektreihe im erklärten festen Sektor tatsächlich summierbar. Der vorher nur bedingte Historienvergleich wird hier geschlossen; sum eta_j² selbst wird weder gebraucht noch als endlich bewiesen.

Für d_N=product(j<N)h_j folgt

1-d_N<=min[1,C_0 eta_0²],
||K_S,N-K_S,0||_F<=min[1,C_0 eta_0²] ||O(K_S,0)||_F.

Die Reständerung ab N ist höchstens min[1,C_0 eta_N²] mal der ursprünglichen Offdiagonalnorm. Dieser beweisgetragene Rest kann grob sein; insbesondere wird hier keine zusätzliche Rate eta_N->0 behauptet. Aus der endlichen positiven Defektsumme und h_j>0 folgt auch d_infty>0: Nach endlich vielen Faktoren gilt 1-h_j<=1/2 und -log h_j<=2(1-h_j); die verbleibende Logsumme ist endlich. Das ist eine mathematische nichtverschwindende Restkohärenz, keine vier exakt erhaltenen Ladungen.

Zwei lokale Diagonalkomponenten bleiben exakt erhalten, beide transversalen teilen d_N. Nichttriviale uniforme Nähe zum Anfang folgt für Klassen mit kontrolliertem n,kappa und kleinem eta_0. Die grobe Schranke kann bis auf 1 abgeschnitten und dann uninformativ sein; solche Fälle bleiben in den Ergebnissen sichtbar.

## Verhältnis zu früheren Grenzen

Die frühere obere Breiten-Stoppgrenze wird nicht als invariant umgedeutet: Der neue Satz verwendet diese Koordinate gar nicht und kann auf dieselbe geordnete untere Paarfläche auch nach ihrem Austritt angewandt werden, sofern die hier genannten C-/M-/Persistenzvoraussetzungen gelten. Das Paar ist in diesem geordneten Sektor spektral kovariant definiert; seine allgemeine physikalische Auswahl und ein räumlicher Transport sind damit nicht hergeleitet.

Der Gegenzeuge aus Runde 29 bleibt bestehen. Dort kappa=epsilon^(-6), eta_0 ungefähr 2epsilon; C_0 eta_0² ist nicht uniform klein. Es gibt somit keinen Widerspruch zum endlichen Einzelschrittverlust bei eta_0->0. Der neue Satz behauptet keine formationsunabhängige uniforme Kleinheit und kein Ergebnis für n=2 oder y_2=y_3. Auswahl-/Seed-/Rangereignisse brauchen weiterhin eigene Bilanz.

## Frische Prüfung

TELESCOPING_MEMORY_PROTOCOL.md vor Auswertung publiziert. Symbolisch exakte Ableitungsidentitäten und rationale Konstanten; unabhängiger allgemeiner Sekanten-/Spurbeweis wie oben. Neun frische Original-Quellaufrufe: n=3,4 mit nichtkommutierendem komplexem F, kappa=1,4,16, sechs Basisfälle plus drei simultane komplexe Eichkontrollen. Jeder Basisfall prüft quantitative Sekantenabnahme und chi²/2-Teleskopvergleich, nicht bloß kleine Matrixreste.

Sechs 500-stellige positive-Last-Präfixe à sechs Ereignisse, n=4, eta_0=.01,.1 und kappa=1,4,16, feste formationgewichtete volle Rekurrenz ohne Randersetzung. Präfixsummen und analytische Restschranken bestanden. Bei eta_0=.1 und kappa=4,16 ist die konservative uniforme Verlustschranke auf 1 abgeschnitten; dies wird nicht als starker Zahlenbefund verkauft. Lasten bis ungefähr 1e-50 sind ausschließlich skalare hochpräzise Präfixe, keine aufgelösten Original-Matrixtrajektorien unter dem Rank-Cutoff; keine gerichtete Intervallarithmetik behauptet.

Original-Kernelrest 9.786377569983968e-16, Lastrest 5.192575747860466e-17, Eichrest 1.6905839730415743e-15; vorab Schwelle 1e-10, Ungleichungsslack 1e-12. Die unendliche Summe folgt aus dem Beweis und nicht aus sechs numerischen Ereignissen. CI separat in CI_VALIDATION.md.

Nächste Abhängigkeit: Wie wird ein solcher geordneter, formationskonditionierter lokaler Sektor aus der vollständigen BFG-Quelle ausgewählt und über Auswahl-/Rangereignisse sowie räumliche Relationen transportiert? Physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen. Lokales mathematisches Gedächtnis ist keine nachgewiesene physikalische Energie-Impuls-Erhaltung.
