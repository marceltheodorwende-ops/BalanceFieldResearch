# Galaxienzweig: Nullvergleich vor Datenfit

## Exakte algebraische Überlappung

V2 §14 Gl.91–96 setzt X=|grad Psi|²/a_Q² und mu(X)=sqrt(X/(1+X)).
Für x=|grad Psi|/a_Q >= 0 folgt exakt

    mu(x²) = x/sqrt(1+x²).

Dies ist die Standard-MOND-Interpolationsfunktion bei Famaey und Binney,
[Modified Newtonian Dynamics in the Milky Way](https://arxiv.org/pdf/astro-ph/0506723),
S.3, Tabelle 1. Die nichtlineare Poisson-Gleichung hat die AQUAL-Form von
[Bekenstein und Milgrom (1984)](https://doi.org/10.1086/162570).
Die Gleichsetzung betrifft diesen quasistatischen Zweig bei gleicher Quelle,
G_BFG=G, a_Q=a_0 und gleichen Randbedingungen. Sie behauptet keine Gleichheit
der vollständigen Theorien und keine Bestätigung von MOND.

In Kugelsymmetrie gilt mu(g/a_Q) g=G_BFG M(r)/r². Mit q=G_BFG M(r)/(a_Q r²)
und t=(g/a_Q)² ergibt sich t²=q²(1+t). Die nichtnegative Lösung ist

    g/a_Q = sqrt((q² + q sqrt(q²+4))/2).

Damit reproduziert die Umformung V2 Gl.102. Im tiefen asymptotischen Regime
folgt v_f^4=G_BFG a_Q M. Das allein unterscheidet den Zweig nicht von obiger Null.

## Möglicher Unterschied und seine Entartung

V2 §14.2 ergänzt M=M_b+M_Omega. Für M_b>0 folgt unter denselben Regimeannahmen

    Delta = log10[v_f^4/(G_BFG a_Q M_b)]
          = log10(1+f_Omega),  f_Omega=M_Omega/M_b.

Das ist eine bedingte Folgerung, keine neue Messung. Ein konstanter unbekannter
f_Omega ist in einer freien Normalisierung a_Q absorbierbar. Ein empirischer
Unterscheider verlangt daher unabhängig bestimmte Normalisierung oder einen
vorhergesagten variierenden Verlauf. Frei aus den Prüfgeschwindigkeiten
rekonstruierte Omega-Massen wären keine unabhängige Vorhersage.

## Prüfplanentwurf mit Freigabekriterien

1. Eine vorgelagerte Realisierung liefert G_BFG, a_Q, rho_Omega und deren zulässige
   Unsicherheit; alternativ unabhängige Kalibrierung mit klar begrenztem
   Geltungsanspruch. V2 §23 nennt diese Herleitung noch offen.
2. Stichprobe, Qualitätsfilter, Einheiten, Distanzen, Inklinationen,
   Masse-Licht-Verhältnisse, äußeres Feld und deren Kovarianzen vor Auswertung
   festlegen. Galaxiengeometrie berücksichtigen: die Kugelformel gilt nicht
   pauschal für vollständige Scheibenrotationskurven.
3. Vorhersagen pro Objekt mit Modellversion und Hash einfrieren. Für Scheiben
   die Feldgleichung lösen oder die asymptotische Näherung mit Fehlergrenze
   begründen. Keine frei nachgeführten Haloprofile.
4. Als primären Endpunkt die gemeinsame Vorhersagegüte der gehaltenen
   Geschwindigkeiten bzw. der vorab gewählten Delta-Residuals verwenden.
   Passende Standard-MOND-Null sowie Newton/GR mit klar spezifizierter
   Materiemodellierung einschließen. Gleiche Daten und faire Kalibrierbudgets.
5. Fehlerverteilung, numerische Fehler, Teststatistik, Signifikanz-/Entscheidungsgrenze,
   Teststärke und Umgang mit Mehrfachtests vor Datenprüfung bestimmen.
   Hier wird keine unbegründete Zahl als fertige Schwelle eingesetzt.
6. Negative Ergebnisse und fehlende Unterscheidbarkeit veröffentlichen. Eine
   Modellrevision ist eine neue explorative Stufe und braucht neue Prüfdaten.

[SPARC](https://arxiv.org/abs/1606.09251) ist ein möglicher Datenbestand für
Scheibengalaxien. In dieser Stufe wurden keine Rotationskurven ausgewertet.
Öffentliche, bereits modellprägende Daten sind nicht automatisch ein blinder
Bestätigungssatz. Ein Datensplit allein entfernt diese Vorgeschichte nicht.

**Entscheidung:** Freigabe für eine bestätigende Auswertung noch nicht erreicht.
Die Rekonstruktion und die unabhängige Parameter-/Observablenbrücke kommen zuerst.
