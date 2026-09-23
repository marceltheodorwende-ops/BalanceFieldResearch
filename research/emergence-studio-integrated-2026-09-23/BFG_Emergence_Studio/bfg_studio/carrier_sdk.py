from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import hashlib
import json
import numpy as np

from .carrier import CarrierAdapter
from .types import BFGState, CoreStep, NumericalPolicy
from .linalg import hermitize


@dataclass(frozen=True)
class CarrierSchema:
    name: str
    domain: str
    description: str
    measurement_mapping: dict[str, str]
    invariant_parameters: dict[str, Any]
    empirical_units: dict[str, str] | None = None
    schema_revision: int = 1

    def validate(self):
        required = {"D", "K", "Y", "R_C"}
        missing = required.difference(self.measurement_mapping)
        if missing:
            raise ValueError(
                "measurement_mapping must declare D, K, Y, R_C; "
                f"missing: {sorted(missing)}"
            )
        if not self.name.strip():
            raise ValueError("carrier name must be nonempty")
        if not self.domain.strip():
            raise ValueError("carrier domain must be nonempty")

    def fingerprint(self) -> str:
        self.validate()
        payload = json.dumps(
            asdict(self),
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class CarrierValidationReport:
    valid: bool
    dimension: int
    checks: dict[str, bool]
    diagnostics: dict[str, float | int | str | None]


def validate_state_contract(
    state: BFGState,
    policy: NumericalPolicy | None = None,
) -> CarrierValidationReport:
    policy = policy or NumericalPolicy()
    D = np.asarray(state.D)
    K = np.asarray(state.K)
    Y = np.asarray(state.Y)
    R = np.asarray(state.R_C)

    n = len(D) if D.ndim == 1 else -1
    shapes = (
        D.ndim == 1
        and K.shape == (n, n)
        and Y.shape == (n, n)
        and R.shape == (n, n)
    )
    finite = bool(
        np.all(np.isfinite(D))
        and np.all(np.isfinite(K))
        and np.all(np.isfinite(Y))
        and np.all(np.isfinite(R))
    ) if shapes else False

    k_hermitian_residual = (
        float(np.linalg.norm(K-K.conj().T, ord="fro"))
        if shapes else float("inf")
    )
    y_hermitian_residual = (
        float(np.linalg.norm(Y-Y.conj().T, ord="fro"))
        if shapes else float("inf")
    )
    k_hermitian = k_hermitian_residual <= 100*policy.atol
    y_hermitian = y_hermitian_residual <= 100*policy.atol

    min_eig_y = (
        float(np.min(np.linalg.eigvalsh(hermitize(Y)).real))
        if shapes and finite else float("-inf")
    )
    y_psd = min_eig_y >= -policy.psd_tol

    state_nonzero = (
        float(np.linalg.norm(D)) > policy.atol
        if shapes and finite else False
    )

    checks = {
        "shape_consistency": bool(shapes),
        "finite_values": bool(finite),
        "K_hermitian": bool(k_hermitian),
        "Y_hermitian": bool(y_hermitian),
        "Y_positive_semidefinite": bool(y_psd),
        "state_nonzero": bool(state_nonzero),
    }
    valid = all(checks.values())
    return CarrierValidationReport(
        valid=valid,
        dimension=max(n, 0),
        checks=checks,
        diagnostics={
            "K_hermitian_residual": k_hermitian_residual,
            "Y_hermitian_residual": y_hermitian_residual,
            "min_eigenvalue_Y": min_eig_y,
            "D_norm": float(np.linalg.norm(D)) if D.ndim else None,
        },
    )


class ValidatedCarrierAdapter(CarrierAdapter):
    """
    Stable SDK contract for independently mapped carriers.

    Domain code supplies the measurement -> BFG mapping and the carrier-specific
    next-state reconstruction. The generic BFG reclosure remains in `core.py`.
    """

    schema: CarrierSchema

    def __init__(self, schema: CarrierSchema):
        schema.validate()
        self.schema = schema
        self._frozen_fingerprint = schema.fingerprint()

    @property
    def mapping_fingerprint(self) -> str:
        return self._frozen_fingerprint

    def assert_no_retuning(self):
        current = self.schema.fingerprint()
        if current != self._frozen_fingerprint:
            raise RuntimeError(
                "carrier schema changed after freeze; no-retuning comparison invalid"
            )

    @abstractmethod
    def map_measurement_to_state(
        self,
        measurement: Any,
        *,
        generation: int = 0,
    ) -> BFGState:
        raise NotImplementedError

    @abstractmethod
    def advance(
        self,
        previous: BFGState,
        step: CoreStep,
        policy: NumericalPolicy,
    ) -> BFGState:
        raise NotImplementedError

    def validate_measurement_state(
        self,
        measurement: Any,
        *,
        generation: int = 0,
        policy: NumericalPolicy | None = None,
    ) -> tuple[BFGState, CarrierValidationReport]:
        self.assert_no_retuning()
        state = self.map_measurement_to_state(
            measurement,
            generation=generation,
        )
        report = validate_state_contract(state, policy)
        if not report.valid:
            failed = [k for k, ok in report.checks.items() if not ok]
            raise ValueError(
                "carrier mapping violates BFG state contract: "
                + ", ".join(failed)
            )
        return state, report


def write_carrier_schema(
    schema: CarrierSchema,
    path: str | Path,
) -> Path:
    schema.validate()
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    payload = asdict(schema)
    payload["mapping_fingerprint"] = schema.fingerprint()
    p.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )
    return p


def load_carrier_schema(path: str | Path) -> CarrierSchema:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    payload.pop("mapping_fingerprint", None)
    schema = CarrierSchema(**payload)
    schema.validate()
    return schema


def no_retuning_comparison(
    adapter: ValidatedCarrierAdapter,
    measurements: list[Any],
    *,
    policy: NumericalPolicy | None = None,
) -> dict[str, Any]:
    """
    Audit only the fixed mapping contract.

    This function deliberately does not optimize adapter parameters. Each supplied
    measurement is mapped with the same frozen schema fingerprint.
    """
    policy = policy or NumericalPolicy()
    adapter.assert_no_retuning()
    fingerprint = adapter.mapping_fingerprint
    reports = []
    for i, measurement in enumerate(measurements):
        state, report = adapter.validate_measurement_state(
            measurement,
            generation=i,
            policy=policy,
        )
        reports.append({
            "index": i,
            "generation": state.generation,
            "dimension": report.dimension,
            "valid": report.valid,
            "checks": report.checks,
            "diagnostics": report.diagnostics,
        })
        adapter.assert_no_retuning()

    return {
        "mapping_fingerprint": fingerprint,
        "measurements": len(measurements),
        "all_valid": all(r["valid"] for r in reports),
        "reports": reports,
    }


class ExternalCarrierTemplate(ValidatedCarrierAdapter):
    """
    Non-functional template.

    Subclass it in a domain module and implement the two abstract methods. Keeping
    it abstract prevents accidental presentation of a placeholder as a real carrier.
    """

    @abstractmethod
    def map_measurement_to_state(
        self,
        measurement: Any,
        *,
        generation: int = 0,
    ) -> BFGState:
        raise NotImplementedError

    @abstractmethod
    def advance(
        self,
        previous: BFGState,
        step: CoreStep,
        policy: NumericalPolicy,
    ) -> BFGState:
        raise NotImplementedError
