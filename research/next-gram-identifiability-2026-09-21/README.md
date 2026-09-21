# Identifizierbarkeit des nächsten Gramoperators

Stand: 21. September 2026. Anschluss an den [Auswahlregeln-Audit](../ctc-selection-audit-2026-09-21/README.md). Mathematische Quellenprüfung; keine Änderung der Referenzimplementierung.

## Ergebnis

Die geprüften Quellenstellen verlangen dieselbe positive Gramkonstruktion auf jeder Stufe. Sie liefern dort keine auswertbare Bestimmung der Faktoren als Funktionen ihrer Eingaben, die zwischen g=f0, g=f0² und g=f0/2 entscheidet. Positivität, die neutrale Identität, reziproke Balance, Polartransport und ein stufenunabhängiges Gesetz reichen im unten definierten endlichen Vergleich nicht aus.

Ein neuer bedingter Befund ist stärker: **Soll der Rebuild nur das neue Paket und seine transportierten Kapazitäten sehen, kann keine dieser drei Regeln allgemein aus diesen Daten berechnet werden.** Sie verwenden Information aus dem verworfenen Anteil des alten Zustands. Ob die Quellen diese strenge Eingabebeschränkung tatsächlich verlangen, bleibt eine Frage der vollständigen Definition ihrer Rekonstruktionsfunktionale; die Klammernotation allein beweist sie nicht.

## Quellen und Reichweite der Suche

Geprüft wurden die relevanten extrahierten Textstellen der fünf vom Autor benannten Grundlagen. Originaldateien wurden erneut gehasht; die Hashes stimmen mit dem verwendeten Extraktionskorpus überein. [EVIDENCE.json](EVIDENCE.json) enthält Dateinamen und Hashes. PDF-Angaben beziehen sich auf die Seiten im Dokument, DOCX-Angaben auf Abschnitte. Es handelt sich nicht um eine vollständige Prüfung aller lokalen BFG-Dateien, aller Gleichungsbilder oder sämtlicher Quellenaxiome.

| Quelle | Geprüfter Anker | Was daraus folgt / was fehlt |
|---|---|---|
| Unified V4, 12.09.2026 | S. 6, Gl. (17)–(19); S. 9–10, BFG-C1 und Gl. (37)–(42) | Gramform, Polartransport und Rebuild; die Faktoren B_C[Paket], W_N[Paket], L_C[Paket] bleiben an dieser Stelle symbolische Funktionale. |
| Endogenous Dual Order Canonical Closure, 08.09.2026 | S. 8–9, Gl. (35)–(43) | Reziproke Gewichte und Paket sind bestimmt, sobald der alte Zustand vorliegt. Gl. (40) ist keine zusätzliche Gleichung für den numerischen nächsten Load ohne definierte Faktoren. |
| Strong Universal Reclosure, 08.09.2026 | S. 8, Abschnitt 5.4; S. 29, bedingter Schließungssatz | Dieselbe positive Konstruktion wird erneut angewandt; der Schließungsanspruch setzt die strukturellen Regeln und Modellergänzungen voraus. |
| Universal Reclosure Unification, 07.09.2026, revised final | S. 6, Gl. (17)–(19); S. 8, Gl. (36); S. 25, Theorem Candidate | Wiederverwendung derselben H_C- und L_C-Konstruktion ist gefordert, deren Auswahl wird dadurch nicht eindeutig. |
| Universal Structural Whitepaper Strong Form V2, DOCX | Abschnitte 6, 23 und 24; Gl. (22)–(24) | Positive Gramgeometrie; tatsächliches Masterspektrum noch nicht aus einem vollständig spezifizierten mikroskopischen Modell berechnet; Konstruktion von D_cov c, W_N, L_C aus einem upstream-Modell ist Forschungsaufgabe. |

Insbesondere: Der in V4 verwendete Gramfaktor K[X] in Y=K[X]*K[X] darf nicht ohne Herleitung mit dem Formationoperator K=c+aleph−Dcap oder dem Paket-Analyseoperator identifiziert werden. Die gleiche Buchstabenwahl liefert kein neues Rekonstruktionsgesetz.

## Satz 1: Unterbestimmtheit unter expliziten Vergleichsannahmen

