# Stabilität und Entartungsgrenze des spektralen Zwei-Moden-Trägers

## Quelle, Kandidat und Einordnung

Unter erklärten BFG-Annahmen abgeleitet; der Störungssatz ist Standardmathematik für Hermitesche Matrizen, angewandt auf dieselbe gepinnte vollständige positive BFG-Quelle aus MANDATE.de.md. Kandidat P_2(Y) ist der orthogonale Projektor auf die beiden kleinsten Lastmoden. Er ist durch Y kovariant bestimmt, sofern die äußere Lücke g=lambda_3-lambda_2>0 ist. Eine Entartung der beiden inneren Eigenwerte stört den Rang-zwei-Unterraum nicht; kritisch ist die Grenze zwischen zweitem und drittem Modus.

Im bereits behandelten geordneten C-Persistenzsektor erhält die streng steigende Spektralabbildung die ausgewählte Fläche exakt. Die Frage dieser Runde ist ihre Empfindlichkeit gegenüber benachbarten Zuständen und eine Fortsetzung bis zur entarteten Grenze. Die lokale Kernel-Gedächtnisschranke aus Runde 31 bleibt gültig und wird nicht durch einen Auswahlsatz über andere Zustände ersetzt.

## Elementarer lückenabhängiger Störungssatz

Sei Y Hermitesch und E=E^dagger mit epsilon=||E||_2<g/2. Setze P=P_2(Y), Q=P_2(Y+E). Das Min-Max-Prinzip gibt |lambda_i(Y+E)-lambda_i(Y)|<=epsilon. Damit bleibt die neue äußere Lücke >=g-2epsilon>0 und beide Projektoren haben Rang zwei.

Wähle orthonormale Eigenvektoren V der unteren zwei neuen Eigenwerte, B=V^dagger(Y+E)V. Für den Kreuzblock X=P^perp V und A=Y eingeschränkt auf P^perp folgt exakt die Sylvestergleichung

AX-XB=-P^perp E V.

Im Eigenrahmen von A und B sind alle Nenner A_i-B_j mindestens g-epsilon. Daher

||X||_F<=||P^perp E V||_F/(g-epsilon)<=sqrt(2)epsilon/(g-epsilon).

Für gleichrangige orthogonale Projektoren gilt ||P-Q||_F²=2||P^perp V||_F². Insgesamt

||P_2(Y+E)-P_2(Y)||_F<=2epsilon/(g-epsilon).

Dies ist eine explizite lokale Stabilitätsgarantie, keine angenommene physikalische Transportgleichung. Für relative Fehlerschranken epsilon/g->0 geht die Projektoränderung gegen null. Eine feste absolute Fehlergrenze liefert bei schrumpfender g keine entsprechende uniforme Kontrolle. Der Satz behauptet keine zusätzliche Dynamik der Störung E.

## Exakte lückenschließende Familie innerhalb C

Setze n=3, t>0 klein,
Y_t=diag(1/10,1/10+t,1/10+2t),
Ytilde_t=R Y_t R^dagger,
R=Rotation um theta=pi/12 in der Ebene der Moden 2,3.

F=I, W=K=I/3, volle positive Persistenz. Für 0<t<=.01 liegen beide Lasten in C. Die äußere Lücke ist g=t. Mit P=diag(1,1,0) ist Q=RPR^dagger und exakt

||Ytilde_t-Y_t||_2=t sin(theta)->0,
||Q-P||_F=sqrt(2)sin(theta)=(sqrt(3)-1)/2>0.

Die beiden nichttrivialen Störungseigenwerte sind ±t sin(theta), bewiesen aus Spur null, Determinante null und quadratischer Spur. Der relative Fehler sin(pi/12)<1/2 erfüllt sogar den Störungssatz; dessen rechte Seite bleibt konstant und widerspricht dem Beispiel nicht. Der absolute Lastfehler geht gegen null, der Projektorabstand bleibt ungefähr .3660254.

