# Die sieben offenen Punkte: präziser Abschlussbedarf

Bewertung am Stand ad1d774. B_C, W_N und L_C werden als drei Operatoren gelesen;
die doppelte Schreibweise in der Anfrage ist keine zusätzliche Definition.

| Nr. | Punkt | Vorhanden | Was zum Schließen fehlt |
| --- | --- | --- | --- |
| 1 | Vollständiges State Update | `formation.prepare_candidate` liefert Split, transportierte Kapazitäten und Gate; M1/M2 sind deklarierte Spielmodelle | Vollständiger typisierter Zustand mit Träger, Vektor, Kapazitäten, Rekonstruktionsdaten und Transport; eindeutige Abbildung aller Komponenten und Erhaltung des zulässigen Zustandsraums |
| 2 | Rekonstruktion B_C, W_N, L_C | V2 §6 Gl.22–24 und V4 S.10 Gl.40 geben die Bauform | Funktionen aus dem Eingabezustand einschließlich Definitionsbereichen, Einheiten, Transformationsregeln und Eindeutigkeit; V2 §23–24 erklärt das vorgelagerte Modell noch zur Aufgabe |
| 3 | Vollständiger Gram-Rebuild | H=B_C† W_N B_C, Y=L_C† H L_C; M1 setzt eine zusätzliche andere Closure | Mit Punkt 2 tatsächlich berechenbare Operatoren; Positivität, Trägerkompatibilität und Kovarianz nachweisen. PSD allein identifiziert keine kanonische Rekonstruktion |
| 4 | Aktualisierter rekursiver Transport | Polarabbildung J in `core.split`; Kapazitätskompression in `formation` | Eigenständiger Endomorphismus R_next auf dem neuen Träger und seine Persistenz-/Stabilitätseigenschaften. J bildet zwischen Trägern ab und ist nicht automatisch dieser Endomorphismus |
| 5 | Vollständige universelle Iteration | `minimal` iteriert M1/M2; V4 Gl.43 schreibt U^n formal | Punkte 1–4, Absorption des Terminalzustands, Wohldefiniertheit bei jedem Schritt; endlicher Lauf ist kein Beweis unendlicher Existenz, Konvergenz oder Universalität |
| 6 | Allgemeiner nichtnormaler Fall | `core.persistent_basis` weist nichtnormale Eingaben ausdrücklich zurück; Persistenzkorrektur als Vorschlag | Präzise Klasse (z.B. endlichdimensional und potenzbeschränkt), periphere Jordanstruktur, oblique Spektralprojektion getrennt von metrischer Projektion; robuste numerische Zertifizierung nahe dem Einheitskreis |
| 7 | Unendlichdimensionale Realisierung | V4 S.11 Gl.45–46 definiert Resolvente und Graphform für abgeschlossenes dicht definiertes K | Kompatible dichte Definitionsbereiche für gesamten Rebuild/Transport, abgeschlossene Formen und Zeugenräume, Spektralisolation, Erhaltung unter Iteration und kontrollierte Diskretisierungsgrenzen |

## Warum Positivität die Rekonstruktion nicht festlegt

Schon auf einem eindimensionalen Träger liefern W_N=L_C=1 und B_C=b die
zulässige Gramlast Y=|b|². Ohne Regel für b sind b=1 und b=2 beide positiv,
ergeben aber C_N=1/2 bzw. 1/5. Die Gram-Bauform allein definiert somit keinen
eindeutigen Update. Dieses Beispiel widerlegt keine zusätzlich spezifizierte
Rekonstruktionsregel; es zeigt genau, weshalb sie benötigt wird.

## Nichtnormalität: die beiden Projektionen sind verschieden

Für R=[[1,a],[0,1/2]], a ungleich 0, gilt

    R^n = [[1, 2a(1-2^(-n))], [0, 2^(-n)]].

R ist nichtnormal und potenzbeschränkt. Der periphere Raum ist span(e1).
Die Spektralprojektion entlang des stabilen Eigenraums ist
P_s=[[1,2a],[0,0]], während die orthogonale Projektion für G=I
P_G=diag(1,0) ist. P_s kommutiert mit R, P_G nicht.
Ein Austausch dieser Projektionen würde den Beweisgegenstand ändern.

Außerdem ist [[1,1],[0,1]] trotz Spektralradius 1 nicht potenzbeschränkt:
die obere rechte Komponente der n-ten Potenz ist n. Eine numerische Prüfung
allein der Eigenwertbeträge genügt im allgemeinen Fall nicht.

Der alte Span aller nichtabklingenden Vektoren bleibt ebenfalls problematisch:
für diag(1,1/2) sind e1 und e1+e2 nichtabklingend, ihre Differenz e2 klingt ab.
Siehe die unveränderte [Persistenzkorrektur](../../docs/PERSISTENCE_PROPOSAL.md).

## Warum die endliche Spektrallösung nicht einfach ins Unendliche übergeht

Auf l²(N) sei S(x0,x1,...)=(0,x0,x1,...). Dann ||S^n x||=||x|| für jedes n.
S hat aber keine Eigenvektoren zu |lambda|=1: Aus Sx=lambda x folgt sukzessive
x0=x1=...=0. Der direkte Summenraum peripherer Eigenvektoren wäre also null,
obwohl kein nichttrivialer Zustand normmäßig abklingt. Dies ist ein explizites
Gegenbeispiel gegen eine uneingeschränkte Übertragung dieser endlichen Definition,
kein Gegenbeispiel gegen den Resolventensatz in V4.

## Reihenfolge und Abnahme

Zuerst 2 und die vollständige Zustandsspezifikation aus 1; anschließend 3 und 4;
dann 1 als implementiertes Gesamtupdate und 5. Punkt 6 ist eine gesonderte
Erweiterung der zulässigen Transportklasse. Punkt 7 benötigt zusätzliche
Funktionalanalysis und folgt nicht aus endlich vielen bestandenen Matrixtests.

Für einen ersten endlichen Realisierungsentwurf müssen feste Eingaben genau einen
Folgezustand bis zur ausdrücklich erlaubten Basisäquivalenz erzeugen; keine
Rückkopplung aus Zielbezeichnungen oder Prüfdaten; dimensionsgerechte Operatoren;
unabhängig kontrollierte Gram- und Transportrechnung; dokumentierte Terminalfälle.
Nicht unterstützte Eingaben sind von physikalischer Terminalität zu unterscheiden.

**Status aller sieben universellen Ansprüche: offen.** Diese Prüfung präzisiert
die Lücken und liefert Gegenbeispiele gegen unzulässige Abkürzungen. Sie gibt
keine erfundene Rekonstruktionsregel als mathematische Reparatur aus.
