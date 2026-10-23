# Endliche obere Aufspaltung: gestoppte Kontrolle des unteren Paares

## BFG-Annahmen und Geltungsbereich

Aus derselben gepinnten vollständigen positiven Persistenzquelle, unverändertes Dynamic-Order-Manuskript und Originalupdate. Standardmathematik unter den erklärten Annahmen: n=4, Y=sZ mit

Z=diag(1+r+a,1+r-a,1-r+b,1-r-b), p=a/r, q=b/r,
0<s<=1/100, 0<r<=1/4, 0<=p<=1/2, 0<q<=1/2.

s=tr(Y)/4 ist ungewichtete Spektralskala. F>0 darf für das lokale Zertifikat beliebige komplexe Einträge haben. Im gemeinsamen Eigenrahmen treten seine positiven Diagonaleinträge nur als Gewichte in rho auf. Simultane unitäre Konjugation ist zulässig. Die obere Zweifachentartung wird jetzt tatsächlich gelockert, aber nur eine bis zum Bereichsaustritt gestoppte Kontrolle bewiesen. Keine Invarianz von p<=1/2 oder r<=1/4 angenommen.

## Volle Quelle und lastabhängiger Gewichtsparameter

Für z_i wie oben und w_i=F_ii>0 gilt

rho=sum_i w_i z_i²/(1+s z_i) / sum_i w_i/(1+s z_i),
G_i=(rho+z_i²)/[(1+s z_i)²(1+s²rho)], T=sum_i G_i,
s_+=s²T/4,
r_+=(G_0+G_1-G_2-G_3)/T,
a_+=2(G_0-G_1)/T, b_+=2(G_2-G_3)/T.

Das ist das vollständige Spektralupdate mit dynamischem alpha=s²rho/(1+s²rho). Keine Gewichte werden eingefroren. Wegen 5/8<=z_i<=11/8 ist rho in [25/64,121/64], unabhängig von der Wahl des positiven F. Alle Eingänge liegen in Klasse C, denn m>=5s/8>=2(11s/8)² und M<=11s/8<=1/2. Strenge Monotonie von g erhält die Eigenordnung. Die beiden unteren Moden sind durch den positiven Abstand 2r-a-b>=r von den oberen getrennt.

## Rationale quantitative Kontraktion der unteren relativen Breite

Definiere L=(1-q_+/q)/r, q_+=b_+/r_+. Rationale Kürzung mit unabhängigem rho=1+t ergibt L-1/2=P/Q. Die absolute Koeffizientenmasse auf s<=1/100,r<=1/4,p<=1/2,q<=1/2,|t|<=1 liefert, mit Q(0)>0:

P>=22552733649640027/8192000000000000>0,
M(P)=42983266350359973/8192000000000000,
Q>=30013884931124821/4096000000000000>0,
M(Q)=35522115068875179/4096000000000000.

Die größere rho-Hülle [0,2] umfasst alle tatsächlichen positiven Gewichte. Für ein Polynom ist die verwendete Untergrenze 2p(0)-M(p), eine exakte rationale Rechteckabschätzung ohne Stichprobenannahme. Daraus folgt für jeden Schritt mit Eingang in diesem Bereich

0<q_+<=q(1-r/2).

Dies ist ein lokales Quellergebnis auch bei beliebigem F>0, kein allgemeines invariantes F/Y-Familientheorem.

## Gestoppte Lyapunov-Summe und Kernel-Gedächtnis

Sei tau der erste Index, dessen Ausgangszustand den geprüften Bereich verlässt. Dann liegen Eingänge j<tau darin. Mit U=q² und r<=1/4 gilt an allen diesen Eingängen

U-U_+ >=(r-r²/4)q² >=(r/2)q² >=2b².

Für jede endliche N<=tau (auch einschließlich des Austrittsereignisses) folgt deshalb

sum(j<N)b_j²+q_N²/2<=q_0²/2.

