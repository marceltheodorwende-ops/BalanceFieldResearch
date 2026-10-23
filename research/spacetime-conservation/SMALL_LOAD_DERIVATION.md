# Kleinlast-Randkarte mit relativer Lastform

## Quellenbereich und Koordinaten
[BFG-abgeleitet] Unveränderte gepinnte Vollpersistenzquelle, F>0, Y>0 und Y<I. Schreibe <X>_F=tr(FX)/tr(F) und

    s=<Y>_F>0, Z=Y/s, <Z>_F=1, mu2=<Z²>_F>=1.

Die letzte Ungleichung folgt aus der positiven formationsgewichteten Varianz. Diese skalare Normierung ist invariant unter simultaner unitärer Basisänderung; Z transformiert kovariant. Für s>0 sind (s,Z) exakt zu Y äquivalent. Dies ist eine Koordinatentrennung und keine Dimensionsreduktion oder neu erfundene Zustandsvariable. F,W,K bleiben erhaltene Eingabedaten im bisherigen Sinn; K wird weiterhin durch den Quellkanal aktualisiert.

## Exakte endliche relative Form
Setze C_s=(I+sZ)^(-1) und

    r_s=<Z² C_s>_F/<C_s>_F,
    alpha=s² r_s/(1+s² r_s), beta=1/(1+s² r_s),
    G_s=(r_s I+Z²)(I+sZ)^(-2)/(1+s² r_s).

Direktes Einsetzen in die vollständige ausgerichtete BFG-Form ergibt

    Y_+=s² G_s,
    s_+=s² <G_s>_F,
    Z_+=G_s/<G_s>_F,
    T_C=sqrt(r_s)(r_s I+Z²)^(-1/2),
    T_B=Z(r_s I+Z²)^(-1/2),
    K_+=T_C K T_C+T_B K T_B.

Der gemeinsame s-Faktor der beiden Kanaloperatoren kürzt sich exakt. Daher kann der Kernelkanal trotz kleiner absoluter Last einen endlichen Effekt besitzen. r_s bleibt die aktuelle, aus F und Z abgeleitete Quellgröße; keine Umgebung wurde eingefroren oder entfernt. Die endlichen Gleichungen bilden mit F,W den bisherigen vollständigen Zustand nur in anderen Koordinaten ab.

## Abgeleitete Randdynamik
Für festes positives Z in endlicher Dimension und festes F>0 gilt r_s=mu2+O(s). Folglich

    alpha=s² mu2+O(s³),
    Y_+=s²(mu2 I+Z²)+O(s³),
    s_+=2mu2 s²+O(s³),
    Z_+ -> R_F(Z)=(mu2 I+Z²)/(2mu2).

R_F(Z)>0 und <R_F(Z)>_F=1. Die formationsgewichtete Normierung wird also exakt im Grenzbild erhalten. Der zugehörige Kernelkanal ist

    Psi_Z(K)=T_C0 K T_C0+T_B0 K T_B0,
    T_C0=sqrt(mu2)(mu2 I+Z²)^(-1/2),
    T_B0=Z(mu2 I+Z²)^(-1/2).

Da T_C0²+T_B0²=I, ist dieser Randkanal vollständig positiv, unital und spurtreu. Gemeinsam mit R_F ist er eine explizite quellenabgeleitete **relative Randkarte**. Der führende s²-Skalenschritt und die relative Form werden aus derselben Dynamik gewonnen.

s=0 ist dabei eine mathematische Grenzkarte mit zusätzlicher relativer Richtungsinformation, kein zulässiger Quellenaufruf, kein nachgewiesener physikalischer Randzustand und keine automatisch kontrollierte unendliche Ereignisfolge. Die O-Terme gelten bei fester Präparation; uniforme Langzeitkontrolle oder gemeinsam singuläre Z/F-Grenzen werden nicht behauptet.

## Endlicher Kernelsprung trotz Y->0
In einer Z-Eigenbasis ist der Grenzfaktor

    h0_ij=(mu2+z_i z_j)/sqrt[(mu2+z_i²)(mu2+z_j²)].

Er ist genau dann eins, wenn z_i=z_j. Der Grenzkanal ist deshalb genau für skalares Z die Identität auf allen Kerneln. Für einzelne mit Z kommutierende K kann der Sprung auch bei nichtskalarem Z verschwinden; das ist keine allgemeine Kanalidentität.

