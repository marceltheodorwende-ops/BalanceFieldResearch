# CTC-SA Referenzimplementierung

Stand: 20.09.2026. Separate Implementierung zum [geprüften mathematischen Modell](../ctc-audit-2026-09-20/CTC_SA_MODEL.md) und [Witness-Erratum](../ctc-audit-2026-09-20/WITNESS_ERRATUM.md). Historische Algorithmen bleiben unverändert.

## Ausführen

Vom Repository-Hauptverzeichnis, mit den bestehenden NumPy-Abhängigkeiten:

```sh
python -m bfg_lab.ctc_sa
python -m unittest discover -s tests -p test_ctc_sa.py -v
```

[Implementierung](../../bfg_lab/ctc_sa.py), [gezielte Tests](../../tests/test_ctc_sa.py), [Beispielausgabe](example.json).

## Zwei getrennte Genauigkeitsbereiche

`projectors_from_certificate` prüft eine vom Aufrufer gelieferte reelle rationale invariante Zerlegung mit dem bestehenden exakten Prüfer `persistence_certificate.verify`. Der persistente Block muss in seiner gelieferten positiven Metrik isometrisch sein; der stabile Block benötigt ein striktes Lyapunov-Zertifikat. Daraus werden sowohl der spektrale/oblique Projektor als auch der graphmetrisch orthogonale Projektor in exakter Brucharithmetik berechnet. Ein leerer stabiler Block ist zulässig, ein leerer persistenter Block nicht. Fehlende Zertifikate werden nicht automatisch gesucht. Eine Ablehnung eines Zertifikats widerlegt nicht die Existenz eines anderen.

`State`, `operators`, `advance` implementieren den endlichen CTC-SA-Zweig mit NumPy. Primitive Daten sind Kapazitäten, Difference-Vektor und eta. R_C, Y, N_R und die Gram-Faktoren werden aus den Modellregeln erzeugt und können nicht unabhängig widersprüchlich eingegeben werden. Die Kapazitäten dürfen in einer beliebigen gemeinsamen unitären Darstellung vorliegen; der neue Zustand wird in orthonormalen Koordinaten des polaren Range ausgegeben. Eigenvektorphasen sind keine physikalischen Daten. Der SA-Rekursionsoperator ist normal; dies ist keine automatische Lösung des allgemeinen nichtnormalen Falls.

## Numerische Grenzen und Terminalität

Die SA-Referenz verwendet TOL=1e-10 für Hermitizität, Kommutativität, spektrale Abstände und volle Unterstützung. Hermitesche Rundungsreste innerhalb der Toleranz werden symmetrisiert. Dies ist eine numerische Konvention, kein exakter Universalitätsnachweis. Sehr kleine Komponenten, nicht auflösbare Spektralgaps, nichtpositive eta, undefinierte Dimensionen oder Unter-/Überlauf können zur Ablehnung führen, auch wenn abstrakte exakte Daten mathematisch zulässig wären.

Ungültige oder numerisch nicht auflösbare Eingaben erzeugen `ValueError`. Nur ein gültiger zweidimensionaler SA-Zustand erzeugt `None` mit Grund `ctc_dimension_floor`. `advance(None)` ist absorbierend. Diese zusätzliche Modellregel ist absichtlich von `formation.formation_gate` getrennt: Das historische Gate behandelt eindimensionale Isolation als vakuos und wird hier nicht geändert.

Der frisch rekonstruierte Gram-Load wird nicht als Kompression des alten Gram-Loads ausgegeben. Der Bericht enthält die Abweichung `gram_inheritance_defect`. Die Energiegrenze wird für die tatsächliche numerische Folge geprüft, ersetzt aber nicht den mathematischen Beweis oder eine Störungsanalyse.

## Öffentliche Schnittstellen

```python
from bfg_lab.ctc_sa import seed, advance, operators

state = seed(5)
while state is not None:
    state, report = advance(state)
    print(report['status'])
```

`operators(state)` gibt unter anderem `spectral_projector`, `metric_projector`, `recursion`, `d_cov`, `b_c`, `gram_from_factors`, `y` und `g` zurück. Im SA-Zweig stimmen beide Projektoren wegen der skalaren Graphmetrik überein. Ihre mögliche Verschiedenheit wird separat mit exakten obliquen Zertifikaten geprüft.

## Unabhängige Prüfwerte

Die Erwartungen im Test stammen aus der vorherigen Bruchrechnung, nicht aus erneutem Aufruf derselben Implementierungsformel:

| Dimension | eta | Energie |
|---|---:|---:|
| 5 | 1 | 10 |
| 4 | 1/5 | 5/6 |
| 3 | 25/624 | 625/23364 |
| 2 | 324480000/164268811201 | 3515200000000/69326858847152401 |

Weitere Tests prüfen oblique versus metrische Projektion, einen anderen positiven Graphoperator, Jordanblock, leeren peripheren/stabilen Raum, ein nichtpositives G, allgemeines eta und nichtuniformen D, unitäre Basisänderung, doppelte Eigenwerte, fehlende volle Unterstützung, nichtkommutierende/nicht-Hermitesche Kapazitäten, Eingabeerhaltung und numerischen Unterlauf.

## Status und weitere Forschung

Dieser Code macht die dokumentierten Modellregeln ausführbar und prüfbar. Er leitet weder ihre Auswahl aus den ursprünglichen BFG-Axiomen her noch validiert er physikalische BFG-Behauptungen. Die drei Auditdokumente bleiben die Grundlage für die Trennung von Definition, bedingtem Satz, numerischer Umsetzung und empirischer Aussage.

Die offene theoretische Aufgabe ist weiterhin die Auswahl der Gram- und Rekursionsregeln: Welche interne Regel unterscheidet beispielsweise r(K) von r(K)^2? Zusätzlich bleiben allgemeine nichtnormale und unendlichdimensionale Erweiterungen eigene Aufgaben. Bestehende Produktionsmodelle werden durch diese Referenz nicht automatisch ersetzt.
