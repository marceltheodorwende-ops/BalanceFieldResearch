# Gleiche Bestände und gleicher Seed schließen die Bilanz nicht – Runde 42

## Ergebnis und präziser Umfang

Es gibt zwei zulässige nichtterminale BFG-Zustände mit identischen vollen Y,F,W,P, identischer ambienter Kernelspur tr K=-6, identischem aktivem Bestand tr(PK)=-4 und identischen Rangdaten. Sogar der Betrag des anstehenden eindeutigen Seeds ist in beiden Fällen exakt2. Trotzdem unterscheiden sich ihre aktiven Ausgangsbestände strikt.

Damit ist die Reduktion auf diese Daten nach dem Faser-Kriterium II89 nicht geschlossen. Seedbetrag, Ränge und die bereits behaltenen Nicht-Kernel-Felder ergänzen die skalare Bilanz nicht ausreichend. Eine Zusatzgröße, die ausschließlich aus diesen Nicht-Kernel-Feldern als Zustandsfunktion gebildet wird, kann den aktiven Bestandsrest ebenfalls nicht allgemein kompensieren. Das ist kein Ausschluss zusätzlicher K-abhängiger Matrixdaten oder jeder möglichen physikalischen Energiebrücke.

Vorabprotokoll PROTOCOL.md Runde42; Quellbindung und gemeinsame Formationseinheit unverändert. Die Zustandskonstruktion ist ein mathematischer Gegenzeugentest, kein vorgeschlagenes physikalisches Energiegesetz.

## 1. Dieselbe rationale Quellgeometrie

Verwende die zulässige n=3-Geometrie aus Runde40:

P=diag(1,1,0), F=diag(1,21/50,0), W=P/2,
Y=[[1/4,0,1/10],[0,1/2,1/10],[1/10,1/10,1/2]].

Dort wurden positive Lasten alpha=1/10, voller Analyse-Rang m=3 und ein eindimensionales Seedkomplement exakt gezeigt. Die tatsächliche Analyse A=A0/sqrt(10), ihre Gram-Matrix H=A0†A0 und SVD-Isometrie U hängen nicht von K ab.

Definiere B4=sum U_t S4 U_t†, X=B4-P sowie den gesamten Kernelrückzug

D=sum U_t U_t†
 =sum A0_t H^(-1) A0_t†
 =[[4369/2497,1020/2497,0],
   [1020/2497,3122/2497,0],
   [0,0,0]].

D ist rational, weil A0 vollen Spaltenrang besitzt. Die aktive Restmatrix X ist reell symmetrisch, auf P gestützt und spurfrei (Runde41).

Das eindimensionale Seedkomplement E=I-S4 hat Rückzug
Bseed=sum U_t E U_t†=D-B4.
Dieser Operator ist positiv, auf P gestützt und hat Spur1. Setze
Z0=D-(3/2)P,
Z=Bseed-P/2=Z0-X.
Der reale aktive 2x2-Block von Z ist [[z1,z2],[z2,-z1]], seine Eigenwerte liegen in[-1/2,1/2].

## 2. Zwei exakte Kernel mit gleichen behaltenen Daten

Setze außerhalb RanP alle Einträge der folgenden Matrix0:
L=[[z2,-z1],[-z1,-z2]].

Damit tr L=0, ||L||_2<=1/2 und
tr(L Bseed)=tr(LZ)+(1/2)tr L=0.
Wähle

K_±=-2I3 ± L.

Beide sind strikt negativ, mit Eigenwerten zwischen-5/2 und-3/2; die BFG-Eingaben bleiben zulässig. Ihre ambiente Spur ist-6, ihre aktive Spur-4. Y,F,W,P sind gleich. Die Trägerdimensionen und Ränge sind ohnehin K-unabhängig bis zur Seedwahl.

Die Seedkompression ist eindimensional, und ihr einziger Eigenwert lautet exakt

lambda_±=tr(K_± Bseed)=-2.

Der eindeutige Seedprojektor ist derselbe E, Formationszuwachs2 und Ausgangsträger P_+=I3. Daher sind auch die **vollen Nicht-Kernel-Ausgangsfelder** F_+,W_+,Y_+,P_+ identisch. Hier wird nicht bloß Gleichheit ihrer Spuren behauptet.

Die Konstruktion von L ist exakt über H^(-1/2) definiert. Die später angegebenen Dezimalmatrizen dienen nur der Originalcode-Kontrolle; sie ersetzen die exakte Definition nicht.

## 3. Unterschiedlicher Ausgangsbestand mit rationalem Zertifikat

Schreibe den aktiven Block X=[[x1,x2],[x2,-x1]] und definiere

w=x1 (Z0)_12 - x2 (Z0)_11.

Dann tr(LX)=2w. Da tr X=0 und die expliziten Seedbeiträge wie zuvor kompensieren, gilt

Delta[tr(PK_±)+tr F]=±2w,
tr(P_+K_{±,+})=-6±2w.

Das rationale Zertifikatsverfahren aus Runde40 wird frisch auf diesen neuen Wedge-Ausdruck angewandt. Mit der rationalen Näherung Q_r an H^(-1/2) werden B4 und X approximiert; ihre exakte Frobenius-Fehlerschranke e_B überträgt sich auf

|w-w_r| <= (|(Z0)_12|+|(Z0)_11|) e_B <4.002e-47.

Die ausschließlich rationalen Vergleiche liefern

6541042265093/10^15 < w < 6541042265096/10^15.

