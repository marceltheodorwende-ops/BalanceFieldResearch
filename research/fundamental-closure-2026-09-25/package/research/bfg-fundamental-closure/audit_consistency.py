"""Static/reproducibility audit for the living BFG Fundamental Closure package."""

from __future__ import annotations

import ast
import collections
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "research" / "bfg-fundamental-closure"

REQUIRED = [
    "README.md",
    "INTEGRATION.md",
    "PACKAGE_STATUS.json",
    "bfg_lab/fundamental_closure.py",
    "tests/test_fundamental_closure.py",
    "research/bfg-fundamental-closure/README.md",
    "research/bfg-fundamental-closure/BFG_ONLY_CONTRACT.md",
    "research/bfg-fundamental-closure/CONSISTENCY_AUDIT.md",
    "research/bfg-fundamental-closure/MASTER_STATE.md",
    "research/bfg-fundamental-closure/UNIVERSAL_STATE_UPDATE_CANDIDATE.md",
    "research/bfg-fundamental-closure/FUNDAMENTAL_CLOSURE_LAW.md",
    "research/bfg-fundamental-closure/CLAIMS.md",
    "research/bfg-fundamental-closure/RESEARCH_PLAN.md",
    "research/bfg-fundamental-closure/FALSIFICATION.md",
    "research/bfg-fundamental-closure/PRIOR_ART_BOUNDARY.md",
    "research/bfg-fundamental-closure/stress_csr.py",
    "research/bfg-fundamental-closure/CSR_STRESS_RESULTS.json",
    "research/bfg-fundamental-closure/stress_neutral_contrast.py",
    "research/bfg-fundamental-closure/NEUTRAL_CONTRAST_STRESS_RESULTS.json",
]

AUTHORITATIVE = [
    RESEARCH / "BFG_ONLY_CONTRACT.md",
    RESEARCH / "MASTER_STATE.md",
    RESEARCH / "UNIVERSAL_STATE_UPDATE_CANDIDATE.md",
    RESEARCH / "FUNDAMENTAL_CLOSURE_LAW.md",
    RESEARCH / "CLAIMS.md",
]

FORBIDDEN_CURRENT = {
    "dual_load_failure": "obsolete terminal label",
    "Current finite committed state uses vector-only quotient": "obsolete state semantics",
}


def fail(msg):
    raise AssertionError(msg)


def check_required():
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail(f"missing required files: {missing}")


def check_python():
    src = (ROOT / "bfg_lab/fundamental_closure.py").read_text(encoding="utf-8")
    tree = ast.parse(src)
    names = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.append(node.name)
    dup = [n for n, c in collections.Counter(names).items() if c > 1]
    if dup:
        fail(f"duplicate top-level Python definitions: {dup}")


def check_claim_ids():
    text = (RESEARCH / "CLAIMS.md").read_text(encoding="utf-8")
    ids = re.findall(r"\|\s*(F\d{3})\s*\|", text)
    dup = [n for n, c in collections.Counter(ids).items() if c > 1]
    if dup:
        fail(f"duplicate claim IDs: {dup}")


def check_json():
    for path in RESEARCH.glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))

    for name in ("CSR_STRESS_RESULTS.json", "NEUTRAL_CONTRAST_STRESS_RESULTS.json"):
        data = json.loads((RESEARCH / name).read_text(encoding="utf-8"))
        reasons = data.get("terminal_or_boundary_counts", {})
        semantics = data.get("runtime_stop_semantics_counts", {})
        ambiguity = sum(v for k, v in reasons.items() if "ambiguity" in k)
        if semantics.get("numerical_unresolved") != ambiguity:
            fail(
                f"{name}: numerical_unresolved={semantics.get('numerical_unresolved')} "
                f"but ambiguity reasons sum to {ambiguity}"
            )

    neutral = json.loads(
        (RESEARCH / "NEUTRAL_CONTRAST_STRESS_RESULTS.json").read_text(encoding="utf-8")
    )
    if "dual_load_failure" in neutral.get("terminal_or_boundary_counts", {}):
        fail("neutral stress JSON still uses obsolete dual_load_failure label")

def check_manifest():
    text = (ROOT / "INTEGRATION.md").read_text(encoding="utf-8")
    listed = re.findall(
        r"^(research/[^\s`]+|bfg_lab/[^\s`]+|tests/[^\s`]+)$",
        text,
        re.M,
    )
    missing = [p for p in listed if not (ROOT / p).exists()]
    if missing:
        fail(f"manifest references missing files: {missing}")


def check_markdown_refs():
    md_files = list(ROOT.rglob("*.md"))
    all_names = {p.name for p in md_files}
    bad = []
    link_pat = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for p in md_files:
        text = p.read_text(encoding="utf-8", errors="replace")
        for target in link_pat.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "#", "mailto:", "sandbox:")):
                continue
            base = target.split("#")[0]
            if base and not (p.parent / base).resolve().exists():
                bad.append((str(p.relative_to(ROOT)), target))
        for name in re.findall(r"`([A-Z0-9_\-]+\.md)`", text):
            if name not in all_names:
                bad.append((str(p.relative_to(ROOT)), name))
    if bad:
        fail(f"broken markdown references: {bad[:20]}")


def check_authoritative_semantics():
    combined = "\n".join(p.read_text(encoding="utf-8") for p in AUTHORITATIVE)
    for term, why in FORBIDDEN_CURRENT.items():
        if term in combined:
            fail(f"{why}: found {term!r} in authoritative files")

    master = (RESEARCH / "MASTER_STATE.md").read_text(encoding="utf-8")
    if r"\rho_F" not in master or r"\rho_W" not in master:
        fail("master state does not contain both rho_F and rho_W")

    law = (RESEARCH / "FUNDAMENTAL_CLOSURE_LAW.md").read_text(encoding="utf-8")
    if r"\mathbf1_{(0,1)}(Y)" in law:
        fail("selection interval incorrectly excludes exact y=0; expected [0,1)")
    if r"\mathbf1_{[0,1)}(Y)" not in law:
        fail("authoritative neutral-selection load interval is missing")

    candidate = (RESEARCH / "UNIVERSAL_STATE_UPDATE_CANDIDATE.md").read_text(encoding="utf-8")
    for phrase in (
        "intrinsic-Gram successor load",
        "Neutral-Contrast Selection Principle",
        "neutral transverse recursive rebuild",
    ):
        if phrase not in candidate:
            fail(f"finite completion status missing: {phrase}")


def main():
    checks = [
        check_required,
        check_python,
        check_claim_ids,
        check_json,
        check_manifest,
        check_markdown_refs,
        check_authoritative_semantics,
    ]
    for fn in checks:
        fn()
    print(json.dumps({
        "status": "PASS",
        "checks": [fn.__name__ for fn in checks],
        "required_files": len(REQUIRED),
    }, indent=2))


if __name__ == "__main__":
    main()
