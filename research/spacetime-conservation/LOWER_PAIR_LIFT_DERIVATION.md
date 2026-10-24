# Unteres Paar: uniforme Gedächtnisschranke bei positiver Last

## Quelle, Voraussetzungen und Ziel

Unter den BFG-Annahmen der vollständigen positiven Persistenz, ausschließlich der gepinnte Dynamic-Order-Quellstand aus MANDATE.de.md. Fortsetzung der n=4-Familie aus FINITE_SPLITTING_DERIVATION.md und LOWER_PAIR_MEMORY_DERIVATION.md: A=diag(1,1,-1,-1), B=diag(0,0,1,-1), Y=s[I+rA+bB]. F>0 hat beide 2x2-Diagonalblöcke I, beliebige damit verträgliche Kreuzblöcke; W wird wie im vollen Persistenzsektor mitgeführt. Gemeinsame unitäre Konjugation ist zulässig. 0<s<=1/100,0<r<=1/4,0<q=b/r<=1/2. Die obere Zweifachentartung ist eine erklärte Anfangsannahme und bleibt in dieser Familie erhalten; sie wird nicht als generisch ausgewählt behauptet.

Abgeleitet mit Standardmathematik: Der untere Bereich bleibt unter jedem endlichen exakten positiven-Last-Ereignis invariant. Für V=b²/r gilt V-V_+>=b²/2. Damit wird die bisher nur am relativen Rand bewiesene summierbare Aufspaltung auf die volle Quelle in dieser Familie übertragen.

## Exakte reduzierte Quellrekurrenz

Schreibe z=(1+r,1+r,1-r+b,1-r-b), c=1-r und

rho = sum_i z_i²/(1+s z_i) / sum_i 1/(1+s z_i),
G_i=(rho+z_i²)/[(1+s z_i)²(1+s²rho)], T=2G_0+G_2+G_3.

Dann alpha=s²rho/(1+s²rho), s_+=s²T/4,
r_+=(2G_0-G_2-G_3)/T, b_+=2(G_2-G_3)/T.

Dies ist das vollständige skalare Spektralupdate in dieser invarianten Familie; F-Kreuzblöcke verschwinden nur in den spektralen Spuren. Die Quelle und ihr alpha werden nicht eingefroren. Die notwendige Umgebung ist weiterhin enthalten.

## Hauptkontrast und Kegel

Alle Eingänge liegen in der bereits bewiesenen Klasse C: m>=5s/8, M<=5s/4, m>=2M² und M<=1/2. Dort ist g_alpha(y) streng steigend und streng konvex. Insbesondere r_+>0,b_+>0.

Zum Vergleich bei demselben s,r ersetze die unteren Lasten s(c±b) durch zweimal sc. Sei L_C=sum(1+y_i)^(-1), L_B=sum y_i²/(1+y_i). Es gilt L_B=L_C+4(s-1), denn sum y_i=4s. Konvexität erhöht L_C beim symmetrischen Aufspalten. Weil s<1, wächst L_B/L_C=1+4(s-1)/L_C und damit alpha gegenüber dem ausgeglichenen Zweiniveau-Fall alpha_0.

Für festes alpha ist [g_alpha(s(c+b))+g_alpha(s(c-b))]/2 >=g_alpha(sc). Ferner sinkt g_alpha(s(1+r))/g_alpha(sc) mit alpha (Vorzeichen der Ableitung proportional zu (sc)²-[s(1+r)]²<0). Der positive Hauptkontrast r_+ ist monoton im Verhältnis der oberen Last zur mittleren unteren Last. Daher

0<r_+<=r_+^(Zweiniveau)<=r/(1+r²)<=r,

wobei die letzte Zweiniveau-Abschätzung aus UNIFORM_LIFT_DERIVATION.md stammt, nicht neu numerisch angenommen wird.

## Quantitativer innerer Kontrast: rationales Zertifikat

Setze L=(1-q_+/q)/r, q_+=b_+/r_+. Die exakte Rekurrenz macht L rational in s,r,q; die scheinbaren Achsenfaktoren sind kürzbar. Geprüft wird L-1/2=P/Q. Der Audit erzeugt P und Q direkt durch exakte rationale Kürzung, setzt Q(0)>0 und liefert auf dem gesamten festgelegten Rechteck für beide Polynome eine positive Untergrenze.

