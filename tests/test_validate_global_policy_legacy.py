#!/usr/bin/env python3
"""Regression: legacy is excluded from active global policy but not from containment."""
from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "legacy_global_audit", ROOT / "scripts/validate-global-audit-policy.py"
)
module = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(module)
LEGACY = "Vivaliz-site/solange-rolla"


def canonical():
    return {
        "schema": module.EXPECTED_SCHEMA,
        "version": module.EXPECTED_VERSION,
        "canonical_repository": module.CANONICAL_REPO,
        "canonical_ref": "main",
        "required_repositories": list(module.EXPECTED_REPOSITORIES),
        "required_blobs": {"AUDIT_POLICY.md": "0" * 40},
        "required_entrypoint_markers": {"AGENTS.md": ["mandatory"]},
    }


class GlobalLegacyPolicyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.make_safe_containment()

    def make_safe_containment(self):
        (self.root / "README.md").write_text(
            "REPOSITÓRIO HISTÓRICO / SUPERSEDIDO\n", encoding="utf-8"
        )
        wf = self.root / ".github/workflows"
        wf.mkdir(parents=True, exist_ok=True)
        guard = (
            "on:\n  pull_request:\n"
            "jobs:\n  gate:\n"
            "    if: github.event.pull_request.head.repo.full_name == github.repository\n"
        )
        (wf / "ci.yml").write_text(guard, encoding="utf-8")
        (wf / "repository-governance.yml").write_text(
            guard + "    run: echo LEGACY_SOLANGE_CONTAINMENT=PASS\n",
            encoding="utf-8",
        )

    def check_legacy(self, manifest=None):
        real_checker = module.verify_legacy_containment
        with patch.dict(os.environ, {"GITHUB_REPOSITORY": LEGACY}), patch.object(
            module, "verify_legacy_containment", side_effect=lambda: real_checker(self.root)
        ):
            return module.check(manifest or canonical(), False)

    def test_exclusion_requires_real_containment(self):
        result = self.check_legacy()
        self.assertTrue(result["ok"], result)
        self.assertFalse(result["repository_covered"])
        self.assertFalse(result["local_manifest_parity"])
        self.assertEqual(result["mode"], "superseded_excluded_by_canonical_manifest")
        self.assertTrue(result["legacy_containment"]["ok"])

    def test_readme_marker_missing_fails(self):
        (self.root / "README.md").write_text("unrelated repository\n", encoding="utf-8")
        self.assertFalse(self.check_legacy()["ok"])

    def test_pull_request_guard_missing_fails(self):
        (self.root / ".github/workflows/ci.yml").write_text(
            "on:\n  pull_request:\n", encoding="utf-8"
        )
        self.assertFalse(self.check_legacy()["ok"])

    def test_push_trigger_in_existing_containment_workflow_fails(self):
        ci = self.root / ".github/workflows/ci.yml"
        ci.write_text(ci.read_text(encoding="utf-8") + "  push:\n", encoding="utf-8")
        self.assertFalse(self.check_legacy()["ok"])

    def test_containment_attestation_missing_fails(self):
        governance = self.root / ".github/workflows/repository-governance.yml"
        governance.write_text(
            governance.read_text(encoding="utf-8").replace(
                "LEGACY_SOLANGE_CONTAINMENT=PASS", "NO_ATTESTATION"
            ), encoding="utf-8"
        )
        self.assertFalse(self.check_legacy()["ok"])

    def test_canonical_metadata_mismatch_fails(self):
        data = canonical()
        data["canonical_repository"] = "untrusted/other"
        self.assertFalse(self.check_legacy(data)["ok"])

    def test_canonical_includes_legacy_must_not_be_exempt(self):
        data = canonical()
        data["required_repositories"].append(LEGACY)
        self.assertFalse(self.check_legacy(data)["ok"])

    def test_nonlegacy_repository_does_not_get_exclusion(self):
        with patch.dict(os.environ, {"GITHUB_REPOSITORY": "Vivaliz-site/site-shopvivaliz"}), patch.object(
            module, "ROOT", self.root
        ):
            result = module.check(canonical(), False)
        self.assertFalse(result["ok"])
        self.assertNotIn("mode", result)


if __name__ == "__main__":
    unittest.main()
