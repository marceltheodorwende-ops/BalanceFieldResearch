# Mathematischer und methodischer Audit des Referenzmonitors

Stand: 15. September 2026. KI-gestützter Auditentwurf für Marcel Wende;
keine unabhängige Begutachtung und keine Freigabe durch den Autor behauptet.
Geprüfter GitHub-Stand: `839119bebf504550dec588ceadff9eb77098b296`.

## Ergebnis und Umfang

**Gesamtentscheidung: überarbeiten.** Der bestehende Monitor ist ein
Konsistenzprüfer gegen eine einzelne Referenz. Seine Aussage bei exakt
zutreffender Referenz ist mathematisch begründbar. Eine Garantie gegen
Fehlalarme bei unsicheren Referenzgewichten besitzt er nicht. Die vorgeschlagene
Mengenreparatur ist als mathematische Spezifikation möglich, aber noch nicht
implementiert oder numerisch zertifiziert.

Dieser Bericht verwendet die drei gelieferten Dokumente als Auditkriterien.
Er prüft den jüngsten R1/R2-Monitor, seine Fehlerannahmen und die vorgeschlagene
Reparatur. Er ist keine vollständige Beweisprüfung der fünf theoretischen BFG-
Quellen. Originaldokumente, Produktionscode, frühere Resultate und Schwellen
werden durch diesen Audit nicht geändert. Historische Experimente werden
nicht nachträglich als präregistrierte Bestätigung umklassifiziert.

## Quellen und angewandte Prüfkriterien

Die Dokumente wurden aus ihrem Word-Haupttext einschließlich Tabellen und
mathematischer Textknoten gelesen. Kein Layoutaudit oder Nachweis vollständiger
Erfassung eingebetteter Grafiktexte wird behauptet. Abschnittsverweise beziehen
sich auf die Dokumentüberschriften, nicht auf unbestätigte Seitenzahlen.

| Quelle | Angewandte Abschnitte | Konsequenz |
| --- | --- | --- |
| BFG_Audit_Complete_Edition.docx | 4/7 Claim-State; 10 Unterscheidbarkeit; 12 Redescription; 15 Schema; 17/18 Fehlerversicherung und Gegenprüfung | Definition, bedingten Satz, Simulation und empirische Aussage getrennt bewerten |
| BFG_Audit_Workflow_Master.docx | 6–9 Status, Interpretationsgrenzen, Prüfplan; 10–11 Provenienz und KI-Arbeitsumfang | Ein Auditobjekt; negative Resultate bewahren; kein Codeumbau während der Bewertung |
| BFG_X_Context_Recovery_Protocol_Master finish.docx | 7–8 Kontext und Quellenhierarchie; 11–16 Grenzen und Ledger | BFG-Theorie, aktuelles Netzwerkexperiment und fremde Kollaborationsbeispiele auseinanderhalten |

Die erwähnten D12RG/IDPC-Stufen sind Kontextbeispiele der Vorlagen, keine
Ergebnisse dieses Repositorys. Vorgaben zu E-Mails sind hier nicht einschlägig;
es wird keine Nachricht an Dritte versandt. Die Vorlagen ersetzen keine
mathematische Evidenz für die im Folgenden bewerteten Aussagen.

SHA-256 der unveränderten Auditquellen:

```text
BFG_Audit_Complete_Edition.docx
ED915F5A468569ED174C3187436BBFFD067FA10EFE3A185EE6ABF414E89711E5
BFG_Audit_Workflow_Master.docx
8A27F722DE0A6F763C134D5F3320C38CD1F713B573D9FE81384E04FFCBFC4D25
BFG_X_Context_Recovery_Protocol_Master finish.docx
C571E2FE9CC7804436B2B9E52B4F8A1541B7AAD50B07B242C83441556232E329
```

## Rekonstruierter Ergebnisstand

