# Geschlossene aktive Kernelreduktion und vollständige Rekonstruktion – Runde 43

## Konstruktives Ergebnis

Auf der BFG-Klasse Q_selection=I mit F,W auf P unterstützt genügt

Pi_act(Ξ)=(PKP,F,W,Y,P)

für das **vollständige nächste BFG-Ereignis**, einschließlich Seed und Terminalentscheidung. Nicht aktive K-Komplementblöcke und P-Kreuzblöcke sind dafür irrelevant. Der aktive Kernelblock selbst kann bei festgehaltenen Nicht-Kernel-Daten aus dem vollständigen K-Ausgang exakt rekonstruiert werden.

Damit ist die in Runde42 verlangte zusätzliche K-abhängige Information konkret bestimmt: den vollständigen aktiven Matrixblock behalten. Bei aktivem Rang2 besitzt er vier reelle Parameter. Dies ist eine quellenbasierte mathematische Reduktion, keine physikalische Viererimpuls- oder Raumzeitableitung.

Vorab: PROTOCOL.md Runde43. Quelle und unveränderte Regeln: SOURCE_MANIFEST.json, vollständiges Dynamic-Order-Manuskript Parts I/II. Standardmathematik: Kompression, Spektralkalkül und vollständig positive lineare Operatorabbildung. Keine zusätzliche physikalische Dynamik.

## 1. Quellklasse und genaue Grenze

Annahmen: P ist der aktuelle orthogonale aktive Projektor; 0<Y<I, positive duale Lasten, F=PFP und W=PWP, tr W=1. Dann Q_selection=I, T_selection=P und P_sel=P.

Das Manuskript zeigt, dass nach einem vollständigen nichtterminalen Ereignis 0<Y_+<I gilt und F_+,W_+ auf P_+ unterstützt sind. Diese Klasse ist deshalb für die weitere **nichtterminale** Fortsetzung relevant. Terminalität bleibt Bestandteil des Updates.

Nicht behauptet wird dieselbe Reduktion für einen beliebigen Anfangszustand mit Q_selection!=I. Dort kann P_sel gegenüber P gedreht sein; die jetzige Beweisbedingung P U_t=U_t wäre mit dem ursprünglichen P nicht automatisch erfüllt. Vollständiges Y wird behalten: keine autonome Dynamik von PKP allein behauptet.

## 2. Exakte Faser-Geschlossenheit

Die Analyse A=[sqrt(alpha) P_G C; sqrt(beta) P_G B] hat beide Zeilenbilder in RanP, weil P_G in diesen Raum abbildet. In jeder zulässigen dünnen SVD A=U Sigma V† haben daher die Blöcke U_C,U_B Bild in P:

P U_t=U_t.

Der Kernelupdate lautet

K_+=sum_t U_t† K U_t
    =sum_t U_t† (PKP) U_t.

Alle vorangehenden Schritte – Selektion, Lasten, alpha/beta, Analyse/SVD, Y_+, R4-Witness und vor dem Seed transportierte Formation – hängen nur von Y,F,W,P ab. Der Seed und seine Terminalentscheidung hängen dann von dem so bestimmten K_+ und S4 ab. Gleiche Pi_act-Daten erzeugen folglich denselben vollständigen Nachfolger bis zur zulässigen SVD-Eichung bzw. denselben Terminalstatus.

Das ist das Faser-Kriterium II89 für diese klar typisierte Klasse. Im Gegensatz zur skalaren Reduktion aus Runde42 wird keine im Ereignis wirksame aktive K-Richtung entfernt. Eine Wiederholung der Argumentation ist auf jedem folgenden nichtterminalen Ereignis derselben Klasse zulässig.

Dies begründet keine erhaltene ambiente Spur: entfernte K-Komplementdaten können eine beliebige ambiente Spur tragen, obwohl sie den Nachfolger nicht beeinflussen. Eine physikalische Energieidentifikation muss diese Differenz ausdrücklich behandeln.

## 3. Explizite Rekonstruktion des aktiven Kernelblocks

Wähle eine Isometrie J:C^r -> RanP, r=rank P, und schreibe

k=J† K J, Yp=J†YJ, Hp=I_r+Yp.

Für Q_selection=I gilt exakt
P_G=J Hp^(-1) J†(I+Y),
P_G C=J Hp^(-1) J†,
P_G B=J Hp^(-1) J†Y.

Deshalb sind die auf die Eingangsfläche beschränkten Analyseblöcke

A_C J=sqrt(alpha) J Hp^(-1),
A_B J=sqrt(beta) J Hp^(-1) Yp.

Aus der vollständigen Kernel-Ausgabe und der Analysegeometrie bilde

Z=J† V Sigma K_+ Sigma V† J.

Da A† diag(K,K) A=V Sigma K_+ Sigma V†, folgt

Hp Z Hp=alpha k+beta Yp k Yp.

Diagonalisiere Yp=S diag(mu_i) S†. Die explizite inverse Formel lautet

(S†kS)_ij = (S† Hp Z Hp S)_ij / (alpha+beta mu_i mu_j).

