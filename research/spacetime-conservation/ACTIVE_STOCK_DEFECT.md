# Zertifizierter Gegenzeuge zum kombinierten aktiven Bestand – Runde 40

## Aussage

Unter den unveränderten BFG-Regeln ist E_act=tr(PK)+tr F **nicht allgemein erhalten**, auch wenn Auswahlverlust0 ist und sich die ausdrücklichen Seedbeiträge exakt kompensieren. Der folgende rationale Zustand besitzt einen eindeutigen zulässigen Seed und einen strikt positiven, rational zertifizierten Bestandsrest:

6599430384017/10^15 < Delta E_act < 6599430384019/10^15.

Dies schließt die Zertifizierungslücke der Kandidatenklasse aus Runde39 durch einen neuen einfachen Zeugen. Die früheren zufälligen n=4/5-Fälle werden dadurch nicht rückwirkend als exakt zertifiziert deklariert. Formationseinheiten sind keine hergeleiteten Joule; die Aussage betrifft genau die ungewichtete additive Kandidatenklasse, nicht jede mögliche Energiebrücke.

Vorab: PROTOCOL.md, Runde40. Quelle und unveränderter Update-Blob: SOURCE_MANIFEST.json. Standardmathematik: Gram-/Polarzerlegung, Sylvester-Abschätzung und exakte rationale Arithmetik. Keine zusätzliche Physik.

## 1. Rationale Eingabe und Zulässigkeit

P=diag(1,1,0), F=diag(1,21/50,0), W=P/2, K=-diag(1,2,3),

Y=[[1/4,0,1/10],[0,1/2,1/10],[1/10,1/10,1/2]].

Gershgorin liefert 3/20 I <= Y <= 7/10 I. Also Q_selection=I, T_selection=P, Witnessmasse1 und Formationsauswahlverlust ell_F=0. Beide Formationseigenwerte auf P sind positiv.

Die Lasten sind Lambda_C=27/25 und Lambda_B=3/25; alpha=1/10, beta=9/10. Mit H_P=P(I+Y)P auf RanP ist P_G C=P H_P^(-1)P. Schreibe A=A0/sqrt(10) mit den beiden ambienten 3x3-Zeilenblöcken

A0_C=diag(4/5,2/3,0),
A0_B=3 A0_C Y
     =[[3/5,0,6/25],[0,1,1/5],[0,0,0]].

Somit

H=A0†A0=[[1,0,18/125],[0,13/9,1/5],[18/125,1/5,61/625]].

A0 hat Rang3: die ersten beiden oberen Zeilen trennen Spalten1/2, die untere erste Zeile besitzt eine nichtverschwindende dritte Komponente. Daher H>0, Ausgangsdimension3, V unitär und S4=V† P V von Rang2.

Alle Zeilenbilder U_C,U_B liegen in RanP. Auf diesem Raum liegt K zwischen -2I und -I, weshalb -2I<=K_+<=-I. Das Seedkomplement I-S4 hat Dimension1: sein Minimalwert ist strikt negativ und automatisch einfach. Das Ereignis ist also mathematisch nichtterminal mit eindeutigem Rang-eins-Seed; P_+=I3. Kein numerischer Terminalfilter wird zur Auswahl des Zeugen verwendet.

## 2. Was trotz Seed-Kompensation übrig bleibt

Die exakte Identität aus Runde39 lautet bei kappa_F=1:

Delta E_act = tr[K(B4-P)]-ell_F,
B4=sum_r U_r S4 U_r†.

Hier ell_F=0. Mit der Polarzerlegung A0=R sqrt(H) und R=U V† gilt

B4=sum_r A0_r H^(-1/2) P H^(-1/2) A0_r†.

Der Faktor sqrt(10) kürzt sich vollständig. Der Seed-Eigenwert braucht für den Gesamtdefekt nicht separat approximiert zu werden: seine negative aktive Kernelkomponente und der positive Formationszuwachs heben sich exakt auf.

Die fehlende Bedingung ist B4=P bzw. nur deren K-gewichtete Spurengleichheit. Der BFG-Update erzwingt diese Bedingung nicht allgemein. Für den vorliegenden K ist der Defekt durch das folgende Zertifikat strikt positiv.

## 3. Rationales Zertifikat ohne Vertrauen in die Gleitkomma-SVD

