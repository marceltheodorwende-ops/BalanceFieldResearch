# Runde 85 – Frische technische Kontrolle der Volltext-Scopeprüfung

Datum: 28. Oktober 2026. Geltung: ausschließlich [DYNAMIC_ORDER_BRIDGE_SCOPE_PROTOCOL.md](DYNAMIC_ORDER_BRIDGE_SCOPE_PROTOCOL.md).

## Ausführung

Das PDF wurde vom Forschungsbranch bezogen. SHA-256-Prüfung: `1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba` (PASS). `pypdf` las 144 Seiten (PASS).

Die frische Endkontrolle prüfte nach Whitespace-Normalisierung 13 feste Textanker auf den PDF-Seiten 27, 28, 29, 54, 62 und 81. Ergebnis: **PASS**.

## Aufbewahrte technische Korrekturen

1. Der erste Wortvergleich scheiterte auf Seite 54, weil der PDF-Extraktor `must change` und `mathematical type` durch einen Zeilenumbruch trennte.
2. Der erste Normalisierungsversuch scheiterte, weil das Aufruf-Quoting die Regex als wörtliches Backslash-S anstatt als Whitespace-Klasse übergab.
3. Der dritte Lauf normalisierte ausschließlich Whitespace korrekt und bestand alle unveränderten Inhaltsanker.

Diese Korrekturen betreffen nur die PDF-Textrepräsentation; der Hash, die Seitenmenge und die Prüfaussagen wurden nicht angepasst. Es gab keine numerische Kalibrierung oder physikalische Parametrisierung.

## Reproduzierbare Prüflogik

1. `sha256(pdf)` gleich dem im Protokoll fixierten Wert;
2. `len(PdfReader(pdf).pages)==144`;
3. die vorab gelisteten Anker liegen nach Ersetzung jeder zusammenhängenden Whitespace-Folge durch ein Leerzeichen auf den jeweiligen Seiten vor.

Die Kontrolle prüft Textpräsenz, nicht den Wahrheitsgehalt der physikalischen Aussagen. Die fachliche Auslegung bleibt auf die zitierten Passagen und die enge Ergebnisformulierung in [DYNAMIC_ORDER_BRIDGE_SCOPE_RESULT.md](DYNAMIC_ORDER_BRIDGE_SCOPE_RESULT.md) begrenzt.