Der untere Paar-Schurfaktor hat unverändert die exakte Form
h=(rho+(1-r)²-b²)/sqrt([rho+(1-r)²-b²]²+4rho b²).
Aus (1-r)²-b²>=35/64 folgt 1-h<=32b²/35. Damit gilt bis einschließlich N=tau

1-product(j<N)h_j<=16q_0²/35,
||K_S,N-K_S,0||_F <=(16/35)q_0² ||O(K_S,0)||_F.

Für einen späteren Abschnitt, dessen Eingänge weiterhin im Bereich liegen, gilt dieselbe Summenabschätzung mit q_N als Ausgangswert. Nach einem Austritt ist dies keine garantierte Restschranke für die gesamte Zukunft. Nur falls die gesamte Trajektorie im Bereich bleibt, würde der Beweis dieselbe allzeitliche Grenze liefern; dies wurde hier ausdrücklich nicht bewiesen.

## Randrekurrenz und exakter positiver Austritt

Bei F=I und s=0 sei mu=1+r²+(a²+b²)/2. Exakt:

r_+=(r+(a²-b²)/4)/mu,
a_+=(1+r)a/mu, b_+=(1-r)b/mu,
p_+/p=(1+r)/[1+r(p²-q²)/4],
q_+/q=(1-r)/[1+r(p²-q²)/4].

Im geprüften Bereich wächst p für p>0, während q fällt. Die innere obere Breite und das untere Gedächtnis müssen daher getrennt beurteilt werden. Dies sind Randidentitäten, kein Originalupdate bei Y=0.

Der Audit prüft zusätzlich exakt rational an der vollen positiven Quelle: r=1/10,p=1/2,q=1/10,s=1/1000,F=I ergibt p_+>1/2; der vollständige rationale Wert steht im JSON. Näherungswert p_+=.5466189288623009. Damit ist der gewählte Bereich auch bei positiver Last tatsächlich nicht invariant. Dies widerlegt nicht jede spätere Kontrolle des unteren Paares und ist kein allgemeines BFG-No-Go.

## Frische Evidenz und Grenze

TWO_SIDED_PAIR_PROTOCOL.md wurde vor Auswertung auf GitHub gespeichert. Rationale Quelle, unabhängiges rho-Zertifikat, Randidentitäten und exakter positiver Austrittszeuge geprüft. Vier 500-stellige positive-Last-Präfixe laufen höchstens sechs Ereignisse und stoppen sofort nach dem ersten Austritt. Beide p_0=.5-Präfixe verlassen den Bereich bereits nach einem Ereignis; beide p_0=.1-Präfixe bleiben für sechs geprüfte Ereignisse darin. Kein nicht geprüfter Zukunftsverlauf wird angehängt.

Zehn frische Original-Quellaufrufe (acht r,p,q-Fälle, zwei komplexe Eichkontrollen) verwenden F mit Identitäts-Diagonalblöcken und komplexen Kreuzblöcken. Kernelrest <4.1e-15, Eichrest <3.5e-15, normierter Lastrest <3.5e-13; vorab Schwellen 1e-10 bzw. 1e-8. Das allgemeinere F-Ergebnis beruht auf dem exakten rho-Zertifikat, nicht auf angeblich ausgeführten beliebigen F-Stichproben. Hochpräzise skalare Präfixe unter dem Original-Rangcutoff sind keine aufgelösten Original-Matrixtrajektorien; 500 Stellen sind keine gerichtete Intervallarithmetik. CI separat in CI_VALIDATION.md.

Nächste Abhängigkeit: untere Kontrolle nach dem oberen Bereichsaustritt, gegebenenfalls mit spektral-geometrischer statt blockrelativer Schranke. Auswahl eines lokalen Zwei-Moden-Trägers ist damit noch nicht allgemein aus der Quelle bestimmt. Räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen. Näherungsweise lokale Kernelkomponenten sind keine vier physikalisch identifizierten Erhaltungsgrößen.
