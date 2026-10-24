# Unterer Zwei-Moden-Träger: summierbarer Kohärenzverlust

## Familie und Geltungsbereich

Fortsetzung von FINITE_SPLITTING_DERIVATION.md, ausschließlich derselbe gepinnte BFG-Kernel und das vollständige Dynamic-Order-Manuskript. n=4, A=diag(1,1,-1,-1), B=diag(0,0,1,-1), Z=I+rA+bB, Y=sZ. Die beiden F-Diagonalblöcke sind I; kleine komplexe Kreuzblöcke sind zulässig, F>0. r<=1/4 und 0<q=b/r<=1/2. c=1-r, untere Eigenwerte c±b. Alle Formeln gelten auch unter simultaner unitärer Konjugation. Keine Änderung der Quelldynamik.

## Lyapunov-Abschätzung am relativen Rand s=0

Mit mu=1+r²+b²/2 gilt r+=(r-b²/4)/mu, b+=(1-r)b/mu. Der bereits bewiesene untere Kegel bleibt invariant. Für V=b²/r folgt exakt

V+/V=(1-r)²/[mu(1-q²r/4)] <= 1-r,

weil mu>=1 und 1-q²r/4>=1-r>0. Deshalb V-V+>=rV=b². Teleskopieren ergibt für jedes N

sum(j=0..N-1) b_j² + V_N <= V_0,

und somit sum(j>=0)b_j²<=b_0²/r_0. Die Restreihe ab N ist höchstens V_N. Das ist ein Beweis für alle Ereignisse, keine Extrapolation aus 2000 numerischen Schritten.

## Exakter lokaler Faktor bei positiver Last

Für den vollen positiven-Last-Schritt setze rho=alpha/[(1-alpha)s²]>0 und v=c²-b². Der Schur-Faktor des unteren Paares lautet

h=(rho+v)/sqrt((rho+v)²+4rho b²).

Aus 1-(1+x)^(-1/2)<=x/2 für x>=0 und (rho+v)²>=4rho v folgt

0<=1-h<=2rho b²/(rho+v)²<=b²/(2v)<=32b²/35,

weil c>=3/4,b<=1/8, also v>=35/64. Dies benötigt keine besondere Wahl von alpha. Der Grenzfall setzt rho=mu. Untere Paar-Diagonalen bleiben exakt konstant; beide transversalen Komponenten tragen denselben Faktor h. Die beiden kleinsten Eigenmoden bilden im geprüften geordneten Bereich dasselbe Paar. Alle Umgebungsdaten, die alpha bestimmen, bleiben nötig: keine autonome Paar-Schließung behauptet.

## Uniformes Gedächtnis am Rand

Im gemeinsamen Eigenrahmen K_S,N=D(K_S,0)+d_N O(K_S,0), d_N=product h_j, mit D diagonalem und O offdiagonalem Anteil. Weil 1-product h_j<=sum(1-h_j), gilt für alle endlichen N und im Grenzwert

1-d_N <= (32/35) b_0²/r_0,

||K_S,N-K_S,0||_F <= (32/35)(b_0²/r_0)||O(K_S,0)||_F.

Die endliche Restkohärenzänderung nach N ist höchstens (32/35)V_N ||O(K_S,0)||_F. Insbesondere liefert r_0=epsilon,b_0=epsilon³ einen O(epsilon^5)-Defekt. Bei b_0>0 sind die transversalen Größen weiterhin nicht exakt erhalten. Bei b_0=0 wird der bekannte exakt entartete Paarfall zurückgewonnen. Diese Abschätzung ist konstruktive Robustheit eines lokalen Kernelträgers, kein Energie-Impuls-Gesetz.

## Frische Prüfung und Grenzen

LOWER_PAIR_MEMORY_PROTOCOL.md wurde vor Auswertung auf GitHub gespeichert. Symbolische Identitäten, vier Randtrajektorien zu je 2000 Schritten und zehn Original-Quellaufrufe (acht Lastfälle, zwei komplexe Eichkontrollen) bestanden. Kernelrest <1.5e-14, Eichrest <4.6e-14; normierter Lastrest siehe JSON, unter 1e-8. Kleine Randbreiten werden als skalare Randrekurrenz ausgewiesen, nicht als numerisch aufgelöste Original-Matrixtrajektorien. Numerische Produkte nahe eins liefern keine hochpräzise Auflösung winziger Verluste; der exakte Beweis trägt die Restabschätzung.

Der erste lokale Auditlauf scheiterte an einem falsch abgetippten Koeffizienten einer entbehrlichen polynomialen Prüfidentität (8 statt 4). Die Prüfung wurde durch eine exakt expandierte nichtnegative Zerlegung ersetzt; die Lyapunov-Ungleichung und Hypothese wurden nicht angepasst. Die endgültige frische Ausführung bestand.

Die Einzelschrittabschätzung gilt auch bei positivem s, solange der Zustand im angegebenen Kegel liegt. Die summierbare Reihe und daraus abgeleitete uniforme Langzeitschranke sind hier nur am Rand bewiesen. q_+<q allein beweist weder die nötige quantitative Abnahme noch alle Voraussetzungen der Teleskopsumme im vollen Quelllauf. Nächster Schritt: positive-s-Lyapunov- oder uniforme Störungsabschätzung für diesen unteren Kegel; danach Auswahl/Isolierung und Transport des Trägers. Physikalische Uhr, Raummaß, vollständiger Viererstrom und Einstein-Herleitung bleiben offen.
