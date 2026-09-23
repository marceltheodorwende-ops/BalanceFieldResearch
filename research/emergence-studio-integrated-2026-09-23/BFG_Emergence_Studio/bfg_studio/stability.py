from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import json

import numpy as np

from .types import NumericalPolicy
from .session import source_tree_fingerprint
from .seeds import make_random_seed_state, make_commuting_control_state

from .sunspot_carrier import load_sunspots, build_window_measurements
from .sunspot_validation import (
    SunspotValidationConfig,
    AnnualSunspotValidationCarrier,
)
from .co2_carrier import (
    CO2CarrierConfig,
    CO2BFGCarrier,
    load_monthly_calibration,
    _measurements_from_monthly as _co2_measurements,
)
from .enso_carrier import (
    ENSOCarrierConfig,
    ENSOBFGCarrier,
    load_enso_monthly,
    _measurements as _enso_measurements,
)


@dataclass(frozen=True)
class PeripheralGroup:
    representative_real: float
    representative_imag: float
    algebraic_multiplicity: int
    geometric_multiplicity: int
    semisimple: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class RecursiveStabilityCertificate:
    dimension: int
    spectral_radius: float
    stable_radius: float | None
    stable_gap: float | None
    peripheral_count: int
    unstable_count: int
    semisimple_peripheral: bool
    spectral_criterion_satisfied: bool
    finite_horizon_peak_norm: float
    finite_horizon_last_norm: float
    finite_horizon: int
    peripheral_groups: tuple[PeripheralGroup, ...]
    eigenvalues: tuple[tuple[float, float], ...]
    tolerances: dict[str, float]

    def to_dict(self) -> dict[str, Any]:
        d=asdict(self)
        d["peripheral_groups"]=[
            g.to_dict() for g in self.peripheral_groups
        ]
        return d


def _group_eigenvalues(
    eigenvalues: np.ndarray,
    grouping_tol: float,
) -> list[list[complex]]:
    groups: list[list[complex]]=[]
    for value in eigenvalues:
        z=complex(value)
        placed=False
        for group in groups:
            center=sum(group)/len(group)
            if abs(z-center) <= grouping_tol*(1.0+abs(center)):
                group.append(z)
                placed=True
                break
        if not placed:
            groups.append([z])
    return groups


def _numerical_nullity(
    matrix: np.ndarray,
    svd_rtol: float,
) -> int:
    a=np.asarray(matrix,dtype=complex)
    if a.size==0:
        return 0
    singular=np.linalg.svd(a,compute_uv=False)
    if singular.size==0:
        return a.shape[1]
    scale=max(float(singular[0]),1.0)
    tol=svd_rtol*max(a.shape)*scale
    rank=int(np.sum(singular>tol))
    return int(a.shape[1]-rank)


def finite_horizon_power_peak(
    operator: np.ndarray,
    horizon: int=128,
) -> tuple[float,float]:
    """
    Numerical diagnostic only; not the theorem.

    Returns max_{0<=n<=horizon} ||A^n||_2 and ||A^horizon||_2.
    """
    a=np.asarray(operator,dtype=complex)
    n=a.shape[0]
    power=np.eye(n,dtype=complex)
    peak=float(np.linalg.norm(power,2))
    last=peak
    for _ in range(horizon):
        power=a@power
        last=float(np.linalg.norm(power,2))
        peak=max(peak,last)
    return peak,last


