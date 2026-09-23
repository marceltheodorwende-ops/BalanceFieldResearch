from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import hashlib
import json
import re

from .session import source_tree_fingerprint


STATUS_EXPLORATORY = "EXPLORATORY"
STATUS_NOT_YET = "NOT_YET_VALIDATED"
STATUS_READY = "READY_FOR_VALIDATION"
STATUS_CONFIRMED = "CONFIRMED"
STATUS_REJECTED = "REJECTED"

VALID_STATUSES = {
    STATUS_EXPLORATORY,
    STATUS_NOT_YET,
    STATUS_READY,
    STATUS_CONFIRMED,
    STATUS_REJECTED,
}

TERMINAL_STATUSES = {STATUS_CONFIRMED, STATUS_REJECTED}

ALLOWED_TRANSITIONS = {
    STATUS_EXPLORATORY: {STATUS_EXPLORATORY, STATUS_NOT_YET, STATUS_READY},
    STATUS_NOT_YET: {STATUS_NOT_YET, STATUS_EXPLORATORY, STATUS_READY},
    STATUS_READY: {STATUS_READY, STATUS_CONFIRMED, STATUS_REJECTED},
    STATUS_CONFIRMED: {STATUS_CONFIRMED},
    STATUS_REJECTED: {STATUS_REJECTED},
}

CONFIRMATION_ACK = "CONFIRM HELDOUT OPENING"


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: str | Path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _slug(text: str) -> str:
    x = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return x or "carrier"


def normalize_status(entry: dict[str, Any]) -> str:
    raw = str(entry.get("status", "")).strip()
    if raw in VALID_STATUSES:
        return raw
    upper = raw.upper()
    if upper.startswith("FAIL") or upper.startswith("REJECT"):
        return STATUS_REJECTED
    if upper.startswith("PASS") or upper.startswith("CONFIRM"):
        return STATUS_CONFIRMED
    if entry.get("primary_statement_passed") is False:
        return STATUS_REJECTED
    if entry.get("primary_statement_passed") is True:
        return STATUS_CONFIRMED
    if entry.get("heldout_metrics_evaluated") is False and "READY" in upper:
        return STATUS_READY
    return STATUS_EXPLORATORY


@dataclass(frozen=True)
class PortfolioEntry:
    carrier_id: str
    name: str
    domain: str
    status: str
    mapping_fingerprint: str | None
    plan_fingerprint: str | None
    heldout_metrics_evaluated: bool | None
    prepared_dir: str | None
    readiness_token: str | None
    frozen_model: str | None
    validation_plan: str | None
    result_artifact: str | None
    raw: dict[str, Any]

    @classmethod
    def from_registry(cls, raw: dict[str, Any]) -> "PortfolioEntry":
        status = normalize_status(raw)
        return cls(
            carrier_id=str(raw.get("id") or _slug(str(raw.get("name", "carrier")))),
            name=str(raw.get("name", "")),
            domain=str(raw.get("domain", "")),
            status=status,
            mapping_fingerprint=raw.get("mapping_fingerprint"),
            plan_fingerprint=raw.get("plan_fingerprint"),
            heldout_metrics_evaluated=raw.get("heldout_metrics_evaluated"),
            prepared_dir=raw.get("prepared_dir"),
            readiness_token=raw.get("readiness_token"),
            frozen_model=raw.get("frozen_model"),
            validation_plan=raw.get("validation_plan"),
            result_artifact=raw.get("result_artifact"),
            raw=dict(raw),
        )

    def summary(self) -> dict[str, Any]:
        return {
            "id": self.carrier_id,
            "name": self.name,
            "domain": self.domain,
            "status": self.status,
            "mapping_fingerprint": self.mapping_fingerprint,
            "plan_fingerprint": self.plan_fingerprint,
            "heldout_metrics_evaluated": self.heldout_metrics_evaluated,
        }