Der vorab festgelegte exakte Zeuge lautet

    F=I2, Z=diag(1/2,3/2), W=I2/2, K=ones(2,2)/2.

Hier mu2=5/4, R_F(Z)=diag(3/5,7/5), h0_12=4/sqrt(21)<1. Die vollständige endogene Formationsformel ist

    alpha(s)=(3s³+5s²)/(3s³+5s²+4s+4).

Es folgen Y_+/s²->diag(3/2,7/2) und ein strikt positiver Kernel-Normsprung

    ||Psi_Z(K)-K||_F=(1-4/sqrt(21))/sqrt(2)≈0.0898934.

Zum Vergleich halte dasselbe F,W,K fest und setze Z=I2. Dann Y=sI2->0, aber der Kernelkanal ist für jedes s>0 exakt die Identität. Beide rohen Lastpfade haben denselben Grenzwert Y=0, während ihre Kernel-Folgewerte verschiedene Grenzwerte besitzen. Somit gibt es keine einzige stetige Fortsetzung dieses ausgerichteten Kernelupdates an den rohen Null-Lastpunkt, die beide Pfade identifiziert. Die relative Randkarte behält genau diese zusätzliche Richtungsinformation.

Dies ist ein begrenzter Befund über diesen Grenzpunkt und die unveränderten Koordinaten, kein allgemeines Verbot anderer Raumzeit-/Zeitkonstruktionen. Insbesondere macht Y->0 bei fester nichtisotroper relativer Form den gesamten Zustandsupdate nicht automatisch zu einem regulären kleinen Zeitschritt.

## Frische Prüfung
[Vorabprotokoll](SMALL_LOAD_PROTOCOL.md), [Prüfcode](small_load_audit.py), [Resultate](small_load_results.json).

Exakte rationale Zeugenrechnung bestätigt alpha/s²->5/4 sowie beide Y-Grenzwerte. Je vier positive Lastskalen beim Zwei-Moden-Zeugen und zwei komplexen Präparationen n=3,4, drei unitäre Zusatzkontrollen und vier skalare Vergleichskontrollen: **19 vollständige Quellaufrufe im finalen Audit**. s=1/20,1/40,1/80,1/160. Die Quelle wurde nie bei s=0 oder unter geänderter Rangtoleranz aufgerufen.

Die exakten endlichen Koordinaten-/Kanalformeln wurden zusätzlich direkt in den Audit aufgenommen und dieselben deklarierten Fälle frisch vollständig wiederholt. Maximaler exakter Quellrest <3.0e-15, Kovarianzrest <1.6e-15, skalarer Kernelrest <6.7e-16. Die vorab festgelegten Asymptotik-Konvergenzkriterien bestanden.

Die endlichen Skalen sind keine exakten Grenzwerte. Beim Zeugen sinkt etwa der Fehler von s_+/s² gegenüber 2mu2 nur von ca. 0.30018 auf 0.04021; der Fehler der relativen Form sinkt von ca. 0.05199 auf 0.00669. Diese sichtbaren Grenzen werden nicht mit den viel kleineren Quell-Identitätsresten verwechselt. Der letzte Zeugen-Kernelsprung ist ca. 0.089939 und bleibt erwartungsgemäß nahe seinem positiven Grenzwert.

Keine fehlgeschlagenen Fälle oder angepassten Kriterien. Manuskript, Grundcode, Lizenzen und empirische Ergebnisse unverändert. GitHub-CI wird getrennt ausgewiesen.

## Nächste Abhängigkeit
Die gemeinsame Kleinlastgrenze liefert eine konkrete geschlossene relative Randdynamik, aber generisch endliche relative Form-/Kernelereignisse. Ein regulärer gemeinsamer Kleinschrittansatz muss zusätzlich die relative Aufspaltung oder einen besonderen Formsektor kontrollieren. Die nahezu isotrope Umgebung von R_F wäre eine konkrete nächste Prüfung; es darf kein unabhängiges Zurücksetzen von Y eingeschmuggelt werden. Physikalische Dauer, Raummaß, vollständiger Energie-Impuls-Strom, Wirkung und Einstein bleiben offen.