Also w>0. Die zwei Ausgangsbestände unterscheiden sich exakt um4w, ungefähr0.0261641690603774 Formationseinheiten. Beide Ausgangsänderungen der kombinierten Größe haben entgegengesetzte Vorzeichen und Betrag ungefähr0.0130820845301887.

Vollständige rationale Q_r-Einträge, Prüfung Q_r>I/10, exakte Residuen und reproduzierbarer Prüftext: [SEED_STOCK_CERTIFICATE.md](SEED_STOCK_CERTIFICATE.md). Es wird kein Vertrauen in eine numerische Seed-Eigenwertgleichheit benötigt; lambda_±=-2 folgt aus der exakten Orthogonalität.

## 4. Faser-Geschlossenheit und Grenze zusätzlicher K-blinder Zustandsgrößen

Betrachte die ausdrücklich typisierte reduzierte Beobachtung

Pi(Ξ)=(Y,F,W,P,tr K,tr(PK)).

Die zwei Eingaben haben genau dasselbe Pi-Bild. Nach einem vollständigen BFG-Ereignis unterscheiden sich mindestens tr K_+ und tr(P_+K_+), während die anderen vier Felder gleich bleiben. Deshalb existiert auf dieser Klasse keine eindeutige reduzierte Ein-Schritt-Dynamik Pi∘U=Ubar∘Pi. Es handelt sich um das konkrete Faser-Kriterium aus II89, nicht bloß um Nichterhaltung einer Größe.

Auch wenn man für dieses Ereignis zusätzlich alle Rangdaten und den Seedbetrag speichert, werden diese beiden Eingaben nicht unterschieden. Der Seedbetrag ist dabei ein diagnostischer Wert des bevorstehenden Ereignisses; er wird nicht als unabhängige neue Quellzustandsvariable eingeführt.

Eine unmittelbare Folgerung betrifft einen möglichen additiven Korrekturbestand R(Y,F,W,P). Für

E=tr(PK)+tr F+R(Y,F,W,P)

ist R vor dem Ereignis gleich und nach dem Ereignis ebenfalls gleich. Sein Änderungsbetrag ist daher für beide Historien derselbe. Er kann nicht gleichzeitig die beiden Defekte+2w und-2w aufheben. Ein universell konservierender K-blinder Zustandskorrekturterm dieser Art existiert folglich nicht auf der geprüften Klasse.

Dasselbe Argument umfasst feste Rang-/Dimensionskorrekturen als Zustandsfunktion. Auch eine direkte Ereignis-Gegenbuchung, die nur den aktuellen Seedbetrag und die aktuellen Ein-/Ausgangsränge benutzt, wäre in beiden Fällen gleich und kann die entgegengesetzten Reste nicht kompensieren. Über Zustandsfunktionen zukünftiger Seedwerte wird damit keine Aussage getroffen. Nicht ausgeschlossen: zusätzliche K-abhängige Richtungs-/Matrixdaten, ausdrücklich retained history, ein anders definierter physikalischer Zustandsbereich oder weitere tatsächlich aus BFG hergeleitete Observablen. Welche davon physikalisch ausgewählt ist, bleibt offen.

## 5. Frische Originalkontrollen

Zwei vorab konstruierte Fälle, keine Randomsuche und keine Änderung der Quelldynamik:

| Kernel | aktive Eingangsspur | ambiente Eingangsspur | Seedwert | Formationszuwachs | kombinierter Defekt |
| --- | ---: | ---: | ---: | ---: | ---: |
| K_- | -4 | -6 | -1.9999999999999996 | 2 | -0.01308208453018711 |
| K_+ | -4 | -6 | -1.9999999999999993 | 1.9999999999999991 | 0.013082084530188887 |

Maximale Frobenius-Differenz der vollständigen Nicht-Kernel-Ausgangsfelder:4.613712248324544e-16. Beide Originalereignisse vollständig und nichtterminal; alle Prüfassertionen bestanden. Numerische Näherung des aktiven L-Blocks:
[[0.42388964860156064,-0.2431002091834632],
 [-0.2431002091834632,-0.42388964860156064]].

Die exakten Aussagen beruhen auf der Konstruktion und rationalen Wedge-Zertifizierung. Die zwei Originalaufrufe prüfen deren Umsetzung mit Gleitkomma-Näherungen. Keine neue Remote-CI-Ausführung behauptet: Dokumentations-/Zertifikatsrunde ohne Audit-, Workflow- oder Originalcodeänderung. Letzter geprüfter Code und dessen CI bleiben separat in CI_VALIDATION.md.

## 6. Nächste sachliche Abhängigkeit

Ein skalarer Zusatz allein aus Formation, Witness, Lastgeometrie, Rang oder Seedbetrag genügt für diese Bestandsreduktion nicht. Die nächste konstruktive Frage muss die fehlende **K-abhängige Richtungsinformation** benennen und prüfen, ob eine quelleninterne Auswahl davon eine geschlossene lokale Beobachtung liefert. Die Wiederherstellung des gesamten Kernels wäre mathematisch möglich, aber noch keine ausgewählte vierdimensionale Energie-Impulsgröße.

Physikalische Energieablesung, Raumrelation, Uhr, Generator-/Lorentztransport und unabhängige Kalibrierung bleiben gesonderte Anforderungen. Der vorliegende begrenzte Faserzeuge ist weder eine Einstein-Herleitung noch eine allgemeine Widerlegung von BFG.
