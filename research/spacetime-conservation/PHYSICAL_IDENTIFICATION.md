# Physikalische Identifikation von Energie und Impuls – Runde 39

## Ergebnis und Geltungsbereich

**Eine physikalische Identifikation ist im geprüften BFG-Stand noch nicht hergeleitet.** Vorhanden sind mathematisch belastbare Bestands- und Austauschbilanzen. Das Manuskript selbst verlangt für Energie und Impuls zusätzliche, unabhängig kalibrierte Messbrücken. Die direkte Gleichsetzung der bisherigen Bestände mit einem vollständigen physikalischen Energie-Impuls-Strom ist damit nicht gerechtfertigt.

Dies ist keine Widerlegung jeder möglichen BFG-Brücke. Untersucht sind der gepinnte endliche Kernel, seine bisherigen Beobachtungen und zwei natürliche additive Gesamtbestände; keine fremde Theorie und keine neu erfundene physikalische Dynamik. Vorabprotokolle stehen in PROTOCOL.md. Ausgangs-Head: 8189830b17da41e193b1caeb7f64cc16e1d5abc3.

## 1. Was die BFG-Quelle tatsächlich festlegt

Quelle: vollständiges Dynamic-Order-Manuskript vom 8. Oktober 2026, SHA256 aus SOURCE_MANIFEST.json; frisch geprüfter lokaler PDF-Hash stimmt überein. Seitenangaben beziehen sich auf PDF-Seiten von 144, nicht die abweichende innere Druckzählung.

| Fundstelle | Quelleninhalt, paraphrasiert | Konsequenz |
| --- | --- | --- |
| I41, PDF40–41 | Physikalische Messung benötigt Mphys mit Kalibrierung und Apparatur. Energie: M_E und Quantenbrücke; Impuls: Generator-/Kinematikabbildung sowie Raumzeit- und Quantenbrücke. | Die Benennung eines Matrixbestands ersetzt diese Abbildungen nicht. |
| I55–56, PDF53–54 | Ereigniszahl ist keine physikalische Zeit. Tclock liefert Dauern; positive interne Gramgeometrie ist nicht die Lorentzmetrik. | Strom pro Ereignis ist noch kein Strom pro Sekunde durch eine räumliche Fläche. |
| I68.2, PDF59 | Ein Energie-Hamiltonoperator kommt aus einer Quantenbrücke; Spektroskopie prüft dessen kalibrierte Differenzen. | K ist damit nicht bereits als Hamiltonoperator identifiziert. |
| I70.1–6, PDF60–61 | Y, Geometrie und Witness sind dimensionslos; K und F teilen eine Formationseinheit EF. EF ist nicht als Joule festgelegt. Sekunden verlangen Tclock; Teilchen-/Quantenobservablen benötigen passende Dimensionen oder feste Umrechnungen. | Gemeinsame Typisierung macht K+F mathematisch möglich, nicht automatisch physikalisch. |
| II86.1, PDF75 | Die kreuzgewichtete Lastgleichheit ist algebraisch und kein physikalischer Energieerhaltungssatz. | alpha Lambda_C = beta Lambda_B ist keine zusätzliche Energiequelle. |
| II86.2, PDF76 | Delta tr F = s_F - ell_F; der Bestand hat Formationseinheiten, ohne Brücke keine physikalische Masse/Energie. | Seed und Auswahl müssen explizit bilanziert bleiben. |

Keine Aussage, das gesamte Repository enthielte überhaupt keine Energiebegriffe oder physikalischen Ansätze. Die Quelle enthält gerade solche **bedingten Brückenvorschläge**; deren Voraussetzungen werden hier nicht als bereits bewiesene Messidentifikation behandelt. Empirische EEG-/Pendeldaten werden in dieser Runde weder neu ausgewertet noch als Energiemessung umgedeutet.

## 2. Kandidatenprüfung

