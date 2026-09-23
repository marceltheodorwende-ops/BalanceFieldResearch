from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import hashlib
import json
import platform
import sys

import numpy as np
import scipy

from .types import BFGState


def _jsonable(value: Any):
    if isinstance(value, np.ndarray):
        if np.iscomplexobj(value):
            return {
                "__ndarray_complex__": True,
                "shape": list(value.shape),
                "real": value.real.tolist(),
                "imag": value.imag.tolist(),
            }
        return {
            "__ndarray__": True,
            "shape": list(value.shape),
            "data": value.tolist(),
        }
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, complex):
        return {"__complex__": True, "real": value.real, "imag": value.imag}
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if hasattr(value, "__dataclass_fields__"):
        return _jsonable(asdict(value))
    return value


def _from_jsonable(value: Any):
    if isinstance(value, list):
        return [_from_jsonable(v) for v in value]
    if not isinstance(value, dict):
        return value
    if value.get("__ndarray_complex__"):
        real = np.asarray(value["real"], dtype=float)
        imag = np.asarray(value["imag"], dtype=float)
        return real + 1j*imag
    if value.get("__ndarray__"):
        return np.asarray(value["data"])
    if value.get("__complex__"):
        return complex(value["real"], value["imag"])
    return {k: _from_jsonable(v) for k, v in value.items()}


def source_tree_fingerprint(package_dir: str | Path | None = None) -> str:
    package_dir = Path(package_dir) if package_dir else Path(__file__).resolve().parent
    h = hashlib.sha256()
    for p in sorted(package_dir.glob("*.py")):
        h.update(p.name.encode("utf-8"))
        h.update(b"\0")
        h.update(p.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def file_sha256(path: str | Path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()


@dataclass(frozen=True)
class ProvenanceManifest:
    experiment: str
    seed: int | None
    parameters: dict[str, Any]
    source_fingerprint: str
    python: str
    numpy: str
    scipy: str
    platform: str
    theory_freeze_level: str = "Identity Closure"
    theory_freeze_source_level: int = 30

    @classmethod
    def build(
        cls,
        experiment: str,
        seed: int | None,
        parameters: dict[str, Any] | None = None,
    ) -> "ProvenanceManifest":
        return cls(
            experiment=experiment,
            seed=seed,
            parameters=_jsonable(parameters or {}),
            source_fingerprint=source_tree_fingerprint(),
            python=sys.version.split()[0],
            numpy=np.__version__,
            scipy=scipy.__version__,
            platform=platform.platform(),
        )

    def to_dict(self) -> dict[str, Any]:
        return _jsonable(asdict(self))


def save_manifest(
    manifest: ProvenanceManifest,
    path: str | Path,
) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        json.dumps(manifest.to_dict(), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return p


def save_bfg_checkpoint(
    state: BFGState,
    directory: str | Path,
    name: str = "checkpoint",
    manifest: ProvenanceManifest | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, str]:
    """
    Save a resumable finite-dimensional BFGState without pickle.

    Arrays live in NPZ; metadata and provenance are JSON. This keeps the checkpoint
    inspectable and avoids arbitrary-code deserialization.
    """
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    arrays_path = directory/f"{name}_arrays.npz"
    metadata_path = directory/f"{name}_metadata.json"
    manifest_path = directory/f"{name}_manifest.json"

    np.savez_compressed(
        arrays_path,
        D=np.asarray(state.D),
        K=np.asarray(state.K),
        Y=np.asarray(state.Y),
        R_C=np.asarray(state.R_C),
    )
    payload = {
        "generation": int(state.generation),
        "name": state.name,
        "metadata": _jsonable(state.metadata),
        "terminal": bool(state.terminal),
        "terminal_reason": state.terminal_reason,
        "extra": _jsonable(extra or {}),
        "arrays_sha256": file_sha256(arrays_path),
    }
    metadata_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    if manifest is None:
        manifest = ProvenanceManifest.build(
            experiment="bfg_checkpoint",
            seed=state.metadata.get("seed")
            if isinstance(state.metadata, dict) else None,
            parameters={"generation": state.generation, "name": state.name},
        )
    save_manifest(manifest, manifest_path)

    return {
        "arrays": str(arrays_path),
        "metadata": str(metadata_path),
        "manifest": str(manifest_path),
    }


def load_bfg_checkpoint(
    directory: str | Path,
    name: str = "checkpoint",
    verify_hash: bool = True,
) -> tuple[BFGState, dict[str, Any], dict[str, Any]]:
    directory = Path(directory)
    arrays_path = directory/f"{name}_arrays.npz"
    metadata_path = directory/f"{name}_metadata.json"
    manifest_path = directory/f"{name}_manifest.json"

    payload = json.loads(metadata_path.read_text(encoding="utf-8"))
    if verify_hash:
        actual = file_sha256(arrays_path)
        expected = payload["arrays_sha256"]
        if actual != expected:
            raise ValueError(
                f"checkpoint array hash mismatch: expected {expected}, got {actual}"
            )

    with np.load(arrays_path, allow_pickle=False) as data:
        state = BFGState(
            D=np.array(data["D"]),
            K=np.array(data["K"]),
            Y=np.array(data["Y"]),
            R_C=np.array(data["R_C"]),
            generation=int(payload["generation"]),
            name=str(payload["name"]),
            metadata=_from_jsonable(payload.get("metadata", {})),
            terminal=bool(payload.get("terminal", False)),
            terminal_reason=payload.get("terminal_reason"),
        )

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    extra = _from_jsonable(payload.get("extra", {}))
    return state, manifest, extra


def save_experiment_ledger(
    directory: str | Path,
    experiment: str,
    seed: int | None,
    parameters: dict[str, Any],
    summary: dict[str, Any],
    events: list[dict[str, Any]] | None = None,
    frames: list[dict[str, Any]] | None = None,
    name: str = "experiment",
) -> dict[str, str]:
    """
    Persist a source-fingerprinted experiment ledger.

    This is intended for exact audit/provenance even when a higher-level experiment
    does not yet support mid-run resumption.
    """
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    manifest = ProvenanceManifest.build(experiment, seed, parameters)

    manifest_path = directory/f"{name}_manifest.json"
    summary_path = directory/f"{name}_summary.json"
    events_path = directory/f"{name}_events.json"
    frames_path = directory/f"{name}_frames.json"

    save_manifest(manifest, manifest_path)
    summary_path.write_text(
        json.dumps(_jsonable(summary), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    events_path.write_text(
        json.dumps(_jsonable(events or []), indent=2),
        encoding="utf-8",
    )
    frames_path.write_text(
        json.dumps(_jsonable(frames or []), indent=2),
        encoding="utf-8",
    )

    return {
        "manifest": str(manifest_path),
        "summary": str(summary_path),
        "events": str(events_path),
        "frames": str(frames_path),
    }
