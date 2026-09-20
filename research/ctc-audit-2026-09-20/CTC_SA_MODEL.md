# CTC-SA: ein expliziter endlicher Modellzweig

## Voraussetzungen und neue Regeln

H ist ein endlichdimensionaler komplexer Hilbertraum, dim H=d≥2. Die selbstadjungierten Kapazitäten Dcap,c,aleph kommutieren, c≥c_*I>0, und K=c+aleph−Dcap hat einfache Eigenwerte lambda_1<0<lambda_2<…<lambda_d. Der aktive Vektor D hat auf jeder Eigenlinie von K einen nichtnulligen Koeffizienten. Ein primitiver Skalar eta>0 bestimmt Y=eta I und G=(1+eta)I.

Folgende Größen sind per neuer Modellregel abgeleitet, keine freien Zustandskoordinaten:

    W_N=L_C=N_R=I,
    D_cov=sqrt(eta)c^(-1), B_C=D_cov c,
    P_s=P_max(K), P=I−P_s,
    r=(lambda_(d−1)−lambda_1)/(lambda_d−lambda_1),
    R_C=P+rP_s, R=R_C, M=I.

D_cov c bedeutet hier Operatorverkettung, keine hergeleitete kovariante Ableitung eines Operatorfelds. Es folgt B_C=sqrt(eta)I und B_C*W_N B_C=Y=eta I. R_C ist normal, potenzbeschränkt und hat einen strikt stabilen letzten Modus; für d=2 ist r=0. Sein reparierter peripherer Raum ist Ran(P), und wegen skalarer G-Metrik ist P zugleich der metrische Projektor.

## Vollständiger Schritt

Für d=2 setze U(X)=⊥. Dies ist eine ausdrückliche Terminalregel dieses endlichen Modellzweigs; der fehlende zweite Kandidateneigenwert allein ist kein allgemeiner Beweis unmöglicher eindimensionaler Formation. Setze ferner U(⊥)=⊥.

Für d≥3 definiere

    a=eta/((1+eta)sqrt(1+eta²)),
    t=||PD||²/||D||²,
    A=a[P;P], J=[P;P]/sqrt(2), E=JJ*,
    H_next=Ran(E), eta_next=2a²t.

Die Kapazitäten werden gemäß V4 durch E(Acap⊕Acap)E auf H_next komprimiert. Das ist über J eingeschränkt auf Ran(P) unitär äquivalent zur Restriktion auf die ersten d−1 Eigenlinien. Setze Y_next=eta_next I und bilde alle abgeleiteten Faktoren und R_C_next erneut nach den obigen Regeln. Der neue aktive Vektor ist

    D_next=(1+eta_next)^(-1) A D.

In Supportkoordinaten:

    J* D_next=sqrt(2)a/(1+eta_next) PD.

## Bedingter Schließungssatz

Dieser Schritt bildet die Klasse C_d nach C_(d−1) ab. Beweis: Alle komprimierten Kapazitäten bleiben selbstadjungiert und kommutieren; die untere c-Schranke bleibt erhalten. Das Spektrum von K_next ist lambda_1,…,lambda_(d−1), also weiterhin einfach mit genau einem negativen Eigenwert. Beide persistenten Loads sind positiv:

    Lambda_keep=||PD||²/(1+eta),
    Lambda_up=eta²||PD||²/(1+eta).

Der alte und der frisch rekonstruierte neue Rekursionsoperator haben positiven Abstand ihres stabilen Eigenwerts zu eins. Der nächste Formationgap lambda_2−lambda_1 ist positiv. Wegen voller Unterstützung gilt 0<t<1; daher eta_next>0 und alle verbleibenden D-Komponenten bleiben nach Multiplikation mit dem positiven Vorfaktor nichtnullig.

Induktion liefert genau d0−2 nichtterminale Schritte. Anschließend greift die explizite Terminalregel, und alle weiteren Iterationen sind ⊥. Dies ist keine unendliche nichtterminale Entwicklung.

## Energiebeweis

Für die tatsächliche ungestörte Folge sei E_n=||D_n||²_(G_n). Direktes Einsetzen ergibt

    E_next/E_n=eta_next/((1+eta_next)(1+eta)).

Aus

    (1+eta)²(1+eta²)−8eta²
      =(eta−1)²(eta²+4eta+1)≥0

folgt a²≤1/8 und wegen t<1 somit eta_next<1/4. Daher E_next/E_n<1/5. Für jeden existierenden nichtterminalen Verlauf gilt E_n≤5^(−n)E_0. Diese Schranke ist nicht als scharf behauptet. Sie ist weder ein allgemeiner Switching-/Inputsatz noch ein Resultat zur unendlichen Dimension.

## Keine Gram-Vererbung

Kompression des alten Y ergibt eta I auf H_next, während der neue Rebuild eta_next I erzeugt. Es gilt sogar eta_next<eta, da

    eta_next/eta=2eta t/((1+eta)²(1+eta²))<1.

Der frühere Gram-Kompatibilitätssatz für gemeinsam komprimierte Faktoren wird deshalb nicht auf diese frische Faktorregel angewendet. Die Skalengeometrie ist hier eine neue Modellentscheidung. Ebenso sind die Auswahl des größten Formationmodus und die Funktion r(K) nicht durch die Quellen als alternativlos bewiesen; etwa r(K)² wäre ebenfalls eine parameterfreie andere Regel.

## Exakt nachgerechnetes Beispiel

Anfang: d=5, c=diag(1,2,3,4,5), Dcap=diag(3,1,1,1,1), aleph=I, D=(1,1,1,1,1), eta=1. K=diag(−1,2,3,4,5).

| Dimension | eta | Energie |
|---|---:|---:|
| 5 | 1 | 10 |
| 4 | 1/5 | 5/6 |
| 3 | 25/624 | 625/23364 |
| 2 | 324480000/164268811201 | 3515200000000/69326858847152401 |

Die Rekursionswerte sind 5/6, 4/5, 3/4, 0. In Dimension vier gilt D=(5/12)(1,1,1,1) in den unitären Supportkoordinaten. Das ältere Beispiel mit konstantem eta=1 hat andere Amplituden und Energien und bleibt eine getrennte historische Modellversion.

## Grenzen

Die ältere algebraische Form R_C=MRM* ist durch M=I erfüllt. Eine vollständige Identifikation mit sämtlichen Strong-Universal-Definitionen von C_E und U_Omega ist damit nicht bewiesen. Allgemeine BFG-interne Rekonstruktion, nichtnormale Modelle, PDE-Kopplung, empirische Vorhersagen und unendlichdimensionale Fortsetzung bleiben offen.