| Kandidat | Geprüft vorhanden | Fehlende bzw. verletzte Identifikationsbedingung |
| --- | --- | --- |
| tr K | Erhaltung im vollen Persistenzsektor; allgemeiner Defekt tr K(D-I). | Nicht allgemein erhalten über Auswahl/Rangwechsel; keine M_E oder SI-Kalibrierung. |
| tr(PK) | Eigene aktive Bestandsbilanz aus Runde38. | Vom ambienten Bestand verschieden; Seed-/Trägerwechsel verändern ihn. |
| tr F | Exakte Formation-Seed-Verlustbilanz II86.2. | Kein isoliert erhaltener Energiebestand; EF allein ist keine Energieeinheit. |
| tr K + tr F | Natürliche Addition gleich typisierter Größen. | Bereits der exakte Runde38-Zeuge: Delta=11/2+9/4=31/4. Universelle Erhaltung dieses Kandidaten widerlegt. |
| tr(PK) + tr F | Im einfachen Rang-eins-Seedzeugen kompensieren sich -9/4 und +9/4 exakt. | Allgemeine Rechnung unten zeigt einen zusätzlichen Transport-/Auswahlrest; neue numerische Quellfälle haben nichtverschwindende Defekte. |
| tr(rho_F K), normalisierte Erwartungen | Früher geprüfte Nichtinvarianz/Fasergrenzen. | Keine neue Konservierung durch Umbenennung; bei unnormalisiertem F zudem Einheit EF² statt EF. |
| Lokale q_a=tr(E_a K), J_ab | Exakte feste-/wechselnde-Cover- und Rangbilanzen, Runden36–38. | Effektlabels sind keine hergeleiteten Raumorte; Zuordnungswechsel können q ändern bei dynamischem Strom0. Kein physikalisches Flächen-/Zeitmaß. |
| Vier Pauli-Koeffizienten einer Zweimodenkompression | Herm(C²)-Determinante besitzt algebraische Lorentzsignatur; bedingte Gedächtnissätze. | Kein allgemeiner Lorentz-Transport: transversale Komponenten werden durch h verändert; Nullkegeldefekte, Auswahl-/Geschlossenheitsgrenzen bleiben. Vier Zahlen allein liefern keinen Energie-Impuls-Vektor. |

K kann im zulässigen Kernel negativ sein; der Seed verlangt eine negative komprimierte Richtung. Das ist kein allgemeines physikalisches Energie-No-Go: Energieverschiebungen und andere Brücken müssen gesondert definiert werden. Hieraus folgt lediglich, dass Positivität einer Formation nicht stillschweigend auf K übertragen werden darf.

## 3. Neue exakte Bilanz des kombinierten aktiven Bestands

**Unter BFG-Annahmen abgeleitet**, kanonische gemeinsame Formationseinheit bzw. numerische Seed-Konvention kappa_F=1. Sei U_C,U_B die tatsächliche rechteckige Analysezerlegung und S4 der vor dem Seed transportierte aktive Projektor. Definiere
B4=sum_r U_r S4 U_r†.
Das vollständige Ereignis liefert K_+=sum_r U_r† K U_r.
Bei vorhandenem Seed gilt P_+=S4+Pi_seed, tr(Pi_seed K_+)=lambda<0 und s_F=-lambda. Ohne Seed sind beide Zusatzterme0. Folglich

Delta[tr(PK)+tr F] = tr[K(B4-P)] - ell_F.

Beweis: aktive Kernelspur zerfällt in tr(K B4)+lambda; die Formationsspur ist tr F-ell_F-lambda. Die expliziten Seedterme heben sich auf. Das erfordert **nicht**, dass B4=P gilt. Der bekannte einfache Rang-eins-Zeuge erfüllt die zusätzliche Kompensation, allgemeine Teilträgerzustände müssen sie nicht erfüllen.

Mit anders dimensionierten Brücken wäre kappa_F bzw. ein zuvor fixierter Umrechnungsfaktor zu berücksichtigen; die jetzige Addition ist keine nachträglich kalibrierte Energieformel. Auch die ambiente Addition hat weiterhin den Defekt tr K(D-I)+s_F-ell_F.