Beide vollen Zustandsfamilien nähern sich demselben isotropen Zustand Y=I/10,F=I,W=K=I/3. Deshalb besitzt dieser konkrete spektrale Selektor dort keine stetige Fortsetzung, die alle solchen Annäherungen erhält. Bei diesem vollständig isotropen Zustand müsste jeder aus dem gesamten Zustand unitär kovariant bestimmte Projektor mit allen U(3)-Transformationen kommutieren. Phasentransformationen erzwingen Diagonalform, Permutationen gleiche Diagonaleinträge: Er wäre ein skalares Vielfaches von I. Ein solcher orthogonaler Projektor hat Rang 0 oder 3, niemals 2. Dies ist eine präzise Grenze an symmetrischen Zuständen, keine Widerlegung von Selektoren mit zusätzlichen nichtisotropen BFG-Daten.

## Dieselbe Grenze unter einem vollständigen Quellereignis

Bei identischen isotropen F,W,K ist alpha für die beiden unitär verwandten Lasten gleich. Das vollständige ausgerichtete Update ist Y_+=g_alpha(Y), also Ytilde_+=R Y_+ R^dagger. In C bleibt P unverändert und Q=RPR^dagger. Mit g_+=lambda_3(Y_+)-lambda_2(Y_+) folgt daher exakt

||Ytilde_+-Y_+||_2=g_+ sin(theta),
||P_2(Ytilde_+)-P_2(Y_+)||_F=sqrt(2)sin(theta).

Ein kleiner werdender roher Lastfehler beweist somit keine zusammenrückenden Träger. Es wird hier keine Verstärkung des Projektorfehlers entlang einer einzelnen exakten Trajektorie behauptet; der Vergleich betrifft zwei Nachbarzustände. Eine numerische oder physikalische Störung müsste relativ zur aktuellen Lücke kontrolliert werden.

## Frische Evidenz

SELECTOR_STABILITY_PROTOCOL.md vor Auswertung auf GitHub gespeichert. Exakte trigonometisch-algebraische Familienidentitäten und der allgemeine Sylvester-/Min-Max-Beweis sind primär. Sechs unabhängige Hermitesche Störungskontrollen n=3,4 mit epsilon/g=.01,.1,.25 bestanden, Ungleichungsslack 1e-12. Diese allgemeinen Matrixkontrollen werden nicht als zusätzliche vollständige BFG-Quellläufe oder als Beweis allgemeiner C-Zugehörigkeit ausgegeben.

Acht frische Original-Quellaufrufe: t=.01,.005,.0025 für beide Familien, plus zwei komplexe simultane Eichkontrollen. Projektorrest 1.699878893145283e-14, Last-Kovarianzrest 2.9531731004193714e-17, Eichrest 4.572393766546984e-14, alle unter vorab 1e-10. Ausgehende Lücken .0014657891907771045,.0007023185402724487,.0003430961508672156 sind kleiner als die Eingänge; die Projektorabstände bleiben ungefähr .3660254. Es werden nur diese endlichen Originalereignisse behauptet, keine numerische Fortsetzung bis zur Entartung. CI separat in CI_VALIDATION.md.

## Folgerung für die offene Auswahl-/Transportfrage

Der untere Träger ist auf dem lückenseparierten Chart mathematisch kovariant und relativ zur Lücke stabil. Für eine Fortsetzung über lückenschließende oder Rang-/Auswahlereignisse braucht es eine begründete zusätzliche Auswahl aus tatsächlich nichtisotropen BFG-Daten oder eine ausdrücklich mengenwertige Behandlung. Die heutige Rechnung entscheidet nicht, welche Alternative die Quelle physikalisch auswählt. Ein lokal wählbarer Basisabgleich ist ebenfalls noch kein räumlicher Transport oder physikalischer Zusammenhang.

Nächste Abhängigkeit: prüfen, welche schon vorhandenen Witness-/Formationsdaten eine lückenschließende Trägerwahl bestimmen und ob diese Wahl mit der vollen Dynamik geschlossen bleibt. Globale universelle Rang-zwei-Auswahl am vollständig isotropen Zustand ist im kovarianten Einzelprojektor-Sinn ausgeschlossen. Physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen.
