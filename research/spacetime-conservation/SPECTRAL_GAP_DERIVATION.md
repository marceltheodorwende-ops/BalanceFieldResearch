# Geordnete Spektrallücke: geometrische Kontraktion, unzureichende Gedächtniskoordinate

## Quelle, Kandidat und Voraussetzungen

Ausschließlich die gepinnte vollständige positive BFG-Persistenzquelle aus MANDATE.de.md. Standardmathematik unter bereits bewiesenen Voraussetzungen: Y hat mindestens drei strikt geordnete Eigenwerte 0<y_1<y_2<y_3, und liegt in Klasse C mit M<=1/2,m>=2M². F>0, notwendige Umgebung bleibt erhalten. Die Eigenbasis bleibt im ausgerichteten vollen Persistenzsektor fest; y_+ = g_alpha(y), g_alpha(y)=[alpha+(1-alpha)y²]/(1+y)², alpha wird aus dem vollständigen Zustand berechnet.

Als Alternative zur früheren oberen Blockbreite wird eta=(y_2-y_1)/(y_3-y_1) geprüft. Der Kandidat kann auch nach einem Austritt aus p<=1/2 wohldefiniert sein. Das ist eine mathematische Wahl des Koordinatenausdrucks und noch keine physikalisch ausgewählte Trägerstruktur.

## Geometrisches Resultat für die volle positive Last

In C ist g_alpha streng steigend und streng konvex. Deshalb sind die Sekantensteigungen S_12=[g(y_2)-g(y_1)]/(y_2-y_1) und S_13=[g(y_3)-g(y_1)]/(y_3-y_1) positiv mit S_12<S_13. Exakt

eta_+ = eta S_12/S_13,
0<eta_+<eta.

Weil C invariant ist und die Ordnung erhalten bleibt, gilt diese Kontraktion an allen endlichen exakten Ereignissen, solange die genannten strikten Lücken vorhanden sind. Es ist keine von Hand eingeführte Uhr, keine Raumdistanz und kein bereits bewiesenes Summierbarkeitsresultat. Insbesondere folgt aus der Monotonie keine quantitative Konvergenzgeschwindigkeit.

## Vorab benannte Gegenfamilie zur Gedächtnisbrücke

Für 0<epsilon<=1/10 wähle n=3,
Y=diag(2epsilon²,4epsilon²,epsilon),
F=diag(1,1,epsilon^6), W=I/3, K=ones(3,3)/3.

F ist für jedes positive epsilon strikt positiv; seine Kondition ist nicht gleichmäßig begrenzt. K ist positiv semidefinit, seine untere Paar-Offdiagonale ist 1/3. Alle Lasten sind strikt geordnet und m=2M², M=epsilon<=1/10. Damit liegt die Familie gerade innerhalb des gültigen Quellbereichs, nicht außerhalb seiner Voraussetzungen.

Es gilt eta=2epsilon/(1-2epsilon)->0. Für das exakte endogene alpha aus L_B/(L_C+L_B) liefert rationale Rechnung alpha/epsilon^4 ->10. Der exakte untere Schurfaktor h_12 ist

h_12=[alpha+(1-alpha)y_1 y_2]/sqrt([alpha+(1-alpha)y_1²][alpha+(1-alpha)y_2²]).

Daraus folgt exakt

h_12² ->81/91,
h_12 ->9/sqrt(91),
1-h_12 ->1-9/sqrt(91)>0.

Der Grenzverlust beträgt ungefähr .05654. Gleichzeitig eta_+/eta->0: Die geometrische Koordinate kontrahiert hier besonders stark, während die lokale Kohärenz um einen nicht verschwindenden Anteil abnimmt. Der Audit speichert die vollständigen rationalen Funktionen und ihre symbolischen Grenzwerte.

Damit ist eine uniforme Behauptung 1-h_12<=phi(eta_0) mit phi(x)->0 für beliebiges positives F widerlegt. Ebenso kann keine allzeitliche Verlustschranke dieser Form gelten, die schon das erste Ereignis einschließt. Der normierte lokale Offdiagonaldefekt ist genau 1-h_12, nicht nur eine numerische Diagnose. Es wird keine Unmöglichkeit für reichere, formationsabhängige oder gleichmäßig konditionierte Schranken behauptet. Die Familie variiert F mit epsilon; es ist ausdrücklich kein Gegenbeispiel gegen einen Satz mit zusätzlich fixiertem oder gleichmäßig elliptischem F.

## Frische Evidenz

SPECTRAL_GAP_PROTOCOL.md wurde vor der Auswertung auf GitHub gespeichert. Exakte endogene alpha-Funktion, eta, eta_+, h² und Grenzwerte wurden mit SymPy berechnet. Die allgemeine geometrische Kontraktion folgt unabhängig aus dem Sekantenbeweis. Sechs frische vollständige Original-Quellaufrufe: epsilon=.1,.05,.025 und je eine komplexe simultane unitäre Eichkontrolle. Untere h-Werte .9434231545585281, .9434478007668806, .9434541986265368; eta nimmt .25,.1111111111111111,.05263157894736842 an, jeweils mit kleinerem eta_+.

Kernelrest 2.0822232086893435e-15, Lastrest 1.7299735885826536e-17, Eichrest 8.300522302177386e-15, Lückenrest 5.689893001203927e-16; vorab Schwellen 1e-10 bzw. 1e-8. Kleinster numerisch geprüfter Formationseigenwert 2.44140625e-10. Kein weiterer numerischer Lauf bis zum singulären Grenzzustand wird behauptet. epsilon=0 ist kein gültiger Originalzustand; der Grenzbeweis verwendet ausschließlich zulässige positive Familienmitglieder. CI separat in CI_VALIDATION.md.

## Nächste tatsächliche Abhängigkeit

Die obere Blockgrenze lässt sich geometrisch umgehen, aber eta allein kontrolliert das lokale Gedächtnis bei beliebigen Formationsgewichten nicht. Eine nächste Abschätzung muss die formationabhängige Mischung alpha und die interne relative Paarbreite mitführen oder zusätzliche Konditionsvoraussetzungen explizit begründen. Solche Voraussetzungen dürfen nicht als bereits quellenausgewählt ausgegeben werden. Die früheren gestoppten und speziellen allzeitlichen Schranken bleiben gültig.

Nach-dem-Austritt-Summierbarkeit ist damit noch offen, jetzt mit einem präzisen Gegenbeispiel gegen die einfache Spektrallücken-Abkürzung. Allgemeine Trägerauswahl, räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen. Eine geometrisch kleiner werdende Lücke ist keine Ableitung physikalischer Erhaltung.