Für p=sum c_ijk s^i r^j q^k sei M(p)=sum |c_ijk| (1/100)^i(1/4)^j(1/2)^k. Dann p>=2p(0)-M(p). Das Zertifikat lautet:

P_unten=892970632270589107/262144000000000000 >0,
M(P)=1204181367729410893/262144000000000000,
Q_unten=39189223413717739/5242880000000000 >0,
M(Q)=44696856586282261/5242880000000000.

Alle Zahlen sind rationale SymPy-Ergebnisse, keine Gitterabschätzungen. Damit L>=1/2 und 0<q_+<=q(1-r/2)<q. Zusätzlich s_+<=2M²<=25s²/8<=s/32. Zusammen mit r_+<=r ist der Bereich invariant für alle endlichen mathematischen Quellereignisse. Die Ordnung hält das untere Paar fest. Positivität verhindert ein endliches mathematisches Verschwinden der Last; numerische Rank-Cutoffs sind davon zu unterscheiden.

## Lyapunov-Summe und lokale Kernelkomponenten

V_+=q_+²r_+ <=(1-r/2)²V <=(1-r/2)V. Folglich

V-V_+>=b²/2,
sum(j=0..N-1)b_j²+2V_N<=2V_0,
sum(j>=N)b_j²<=2V_N.

Der exakte Quell-Schurfaktor h_j des unteren Paares erfüllt bereits bewiesen 0<h_j<=1 und 1-h_j<=32b_j²/35. Für d_N=product(j<N)h_j gilt deshalb nun für die volle positive Last

1-d_N<=(64/35)b_0²/r_0,
||K_S,N-K_S,0||_F<=(64/35)(b_0²/r_0)||O(K_S,0)||_F.

Die Reständerung nach N ist höchstens (64/35)V_N ||O(K_S,0)||_F. Die lokale Diagonale bleibt exakt konstant; beide transversalen Komponenten sind nur näherungsweise erhalten. Bei r_0=epsilon,b_0=epsilon³ ist die uniforme Schranke O(epsilon^5). Das gilt für alle endlichen Ereigniszahlen und den existierenden Grenzwert d_infty. Keine physikalische Zeit wurde eingeführt.

## Frische Evidenz und Reichweite

Vorab: LOWER_PAIR_LIFT_PROTOCOL.md. Exaktes rationales Zertifikat wie oben; vier positive-Last-Präfixe mit sechs Ereignissen bei 500 Dezimalstellen, ohne Randersetzung. Der Audit prüft Kegel, V-Dekrement, Summen-/Restschranke und Kohärenzprodukt. Die Restabschätzung stammt aus dem Beweis, nicht aus einem unendlich fortgesetzten Zahlenlauf. 500-stellige Auswertung ist keine gerichtete Intervallarithmetik; sehr kleine positive Lasten werden nur in der reduzierten skalaren Karte gerechnet.

Zusätzlich acht frische vollständige Original-Quellaufrufe und zwei komplexe unitäre Eichkontrollen; Kernel/Eich-Reste unter 1e-10 und normierte Lastreste unter 1e-8, exakte Werte in lower_pair_lift_results.json. Keine Original-Matrixtrajektorie unterhalb ihres numerischen Rangschwellwerts behauptet. CI dieses Codes separat in CI_VALIDATION.md.

Die Lücke der positiven-Last-Summierbarkeit ist damit für diese erklärte Familie geschlossen. Nicht geschlossen: quellenbasierte generische Auswahl/Isolierung eines solchen Trägers, Stabilität gegen zusätzliche obere Aufspaltung und allgemeine Formationsgewichte, räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom. Das frühere obere Verstärkungsresultat bleibt bestehen. Ein stabiler lokaler Kernelbestand ist weder eine Lorentz-Dynamik noch ein hergeleiteter Viererstrom. Nächste konkrete Abhängigkeit: prüfen, wie weit Auswahl und Gedächtnisschranke ohne die obere Entartung und die ausgeglichenen F-Blöcke tragen; Gegenbeispiele sind beizubehalten.