def recursive_stability_certificate(
    operator: np.ndarray,
    *,
    unit_tol: float=1e-8,
    grouping_tol: float=1e-7,
    svd_rtol: float=1e-9,
    horizon: int=128,
) -> RecursiveStabilityCertificate:
    """
    Numerically audit the finite-dimensional power-boundedness criterion.

    Exact theorem:
      A is power bounded iff
      (i) sigma(A) is contained in the closed unit disk, and
      (ii) every eigenvalue on the unit circle is semisimple.

    The returned boolean checks finite-precision hypotheses only.
    """
    a=np.asarray(operator,dtype=complex)
    if a.ndim!=2 or a.shape[0]!=a.shape[1]:
        raise ValueError("recursive operator must be a square matrix")
    if not np.all(np.isfinite(a)):
        raise ValueError("recursive operator contains non-finite values")

    eig=np.linalg.eigvals(a)
    mod=np.abs(eig)
    rho=float(np.max(mod)) if eig.size else 0.0

    unstable_mask=mod>1.0+unit_tol
    peripheral_mask=np.abs(mod-1.0)<=unit_tol
    stable_mask=mod<1.0-unit_tol

    unstable_count=int(np.sum(unstable_mask))
    peripheral_count=int(np.sum(peripheral_mask))

    stable_radius=(
        float(np.max(mod[stable_mask]))
        if np.any(stable_mask)
        else None
    )
    stable_gap=(
        float(1.0-stable_radius)
        if stable_radius is not None
        else None
    )

    peripheral_values=eig[peripheral_mask]
    groups_raw=_group_eigenvalues(
        peripheral_values,grouping_tol
    )
    groups=[]
    semisimple=True
    for group in groups_raw:
        representative=sum(group)/len(group)
        alg=len(group)
        geom=_numerical_nullity(
            a-representative*np.eye(a.shape[0],dtype=complex),
            svd_rtol,
        )
        ok=geom>=alg
        semisimple=semisimple and ok
        groups.append(
            PeripheralGroup(
                representative_real=float(np.real(representative)),
                representative_imag=float(np.imag(representative)),
                algebraic_multiplicity=alg,
                geometric_multiplicity=geom,
                semisimple=bool(ok),
            )
        )

    criterion=bool(
        unstable_count==0
        and semisimple
        and rho<=1.0+unit_tol
    )
    peak,last=finite_horizon_power_peak(a,horizon=horizon)

    return RecursiveStabilityCertificate(
        dimension=int(a.shape[0]),
        spectral_radius=rho,
        stable_radius=stable_radius,
        stable_gap=stable_gap,
        peripheral_count=peripheral_count,
        unstable_count=unstable_count,
        semisimple_peripheral=bool(semisimple),
        spectral_criterion_satisfied=criterion,
        finite_horizon_peak_norm=peak,
        finite_horizon_last_norm=last,
        finite_horizon=int(horizon),
        peripheral_groups=tuple(groups),
        eigenvalues=tuple(
            (float(np.real(z)),float(np.imag(z)))
            for z in eig
        ),
        tolerances={
            "unit_tol":float(unit_tol),
            "grouping_tol":float(grouping_tol),
            "svd_rtol":float(svd_rtol),
        },
    )


def feedback_margin_certificate(
    B: float | complex,
    epsilon: float,
) -> dict[str,Any]:
    """
    Scalar feedback criticality certificate for IB=A/(1-B).

    This is logically distinct from operator power-boundedness.
    """
    if epsilon<=0:
        raise ValueError("epsilon must be positive")
    margin=float(abs(1.0-B))
    return {
        "margin":margin,
        "epsilon":float(epsilon),
        "admissible":bool(margin>=epsilon),
        "critical":bool(margin<epsilon),
    }


def neutral_resolvent_certificate(
    Y: np.ndarray,
    tol: float=1e-9,
) -> dict[str,Any]:
    """
    Exact-construction audit for C_N=(I+Y)^-1 and B_N=I-C_N.

    If Y is Hermitian PSD, then 0<C_N<=I and 0<=B_N<I.
    """
    y=np.asarray(Y,dtype=complex)
    if y.ndim!=2 or y.shape[0]!=y.shape[1]:
        raise ValueError("Y must be square")
    hermitian_res=float(np.linalg.norm(y-y.conj().T,2))
    yh=0.5*(y+y.conj().T)
    eig_y=np.linalg.eigvalsh(yh)
    psd=bool(float(np.min(eig_y))>=-tol)

    I=np.eye(y.shape[0],dtype=complex)
    C=np.linalg.solve(I+y,I)
    B=I-C
    partition=float(np.linalg.norm(C+B-I,2))
    eig_c=np.linalg.eigvalsh(0.5*(C+C.conj().T))
    eig_b=np.linalg.eigvalsh(0.5*(B+B.conj().T))

    return {
        "hermitian_residual":hermitian_res,
        "Y_psd":psd,
        "Y_min_eigenvalue":float(np.min(eig_y)),
        "partition_residual":partition,
        "C_min_eigenvalue":float(np.min(eig_c)),
        "C_max_eigenvalue":float(np.max(eig_c)),
        "B_min_eigenvalue":float(np.min(eig_b)),
        "B_max_eigenvalue":float(np.max(eig_b)),
        "neutral_bounds_satisfied":bool(
            psd
            and float(np.min(eig_c))> -tol
            and float(np.max(eig_c))<=1.0+tol
            and float(np.min(eig_b))>=-tol
            and float(np.max(eig_b))<=1.0+tol
            and partition<=10*tol
        ),
    }


