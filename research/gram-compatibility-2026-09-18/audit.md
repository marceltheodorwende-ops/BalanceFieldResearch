# Auditprotokoll

Die drei Auditwerkzeuge sind über das bestehende
[Quellenregister](../prediction-audit-2026-09-18/sources.json) identifiziert.

- Complete Edition: Neuer Satz ist explizit bedingt; der Gegenfall ist auf
  die genannte lokale Klasse begrenzt. G1 wird nicht rückwirkend zum Quellenaxiom.
- Workflow Master: Der negative Kompatibilitätsbefund bleibt erhalten;
  keine Änderung der Originale und keine Ausblendung von Kanalverlusten.
- Context Recovery: „DKF“ wurde im Gesprächskontext als D_cov c interpretiert.
  Die Autorisierung zum Arbeiten ist keine mathematische Prämisse.

Quellenprüfung: V2 §6 Gl.22–24, §9 Gl.49–50 und §24 sowie V4 Gl.37–41.
Die flache Ableitung auf dem Operatorfeld und die konstante Trägerbasis sind
explizite lokale Realisierungsannahmen. Es wird nicht behauptet, V2 definiere
damit bereits jeden kovarianten Ableitungsfall vollständig.

Verifikation: Der geschlossene Gegenfall wurde analytisch ausgerechnet und mit
den bestehenden Funktionen `prepare_candidate` und `gram.rebuild` kontrolliert.
`check.py` prüft den Gate-Erfolg, den tatsächlich erzeugten Polarträger, beide
Lasten, den Verlustterm sowie einen kompatiblen Kontrollfall. Zahlen nahe eins
werden als Fließkommawerte ausgegeben; der exakte Beweis steht im Haupttext.
Keine empirischen Daten, kein vollständiger Universalitätsbeweis.

Abschlussentscheidung: bedingte interne Gram-Herleitung erreicht;
allgemeine interne Herleitung von G1 nicht erreicht und im geprüften Fall
mit der induzierten Rekonstruktion unverträglich. Die frühere G1-Stufe bleibt
als historischer Vorschlag bestehen, die neue Stufe dokumentiert ihre Prüfung.
