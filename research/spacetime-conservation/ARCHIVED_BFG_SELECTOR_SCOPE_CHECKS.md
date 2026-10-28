# Runde82 – Reproduzierbare Archiv- und Scope-Prüfung

## Vorabkriterium

Siehe [PROTOCOL.md](PROTOCOL.md): Positiv wäre nur eine vorhandene Regel, die aus BFG-Daten allein eine eindeutige Zustands-/Operatorzuordnung liefert und den Runde80-Seedzeugen ohne Zusatzannahme abdeckt.

## Frische Ausführung

Am 26. Oktober 2026 wurde die unveränderte DOCX-Primärdatei mit der lokalen gebündelten Python-Laufzeit gelesen (nur `zipfile`, `re`, `hashlib`). Die Prüfung extrahierte `word/document.xml`, bildete SHA-256 über die unveränderten Bytes und prüfte diese drei exakten Scope-Aussagen:

```text
sha256 = 9784c915d4b060dae068258166fe46448694cd32055eed69b00ecda6703eb6c2
"LPCP is introduced as a new BFG physical principle, not promoted retroactively to a Level-0 theorem." = True
"under an explicitly stated quadratic-causality assumption" = True
"under the standard consistency assumptions" = True
```

Die drei Treffer zeigen nicht bloß, dass das Archiv über Raumzeit spricht, sondern dass sein Brückenbaustein als zusätzliche physikalische Annahme ausgewiesen ist. Er kann daher unter der Quellenbindung des Mandats nicht stillschweigend als Konsequenz des gepinnten vollständigen Updates verwendet werden.

## Getrennte Evidenz

Dies ist eine lokale Text-/Integritätskontrolle, keine GitHub-CI-Ausführung und keine numerische Prüfung des Dynamic-Order-Updates. Die bestehende CI wird nach diesem Dokumentationscommit separat verfolgt.
