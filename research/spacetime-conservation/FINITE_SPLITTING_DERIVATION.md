# Endliche zusätzliche Aufspaltung: nichtlineare relative Grenze

## Konkrete Familie und Geltungsbereich
[BFG-abgeleitete Randkarte und exakte Quellenmonotonie] Verwende n=4 mit

    A=diag(1,1,-1,-1),
    B_+=diag(1,-1,0,0), B_-=diag(0,0,1,-1),
    Z=I+rA+bB_sigma, Y=sZ.

F ist I plus eine kleine positive-erhaltende hermitesche Kreuzblockkopplung, sodass seine Diagonalblöcke I sind; simultane unitäre Basisänderungen sind erlaubt. Damit gilt <Z>_F=1 und s=<Y>_F. Die endliche Familie besitzt drei Lastwerte: eine gespaltene Zweiergruppe und einen gemeinsamen Wert im anderen Zweierblock. Es wird keine universelle Störungsklasse oder allgemeine physikalische Stabilität behauptet.

Setze q=b/r, r>0, b>0. q misst die innere Breite relativ zur Hauptaufspaltung, keine räumliche Entfernung. Die Grenzkarte s->0 ist die zuvor quellenabgeleitete R_F; die quantitative lange Austrittsaussage dieses Abschnitts betrifft zunächst diese Randkarte.

## Exakte nichtlineare Rekurrenzen
Aus mu=<Z²>_F=1+r²+b²/2 und R_F(Z)=(mu I+Z²)/(2mu) folgt ohne Linearisierung

    r_+=(r+sigma b²/4)/mu,
    b_+=(1+sigma r)b/mu,
    q_+/q=(1+sigma r)/(1+sigma q²r/4).

Für die obere Aufspaltung sigma=+1 gilt bei 0<q<2 und 0<r<1/4

    q_+>q,
    2-q_+=(2-q)(1-qr/2)/(1+q²r/4)>0.

Die relative Breite wächst, während die geordnete Dreiniveaustruktur vor einer etwaigen Grenzkollision erhalten bleibt.

Für die untere Aufspaltung sigma=-1 bildet

    0<r<=1/4, 0<q<=1/2

einen invarianten relativen Kontraktionsbereich: 0<r_+<r und

    q-q_+=qr(1-q²/4)/(1-q²r/4)>0.

Damit bleibt q_j<=q0 für alle Randschritte. Dies kontrolliert endliche relative innere Breiten, nicht bereits die Nähe jeder Komponente zu einer ungeänderten Vergleichstrajektorie.

## Nichtlinearer Austritt aus einer relativen Störungsumgebung
Starte im oberen Fall mit r0=epsilon<=1/10 und q0=epsilon², also b0=epsilon³. Definiere den ersten Austritt tau aus

    0<r<1/4, 0<q<1/2.

Beide möglichen Austrittsarten werden berücksichtigt; es wird nicht im Nachhinein nur eine behalten. Solange kein Austritt vorliegt, gilt q²/2<=1/8 und daher

    r_+>=r/[1+(9/8)r²].

Die rechte Vergleichsabbildung ist auf [0,1/4] steigend. Sei w0=epsilon und w_+=w/[1+(9/8)w²]. Für x=1/w² ergibt sich exakt
x_+-x=9/4+(81/64)w²<=14481/6400<5/2.
Induktion liefert somit

    r_j>=w_j>=epsilon/sqrt[1+(5/2)j epsilon²].

Für j epsilon²<=2 folgt r_j>=epsilon/sqrt(6). Ferner ist im selben Bereich

    q_+/q
      =1+r(1-q²/4)/(1+q²r/4)
      >=1+(12/13)r
      >=1+epsilon/3.

Für die letzte grobe Schranke genügt 1/sqrt(6)>2/5 und 24/65>1/3. Somit muss spätestens nach

    n_bound=ceil(log[(1/2)/q0]/log(1+epsilon/3))

ein Austritt eintreten, sofern n_bound<=2/epsilon². Andernfalls würde q_n>=q0(1+epsilon/3)^n die Definition des ersten Austritts verletzen. Die Bedingung gilt für alle hinreichend kleinen epsilon und für alle vier vorab gewählten Kontrollpräparationen. Insbesondere

    tau=O(epsilon^(-1) log(1/epsilon)),
    epsilon² tau ->0.

Dies ist ein **nichtlinearer Austritt endlicher Störungen aus einer relativen Umgebung**. Er wurde aus exakten Rekurrenzen und Vergleichsungleichungen bewiesen, nicht durch Extrapolation der vorherigen Tangentenverstärkung.

