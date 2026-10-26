# Runde84 – frische Kontrolle: Zwei-Sektor-Stromklassifikation

Vorabprotokoll: [TWO_SECTOR_LOCAL_CURRENT_PROTOCOL.md](TWO_SECTOR_LOCAL_CURRENT_PROTOCOL.md).  
Ergebnis: [TWO_SECTOR_LOCAL_CURRENT_RESULT.md](TWO_SECTOR_LOCAL_CURRENT_RESULT.md).

## Durchführung

Die Kontrolle importierte ausschließlich den vorhandenen Update über `audit.load_update()`; dieser prüft vor Import die Blob-ID `ff8b0a7ec922ccfeacae5bc9ce6c104b79286498`. Keine Quell-, Audit-, Workflow- oder Manuskriptdatei wurde verändert.

Für jeden nichtterminalen Schritt wurde mit dem aktuellen (Z) und ({E_+,E_-}) gerechnet:
[
 delta q_pm(A)=
 operatorname{tr}(E_{pm,+}A_+)-operatorname{tr}(E_pm A),
 quad
 r_Phi(A)=|A_+-VPhi_c(A)V^dagger|,
]
[
 r_{m coh}(A)=
 |operatorname{off}_{Z_+}(V^dagger A_+V)-coperatorname{off}_Z(A)|.
]
Hier sind (A=K,F,W), (V=mathrm{t4}), (Z_+=VZV^dagger), und (c) wird aus (alpha) und den beiden Sektorlasten der tatsächlichen Eingabe bestimmt.

## Festgelegte Eingaben

1. Kompatible Viermoden-Präparation:
   [
   Z=operatorname{diag}(1,1,-1,-1),quad
   Y=operatorname{diag}(.2,.2,.6,.6),quad K=mathbf1mathbf1^dagger,
   ]
   [
   F=operatorname{diag}(1,2,3,4),quad
   W=operatorname{diag}(.4,.1,.2,.3).
   ]
   Zwei Ereignisse, danach identische komplex-unitäre Eichkopie mit Seed (20261026).

2. Gleiche Präparation, einmal mit (W_{13}=W_{31}=.1), einmal mit (F_{13}=F_{31}=.2). Je ein Ereignis.

3. Tatsächlicher Runde80-Seed:
   [
   v=(sqrt3/2,1/2)^T,quad P=F=W=vv^dagger,quad
   Y=operatorname{diag}(1/4,1/2),quad K=-operatorname{diag}(1,2).
   ]
   Nach seinem ersten nichtterminalen Ereignis ein Folgeereignis; zusätzlich eine komplex-unitäre Eichkopie mit demselben Seed.

## Ausgabe

```json
{
  "status": "PASS",
  "original_calls": 8,
  "tolerance": 1e-10,
  "compatible": {
    "c_step_1": 0.8788174152965355,
    "c_step_2": 0.995974327341904,
    "max_sector_change": 4.440892098500626e-15,
    "max_channel_residual": 6.2378128349854145e-15,
    "max_coherence_residual": 3.3601491028851666e-15
  },
  "off_channel_but_sector_preserving": {
    "witness_channel_defect": 0.017137805481106588,
    "formation_channel_defect": 0.034275610962213175,
    "max_sector_change": 4.440892098500626e-16
  },
  "actual_seed_followup": {
    "c": 0.5815270582438091,
    "witness_channel_defect": 0.10232050639641901,
    "formation_channel_defect": 0.025580126599104802,
    "max_sector_change": 2.220446049250313e-16
  },
  "complex_seed_followup": {
    "witness_channel_defect": 0.10232050639641892,
    "formation_channel_defect": 0.025580126599104913,
    "max_sector_change": 4.440892098500626e-16
  }
}
```

## Retained Kontrolle

Der erste Ausführungsentwurf erwartete bei den beiden Kohärenzpräparationen irrtümlich einen nichtverschwindenden diagonalen Sektortransfer. Die vorab relevantere Kanaldefektprüfung bleibt jedoch bestehen und zeigte die angegebenen Defekte. Der Befund selbst ist stärker und enger: Selbst dort bleibt (J=0); nur die gemeinsame Kohärenzkanalbeschreibung von (F/W) bricht. Keine Kennzahl wurde angepasst oder als physikalische Größe umgedeutet.