class ValidationPortfolio:
    def __init__(
        self,
        project_root: str | Path | None = None,
        registry_path: str | Path | None = None,
    ):
        self.project_root = (
            Path(project_root)
            if project_root is not None
            else Path(__file__).resolve().parent.parent
        )
        self.registry_path = (
            Path(registry_path)
            if registry_path is not None
            else self.project_root / "EMPIRICAL_BENCHMARK_REGISTRY.json"
        )
        self._payload = json.loads(self.registry_path.read_text(encoding="utf-8"))
        raws = self._payload.get("empirical_benchmarks", [])
        self.entries = [PortfolioEntry.from_registry(r) for r in raws]
        ids = [e.carrier_id for e in self.entries]
        if len(ids) != len(set(ids)):
            raise ValueError("portfolio carrier ids must be unique")

    def get(self, carrier_id: str) -> PortfolioEntry:
        for entry in self.entries:
            if entry.carrier_id == carrier_id:
                return entry
        raise KeyError(f"unknown carrier id: {carrier_id}")

    def resolve(self, relative_or_absolute: str | None) -> Path | None:
        if not relative_or_absolute:
            return None
        p = Path(relative_or_absolute)
        return p if p.is_absolute() else self.project_root / p

    def audit_entry(self, entry: PortfolioEntry) -> dict[str, Any]:
        checks: dict[str, bool] = {}
        diagnostics: dict[str, Any] = {}

        checks["valid_status"] = entry.status in VALID_STATUSES
        checks["name_present"] = bool(entry.name.strip())
        checks["domain_present"] = bool(entry.domain.strip())
        checks["mapping_fingerprint_shape"] = (
            entry.mapping_fingerprint is None
            or len(str(entry.mapping_fingerprint)) == 64
        )
        checks["plan_fingerprint_shape"] = (
            entry.plan_fingerprint is None
            or len(str(entry.plan_fingerprint)) == 64
        )

        if entry.status == STATUS_READY:
            checks["heldout_not_evaluated"] = (
                entry.heldout_metrics_evaluated is False
            )
            token = self.resolve(entry.readiness_token)
            frozen = self.resolve(entry.frozen_model)
            plan = self.resolve(entry.validation_plan)
            checks["readiness_token_exists"] = bool(token and token.exists())
            checks["frozen_model_exists"] = bool(frozen and frozen.exists())
            checks["validation_plan_exists"] = bool(plan and plan.exists())
        elif entry.status in TERMINAL_STATUSES:
            evaluated = entry.heldout_metrics_evaluated
            if evaluated is None:
                evaluated = "primary_statement_passed" in entry.raw
            checks["confirmatory_result_recorded"] = bool(evaluated)
            result = self.resolve(entry.result_artifact)
            if entry.result_artifact:
                checks["result_artifact_exists"] = bool(result and result.exists())

            if entry.status == STATUS_CONFIRMED:
                checks["terminal_result_consistent"] = (
                    entry.raw.get("primary_statement_passed", True) is not False
                )
            else:
                checks["terminal_result_consistent"] = (
                    entry.raw.get("primary_statement_passed", False) is not True
                )
        else:
            # Exploratory / not-yet states must not claim held-out success.
            checks["no_confirmatory_pass_claim"] = (
                entry.raw.get("primary_statement_passed") is not True
            )

        diagnostics["status"] = entry.status
        diagnostics["heldout_metrics_evaluated"] = entry.heldout_metrics_evaluated
        return {
            "id": entry.carrier_id,
            "valid": all(checks.values()),
            "checks": checks,
            "diagnostics": diagnostics,
        }

    def audit(self) -> dict[str, Any]:
        reports = [self.audit_entry(e) for e in self.entries]
        counts = {s: 0 for s in sorted(VALID_STATUSES)}
        for e in self.entries:
            counts[e.status] = counts.get(e.status, 0) + 1
        return {
            "valid": all(r["valid"] for r in reports),
            "carrier_count": len(self.entries),
            "status_counts": counts,
            "source_fingerprint": source_tree_fingerprint(),
            "entries": reports,
        }

    def public_summary(self) -> dict[str, Any]:
        # This contains registry metadata only. It never opens a held-out dataset.
        return {
            "source_fingerprint": source_tree_fingerprint(),
            "entries": [e.summary() for e in self.entries],
            "audit": self.audit(),
        }


    def record_confirmatory_result(
        self,
        carrier_id: str,
        *,
        passed: bool,
        result_artifact: str,
        metrics: dict[str, Any] | None = None,
    ) -> PortfolioEntry:
        entry = self.get(carrier_id)
        if entry.status in TERMINAL_STATUSES:
            raise RuntimeError(
                f"carrier {carrier_id} already has terminal status {entry.status}"
            )
        new_status = STATUS_CONFIRMED if passed else STATUS_REJECTED
        if not self.transition_allowed(entry.status, new_status):
            raise RuntimeError(
                f"illegal portfolio transition: {entry.status} -> {new_status}"
            )

        raws = self._payload.get("empirical_benchmarks", [])
        updated = None
        for raw in raws:
            raw_id = str(raw.get("id") or _slug(str(raw.get("name", "carrier"))))
            if raw_id == carrier_id:
                raw["id"] = carrier_id
                raw["status"] = new_status
                raw["heldout_metrics_evaluated"] = True
                raw["primary_statement_passed"] = bool(passed)
                raw["result_artifact"] = str(result_artifact)
                raw["retuning_after_heldout"] = False
                if metrics:
                    raw["confirmatory_metrics"] = metrics
                updated = raw
                break
        if updated is None:
            raise KeyError(f"unknown carrier id: {carrier_id}")

        self.registry_path.write_text(
            json.dumps(self._payload, indent=2), encoding="utf-8"
        )
        # Reload immutable view after committing the terminal result.
        refreshed = ValidationPortfolio(
            project_root=self.project_root,
            registry_path=self.registry_path,
        )
        return refreshed.get(carrier_id)

    @staticmethod
    def transition_allowed(old_status: str, new_status: str) -> bool:
        if old_status not in ALLOWED_TRANSITIONS:
            return False
        return new_status in ALLOWED_TRANSITIONS[old_status]