| Aussage | Status im Audit | Zulässige Interpretation |
| --- | --- | --- |
| 53 veröffentlichungsbezogene Tests bestanden | Berichteter Ausführungsbefund des vorherigen Laufs; hier kein neuer Testlauf | Code erfüllt diese geprüften Anforderungen, keine universelle Garantie |
| Frühere Konsistenzprüfung erkennt 0/24 Kantenentfernungen | Negativer synthetischer Befund | Methode hierfür im geprüften Katalog unzureichend |
| Referenzmodell erkennt mit allen Sensoren 21/24 Kantenentfernungen | Exploratives Simulationsergebnis | Zusätzliche Referenzinformation hilft in diesem Katalog |
| Bekannter Anfangsimpuls erkennt 4/4 zuvor unsichtbare Fälle | Exploratives Kleinstbeispiel | Anregung kann Unterscheidbarkeit herstellen, nicht garantieren |
| Falsche Gewichte erzeugen Alarme bei 8/8 intakten angeregten Vergleichsfällen | Negativer Befund für die Ausfallinterpretation | Einzelreferenz ist zu eng; Alarm ist nicht eindeutig kausal |
| Größere ehrliche Kalibriergrenze: nur 1/4 Ausfälle erkannt | Sensitivitätsverlust | Fehlerabsicherung und Erkennbarkeit stehen im Zielkonflikt |
| BFG-spezifischer Mehrwert des Monitors | Offen, nicht nachgewiesen | Diffusions- und Referenzrechnung nicht als BFG-Neuheit ausgeben |

Evidenzanker: `docs/DETECTION_FINDINGS.md`, `docs/REFERENCE_FINDINGS.md`,
`docs/REFERENCE_STRESS_FINDINGS.md`, `bfg_lab/reference.py`,
`bfg_lab/reference_stress.py`. Bewertet wurden die vorhandenen Befunde und
die zugehörige Logik. Keine zusätzlichen empirischen Resultate entstanden.

## Befund A Einzelreferenz und Modellfehler

Der Code propagiert einen kalibrierten Anfangszustand mit einer festen Matrix
R0. Sein Fehlerbudget enthält Anfangs- und Sensorfehler. Der Fehler durch
R_true != R0 fehlt. Das ist keine widerlegte Fehlerrechnung innerhalb ihrer
Annahmen; es ist eine fehlende Voraussetzung für ihre Anwendung auf unsichere
Gewichte. Die zusätzliche Konstante 1e-10 ist eine numerische Konvention und
kein hergeleiteter Gesamtfehlernachweis aller Matrixoperationen.

Für das exakte diskrete Modell x_k=R0^k x0 gilt komponentenweise
`|R0^k(x0-xhat0)| <= |R0|^k delta0`. Zusammen mit einer tatsächlich gültigen
Sensorfehlergrenze begründet dies das vorhandene Budget in exakter Arithmetik.
Es umfasst weder unbekannte äußere Anregung noch falsche Gewichte.

## Befund B Präzise Mengenreparatur

Vor der nächsten Auswertung sind festzulegen:

- Theta_H: zulässige gesunde, zeitlich feste Parameter und Topologien;
- X0: zulässige Anfangszustände aus der Kalibrierung;
- S: bekannte Sensorabbildung, feste Messzeiten t_k;
- E_k: tatsächlich geltende Messfehlerbereiche;
- bekannte Eingaben; zunächst keine nachträglichen unbekannten Kräfte.

Für Diffusion sei f(theta,x0,t)=exp(-t L(theta))x0. Definiere die **gemeinsame**
Verträglichkeitsmenge über die bisherige Messhistorie:

`F_H(y) = {(theta,x0) in Theta_H x X0 : y_k - S f(theta,x0,t_k) in E_k für alle k}`.

Ein und derselbe Parameter und Anfangszustand müssen alle Zeiten erklären.
Für jeden Zeitpunkt einen anderen passenden Parameter auszuwählen ist nicht
dieselbe Hypothese eines festen Netzwerks.

**Bedingter Satz.** Wenn der wirkliche gesunde Parameter theta* in Theta_H,
der wirkliche Anfangszustand x0* in X0 und alle wirklichen Messfehler in E_k
liegen und die Dynamik korrekt beschrieben ist, dann ist F_H(y) nicht leer.

**Beweis.** Das Paar (theta*,x0*) erfüllt nach diesen Voraussetzungen sämtliche
definierenden Ungleichungen. Es ist somit ein Element von F_H(y). Ein Alarm,
der nur bei bewiesener Leerheit ausgegeben wird, tritt unter den Voraussetzungen
nicht auf. Dies ist eine logische Garantie, keine geschätzte Fehlalarmrate.