Sei S=H^(-1/2). Die in [ACTIVE_STOCK_CERTIFICATE.md](ACTIVE_STOCK_CERTIFICATE.md) gespeicherte **rationale symmetrische** Matrix Q_r ist eine Näherung an S. Ihre Erzeugung mit 100-stelliger Rechnung dient nur zur Kandidatensuche. Die Zertifizierung benötigt danach ausschließlich exakte rationale Operationen:

1. Alle drei führenden Hauptminoren von Q_r-I/10 sind positiv. Damit Q_r>I/10.
2. Berechne R=Q_r²-H^(-1) exakt und e=10 sum_ij |R_ij|. Hier e<1.384e-48.
3. Mit E=Q_r-S gilt Q_r E+E S=R. Da Q_r>I/10 und S>0, folgt durch Frobenius-Skalarprodukt/Cauchy-Schwarz ||E||_F<=10||R||_F<=e.
4. Setze a=sum_r ||A0_r||_F² und q=sum_ij |(Q_r)_ij|. Für den mit Q_r gebildeten B4-Näherungswert gilt
   ||B4(Q_r)-B4(S)||_F <= a(2q e+e²).
5. Da ||K||_F<=sum |K_ij|=6, ist der Spurfehler höchstens b=6a(2q e+e²)<3.648e-46.

Der rationale Mittelpunkt c=tr[K(B4(Q_r)-P)] erfüllt durch exakten Bruchvergleich

6599430384017/10^15 < c-b < c+b < 6599430384019/10^15.

Sein Dezimalwert ist etwa0.0065994303840177635158542230734271716821124427581797. Der Beweis verwendet die rationalen Vergleiche, nicht die Dezimaldarstellung. Für das Sylvesterargument ist keine Kommutativität zwischen Q_r und H vorausgesetzt.

## 4. Frische Originalkontrollen und dokumentierte Korrektur

Originalupdate mit genau dieser Eingabe: Delta E_act=0.006599430384018223, Seed-Formationsgewinn1.2568997908165365. Eine komplexe unitäre Eichkontrolle, festgelegt durch Zufallsseed20261025, liefert0.006599430384016225; Eichrest1.9984014443252818e-15. Maximaler Rest der aktiven Bilanz4.172009959724221e-16. Beide vollständigen Ereignisse nichtterminal.

Es gab einen explorativen Originalaufruf nach der Vorabregistrierung; die abschließende Zertifikatsrechnung enthält zusätzlich zwei Originalaufrufe (derselbe rationale Zustand frisch und seine Eichversion). Also drei Aufrufe insgesamt, zwei im finalen Zertifikatslauf; keine Randomsuche.

Der erste symbolische Kontrolllauf brach an einer fehlerhaften Hilfsformel vor der Zertifizierung ab: Lambda_B/Lambda_C war irrtümlich mit Y² statt mit Y P Y im komprimierten Formationsterm geschrieben. Der tatsächliche Quellcode und A0 waren korrekt und unverändert. Die korrigierte Quellkompression liefert exakt1/9, danach lief das gesamte rationale Zertifikat samt Originalkontrollen frisch erfolgreich durch. Der Abbruch wird nicht als bestanden gezählt.

Vollständige rationale Q_r-Einträge, Kontrollausgabe und ausführbare Rechnung stehen in ACTIVE_STOCK_CERTIFICATE.md. Keine Produktions-, Audit- oder Workflowdatei geändert. Diese Dokumentationsrunde beansprucht keinen neuen Remote-CI-Pass; letzter geprüfter Code und dessen Actions-Nachweise bleiben in CI_VALIDATION.md getrennt.

## 5. Bedeutung und nächste Abhängigkeit

Ein bloßes Addieren der Formation zum aktiven Kernelbestand schließt die Energiefrage nicht: sogar ohne Formationselektion bleibt nach exakter Seed-Kompensation ein interner Transportrest. Eine globale Reserve, die diesen Rest nachträglich wegdefiniert, wäre eine neue Konstruktion und noch kein hergeleitetes physikalisches Gesetz.

Eine sinnvolle nächste mathematische Frage ist, unter welchen quelleninternen Bedingungen B4=P gilt und welche coherenzabhängigen Beiträge B4-P bestimmen. Für die physikalische Energie-/Impulsidentifikation bleiben die in Runde39 genannten M_E-, Raum-/Uhr-/Quantenbrücken samt unabhängiger Kalibrierung und vollständigem Strom erforderlich. Kein Einstein-Grenzfall oder allgemeines BFG-No-Go folgt aus diesem begrenzten Gegenbeispiel.
