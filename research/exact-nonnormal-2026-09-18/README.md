# Exakte Zertifikate für endlichdimensionale nichtnormale Persistenz

Ausgangsstand: 027cfa6f2299d449edb9106a84b206305942e8b4.
Ergebnis: implementierter exakter Prüfer für **gelieferte** rationale
Zerlegungen und Metriken. Keine automatische Lösung für beliebige Operatoren,
keine Rekonstruktion von R_next und keine vollständige Lösung von Problem 6.

## Zertifikat und Satz

Für eine reell-rationale Matrix R liefert der Aufrufer eine invertierbare
rationale Basis S und eine Blockdimension p, so dass

    S^-1 R S = diag(A,T).

Zusätzlich liefert er rationale symmetrische positiv definite M,N mit

    A^T M A = M,
    N - T^T N T > 0.

Leere Blöcke sind erlaubt; ihre Metrik wird als [] angegeben.
Erfüllt das Zertifikat diese exakten Identitäten und Ungleichungen, ist R
potenzbeschränkt, die ersten p Spalten von S spannen genau den peripheren
Eigenraum auf und die übrigen Spalten den stabilen verallgemeinerten Eigenraum.

Beweis: A ist eine Isometrie in der M-Norm und invertierbar; in orthonormalen
Koordinaten für diese Norm ist A orthogonal. Seine Eigenwerte liegen auf dem
Einheitskreis und sind über C semisimpel. Für T zeigt die strikte Lyapunov-
Ungleichung, dass das Maximum von ||Tx||_N² auf der kompakten Einheitssphäre
||x||_N=1 kleiner als eins ist. Also existiert q<1 mit ||T^k||_N<=q^k.
Ähnlichkeit durch S verändert die Normschranken nur um eine feste Konstante.
Damit ist die Zerlegung genau persistent/stabil; die Aussage setzt keine
Normalität von R in der ursprünglichen euklidischen Norm voraus.

Die zugehörige Spektralprojektion ist

    P_spec = S diag(I_p,0) S^-1.

Sie kommutiert mit R und ist idempotent, aber im Allgemeinen nicht orthogonal.
Sie ersetzt nicht den BFG-Metrikprojektor W(W†GW)^-1 W†G. Eine Gleichsetzung
dieser Projektoren wurde bereits im früheren Audit ausgeschlossen.

## Implementierung

`bfg_lab.persistence_certificate.verify` prüft mit `fractions.Fraction`:
Dimensionen, rationale Eingaben, Invertierbarkeit, exakt verschwindende
Nebenblöcke, Metriksymmetrie, positive Definitheit und beide Transportbedingungen.
Positive Definitheit wird durch exakte positive Schurkomplement-/LDL-Pivots
geprüft. Weder Eigenwertrundung noch Toleranz am Einheitskreis ist beteiligt.

Beispiel:

```python
from bfg_lab.persistence_certificate import verify

certificate = verify(
    [[1, 1], [0, '1/2']],
    [[1, -2], [0, 1]],
    1, [[1]], [[1]],
)
assert certificate['spectral_projector'] == [[1, 2], [0, 0]]
```

Dies zertifiziert den bekannten nichtnormalen Gegenfall mit obliquer Projektion.
Ein stabiler Jordanblock ist zulässig, wenn seine Lyapunov-Metrik mitgeliefert
wird. Ein nichttrivialer Jordanblock auf dem Einheitskreis erfüllt das
Persistenzzertifikat nicht. Eine beliebig nahe, aber echt innere rationale
Eigenzahl wird nicht irrtümlich zur persistenten Mode erklärt.

## Grenzen

Ein abgewiesenes Zertifikat beweist nur, dass die gelieferten Daten die
Prüfbedingungen nicht erfüllen; es beweist nicht die Unmöglichkeit anderer
Zertifikate. Die Funktion sucht weder S noch M,N. Es wird keine Vollständigkeit
für rationale Zertifikate aller reell-rationalen R behauptet. Komplexe
Eingabeoperatoren, irrational spezifizierte Daten und unendliche Räume sind
außerhalb dieser Implementierung. Große Brüche können hohe Rechenkosten verursachen.
Ein Zertifikat eines R sagt nichts darüber aus, ob BFG dieses R intern erzeugt.

Die bestehende `core.persistent_basis` bleibt unverändert und weiterhin auf
normale numerische Eingaben beschränkt. Der neue Prüfer ist ein separater,
expliziter Nachweisweg; er wird nicht unbemerkt in die Universaliteration eingebaut.

## Audit

Complete Edition: bedingter mathematischer Satz, exakte Implementierung und
empirische Aussagen getrennt; kein Zertifikatversagen als Operatorwiderlegung.
Workflow Master: eigener Prüfgegenstand und neue Stufe, alte Ergebnisse erhalten.
Context Recovery: verwendet den korrigierten peripheren Persistenzbegriff aus
dem [Vorschlag](../../docs/PERSISTENCE_PROPOSAL.md), nicht die fehlerhafte
Span-Definition als angeblich äquivalent. Die drei Auditdateien bleiben durch
das [Register](../prediction-audit-2026-09-18/sources.json) identifiziert.

Quellenbezug: V4 Gl.27–29 und die dokumentierte interne Korrektur; der obige
lineare-algebraische Beweis ist vollständig angegeben. Keine Naturbestätigung.