def jordan_counterexample(size:int=2)->np.ndarray:
    if size<2:
        raise ValueError("Jordan counterexample requires size >=2")
    A=np.eye(size,dtype=complex)
    for i in range(size-1):
        A[i,i+1]=1.0
    return A


def _audit_operator_family(
    carrier_id:str,
    operators:list[np.ndarray],
    horizon:int,
)->dict[str,Any]:
    certs=[
        recursive_stability_certificate(op,horizon=horizon)
        for op in operators
    ]
    passed=sum(int(c.spectral_criterion_satisfied) for c in certs)
    semisimple=sum(int(c.semisimple_peripheral) for c in certs)
    max_rho=max(c.spectral_radius for c in certs) if certs else None
    min_gap=min(
        [c.stable_gap for c in certs if c.stable_gap is not None],
        default=None,
    )
    max_peak=max(c.finite_horizon_peak_norm for c in certs) if certs else None
    return {
        "carrier_id":carrier_id,
        "operators":len(certs),
        "criterion_passed":passed,
        "semisimple_peripheral":semisimple,
        "pass_fraction":passed/max(len(certs),1),
        "max_spectral_radius":max_rho,
        "minimum_stable_gap":min_gap,
        "maximum_finite_horizon_power_norm":max_peak,
    }


def _sunspot_operators(root:Path)->list[np.ndarray]:
    frozen=json.loads(
        (root/"outputs/real_sunspots/sunspot_frozen_model.json")
        .read_text(encoding="utf-8")
    )
    cfg=dict(frozen["config"])
    cfg["ar_coefficients"]=tuple(cfg["ar_coefficients"])
    carrier=AnnualSunspotValidationCarrier(
        SunspotValidationConfig(**cfg)
    )
    years,values=load_sunspots()
    measurements=build_window_measurements(
        years,values,carrier.config.lag
    )
    return [
        carrier.map_measurement_to_state(m,generation=i).R_C
        for i,m in enumerate(measurements)
    ]


def _co2_operators(root:Path)->list[np.ndarray]:
    frozen=json.loads(
        (root/"outputs/real_co2/co2_frozen_model.json")
        .read_text(encoding="utf-8")
    )
    cfg=dict(frozen["config"])
    carrier=CO2BFGCarrier(CO2CarrierConfig(**cfg))
    monthly=load_monthly_calibration(
        calibration_end=carrier.config.calibration_end
    )
    measurements=_co2_measurements(
        monthly,carrier.config.lag
    )
    return [
        carrier.map_measurement_to_state(m,generation=i).R_C
        for i,m in enumerate(measurements)
    ]


def _enso_operators(root:Path)->list[np.ndarray]:
    frozen=json.loads(
        (root/"outputs/real_enso/enso_frozen_model.json")
        .read_text(encoding="utf-8")
    )
    cfg=dict(frozen["config"])
    cfg["month_climatology"]=tuple(cfg["month_climatology"])
    carrier=ENSOBFGCarrier(ENSOCarrierConfig(**cfg))
    series=load_enso_monthly()
    measurements=_enso_measurements(
        series,carrier.config.month_climatology,carrier.config.lag
    )
    return [
        carrier.map_measurement_to_state(m,generation=i).R_C
        for i,m in enumerate(measurements)
    ]