**Grenze.** Damit ist weder die Güte der gesetzten Bereiche bewiesen noch eine
Erkennung jedes Fehlers garantiert. Wählt man Theta_H zu eng, geht die Garantie
verloren. Wählt man sie sehr breit, können echte Ausfälle vereinbar bleiben.

## Befund C Gitter und Hüllen sind keine exakten Entscheider

Eine endliche Stichprobe aus einem kontinuierlichen Parameterbereich genügt
nicht zum Beweis von Leerheit. Gegenbeispiel: Zwei-Knoten-Diffusion mit
Kantengewicht theta in [0.9,1.1] hat die normierte Abweichung exp(-2 theta t).
Bei t=1 und wahrem theta=1 ist die rauschfreie Messung exp(-2). Das Gitter
{0.9,1.1} enthält keinen exakten Treffer, obwohl eine gesunde Referenz existiert.
Ein Alarm nach erfolgloser Gittersuche wäre falsch.

Eine garantiert umfassende äußere Hülle erlaubt einen **einseitigen** Test:
Messung außerhalb der Hülle schließt die gesunde Familie aus. Innerhalb der
Hülle bedeutet nur »nicht ausgeschlossen«, nicht »eine gemeinsame Referenz
wurde gefunden«. Lose Intervallhüllen können nicht gemeinsam realisierbare
Zeitpunkte kombinieren. Ein Optimierer ohne Machbarkeitszertifikat darf aus
Nichtkonvergenz ebenfalls keinen Ausschluss ableiten.

Für einen implementierten Entscheider sind daher mindestens die Zustände
`compatible_witness`, `healthy_family_excluded` und `unresolved` zu unterscheiden.
Ein numerischer Fehler gehört in `unresolved`, nicht in den Ausfallzähler.

## Befund D Eine konservative mathematische Startgrenze

Für symmetrische, positiv semidefinite Graph-Laplacematrizen L und L0 mit
`||L-L0||_2 <= eta` folgt durch die Integralidentität

`exp(-tL)-exp(-tL0) = - integral_0^t exp(-(t-s)L) (L-L0) exp(-sL0) ds`

und die Kontraktivität beider Exponentialoperatoren:

`||exp(-tL)-exp(-tL0)||_2 <= t eta`.

Beide Laplacematrizen vernichten den konstanten Vektor. Daher lässt sich für
eine Referenz xhat0 und P als Zentrierungsprojektion der Modellfehler begrenzen:

`||x(t)-exp(-tL0)xhat0||_2 <= epsilon_x + t eta ||P xhat0||_2`,

wenn `||x0-xhat0||_2 <= epsilon_x`. Für einen einzelnen Knotensensor kommt
seine absolute Messfehlergrenze epsilon_y hinzu. Bei allgemeinem S tritt der
Faktor `||S||_2` auf. t und L müssen zueinander passende Zeiteinheiten haben.

Bei symmetrischen Kantengewichtsfehlern |Delta w_ij|<=b_ij kann
`eta = 2 max_i sum_j b_ij` als konservative Schranke verwendet werden: Die
absolute Zeilensumme von Delta L ist höchstens dieser Wert und Delta L ist
symmetrisch. Der wahre und der Referenzgraph müssen zulässige nichtnegative
Gewichte besitzen.

Dies ist ein hergeleiteter Ansatz für eine äußere Hülle, kein bereits
implementierter oder extern begutachteter Reparaturnachweis. Die Hülle wächst
mit t und kann sehr unempfindlich sein. Numerisch zertifizierte Berechnung
erfordert zusätzlich nachgewiesene Rundungsfehlergrenzen. Eine bloße Erhöhung
der bestehenden Konstante 1e-10 erfüllt diese Anforderung nicht.

## Befund E Ausfallbehauptung und Unterscheidbarkeit

»Keine gesunde Referenz erklärt die Daten« bedeutet zunächst Modellkonflikt.
Für die Diagnose eines Kantenfehlers braucht es eine deklarierte Fehlerfamilie
Theta_F sowie eine zugehörige Verträglichkeitsmenge F_F(y):

| F_H | F_F | Aussage |
| --- | --- | --- |
| nicht leer | nicht leer | nicht unterscheidbar |
| leer | nicht leer | innerhalb dieser Modellfamilien mit Fehler vereinbar |
| leer | leer | beide Familien unzureichend; keine Diagnose erzwingen |
| nicht leer | leer | gesunde Familie vereinbar; kein allgemeines Gesundheitszertifikat |

