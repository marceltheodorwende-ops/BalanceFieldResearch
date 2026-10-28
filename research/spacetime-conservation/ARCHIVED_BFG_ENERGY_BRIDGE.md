# Archivvergleich: strukturelle Energie und die fehlende physikalische Brücke

**Runde 81, 26. Oktober 2026.** Diese Prüfung folgt der ausdrücklichen Nutzerfreigabe, die lokal vorhandenen älteren BFG-Dokumente als Vergleichskorpus zu verwenden. Der Dynamic-Order-Text vom 8. Oktober bleibt die aktive Quelle der bestehenden Dynamik. Die Archivtexte dürfen deshalb nur eine bereits vorhandene interne Regel nachweisen; sie dürfen keine neue Carrier-, Mess-, Hamiltonian-, Zeit- oder konstitutive Annahme einschmuggeln.

## Frage und Kriterium

Geprüft wird, ob der Archivkorpus zusammen mit der aktuellen BFG-Dynamik eine Zustands- und Energiebrücke bestimmt: einen lokalen Zustand oder Energieoperator, der aus BFG-Daten allein folgt, mit Witness, Formation und dem Zwei-Sektor-Generator kompatibel ist und ohne externe physikalische Karte auskommt.

Ein Archivkandidat scheitert als **interne physikalische** Brücke, sobald er entweder (a) nur ein dimensionsloser struktureller Skalar ist, (b) eine externe Carrier-/Konstitutionskarte verlangt, oder (c) mehrere sektorverträgliche Operatoren bei denselben BFG-Daten offenlässt. Das ist kein allgemeines BFG-No-Go.

## Befund des Vergleichskorpus

Die beiden geprüften Whitepaper formulieren keine verborgene Hamilton-Regel. Sie unterscheiden ausdrücklich strukturelle Schließungslasten von joulewertiger Energie. Ihre neutralen Anteile sind

\[
r_N(D)=\frac{\langle D,C_N(Y)D\rangle}{\langle D,D\rangle},
\qquad
b_N(D)=\frac{\langle D,B_N(Y)D\rangle}{\langle D,D\rangle}=1-r_N(D).
\]

Sie erlauben lediglich physikalische Readouts der Form \(E_{\rm bind}=\mathcal R_E^{\rm bind}[r_N,\mathrm{carrier}]\) und \(E_{\rm exp}=\mathcal R_E^{\rm out}[b_N,\mathrm{carrier}]\), bezeichnen \(\mathcal R_E\) aber selbst als empirische konstitutive Karten, nicht als BFG-Grunddynamik. Beim atomaren Realisierungstest wird ein Carrier-Hamiltonian ebenfalls aus Standardphysik und Messdaten bezogen, nicht aus der BFG erzeugt.

Der Preprint vom 21. September definiert zusätzlich eine strukturelle quadratische Größe \(E=(1+\eta)\lVert D\rVert^2\) und zeigt in seiner endlichen SA-Klasse Kontraktion. Er sagt ausdrücklich, dass dies keine joulewertige Interpretation ist und dass Rekursionstiefe nicht als vergangene physikalische Zeit gelesen werden darf.

## Frische algebraische Prüfung

Die reproduzierbare Rechnung in [bfg_archive_energy_bridge_check.py](bfg_archive_energy_bridge_check.py) nimmt ein nichtentartetes Zwei-Sektor-\(Y=\operatorname{diag}(1/4,1/2)\) und einen normierten Carrierzustand. Sie bestätigt exakt:

1. \(r_N=268/375\) und \(b_N=107/375\), also \(r_N+b_N=1\).
2. Beide Anteile bleiben bei positiver Reskalierung des unnormierten Carriers unverändert. Sie setzen daher selbst keine dimensionsbehaftete Energieskala.
3. Bei denselben BFG-Daten und demselben sektoralen Involutionsoperator \(Z=\operatorname{diag}(1,-1)\) sind \(H_1=\operatorname{diag}(0,1)\) und \(H_2=\operatorname{diag}(0,3)\) beide sektorverträglich, liefern aber verschiedene Erwartungen \(16/25\) beziehungsweise \(48/25\).

Somit wählt die Zwei-Sektor-Kompatibilität weder \(H_1\) noch \(H_2\) aus. Die Archivgrößen geben sinnvolle dimensionslose Bilanz-Readouts und eine positive strukturelle Energie, aber keinen aus der BFG bestimmten physikalischen Energieoperator, Energie-Impuls-Strom oder eine Uhr.

## Positiver Nutzen

Der Archivvergleich schärft die Forschungsroute: Die neutralen Anteile \(r_N,b_N\) sind die natürliche interne Schnittstelle für eine spätere physikalische Readout-Prüfung. Sie ersetzen aber die noch fehlende, unabhängig begründete Carrier-Zustandskarte nicht. Ein positiver nächster Schritt wäre deshalb nur eine bereits vorhandene BFG-Regel, die genau diese Carrierkarte oder eine äquivalente gemeinsame Zustandszuordnung festlegt. Ohne eine solche Regel wäre die Zuordnung eine neue Annahme.

## Grenzen

Der Befund widerlegt weder die lokale mathematische Zwei-Sektor-Klasse noch jede künftige physikalische Realisierung. Er hält nur fest, dass die kontrollierten Archivtexte die fehlende Brücke nicht ergänzen; sie benennen sie selbst als empirische bzw. konstitutive Aufgabe.
