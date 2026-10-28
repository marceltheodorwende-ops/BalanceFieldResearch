# Unteres Paar bei negativer Formation: alternative Lyapunov-Schranke

## Quelle und Bereich

Unter erklärten BFG-Annahmen abgeleitet mit Standardmathematik, derselbe gepinnte volle Persistenzsektor und unveränderte Quelle aus MANDATE.de.md. Familie Y=s(I+rA+bB), A=diag(1,1,-1,-1), B=diag(0,0,1,-1), F>0 mit Diagonalblöcken (1+delta)I und (1-delta)I sowie verträglichen komplexen Kreuzblöcken. Obere Lastentartung bleibt Voraussetzung. Neue Richtung -1/8<=delta<=0; 0<s<=1/100,0<r<=1/4,0<q=b/r<=1/2. s=tr(Y)/4 ist ungewichtete Spektralskala. Der frühere Gegenzeuge gegen r-Monotonie bleibt gültig; r darf jetzt wachsen.

## Kegel ohne r-Monotonie

Die exakte reduzierte positive-Last-Rekurrenz ist die aus LOWER_PAIR_FORMATION_DERIVATION.md, mit signed delta. Um den Hauptkontrast zu begrenzen, ersetze die beiden unteren Lasten s(1-r±b) durch zweimal s(1-r). Bei festem s,r,delta bleibt die formationgewichtete Lastsumme 4s(1+delta r) erhalten. Die Identität L_B=L_C+4s(1+delta r)-4 und Konvexität von 1/(1+y) zeigen: Aufspalten erhöht L_C und alpha, da 4s(1+delta r)-4<0. Zusätzlich erhöht Konvexität von g_alpha den unteren Lastmittelwert. Wie zuvor sinkt das obere/untere g-Verhältnis mit alpha. Deshalb r_+<=R_s(r,delta), wobei R_s die volle Zweiniveau-Quelle ist.

Setze a=-delta in [0,1/8]. Für die Zweiniveau-Quelle gilt

rho_2=[1+r²-2ar+s(1-r²)(1-ar)]/[1+s+asr],
g_±=[rho_2+(1±r)²]/[1+s(1±r)]²,
R_s=(g_+-g_-)/(g_++g_-), B_a(r)=r/(1-ar+r²).

Der Audit kürzt E=(B_a-R_s)/(sr)=P/Q exakt rational. Auf s<=1/100,r<=1/4,a<=1/8 erhält die absolute Koeffizientenmasse mit Q(0)>0:

P>=286991699/163840000>0, M(P)=368368301/163840000,
Q>=201827867821/262144000000>0, M(Q)=322460132179/262144000000.

Damit R_s<=B_a. Die Ableitung B_a'=(1-r²)/(1-ar+r²)²>0 und
B_a(1/4)<=1/4 (weil a<=1/8<1/4) ergeben 0<r_+<=1/4, ohne r_+<=r zu verlangen.

Das rho-unabhängige Zertifikat aus Runde 26 gilt weiterhin, da rho als positives Mittel der z_i² in derselben Hülle liegt: 0<q_+<=q(1-r/2). s_+<=25s²/8<=s/32 gilt ebenfalls. Somit ist der Kegel bei jedem endlichen exakten Quellereignis invariant. Alle Eingänge liegen in der bekannten geordneten Klasse C; das untere Paar bleibt dieselbe Spektralfläche. F und delta bleiben im ausgerichteten vollen Persistenzsektor erhalten.

## Andere Lyapunov-Funktion, schwächere uniforme Schranke

Wähle U=q². Aus q_+<=q(1-r/2) folgt

U-U_+ >= (r-r²/4)q² >= (r/2)q² >=2r²q²=2b²,

wobei die letzte Ungleichung nur r<=1/4 benötigt. Teleskopieren liefert für jedes N

sum(j<N)b_j²+U_N/2<=U_0/2,
sum(j>=N)b_j²<=q_N²/2.

Der bereits exakt hergeleitete Schurfaktor erfüllt 1-h_j<=32b_j²/35. Für d_N=product(j<N)h_j und lokale Offdiagonale O(K_S,0) folgt deshalb

1-d_N<=16q_0²/35,
||K_S,N-K_S,0||_F<=(16/35)q_0² ||O(K_S,0)||_F.

Die Reständerung ab N ist höchstens (16/35)q_N² ||O(K_S,0)||_F. Zwei Diagonalkomponenten bleiben exakt, zwei transversale näherungsweise erhalten. Die Aussagen gelten für alle endlichen Ereigniszahlen und den existierenden Grenzwert des positiven Kohärenzprodukts. Die neue Schranke ist schwächer als die alte (64/35)r_0 q_0² für den nichtnegativen Bereich, dafür braucht sie keine Abnahme von r. Bei r_0=epsilon,b_0=epsilon³ liefert sie O(epsilon^4) statt der dort engeren O(epsilon^5)-Schranke. Die frühere stärkere Aussage wird nicht ersetzt oder als negativ widerlegt.

Zusammen mit Runde 26 besitzt damit die erklärte Familie für delta in [-1/8,1/2] eine uniforme lokale Gedächtnisschranke, mit der engeren Variante für delta>=0. Kein Anspruch für delta<-1/8 oder beliebige Formationsblöcke.

## Frische Evidenz und erhaltene Grenzen

Vorabprotokoll LOWER_PAIR_SIGNED_PROTOCOL.md vor Auswertung gespeichert. Neues exakt rationales Vergleichszertifikat; vier volle positive-s-Präfixe à sechs Ereignisse bei 500 Dezimalstellen, keine Randersetzung. In beiden kleinen-r-Präfixen wächst r bei mindestens einem Ereignis. Acht frische vollständige Original-Quellaufrufe einschließlich zweier komplexer Eichkontrollen bestanden; Kernelrest 7.038446774289103e-16, Eichrest 1.938199254140863e-15, normierter Lastrest 2.849592454037321e-13, unter vorab festgelegten 1e-10 bzw. 1e-8. Ein Originalfall r=.05,delta=-.125,q=.1,s=.001 liefert r_+=.05008176369701517>r bei q_+=.09502137347590724<q. Das alte Monotonieproblem verschwindet also nicht durch die positive Last; die neue Funktion umgeht es nachweisbar.

Präfixe mit extrem kleinen Lasten sind reduzierte hochpräzise skalare Rechnungen, keine aufgelösten Original-Matrixtrajektorien unter deren Rank-Cutoff. 500 Dezimalstellen sind keine gerichtete Intervallarithmetik. Die gesamte Restreihe ist analytisch begrenzt, nicht numerisch extrapoliert. CI und exakter geprüfter Commit separat in CI_VALIDATION.md.

Die obere Zweifachentartung und die Form der F-Blöcke bleiben zusätzliche Familienannahmen, keine generisch ausgewählten BFG-Zustände. Nächster Schritt: Einfluss einer endlichen zusätzlichen oberen Lastaufspaltung auf unteres Paar und Wahl des Trägers. Räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen; die Kernelabschätzung hat diese physikalischen Bedeutungen nicht abgeleitet.
