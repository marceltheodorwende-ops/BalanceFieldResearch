# Vorabprotokoll: Formations-Ungleichgewicht und kritische Skala

Ausgangspunkt 680c7f624211103e089e59bf26c215fd28386745. Zwei-Niveau-A mit A²=I; delta=<A>_F in (-1,1) ist konstant. Schreibe Y=s(I+rA), wobei s hier der spektrale MITTELPUNKT und bei delta!=0 nicht die formationsgewichtete Gesamtlast ist. Prüfe die exakte positive-s-Quotientenform q=[1+r²+2delta r+s(1-r²)(1+delta r)]/[1+s-delta sr]. Die Grenzkarte s->0 soll r_+=r/(1+delta r+r²) besitzen.

Vorabfragen: (1) feste delta>0: Kontrast sinkt, 1/r_+-1/r=delta+r liefert r_j<=1/(1/epsilon+delta j). (2) delta<0: der positive Randfixpunkt r*=-delta besitzt h*=sqrt(1-delta²); prüfe die monotone Annäherungsfaktorisierung. (3) kritische gemeinsame Skala delta=kappa epsilon, r0=epsilon, t=N epsilon²: erwarte u'=-u²(kappa+u), log d'=-u²/2. Für kappa=0 gilt das bisherige Ergebnis; für kappa=+/-1/2 vergleiche mit der unabhängig implizit gelösten ODE und d=sqrt[(kappa+u)/(kappa+1)].

Vor Auswertung: symbolische exakte q-/Rand-/Fixpunktidentitäten und kritische Koeffizienten; kappa=-1/2,0,1/2, epsilon=1/10,1/20,1/40,1/80, T=1/2 mit50,200,800,3200 Randschritten. Letzte Form-/Dämpfungsfehler <0.01 und <0.4 erster. Feste delta=1/20: prüfe die obige r-Schranke numerisch für dieselben Folgen, ohne aus kurzen Folgen einen falschen Grenzwert zu behaupten.

Originalquelle: n=2,4 mit komplex gedrehtem A und positivem nichtkommutierendem F mit delta=-1/20,0,1/40,1/20; r=1/20,s=1/1000. Beim delta=1/40-Fall zwei Ereignisse, sonst eines; je eine zusätzliche unitäre Kontrolle: insgesamt12 vollständige Quellaufrufe. Quell-/Rekurrenz-/Kovarianzreste <1e-10. Seed20261111.

Grenzen: Die kritischen Langfolgen und die Phasenklassifikation gelten zunächst für die quellenabgeleitete Randkarte. Der vorige uniforme positive-s-Beweis gilt ausdrücklich nur bei delta=0; eine Übertragung auf delta!=0 wird nicht ohne neue Fehlerkontrolle beansprucht. Keine physikalische Uhr-/Energie-Impuls-/Einstein-Herleitung.
