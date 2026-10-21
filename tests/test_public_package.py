from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "README.md",
    "LICENSE",
    "AGENTS.md",
    "specs/meeting-brief-contract.md",
    "skills/meeting-recording-brief/SKILL.md",
    "skills/meeting-recording-brief/references/output-template.md",
    "agents/hermes/SKILL.md",
    "agents/claude-code/SKILL.md",
    "agents/codex/AGENTS.md",
}


class PublicPackageTests(unittest.TestCase):
    def test_has_portable_skill_and_host_adapters(self):
        missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
        self.assertEqual(missing, [])

    def test_no_private_machine_or_recording_markers(self):
        prohibited = ("/root/", "[REDACTED]", "Bitrix24", "Битрам", "MENhausen")
        checked = [path for path in ROOT.rglob("*") if path.suffix in {".md", ".toml"}]
        for path in checked:
            content = path.read_text(encoding="utf-8")
            for marker in prohibited:
                self.assertNotIn(marker, content, f"{marker} leaked into {path.relative_to(ROOT)}")

    def test_every_adapter_points_to_one_contract(self):
        for path in (ROOT / "agents").rglob("*.md"):
            self.assertIn("specs/meeting-brief-contract.md", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