def run_master_stability_audit(
    project_root:str|Path|None=None,
    *,
    horizon:int=64,
)->dict[str,Any]:
    """
    Numerical theorem-hypothesis audit.

    This does not prove the theorem; it checks that the current finite-dimensional
    master carriers satisfy its spectral hypotheses to declared tolerances.
    """
    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )

    # Synthetic exact controls.
    stable=np.diag([1.0,np.exp(0.3j),0.8,0.55]).astype(complex)
    jordan=jordan_counterexample(2)
    unstable=np.diag([1.0,1.01]).astype(complex)

    controls={
        "stable_semisimple":
            recursive_stability_certificate(stable,horizon=horizon).to_dict(),
        "jordan_unit_circle":
            recursive_stability_certificate(jordan,horizon=horizon).to_dict(),
        "supercritical":
            recursive_stability_certificate(unstable,horizon=horizon).to_dict(),
    }
    controls_pass=bool(
        controls["stable_semisimple"]["spectral_criterion_satisfied"]
        and not controls["jordan_unit_circle"]["spectral_criterion_satisfied"]
        and not controls["supercritical"]["spectral_criterion_satisfied"]
    )

    families=[
        _audit_operator_family(
            "annual-sunspots",_sunspot_operators(root),horizon
        ),
        _audit_operator_family(
            "mauna-loa-co2",_co2_operators(root),horizon
        ),
        _audit_operator_family(
            "enso-pacific-sst",_enso_operators(root),horizon
        ),
    ]
    total=sum(f["operators"] for f in families)
    passed=sum(f["criterion_passed"] for f in families)

    # Current synthetic core seed states.
    seed_states=[
        make_random_seed_state(dim=6,persistent_rank=4,seed=17),
        make_commuting_control_state(dim=6,persistent_rank=4,seed=17),
    ]
    synthetic=[
        recursive_stability_certificate(
            state.R_C,horizon=horizon
        ).to_dict()
        for state in seed_states
    ]
    synthetic_pass=all(
        x["spectral_criterion_satisfied"] for x in synthetic
    )

    result={
        "audit_passed":bool(
            controls_pass
            and synthetic_pass
            and passed==total
        ),
        "theorem_scope":"finite-dimensional recursive closure operators",
        "claim_class":"numerical audit of theorem hypotheses",
        "source_fingerprint":source_tree_fingerprint(),
        "horizon":horizon,
        "controls_passed":controls_pass,
        "synthetic_core_passed":synthetic_pass,
        "development_carrier_operators":total,
        "development_carrier_criterion_passed":passed,
        "development_carrier_pass_fraction":passed/max(total,1),
        "families":families,
        "controls":controls,
        "synthetic_core":synthetic,
        "interpretation_guard":{
            "global_all_BFG_carriers_proved":False,
            "infinite_dimensional_extension_proved":False,
            "natural_realization_proved":False,
            "note":(
                "The mathematical theorem is exact under its stated finite-"
                "dimensional assumptions. This audit only checks numerical "
                "hypotheses for the current implemented operators."
            ),
        },
    }
    return result


def write_stability_audit(
    result:dict[str,Any],
    outdir:str|Path,
)->dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"recursive_stability_audit.json"
    json_path.write_text(
        json.dumps(result,indent=2),encoding="utf-8"
    )

    md_path=outdir/"RECURSIVE_STABILITY_AUDIT.md"
    lines=[
        "# BFG Recursive Stability Audit",
        "",
        f"Audit: **{'PASS' if result['audit_passed'] else 'FAIL'}**",
        "",
        "This is a numerical audit of the hypotheses of the finite-dimensional "
        "recursive stability theorem. It is not the theorem itself.",
        "",
        f"Development/carrier operators checked: "
        f"`{result['development_carrier_operators']}`",
        "",
        f"Spectral criterion satisfied: "
        f"`{result['development_carrier_criterion_passed']}/"
        f"{result['development_carrier_operators']}`",
        "",
        "| Carrier | Operators | Pass fraction | Max rho | Min stable gap |",
        "|---|---:|---:|---:|---:|",
    ]
    for f in result["families"]:
        lines.append(
            f"| {f['carrier_id']} | {f['operators']} | "
            f"{f['pass_fraction']:.6f} | "
            f"{f['max_spectral_radius']:.12g} | "
            f"{f['minimum_stable_gap']:.6g} |"
        )
    lines += [
        "",
        "Control behavior:",
        "",
        f"- semisimple unit-circle control accepted: "
        f"`{result['controls']['stable_semisimple']['spectral_criterion_satisfied']}`",
        f"- unit-circle Jordan block rejected: "
        f"`{not result['controls']['jordan_unit_circle']['spectral_criterion_satisfied']}`",
        f"- supercritical eigenvalue rejected: "
        f"`{not result['controls']['supercritical']['spectral_criterion_satisfied']}`",
        "",
        "Interpretation guard: a PASS means the current finite-dimensional "
        "operators satisfy the theorem's numerical spectral hypotheses. It does "
        "not prove every possible BFG carrier or an infinite-dimensional extension.",
    ]
    md_path.write_text("\n".join(lines)+"\n",encoding="utf-8")
    return {
        "json":str(json_path),
        "markdown":str(md_path),
    }
