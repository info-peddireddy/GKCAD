from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PhaseZeroArtifactTests(unittest.TestCase):
    def test_required_phase_zero_files_exist(self) -> None:
        required = [
            "KCAD_QUESTIONS.md",
            "config/company.yaml",
            "docs/prototype-assessment.md",
            "docs/severity.md",
        ]
        for relative_path in required:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)

    def test_configuration_uses_safe_defaults(self) -> None:
        text = (ROOT / "config/company.yaml").read_text(encoding="utf-8")
        self.assertIn("units: us_customary", text)
        self.assertIn("Released", text)
        self.assertIn("licensed_standards: []", text)

    def test_decisions_are_recorded(self) -> None:
        adrs = sorted((ROOT / "docs/adr").glob("ADR-*.md"))
        self.assertGreaterEqual(len(adrs), 3)
