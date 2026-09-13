"""Run with python -m bfg_lab --output results."""
import argparse
import json
from pathlib import Path
import numpy as np
from .core import neutral, persistent_basis, split


def experiment(scenario):
    n = 8
    state = np.zeros(n)
    state[0] = 1.
    rows = []
    for step in range(81):
        adjacency = np.zeros((n,n))
        for i in range(n):
            weight = 1.
            if scenario == "edge_failure" and step >= 20 and i == 0:
                weight = 0.
            if scenario == "coupling_drift":
                weight = 1. - .8 * step / 80
            adjacency[i,(i+1)%n] = adjacency[(i+1)%n,i] = weight
        lap = np.diag(adjacency.sum(axis=1)) - adjacency
        # Fixed time step: all scenarios remain symmetric and power bounded.
        r = np.eye(n) - .2 * lap
        y = lap + .2*np.eye(n)
        c, b, _ = neutral(y)
        w = persistent_basis(r)
        result = split(y, state, w)
        norm2 = float(state @ state)
        off = c - np.diag(np.diag(c))
        row = dict(step=step, disagreement=float(np.linalg.norm(state-state.mean())),
                   integration=float(np.linalg.norm(off)**2/np.linalg.norm(c)**2),
                   differentiation=float(np.linalg.eigvalsh(c).min()),
                   retention=float(np.vdot(state,c@state).real/norm2),
                   complement=float(np.vdot(state,b@state).real/norm2),
                   spectral_gap=float(1-np.sort(np.linalg.eigvalsh(r))[-2]),
                   witness_rank=w.shape[1], status=result["status"],
                   dual_gain=result.get("gain"), state=state.tolist())
        rows.append(row)
        state = r @ state
    return rows


HTML = '''<!doctype html><html lang="de"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>BFG Network Lab</title><style>
body{font:17px system-ui;background:#101923;color:#e7edf3;max-width:1040px;margin:40px auto;padding:0 24px}
h1{font-size:38px;margin-bottom:8px}p{line-height:1.6;color:#b9c9d6}select{font:inherit;padding:8px;background:#203140;color:white;border:1px solid #597080;border-radius:6px}
svg{width:100%;background:#172635;border-radius:12px;margin-top:24px}table{width:100%;border-collapse:collapse}td,th{padding:12px;border-bottom:1px solid #354654;text-align:left}a{color:#64d8bd}
</style><h1>BFG Network Lab</h1><p>V4 · Experimenteller Demonstrator · 8 Knoten</p>
<p>Die Netzwerke folgen einer vorgegebenen linearen Konsensdynamik. BFG-Groessen werden als Diagnostik ausgelesen. Diese Simulation ist keine Implementierung der vollstaendigen universellen Rekursion und kein empirischer Nachweis.</p>
<label>Szenario <select id="scenario"><option value="impulse">Impuls</option><option value="edge_failure">Verbindungsausfall ab Schritt 20</option><option value="coupling_drift">Schleichend sinkende Kopplung</option></select></label>
<label> Messgroesse <select id="metric"><option value="disagreement">Abweichung vom Konsens (Vergleichswert)</option><option value="integration">Integration</option><option value="differentiation">Differenzierung</option><option value="retention">Retention</option><option value="spectral_gap">Spektralluecke (Vergleichswert)</option><option value="dual_gain">Lokaler Dual-Gain</option></select></label>
<svg viewBox="0 0 900 320" role="img" aria-label="Verlauf der ausgewaehlten Messgroesse"><path d="M60 20V270H870" fill="none" stroke="#8197a8"/><polyline id="line" fill="none" stroke="#64d8bd" stroke-width="3"/><text x="60" y="300" fill="white">0</text><text x="780" y="300" fill="white">80 Schritte</text><text id="scale" x="65" y="40" fill="white"></text></svg>
<table><thead><tr><th>Messgroesse</th><th>Anfang</th><th>Ende</th></tr></thead><tbody id="summary"></tbody></table>
<p>Persistenz: peripherer Spektralraum, mit numerischer Toleranz 1e-10. Das ist eine offengelegte Interpretation von Gleichung 27; die gedruckte Span-Definition hat ein Gegenbeispiel. Keine Vorhersageueberlegenheit behauptet.</p>
<script>const data=__DATA__;const scenario=document.getElementById('scenario'),metric=document.getElementById('metric');function draw(){const rows=data.scenarios[scenario.value],key=metric.value,values=rows.map(r=>r[key]);const max=Math.max(...values,1e-9);document.getElementById('line').setAttribute('points',values.map((v,i)=>`${60+810*i/80},${270-240*v/max}`).join(' '));document.getElementById('scale').textContent='Skala: 0 bis '+max.toPrecision(4);document.getElementById('summary').innerHTML=['disagreement','integration','differentiation','retention','complement','spectral_gap','dual_gain'].map(k=>`<tr><td>${k}</td><td>${rows[0][k].toFixed(6)}</td><td>${rows[80][k].toFixed(6)}</td></tr>`).join('');}scenario.onchange=metric.onchange=draw;draw();</script></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    data = dict(model="Synthetic consensus network; BFG readouts only", tolerance=1e-10,
                numpy_version=np.__version__, scenarios={s:experiment(s) for s in
                ("impulse", "edge_failure", "coupling_drift")})
    args.output.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, indent=2, allow_nan=False)
    (args.output/"network.json").write_text(payload, encoding="utf-8")
    (args.output/"network.html").write_text(HTML.replace("__DATA__",payload), encoding="utf-8")
    print(f"Generated {args.output/'network.json'} and {args.output/'network.html'}")


if __name__ == "__main__":
    main()