Vorausgesetzt sei die endliche SA-Struktur des [Referenzmodells](../ctc-audit-2026-09-20/CTC_SA_MODEL.md): kommutierende selbstadjungierte Kapazitäten, c>0, einfaches Formationsspektrum mit genau einem negativen Eigenwert, volle Unterstützung von D, Y=eta I mit eta>0 und die reparierte persistente Projektion P. Moduswahl und Polartransport bleiben fest. Betrachtet werden d>=3; bei d=2 gilt die bereits deklarierte Terminalregel.

Sei g(eta,t) eine beliebige feste, überall endliche positive Funktion auf eta>0, 0<t<1, mit t=||PD||²/||D||². Setze auf dem nächsten Support

    W_next=L_next=I,
    D_cov,next=sqrt(g)c_next^(-1),
    B_next=D_cov,next c_next=sqrt(g)I,
    Y_next=g I.

Dann ist die Gramidentität exakt erfüllt. Der neutrale Resolvent ist (1+g)^(-1)I. Die transportierten Kapazitäten und ihre Formation bleiben von g unabhängig. Der nächste aktive Vektor ist

    D_next=sqrt(2)a(eta)/(1+g) P D,
    a(eta)=eta/((1+eta)sqrt(1+eta²)).

Er besitzt weiterhin volle Unterstützung auf allen verbleibenden Eigenlinien. Somit bleibt die abgeschwächte Strukturklasse geschlossen. Dies ist eine Familie verschiedener Ergänzungsmodelle, nicht eine Familie weiterer Lösungen des bereits vollständig festgelegten SA-Modells. Sie beansprucht nicht, jeden sonstigen BFG-Sektor zu erfüllen.

Für E=(1+eta)||D||² gilt exakt

    E_next/E = 2a(eta)²t / ((1+g)(1+eta)).

Da (1+eta)²(1+eta²)−8eta²=(eta−1)²(eta²+4eta+1)>=0, ist a²<=1/8. Wegen t<1 gilt daher E_next/E<1/4 für jede solche Wahl. Insbesondere erfüllen f0=2a²t, f0² und f0/2 diese Bedingungen. Jede einzelne ist stufenunabhängig; No-Retuning wählt daher keine davon aus.

Die reziproke Balance bestimmt die alten Paketgewichte, nicht die neue Gram-Skala. Den berechneten Paketgewinn mit dieser Skala gleichzusetzen ist eine weitere Identifikation. Auch die neutrale Minimierung bestimmt bei gegebenem Y die Response, nicht Y selbst.

## Satz 2: Das Paket allein enthält den normierten Gewinn nicht

Definiere T(X) als das neue Paket mitsamt neuem Support und transportierten Kapazitäten; die alte Norm wird dabei nicht als Zusatzdatum mitgegeben. Eine Funktion h(X) lässt sich genau dann als F(T(X)) schreiben, wenn sie auf jeder Faser von T konstant ist: Aus T(X)=T(X') muss h(X)=h(X') folgen. Notwendigkeit ist direkt; für die Umkehrung definiert man F auf dem Bild durch einen beliebigen Urbildzustand, was wegen der Faserkonstanz wohldefiniert ist.

Konkretes Gegenbeispiel im SA-Modell:

    d=3, eta=1, c=diag(1,2,3), aleph=I,
    Dcap=diag(3,1,1), K=diag(-1,2,3),
    P=diag(1,1,0), D_z=(1,1,z), z>0.

Alle diese Zustände sind zulässig. a=1/(2sqrt(2)), die beiden reziproken Gewichte sind jeweils 1/2. Daher ist das Paket in sechs direkten Summenkoordinaten für jedes z dasselbe:

    p=a(1,1,0;1,1,0).

Auch P, J, alter Gramoperator, transportierte Kapazitäten und nächste Formation sind identisch. In Supportkoordinaten ist p=(1/2,1/2). Es gilt ||p||²=1/2 und ||p||²_(G⊕G)=1, während ||D_z||²_G=2(2+z²). Somit

    f0(X_z)=1/[2(2+z²)].

| Alter Zustand | f0 | f0² | f0/2 |
|---|---:|---:|---:|
| z=1 | 1/6 | 1/36 | 1/12 |
| z=2 | 1/12 | 1/144 | 1/24 |

Gleiche Rebuild-Eingaben liefern für jede der drei Regeln verschiedene gewünschte Ausgaben. Keine lässt sich daher auf dieser Klasse als ausschließlich paketbasierte Funktion realisieren. Die Brüche und Normrelationen wurden mit rationaler Arithmetik kontrolliert; dies ergänzt den symbolischen Beweis.