Frische originale Quellaufrufe mit vorab fixiertem Seed20261024:

| Eingangs-/Ausgangsdimension | Delta tr K | Delta tr(PK) | Delta tr F | Delta ambient+F | Delta aktiv+F |
| --- | ---: | ---: | ---: | ---: | ---: |
| 3 -> 2 | 6.135961034677335 | -3.5120253989046404 | 3.5120253989046404 | 9.647986433581975 | 0 |
| 4 -> 4 | 2.797022356808945 | -6.282872596278985 | 6.269391989809019 | 9.066414346617965 | -0.013480606469965295 |
| 5 -> 4 | 1.6198883644781858 | -17.32557755933555 | 17.35517608794662 | 18.975064452424807 | 0.029598528611071373 |

Alle drei Ereignisse nichtterminal. Werte sind **numerische Gegenkontrollen**, keine rational exakten Gegenbeweise und kein zusätzlicher CI-Test. Die Differenzen der letzten beiden Fälle liegen weit über bloßer Rundungsgröße; eine intervallzertifizierte/exakte Gegenkonstruktion bleibt eine mögliche weitere mathematische Absicherung. Das ambiente No-Go besitzt bereits den exakten Zeugen oben.

Reproduktion im vorhandenen Auditverzeichnis:
```python
import numpy as np
import audit
update = audit.load_update()
rng = np.random.default_rng(20261024)
for n in (3, 4, 5):
    z = audit.complex_unitary(rng, n)
    p = z[:, :n//2] @ z[:, :n//2].conj().T
    z = audit.complex_unitary(rng, n)
    y = (z * np.linspace(.15, .7, n)) @ z.conj().T
    f = p @ audit.pos(rng, n) @ p
    w = p / (n//2)
    k = -audit.pos(rng, n)
    out = update(k, f, w, y, p)
    assert out["terminal"] is None
    dk = np.trace(out["k"]).real - np.trace(k).real
    da = np.trace(out["p"] @ out["k"]).real - np.trace(p @ k).real
    df = np.trace(out["f"]).real - np.trace(f).real
    print(n, len(out["k"]), dk, da, df, dk+df, da+df)
```
Die letzte Gesamtspur kann sich je nach Additionsreihenfolge um etwa 1.8e-15 unterscheiden. Der feste Vierdimensionalfall ist zusätzlich als volle Eingabematrix in [PHYSICAL_IDENTIFICATION_FIXTURE.md](PHYSICAL_IDENTIFICATION_FIXTURE.md) gespeichert. Ein nach erfolgreicher Rechnung entstandener Werkzeug-Wrapperfehler beim Speichern der Ausgabe betraf keine Quellberechnung; die erneute Ausgabe zur Fixture-Erfassung bestätigte dieselben Werte.

## 4. Neue Skalierungsprüfung: was der Kernel nicht kalibriert

**Exakt unter BFG-Annahmen:** Für jedes lambda>0 definiere S_lambda(K,F,W,Y,P)=(lambda K,lambda F,W,Y,P).
Die Selektion hängt von Y,P,W ab und bleibt gleich. F_sel und beide Lasten skalieren mit lambda; ihre Quotienten alpha,beta bleiben gleich. Analyse, SVD-Räume, Y_+, Witness und S4 bleiben gleich bis auf zulässige Eichwahl. K_+ und der transportierte Formationsteil skalieren. Die Eigenwerte der Seedkompression skalieren mit lambda, ihre Ordnung, Vorzeichen und Einfachheit bleiben gleich; derselbe Seedprojektor und sein lambda-facher Bestand resultieren. Daher gilt auf den mathematischen nichtterminalen Strata

U_BFG S_lambda = S_lambda U_BFG

als Gleichheit der Eichklassen. Exakte Terminalentscheidungen bleiben ebenfalls erhalten. Das ist **Homogenität der Formationseinheit**, keine Aussage, skalierte Zustände seien physikalisch identisch, und kein Beweis, Energie lasse sich grundsätzlich nicht kalibrieren. Endliche numerische Toleranzen können nahe Stratumgrenzen anders reagieren.

