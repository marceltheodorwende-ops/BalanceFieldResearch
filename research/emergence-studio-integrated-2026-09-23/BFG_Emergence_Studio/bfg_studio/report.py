from pathlib import Path
import csv, json
import numpy as np
import matplotlib.pyplot as plt

def rows_for_run(run):
    rows=[]
    for s in run.steps:
        rows.append({
            "generation":s.generation,
            "success":s.success,
            "terminal_reason":s.terminal_reason or "",
            "persistent_rank":s.diagnostics.get("persistent_rank"),
            "support_rank":s.diagnostics.get("support_rank"),
            "lambda_keep":s.lambda_keep,
            "lambda_up":s.lambda_up,
            "omega_keep":s.omega_keep,
            "omega_up":s.omega_up,
            "formation_eigenvalue":s.formation_eigenvalue,
            "formation_gap":s.formation_gap,
            "spectral_novelty":s.spectral_novelty,
            "spectral_mismatch":s.spectral_mismatch,
            "commutator_norm":s.commutator_norm,
            "second_moment_loss":s.second_moment_loss,
            "crossfed_gain":s.diagnostics.get("crossfed_gain"),
            "neutral_partition_residual":s.diagnostics.get("neutral_partition_residual"),
            "reciprocal_balance_residual":s.diagnostics.get("reciprocal_balance_residual"),
            "PY_commutator_norm":s.diagnostics.get("PY_commutator_norm"),
            "schur_stratum_compatible":s.diagnostics.get("schur_stratum_compatible"),
        })
    return rows

def write_run_report(run, outdir, stem="run"):
    outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    rows=rows_for_run(run)
    csv_path=outdir/f"{stem}.csv"
    if rows:
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    json_path=outdir/f"{stem}_summary.json"
    json_path.write_text(json.dumps(run.summary(),indent=2,default=str),encoding="utf-8")

    p1=p2=""
    if rows:
        g=np.array([r["generation"] for r in rows],float)
        m=np.array([np.nan if r["spectral_mismatch"] is None else r["spectral_mismatch"] for r in rows],float)
        gain=np.array([np.nan if r["crossfed_gain"] is None else r["crossfed_gain"] for r in rows],float)
        lam=np.array([np.nan if r["formation_eigenvalue"] is None else r["formation_eigenvalue"] for r in rows],float)

        p1=outdir/f"{stem}_novelty.png"
        plt.figure(figsize=(7.2,4.2)); plt.plot(g,m,marker="o")
        plt.xlabel("Generation"); plt.ylabel("Normalized spectral mismatch")
        plt.title("BFG structural novelty trajectory"); plt.tight_layout(); plt.savefig(p1,dpi=150); plt.close()

        p2=outdir/f"{stem}_stability.png"
        plt.figure(figsize=(7.2,4.2)); plt.plot(g,gain,marker="o",label="cross-fed gain")
        plt.plot(g,lam,marker="s",label="lowest formation eigenvalue")
        plt.xlabel("Generation"); plt.title("BFG stability / formation trajectory"); plt.legend()
        plt.tight_layout(); plt.savefig(p2,dpi=150); plt.close()

    return {"csv":str(csv_path),"summary_json":str(json_path),
            "novelty_plot":str(p1),"stability_plot":str(p2)}