class BlindHeldoutGuard:
    """
    Cryptographic guard around confirmatory held-out opening.

    A READY carrier is sealed from its frozen plan/model/readiness artifacts.
    Confirmation requires a separately issued permit with an explicit acknowledgement.
    The guard never evaluates held-out targets itself.
    """

    def __init__(self, portfolio: ValidationPortfolio):
        self.portfolio = portfolio
        self.validation_dir = portfolio.project_root / "validation"
        self.seal_dir = self.validation_dir / "seals"
        self.permit_dir = self.validation_dir / "permits"
        self.seal_dir.mkdir(parents=True, exist_ok=True)
        self.permit_dir.mkdir(parents=True, exist_ok=True)

    def _artifact_digest(self, rel: str | None) -> dict[str, str] | None:
        p = self.portfolio.resolve(rel)
        if p is None or not p.exists():
            return None
        return {
            "path": str(Path(rel)) if rel is not None else str(p),
            "sha256": file_sha256(p),
        }

    def build_seal(self, carrier_id: str) -> dict[str, Any]:
        entry = self.portfolio.get(carrier_id)
        if entry.status != STATUS_READY:
            raise RuntimeError(
                f"carrier {carrier_id} cannot be sealed for confirmation "
                f"from status {entry.status}"
            )
        audit = self.portfolio.audit_entry(entry)
        if not audit["valid"]:
            failed = [k for k, ok in audit["checks"].items() if not ok]
            raise RuntimeError(
                "portfolio entry is not ready to seal: " + ", ".join(failed)
            )

        artifacts = {
            "readiness_token": self._artifact_digest(entry.readiness_token),
            "frozen_model": self._artifact_digest(entry.frozen_model),
            "validation_plan": self._artifact_digest(entry.validation_plan),
        }
        payload = {
            "carrier_id": entry.carrier_id,
            "status": entry.status,
            "mapping_fingerprint": entry.mapping_fingerprint,
            "plan_fingerprint": entry.plan_fingerprint,
            "source_fingerprint": source_tree_fingerprint(),
            "artifacts": artifacts,
            "heldout_metrics_evaluated": False,
        }
        canonical = json.dumps(
            payload, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        payload["seal_fingerprint"] = _sha256_bytes(canonical)

        path = self.seal_dir / f"{entry.carrier_id}.json"
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return payload

    def audit_seal(self, carrier_id: str) -> dict[str, Any]:
        entry = self.portfolio.get(carrier_id)
        path = self.seal_dir / f"{carrier_id}.json"
        if not path.exists():
            return {"valid": False, "reason": "seal_missing"}

        seal = json.loads(path.read_text(encoding="utf-8"))
        checks = {
            "carrier_id": seal.get("carrier_id") == entry.carrier_id,
            "status_ready": entry.status == STATUS_READY,
            "source_fingerprint": (
                seal.get("source_fingerprint") == source_tree_fingerprint()
            ),
            "mapping_fingerprint": (
                seal.get("mapping_fingerprint") == entry.mapping_fingerprint
            ),
            "plan_fingerprint": (
                seal.get("plan_fingerprint") == entry.plan_fingerprint
            ),
            "heldout_not_evaluated": entry.heldout_metrics_evaluated is False,
        }
        for key, rel in {
            "readiness_token": entry.readiness_token,
            "frozen_model": entry.frozen_model,
            "validation_plan": entry.validation_plan,
        }.items():
            expected = (seal.get("artifacts") or {}).get(key)
            p = self.portfolio.resolve(rel)
            checks[f"{key}_exists"] = bool(p and p.exists())
            checks[f"{key}_unchanged"] = bool(
                expected
                and p
                and p.exists()
                and expected.get("sha256") == file_sha256(p)
            )

        canonical_payload = {
            k: v for k, v in seal.items() if k != "seal_fingerprint"
        }
        canonical = json.dumps(
            canonical_payload, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        checks["seal_integrity"] = (
            seal.get("seal_fingerprint") == _sha256_bytes(canonical)
        )
        return {
            "valid": all(checks.values()),
            "checks": checks,
            "seal_fingerprint": seal.get("seal_fingerprint"),
        }

    def issue_confirmation_permit(
        self,
        carrier_id: str,
        acknowledgement: str,
    ) -> Path:
        if acknowledgement.strip() != CONFIRMATION_ACK:
            raise ValueError(
                f"confirmation acknowledgement must be exactly: "
                f"{CONFIRMATION_ACK!r}"
            )
        seal_audit = self.audit_seal(carrier_id)
        if not seal_audit["valid"]:
            raise RuntimeError("cannot issue permit: held-out seal audit failed")

        seal_path = self.seal_dir / f"{carrier_id}.json"
        seal = json.loads(seal_path.read_text(encoding="utf-8"))
        payload = {
            "carrier_id": carrier_id,
            "seal_fingerprint": seal["seal_fingerprint"],
            "mapping_fingerprint": seal["mapping_fingerprint"],
            "plan_fingerprint": seal["plan_fingerprint"],
            "acknowledgement": CONFIRMATION_ACK,
            "consumed": False,
        }
        canonical = json.dumps(
            payload, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        payload["permit_fingerprint"] = _sha256_bytes(canonical)

        path = self.permit_dir / f"{carrier_id}.json"
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return path

    def validate_confirmation_permit(
        self,
        carrier_id: str,
        permit_path: str | Path,
    ) -> dict[str, Any]:
        permit_path = Path(permit_path)
        if not permit_path.exists():
            raise RuntimeError("confirmation permit does not exist")
        permit = json.loads(permit_path.read_text(encoding="utf-8"))
        seal_audit = self.audit_seal(carrier_id)
        if not seal_audit["valid"]:
            raise RuntimeError("held-out seal is no longer valid")
        seal = json.loads(
            (self.seal_dir / f"{carrier_id}.json").read_text(encoding="utf-8")
        )

        checks = {
            "carrier_id": permit.get("carrier_id") == carrier_id,
            "acknowledgement": (
                permit.get("acknowledgement") == CONFIRMATION_ACK
            ),
            "not_consumed": permit.get("consumed") is False,
            "seal_fingerprint": (
                permit.get("seal_fingerprint") == seal.get("seal_fingerprint")
            ),
            "mapping_fingerprint": (
                permit.get("mapping_fingerprint") == seal.get("mapping_fingerprint")
            ),
            "plan_fingerprint": (
                permit.get("plan_fingerprint") == seal.get("plan_fingerprint")
            ),
        }
        canonical_payload = {
            k: v for k, v in permit.items() if k != "permit_fingerprint"
        }
        canonical = json.dumps(
            canonical_payload, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        checks["permit_integrity"] = (
            permit.get("permit_fingerprint") == _sha256_bytes(canonical)
        )
        if not all(checks.values()):
            failed = [k for k, ok in checks.items() if not ok]
            raise RuntimeError(
                "invalid confirmation permit: " + ", ".join(failed)
            )
        return {
            "valid": True,
            "checks": checks,
            "permit_fingerprint": permit["permit_fingerprint"],
        }

    def consume_confirmation_permit(
        self,
        carrier_id: str,
        permit_path: str | Path,
    ) -> dict[str, Any]:
        permit_path = Path(permit_path)
        audit = self.validate_confirmation_permit(carrier_id, permit_path)
        permit = json.loads(permit_path.read_text(encoding="utf-8"))
        permit["consumed"] = True
        permit["opened_under_seal"] = True
        # Re-sign the consumed state so later audits can prove the explicit opening.
        canonical = json.dumps(
            {k: v for k, v in permit.items() if k != "permit_fingerprint"},
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        permit["permit_fingerprint"] = _sha256_bytes(canonical)
        permit_path.write_text(json.dumps(permit, indent=2), encoding="utf-8")
        return {
            "consumed": True,
            "carrier_id": carrier_id,
            "prior_permit_fingerprint": audit["permit_fingerprint"],
            "consumed_permit_fingerprint": permit["permit_fingerprint"],
        }


def write_portfolio_report(
    portfolio: ValidationPortfolio,
    outdir: str | Path | None = None,
) -> dict[str, str]:
    outdir = (
        Path(outdir)
        if outdir is not None
        else portfolio.project_root / "validation"
    )
    outdir.mkdir(parents=True, exist_ok=True)
    summary = portfolio.public_summary()
    guard = BlindHeldoutGuard(portfolio)
    guard_status = {}
    for entry in portfolio.entries:
        if entry.status == STATUS_READY:
            guard_status[entry.carrier_id] = guard.audit_seal(entry.carrier_id)
        else:
            guard_status[entry.carrier_id] = {
                "valid": None,
                "reason": "not_applicable_for_terminal_or_development_status",
            }
    summary["confirmation_guard"] = guard_status

    json_path = outdir / "portfolio_status.json"
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    md_path = outdir / "PORTFOLIO_STATUS.md"
    lines = [
        "# BFG Emergence Studio — Validation Portfolio",
        "",
        f"Portfolio audit: **{'PASS' if summary['audit']['valid'] else 'FAIL'}**",
        "",
        "| Carrier | Domain | Status | Held-out evaluated | Confirmatory seal |",
        "|---|---|---|---:|---:|",
    ]
    for entry in portfolio.entries:
        seal_state = summary["confirmation_guard"][entry.carrier_id]["valid"]
        lines.append(
            f"| {entry.name} | {entry.domain} | {entry.status} | "
            f"{entry.heldout_metrics_evaluated} | {seal_state} |"
        )
    lines += [
        "",
        "A `READY_FOR_VALIDATION` entry is not an empirical pass.",
        "Terminal confirmatory results are immutable for their frozen plan.",
        "",
        f"Source fingerprint: `{summary['source_fingerprint']}`",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"json": str(json_path), "markdown": str(md_path)}
