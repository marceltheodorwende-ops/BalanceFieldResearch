"""Render the result report and an SVG plot from persisted results only."""
import csv
import gzip
import hashlib
import json
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR','/tmp/bfg-eeg-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent


def main():
    result=ROOT/'results'
    s=json.loads((result/'summary.json').read_text())
    models=s['models'];labels=list(models)
    means=[models[k]['mean_relative_frobenius_common'] for k in labels]
    low=[means[i]-models[k]['ci95'][0] for i,k in enumerate(labels)]
    high=[models[k]['ci95'][1]-means[i] for i,k in enumerate(labels)]
    fig,ax=plt.subplots(figsize=(8,4))
    ax.bar(labels,means,yerr=[low,high],capsize=4,color=['#b24b45','#416b86','#567b54','#927044'])
    ax.set_ylabel('Relative next-window covariance error (lower is better)')
    ax.set_title('Held-out real EEG: subject means and 95% bootstrap intervals')
    ax.set_ylim(bottom=0);fig.tight_layout();fig.savefig(result/'covariance_error.svg');plt.close(fig)
    qc=list(csv.DictReader((result/'qc.csv').open()))
    rejected=sum(r['status']!='loaded' for r in qc)
    badwindows=sum(int(r['windows'])-int(r['valid']) for r in qc)
    lines=['# Real EEG covariance prediction results','',
        'This experiment tests a specified additional EEG preparation and covariance readout attached to the finite BFG kernel. It does not test physical universality or phenomenal consciousness.','',
        f"**Outcome: {'the predeclared practical success target was met' if s['practical_success'] else 'the predeclared practical success target was not met'}.**",'',
        f"The held-out evaluation includes {s['heldout_subjects']} subjects and {s['eligible_holdout_pairs']} eligible two-second window pairs. The common nonterminal comparison contains {s['common_pairs']} pairs. {rejected} recordings were excluded; {badwindows} windows failed the fixed quality criteria across development and holdout recordings.",'',
        '| Model | Mean relative covariance error | 95% subject bootstrap interval | Coverage |','|---|---:|---:|---:|']
    for k,v in models.items():
        lines.append(f"| {k} | {v['mean_relative_frobenius_common']:.6f} | [{v['ci95'][0]:.6f}, {v['ci95'][1]:.6f}] | {100*v['coverage']:.2f}% |")
    lines+=['','All table errors use the common nonterminal subset. Comparator errors on all eligible pairs are also recorded in summary.json. Subjects are weighted equally, with runs averaged within subjects.','',
        '| Comparator | BFG minus comparator error | 95% paired subject bootstrap interval |','|---|---:|---:|']
    for k,v in s['comparisons'].items():
        lines.append(f"| {k} | {v['bfg_minus_comparator']:.6f} | [{v['ci95'][0]:.6f}, {v['ci95'][1]:.6f}] |")
    lines+=['','Positive differences mean BFG is worse. Intervals are exploratory and unadjusted for multiple comparisons.','',
        '![Held-out covariance error](results/covariance_error.svg)','',
        '## Conditions','', '| Condition | BFG | Persistence | Linear | Frozen geometry |','|---|---:|---:|---:|---:|']
    for label,v in s['conditions'].items():
        lines.append('| '+label+' | '+' | '.join(f'{v[k]:.6f}' for k in ('bfg','persistence','linear','frozen_geometry'))+' |')
    lines+=['','## Interpretation and limits','',
        'The EEG bridge resets a full state from each current measurement window. K, P and the witness identification are constitutive choices; the measurement-to-state identification and the two-second clock are not derived by the paper. This is one-step prediction with measurement assimilation, not an independently calibrated autonomous many-step physical orbit.','',
        'The canonical load damping and the absolute scale of measured covariance may be poorly matched by this preparation/readout. No amplitude correction was fitted after evaluation. Failure rejects this tested bridge/predictor and does not invalidate algebraic matrix identities. A feature classifier or an unconstrained fitted map would answer a different question.','',
        'These short baseline runs include eyes-open and eyes-closed recordings, not sleep, anesthesia, interventions or reports of subjective experience. The fixed eight-channel montage and basic artifact screening do not eliminate every EEG artifact. Subjects were separated by numeric ID rather than randomized; independent external replication remains needed.','',
        f"The rank sensitivity audit changed {s['rank_sensitivity_changed_pairs']} held-out pair outcomes between tolerances 1e-10 and 1e-14. Exact-rank mathematics remains distinct from floating-point thresholding.",'',
        '## Reproduction','',
        'From this directory, install requirements.txt in a virtual environment, run `python -m unittest -v test_experiment`, then `python experiment.py download`, `python experiment.py evaluate`, and `python report.py`. Downloads use the original PhysioNet URLs with retries. Raw EDF data are not committed. `results/windows.csv.gz` stores all window sufficient statistics in squared volts; `pairs.csv.gz` stores each prediction loss and terminal status. Decompress these with gzip or read them with Python gzip.open. `subjects.csv`, `qc.csv`, `data_manifest.csv`, `development_parameters.json` and `summary.json` expose aggregation, exclusions and fitted values.','',
        'The frozen protocol was committed before measurement download as 37f31b1b8aae878418fe2510a55b7896bb114579. Paper source: commit 76d9e87b4275ec41b3dcd84434e2ee3791a8d076, dated 6 October 2026. The original PDF controls formula typography.','',
        '## Data attribution and rights','',
        'Schalk, G. (2009). EEG Motor Movement/Imagery Dataset, version 1.0.0. PhysioNet. https://doi.org/10.13026/C28G6P. Original acquisition publication: Schalk et al., BCI2000: A General-Purpose Brain-Computer Interface (BCI) System, IEEE Transactions on Biomedical Engineering 51(6), 1034–1043 (2004).','',
        'Third-party measurements and derived measurement tables retain Open Data Commons Attribution License 1.0 attribution: https://opendatacommons.org/licenses/by/1-0/. This does not change the repository rights notice for original code or documentation. Source: https://physionet.org/content/eegmmidb/1.0.0/.','',
        'PhysioNet platform citation: Pollard et al. (2026), PhysioNet as a global platform for biomedical research, Nature Health, https://doi.org/10.1038/s44360-026-00096-z.','']
    (ROOT/'README.md').write_text('\n'.join(lines))
    for name in ('windows.csv','pairs.csv'):
        path=result/name
        with path.open('rb') as source, (result/(name+'.gz')).open('wb') as dest:
            with gzip.GzipFile(filename='',mode='wb',fileobj=dest,mtime=0) as zipped:
                zipped.write(source.read())
        path.unlink()
    paths=[p for p in ROOT.rglob('*') if p.is_file() and 'raw' not in p.parts and '__pycache__' not in p.parts and p.name not in ('SHA256SUMS.txt','upload.json')]
    (ROOT/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(ROOT))+'\n' for p in sorted(paths)))


if __name__=='__main__':main()