Unbekannte Kräfte oder falsch deklarierte Fehlergrenzen können ebenfalls
F_H leeren. Nur eine ausreichend spezifizierte Alternative und die offen
genannten Annahmen tragen eine weitergehende Interpretation. Der Gleichgewichts-
Gegenfall bleibt gültig: Für x0=c*1 sind die Verläufe aller ungestörten
Graph-Laplacematrizen identisch. Mehr Tests können diese Nichtunterscheidbarkeit
nicht beseitigen; eine zusätzliche Beobachtung oder Anregung ist nötig.

## Methodische Bewertung nach den Vorlagen

1. **Claim-State:** R1/R2 sind Simulationen und Diagnostik. Die oben formulierten
   Sätze sind bedingte mathematische Aussagen mit Beweisargumenten. Die neue
   Implementierung bleibt offen.
2. **Fehlerledger:** Frühere verpasste Ausfälle und Alarme bei falschen Gewichten
   bleiben negative Befunde. Ein verbessertes Verfahren rettet diese Stufen nicht.
3. **Redescription-Null:** Die Referenzmethode ist ohne BFG-Vokabular vollständig
   formulierbar. BFG-spezifische Neuheit und ablationsgestützter Mehrwert sind
   nicht belegt. Rollenbezeichnungen werden hier nicht künstlich zugeordnet.
4. **No-retuning:** Die dokumentierten lokalen Vorabpläne sind nützlich. Da Plan
   und Befund gemeinsam nach Ausführung veröffentlicht wurden, beweist ein
   Planhash allein keine öffentlich überprüfbare zeitliche Präregistrierung.
5. **Informationsfairness:** Mehr Referenzwissen und vollständige Anfangskalibrierung
   sind ein größeres Beobachtungsbudget. Bessere Trefferquoten gegenüber einem
   unwissenden Monitor belegen keine algorithmische Überlegenheit bei gleichem Budget.
6. **Provenienz:** Bisherige kombinierte Code-/Ergebnisänderungen waren keine
   isolierten Reviewbeiträge im Sinn der jetzt gelieferten Vorlagen. Dieser Audit
   bildet deshalb ein separates Objekt. Kein nachträgliches Umschreiben der Historie.

## Nächster eng begrenzter Prüfauftrag

Zuerst eine äußerlich abgesicherte gesunde Referenzhülle für symmetrische
Diffusion spezifizieren. Die Parameterbereiche müssen unabhängig von den
anschließend ausgewerteten Daten begründet sein. Primäres Sicherheitskriterium:
kein gesunder, innerhalb aller deklarierten Grenzen liegender Verlauf darf
ausgeschlossen werden. Sensitivität wird separat berichtet; Enthaltung zählt
nicht als Erkennung.

Vor Implementierung die aktuelle Herleitung prüfen und einen eigenen Plan
festhalten. Zwingende Gegenprüfungen: wahrer Parameter zwischen Gitterpunkten,
Randwerte der Gewichte, extremale Kalibrier-/Sensorfehler, nuller Anfangskontrast,
unterbrochene Graphen, fehlende Sensoren und eine Messhistorie, deren einzelne
Zeitpunkte nur mit unterschiedlichen Parametern passen. Rechenfehler müssen
als ungeklärt enden. Neue Datenfälle dürfen nach Kenntnis der Ergebnisse nicht
zur Umdefinition des primären Kriteriums verwendet werden.

## Kompakter maschinenlesbarer Auditstatus

```json
{
  "audit_id": "BFG-R2-MATH-AUDIT-2026-09-15",
  "scope": "single_reference_to_uncertain_healthy_family",
  "current_claim_state": "simulation_model",
  "proposed_repair_state": "conditional_mathematical_specification",
  "redescription_status": "open",
  "bfg_specific_added_value": "not_established",
  "no_retuning_status": "exploratory",
  "transport_decision": "revise",
  "implementation_verified": false,
  "human_review_required": true,
  "independent_review_completed": false,
  "failure_condition": "exclude a true healthy trajectory within all declared bounds",
  "allowed_interpretation": "conditional exclusion of the declared healthy family",
  "forbidden_interpretation": "unconditional physical fault diagnosis or BFG confirmation"
}
```