Eine relative Breite von 1/2 bedeutet nicht automatisch eine Abweichung von Ordnung eins im rohen Y: Auch r und s können klein bleiben. Der Befund betrifft die Robustheit der gewählten relativen Zwei-Niveau-/Langsamkoordinaten. Eine quantitative große physikalische Störung oder allgemeine BFG-Instabilität wird nicht behauptet.

## Exakte nichtlineare Richtung bei positiver Last
Für die vollständige positive-s-Quelle auf C ist die gemeinsame skalare Abbildung g_alpha strikt steigend und strikt konvex. Ihre endogene alpha hängt vom aktuellen Zustand ab; für die drei Lastwerte eines Ereignisses ist es dieselbe tatsächliche alpha. Das Argument friert keine Ereignisfolge oder Formationslast ein.

Im oberen Fall seien x1>x2>x3 die geordneten Lastwerte und
t=(x1-x2)/(x2-x3)=2q/(2-q).
Nach dem Ereignis

    t_+/t=
      [(g(x1)-g(x2))/(x1-x2)]
      /[(g(x2)-g(x3))/(x2-x3)] >1.

Da q=2t/(t+2) streng wächst, ist q_+>q. Im unteren Fall bezeichnet t das Verhältnis der unteren zur oberen Lücke. Die beiden Sekantensteigungen tauschen ihre Rollen, daher t_+/t<1 und q_+<q. Die Lastreihenfolge bleibt auf C erhalten; damit bleibt 0<q_+<2. Diese nichtlineare Richtung gilt für jedes endliche exakte positive-Last-Ereignis in der angegebenen Familie.

Die quantitative lange Austrittszeit der Randkarte wurde damit noch nicht uniform auf die gestörte positive-s-Quelle übertragen. Dafür fehlt eine entsprechende nichtlineare Fehler-/Vergleichskontrolle. Der frühere uniforme Satz innerhalb des ungestörten Zwei-Niveau-Sektors allein genügt dafür nicht.

## Frische Evidenz
[Vorabprotokoll](FINITE_SPLITTING_PROTOCOL.md), [Prüfcode](finite_splitting_audit.py), [Resultate](finite_splitting_results.json).

Symbolisch geprüft: beide vollständigen Randrekurrenzen, relative Quotienten und obere/untere Faktorisierungen. Die Austrittsabschätzung verwendet die exakten rationalen Vergleichskonstanten; Stichproben ersetzen den Satz nicht.

Für epsilon=1/10,1/20,1/40,1/80 und T=2 verlassen die oberen Präparationen den relativen q-Bereich nach 50,124,295,684 Randschritten, jeweils unter den bewiesenen oberen Schranken 120,321,806,1942. Bei keiner dieser Kontrollen trat zuerst der alternative r-Austritt auf; diese Möglichkeit bleibt im Satz erhalten. Die unteren Kontrollen blieben für 200,800,3200,12800 Randschritte im Kontraktionsbereich.

Sehr kleine untere q-Schätzwerte bis etwa 1.18e-47 stammen aus direkten skalaren Randrekurrenzen. Sie sind weder entsprechende Auflösung im Original-Matrixcode noch ein relatives Gleitkomma-Positivitätszertifikat; die exakte Positivität und Invarianz folgen aus der Formel.

Zusätzlich **18 vollständige Original-Quellaufrufe**: 16 komplex gedrehte n=4-Präparationen mit endlichen oberen/unteren Breiten und zwei unitäre Lastkontrollen. Die vollständigen Folgelasten wurden unabhängig rational aus allen vier Eingangs-Lastwerten und den echten Formationsgewichten berechnet. Größter Lastrest <1.4e-18, Last-Kovarianzrest <1.8e-18, normierter r/b-Rest <7.2e-13. Vorgegebene Grenzen 1e-10 beziehungsweise 1e-8 unverändert. Alle oberen q nahmen zu, alle unteren ab; die Reihenfolge blieb erhalten.

Keine Fälle verworfen oder Kriterien angepasst. Manuskripte, Grundcode, Lizenzen und empirische Ergebnisse unverändert. Lange Randfolgen, kurze Originalchecks und die noch offene uniforme lange Quellenkontrolle bleiben getrennt; CI separat ausgewiesen.

## Nächste Abhängigkeit
Die endliche obere Randempfindlichkeit und ein unterer relativer Kontraktionsbereich sind nun konstruktiv kontrolliert. Offen bleibt die quantitative nichtlineare positive-s-Übertragung sowie die BFG-interne Auswahl/Isolierung eines geeigneten lokalen Trägers. Der untere Bereich ist ein konkreter weiterer Ansatz, aber noch kein ausgewählter physikalischer Zwei-Moden-Raum. Physikalische Uhr, räumlicher Transportmaßstab, vollständiger Energie-Impuls-Strom, Wirkung und Einstein bleiben offen.
