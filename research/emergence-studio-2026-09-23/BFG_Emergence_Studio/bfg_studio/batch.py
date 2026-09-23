from __future__ import annotations

from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import csv
import json
import os

from .alife import SelfOrganizationParameters, simulate_self_organization
from .population import PopulationParameters, simulate_population
from .evolution import EvolutionParameters, simulate_evolution
from .session import ProvenanceManifest, save_experiment_ledger


@dataclass
class BatchItem:
    seed: int
    mode: str
    summary: dict


@dataclass
class BatchSweep:
    mode: str
    items: list[BatchItem]
    workers: int
    source_fingerprint: str

    def summary(self):
        return {
            "mode":self.mode,
            "runs":len(self.items),
            "workers":self.workers,
            "source_fingerprint":self.source_fingerprint,
            "items":[asdict(i) for i in self.items],
        }


def _alife_one(seed:int,steps:int):
    p=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    run=simulate_self_organization(seed=seed,steps=steps,params=p)
    return BatchItem(seed,"alife",run.summary())


def _population_one(seed:int,generations:int):
    org=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    pop=PopulationParameters(
        min_unit_nodes=4,max_unit_nodes=40,max_population=16,
        node_birth_threshold=0.88,
    )
    run=simulate_population(
        seed=seed,generations=generations,
        org_params=org,pop_params=pop
    )
    return BatchItem(seed,"population",run.summary())


def _evolution_one(seed:int,generations:int):
    org=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    pop=PopulationParameters(
        min_unit_nodes=4,max_unit_nodes=40,max_population=16,
        node_birth_threshold=0.90,
    )
    evo=EvolutionParameters(
        mutation_rate=0.8,mutation_sigma=0.05,
        carrying_capacity=8,max_candidate_population=16,
        minimum_reproductive_age=4,
    )
    run=simulate_evolution(
        seed=seed,generations=generations,
        base_org=org,base_pop=pop,evo=evo
    )
    return BatchItem(seed,"evolution",run.summary())


def run_seed_sweep(
    seeds:list[int],
    mode:str="alife",
    horizon:int=20,
    workers:int|None=None,
) -> BatchSweep:
    workers=workers or min(8,max(1,os.cpu_count() or 1))
    if mode=="alife":
        fn=lambda s:_alife_one(s,horizon)
    elif mode=="population":
        fn=lambda s:_population_one(s,horizon)
    elif mode=="evolution":
        fn=lambda s:_evolution_one(s,horizon)
    else:
        raise ValueError("mode must be one of: alife, population, evolution")

    with ThreadPoolExecutor(max_workers=workers) as ex:
        items=list(ex.map(fn,[int(s) for s in seeds]))

    manifest=ProvenanceManifest.build(
        experiment=f"parallel_{mode}_seed_sweep",
        seed=None,
        parameters={
            "seeds":[int(s) for s in seeds],
            "horizon":int(horizon),
            "workers":workers,
        },
    )
    return BatchSweep(
        mode=mode,items=items,workers=workers,
        source_fingerprint=manifest.source_fingerprint
    )


def write_seed_sweep(
    sweep:BatchSweep,
    outdir:str|Path,
    stem:str="seed_sweep",
):
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)
    json_path=outdir/f"{stem}.json"
    json_path.write_text(
        json.dumps(sweep.summary(),indent=2,default=str),
        encoding="utf-8"
    )
    csv_path=outdir/f"{stem}.csv"
    rows=[]
    for item in sweep.items:
        rows.append({
            "seed":item.seed,
            "mode":item.mode,
            "summary":json.dumps(item.summary,sort_keys=True,default=str),
        })
    if rows:
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)

    ledger=save_experiment_ledger(
        outdir,
        experiment=f"parallel_{sweep.mode}_seed_sweep",
        seed=None,
        parameters={
            "workers":sweep.workers,
            "seeds":[i.seed for i in sweep.items],
        },
        summary=sweep.summary(),
        name=f"{stem}_provenance",
    )
    return {
        "json":str(json_path),
        "csv":str(csv_path),
        **{f"provenance_{k}":v for k,v in ledger.items()},
    }