**Reichweite:** V4 Gl. (40) schreibt die Funktionale mit dem Paket als Argument. Falls dieses Argument nur Kurznotation für den vollständigen alten Zustand ist, greift der Ausschluss nicht. Dann muss diese zusätzliche Abhängigkeit aber ausdrücklich definiert werden. Das derzeitige SA-Modell arbeitet als Funktion des vollständigen alten Zustands und wird durch diesen Befund nicht inkonsistent.

## Konsequenz für die weitere Reparatur

Es sind zwei unterschiedliche Aufgaben zu trennen:

1. **Zulässige Eingaben festlegen.** Entweder nur Paket und transportierte Geometrie oder zusätzlich definierte alte Zustandsdaten. Für die aktuelle Regel genügt bei mitgeführter alter Paketmetrik die alte Energie E_old als Zusatzskalar: g=||p||²_(G_old⊕G_old)/E_old. Das macht die Regel berechenbar, begründet aber ihre Auswahl noch nicht. Im skalaren Fall reichen beispielsweise eta_old und E_old neben dem Paket.
2. **Die Funktion auswählen.** Selbst bei vollständigem altem Zustand bleiben f0, f0² und f0/2 zulässig unter Satz 1. Benötigt wird ein unabhängiges Quellenaxiom oder ein operationalisierter Vergleich. Paketabhängigkeit allein wählt ebenfalls kein Gesetz aus; etwa konstante positive Loads 1 und 2 sind unter den schwachen Positivitätsbedingungen beide möglich.

Eine zusätzliche Gram-Vererbung Y_next=J*(Y⊕Y)J würde im skalaren Zweig g=eta liefern. Das wäre eine andere feste Zusatzregel, keine Folgerung der Positivität. Ebenso wäre die Gleichsetzung des Gramoperators mit einem Produkt des Paket-Analyseoperators eine zusätzliche Identifikation.

## Unabhängige Identifizierung über den neutralen Response

Im skalaren endlichen Modell ist C_next=sI mit s=1/(1+g). Wenn s durch eine separat definierte Response-Messung bestimmt wird, folgt g=1/s−1. Für den bisherigen d=5-Seed sagen die drei Regeln voraus:

| Regel | g | s |
|---|---:|---:|
| f0 | 1/5 | 5/6 |
| f0² | 1/25 | 25/26 |
| f0/2 | 1/10 | 10/11 |

Ein vorab abgesichertes Intervall 0<s_low<=s<=s_high<=1 ergibt g in [1/s_high−1,1/s_low−1]. Eine Vorhersage außerhalb des Intervalls ist unter der festgelegten Messabbildung ausgeschlossen. Ein erzeugtes s aus derselben Updateformel ist keine unabhängige Messung. Einheiten, Eingaben, Messabbildung, Unsicherheiten und Wiederholungsplan fehlen derzeit; daher liegt hier ein Identifizierungsweg, kein ausgeführter empirischer Test vor.

## Auditstatus und nächster konkreter Auftrag

Angewandt wurden Claim-State, Unterscheidbarkeit, Redescription und Provenienz der drei BFG-Auditvorlagen. Definitionen und bedingte Beweise sind von Quellenbefunden, Programmtests und empirischen Aussagen getrennt. Historische negative Befunde und Quellendokumente bleiben erhalten.

Der nächste Auditauftrag lautet: Definiere den vollständigen Eingaberaum von B_C[·], W_N[·], L_C[·] aus den Originalquellen. Prüfe zuerst die Faserkonstanz am angegebenen Zustandspaar. Falls alte Norminformation zugelassen ist, nenne die Quelle dafür und suche anschließend eine unabhängige Bedingung, die g=f0 gegenüber g=f0² und g=f0/2 auswählt. Falls keine vorliegt, ist die Funktion weiterhin als Modellergänzung auszuweisen. Die Benennung eines gewünschten Gesetzes als Axiom ersetzt diese Herleitung nicht.

Kein Gesamttestlauf war für diese reine Dokumentationsstufe erforderlich. Die sieben allgemeinen Probleme sind dadurch nicht geschlossen; die Gram-Rebuild-Lücke ist jetzt präziser lokalisiert.
