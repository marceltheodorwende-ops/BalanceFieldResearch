# Unteres Paar bei ungleichen Formationsgewichten

## Quelle und erklärte Erweiterung

Unter den genannten BFG-Annahmen abgeleitet, Standardmathematik: dieselbe gepinnte vollständige positive Persistenzquelle wie MANDATE.de.md, keine neue Dynamik. Y=s[I+rA+bB], A=diag(1,1,-1,-1), B=diag(0,0,1,-1). Obere Lastentartung bleibt Voraussetzung. s=tr(Y)/4 ist hier die ungewichtete Spektralskala, nicht die Formationsmittel-Last. F>0 hat im gemeinsamen Eigenrahmen Diagonalblöcke (1+delta)I_2 und (1-delta)I_2, mit zulässigen komplexen Kreuzblöcken. Diese bleiben in spektralen Spuren unsichtbar; der volle Kernelkanal und W werden mitgeführt. 0<=delta<=1/2, 0<s<=1/100,0<r<=1/4,0<q=b/r<=1/2.

Die Voraussetzung exakt gleicher Formationsgewichte beider Blöcke wird einseitig gelockert. Dies ist keine Aussage für beliebiges F, keine Auswahl der Familie durch die Quelle und keine Robustheit gegen obere Lastaufspaltung.

## Exakte Gewichtsabhängigkeit

Für z=(1+r,1+r,1-r+b,1-r-b), w=(1+delta,1+delta,1-delta,1-delta) gilt

rho=sum_i w_i z_i²/(1+s z_i) / sum_i w_i/(1+s z_i),
G_i=(rho+z_i²)/[(1+s z_i)²(1+s²rho)], T=2G_0+G_2+G_3,
s_+=s²T/4, r_+=(2G_0-G_2-G_3)/T, b_+=2(G_2-G_3)/T.

Da alle Gewichte positiv sind, ist rho ein gewichtetes Mittel der z_i². Im festgelegten Kegel liegt rho in [25/64,25/16]. Der folgende innere Kontraktionsbeweis braucht keine feinere Kenntnis von F.

## Exaktes rho-unabhängiges Rechteckzertifikat

Setze q_+=b_+/r_+ und L=(1-q_+/q)/r. Wie in Runde 25, jetzt aber mit unabhängigem rho=1+t, wird L-1/2=P/Q rational gekürzt. Auf s<=1/100,r<=1/4,q<=1/2,|t|<=5/8 zertifiziert die absolute Koeffizientenmasse M(p)=sum |c| (1/100)^i(1/4)^j(1/2)^k(5/8)^l:

P>=2P(0)-M(P)=541665266387/163840000000 >0,
M(P)=769054733613/163840000000,
Q>=2Q(0)-M(Q)=3119687164519/409600000000 >0,
M(Q)=3433912835481/409600000000.

Die größere rho-Hülle [3/8,13/8] enthält [25/64,25/16]. Das ist eine symbolische rationale Ungleichung über das gesamte Rechteck, keine Stichprobe. Insbesondere q_+<=q(1-r/2). Positives q_+ und Ordnung folgen aus der bekannten Klasse C. Das Zertifikat für den inneren Kontrast ist sogar von der Blockgewichtsbeschränkung unabhängig, solange der Lastkegel und Positivität vorliegen. Die weiteren Kegel-/V-Aussagen unten benötigen die einseitige Blockannahme.

## Hauptkontrast bei einseitiger Formation

Bei festem Y steigt alpha mit delta. Schreibe L_B/L_C=[(1+delta)A+(1-delta)B]/[(1+delta)C+(1-delta)D], wobei A/C=y_upper² und B/D das positive gewichtete Mittel der beiden unteren y² ist. Da y_upper>y_lower, gilt AD-BC>0; die Ableitung nach delta ist 2(AD-BC)/[(1+delta)C+(1-delta)D]²>0. Auch alpha=(L_B/L_C)/(1+L_B/L_C) steigt.