Alle mu_i>0 und alpha,beta>0, daher sind sämtliche Nenner strikt positiv. Die Abbildung k -> vollständiges K_+ ist also injektiv; keine aktive Hermitesche K-Richtung geht im vollständigen Kernel-Ausgang verloren.

Diese Rekonstruktion benutzt den **vollständigen K_+**, Sigma,V und die behaltene Geometrie. Sie ist keine Rekonstruktion allein aus tr K_+, einem Energieablesewert oder nur P_+K_+P_+. Positivität der Nenner ist zudem keine uniforme numerische Konditionsschranke: alpha und relevante Spektralskalen können sich entlang einer Familie verändern.

## 4. Vier Kernelparameter und ihre Grenzen

Bei festem Y,F,W,P ist

Phi(k)=sum_t (J†U_t)† k (J†U_t)

eine vollständig positive lineare Abbildung von Herm(C^r) nach Herm(C^m). Sie ist **unital**:
Phi(I_r)=sum U_t† P U_t=I_m.
Die gesamte Seed-/Formationsdynamik ist dadurch nicht als linearer oder vollständig positiver Kanal behauptet.

Aus dem Rekonstruktionsbeweis folgt reeller Rang r². Jede lineare Beobachtung des aktiven Eingangs-Kernels, die den **vollständigen K-Ausgang** bei festem Nicht-Kernel-Zustand eindeutig vorhersagen soll, muss daher Rang mindestens r² haben. Für r=2 genügen und sind hierfür vier unabhängige reelle Kernelkoordinaten erforderlich; bei fest vorgegebener Spur ist die entsprechende affine Dimension drei.

Der Quellträger wird damit nicht automatisch zweidimensional ausgewählt: r wird durch P bestimmt, nicht durch das gewünschte Lorentz-Ergebnis. Aus den beiden Analysekanälen folgt r<=m<=min(n,2r); bei r=2 kann die Ausgangsdimension2,3 oder4 sein. Seed und aktive Projektion verändern anschließend den aktiven Rang. Es ist deshalb noch keine autonom geschlossene Theorie eines dauerhaften Herm(C²)-Raumzeitfeldes gewonnen.

Auch Unitalität ist keine Spur-/Energieerhaltung: Phi(I_r)=I_m hat bei m!=r verschiedene Spuren. Die in früheren Runden gezeigten Transportreste und Nullkegeldefekte werden durch Injektivität nicht aufgehoben.

## 5. Frische Originalkontrollen

Drei vorab festgelegte vollständige Aufrufe, alle nichtterminal:

1. Rationale n=3/r=2-Geometrie aus Runde40, K=-diag(1,2,3).
2. Dieselbe Geometrie mit K+H, H=[[0,0,.2],[0,0,.3i],[.2,-.3i,.4]]. Hier PHP=0, ||H||_F=0.6480740698407861; die vollen Kernel sind deutlich verschieden.
3. Ein komplexer n=4/r=2-Zustand mit Zufallsseed20261026, positivem Y-Spektrum(.15,.3,.5,.7), unterstützt positivem F und negativem K.

Maximale volle Nachfolgerdifferenz der beiden ersten Fälle:6.982695313449726e-17. Die Rekonstruktionsreste sind etwa3.97e-15 für n=3 und3.22e-14 für n=4; Unitalitätsreste<1.14e-15, Stützreste<5.1e-15. Der reelle Abbildungsrang ist in allen Fällen4. Die Ausgangsdimensionen sind3,3,4, die aktiven Ausgangsränge jeweils3.

Vollständige Kontrolle und Ausgabe: [ACTIVE_KERNEL_CHECKS.md](ACTIVE_KERNEL_CHECKS.md). Die Beweise liefern die allgemeine Aussage; die Zahlen sind proportionale Implementierungskontrollen. Keine neuen Audit-, Workflow- oder Originalcodedateien; kein neuer Remote-CI-Pass behauptet. Letzter Remote-geprüfter Code bleibt in CI_VALIDATION.md separat.

## 6. Nächste Abhängigkeit

Die konstruktive Antwort auf die zuletzt demonstrierte skalare Faserlücke lautet: aktives K vollständig behalten. Offen ist nun die quellenbasierte Auswahl eines lokalen Rang-zwei-Trägers samt Fortsetzung über Rangwechsel, ohne die entscheidenden K-Richtungen wieder zu verwerfen. Der hier bewiesene Rang4 betrifft nur den Kernelanteil bei festgehaltener voller Geometrie und Formation/Witness.

Ein physikalischer Fortschritt muss zusätzlich räumliche Relationen, Uhr, Energie-/Impulsablesung und ihre Transformations-/Generatorrolle liefern. Keine dieser Brücken folgt allein daraus, dass ein aktiver Rang-zwei-Kernel vier reelle Komponenten besitzt. Die Ergebnisse geben eine geschlossene mathematische Kontrollbeschreibung, keine vollständige Energie-Impuls- oder Einstein-Herleitung.