Frisch kontrolliert bei lambda=3.7: volle Persistenz n=2, K=[[2,.2i],[-.2i,1]], F=diag(1,2), W=I/2,Y=diag(.2,.4),P=I; außerdem der exakte Seedzeuge aus Runde38. Je Originalzustand und skalierter Zustand ein Quellaufruf, insgesamt4. Alle fünf Ausgangsfelder korrekt skaliert/gleich; maximaler normierter Rest6.6099991313257e-16. Seed-Formationsgewinn beim unskalierten Zeugen2.249999999999999. Drei zusätzliche Bestandsfälle ergeben insgesamt7 neue unterschiedliche Quellaufrufe; reine Wiederholungen zur Fixture-Erfassung sind darin nicht doppelt gezählt.

Der Kernel allein wählt damit keinen Zahlenfaktor Joule/EF. Eine unabhängige Kalibrierung kann diesen wählen, ersetzt aber weder die Raum-/Zeitabbildung noch ein Erhaltungsgesetz.

## 5. Konkret nächster notwendiger Schritt

Keine weitere Umbenennung von q oder Spur. Eine physikalische Brücke muss vor ihrer Prüfung Folgendes festlegen:

1. **Energieablesung:** entweder einen konkreten Operator H(Ξ) mit festgelegter Zustandsabbildung rho_Q oder eine konkrete skalare M_E. K als H bleibt eine zu prüfende Hypothese; rho_W und F/tr F sind laut I57 verschiedene Kandidaten. Einheit und Nullpunkt unabhängig fixieren.
2. **Impuls und Transport:** aus BFG-Daten bestimmte räumliche Relationen, lokale Träger, physikalische Uhr und die Wirkung räumlicher/zeitlicher Transformationen angeben. Dann erst prüfen, ob die Komponenten die beanspruchten Generator-/Vierervektorrollen erfüllen. Interne unitäre Eichkovarianz ersetzt keinen physikalischen Boost.
3. **Vollständige Bilanz:** am unveränderten Update zeigen, welche Quelle, welcher Fluss und welche Reserve die oben berechneten Auswahl-/Transportreste trägt; physikalische Energie nicht durch eine rückblickend definierte Gegenbuchung erzwingen.
4. **Unabhängiger Test:** Zustandspräparation aus D_prep, festgelegte Apparaturabbildung und Unsicherheiten; danach Holdout-Spektroskopie/Kalorimetrie bzw. Rückstoß-/Impulsmessung gemäß I41/I68–69. Eine vorhandene empirische Anpassung ist nicht automatisch dieser Test.

Innerhalb der jetzigen rein mathematischen Quelle lässt sich als nächstes die exakte Struktur von B4-P und die Stabilität der kombinierten Bestandsdefekte weiter prüfen. Ein **physikalischer** Fortschritt benötigt dagegen eine inhaltlich bestimmte und unabhängig prüfbare M_E-/Raumzeit-/Quantenbrücke. Diese fehlende Auswahl wird nicht automatisch durch zusätzliche Matrixidentitäten geschlossen. Keine vollständige Einstein-Herleitung behauptet.

## Validierung

Dokumentationsrunde: keine Änderung an Quellcode, Auditcode, Workflow, Anforderungen, Manuskript oder empirischen Dateien. Frische Beweise, Quellenlektüre, PDF-Hash und sieben unterschiedliche Original-Quellaufrufe wie oben; erneute Fixture-Erfassung getrennt. Keine neue Remote-CI-Ausführung behauptet. Der zuletzt CI-geprüfte Code bleibt 7d0cc91bf7d1023a9c3cd32f127e52ef5d8722f9 mit den in CI_VALIDATION.md dokumentierten beiden erfolgreichen Runde38-Läufen. Neue Dokumentationscommits sind kein zusätzlicher Remote-Test der numerischen Gegenkontrollen.