Für beliebige untere y_i<y_upper sinkt g_alpha(y_upper)/g_alpha(y_i) mit alpha. Daher steigt das Verhältnis der mittleren unteren zur oberen Folgelast und r_+ sinkt mit delta. Aus Runde 25 folgt so

0<r_+(delta)<=r_+(0)<=r/(1+r²)<=r.

Außerdem s_+<=25s²/8<=s/32. Damit bleibt der Kegel invariant. Formation F und somit delta bleiben im ausgerichteten vollen Persistenzsektor unverändert.

Mit V=b²/r=q²r folgt wie zuvor V_+<=q²(1-r/2)²r<=(1-r/2)V. Also

V-V_+>=b²/2,
sum(j<N)b_j²+2V_N<=2V_0,
sum(j>=N)b_j²<=2V_N.

Weil der exakte lokale Schurfaktor unabhängig von dieser Gewichtsverteilung 1-h_j<=32b_j²/35 erfüllt, bleibt die volle lokale Kerneländerung für alle Ereigniszahlen beschränkt:

||K_S,N-K_S,0||_F <= (64/35)(b_0²/r_0)||O(K_S,0)||_F.

Die obere Last bleibt zweifach entartet, das untere Paar in derselben geordneten Spektralfläche. Zwei diagonale Komponenten sind exakt konstant, die beiden transversalen teilen das Kohärenzprodukt. Es ist weiterhin keine exakte Erhaltung aller vier Komponenten bei b>0.

## Negative Richtung: beibehaltene Grenze

Für signed delta in (-1,1) folgt am relativen Rand s=0 exakt

mu=1+r²+2delta r+(1-delta)b²/2,
D=1+r²+delta r+(2-delta)b²/4,
r_+=(r-b²/4)/D, b_+=(1-r)b/D.

Der Quotient q_+/q=(1-r)/(1-q²r/4) ist dort unabhängig von delta. Der Hauptkontrast muss aber nicht fallen: Das vorab erklärte Beispiel r=1/20,q=1/10,b=1/200,delta=-1/2 ergibt r_+=15998/312805>1/20. Damit ist die pauschale Fortsetzung von r_+<=r auf negative Gewichtsverschiebung widerlegt. Dies widerlegt weder die Summierbarkeit selbst noch BFG. Eine andere Lyapunov-Funktion oder ein größerer invarianten Bereich kann diese Richtung eventuell behandeln; hier bleibt sie offen. Die Grenzkarte ist nicht als ausgeführtes Original-Update bei Y=0 gemeint.

## Evidenz und nächste Abhängigkeit

LOWER_PAIR_FORMATION_PROTOCOL.md wurde vor Auswertung publiziert. Exaktes Rechteckzertifikat und signed Randidentitäten; sechs neue positive-Last-Präfixe von je sechs Ereignissen bei 500 Dezimalstellen, einschließlich delta=0 als Vergleich zum gelockerten Ansatz, ohne Randersetzung. Analytisch eingeschlossene Restreihe, keine unendliche numerische Fortsetzung oder gerichtete Intervallarithmetik behauptet.

14 frische Original-Quellaufrufe (zwölf Fälle, zwei komplexe unitäre Eichkontrollen) bestanden: Kernelrest 2.1889543413787788e-15, Eichrest 2.9945126497314727e-15, normierter Lastrest 2.308039498608475e-13. Schwellen vorab 1e-10 bzw. 1e-8. Hochpräzise skalare Lasten unter dem Original-Rangcutoff sind keine aufgelösten Original-Matrixtrajektorien. CI separat in CI_VALIDATION.md.

Nächster konkreter Schritt: untere Auswahl/Gedächtnis bei zusätzlicher oberer Lastaufspaltung oder allgemeinerer Formation; die negative Richtung benötigt einen anderen Hauptkontrastvergleich. Räumliche Transportstruktur, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen. Diese lokale Kernelabschätzung liefert dafür noch keine Einheiten, Translationen oder physikalische Wirkung.
