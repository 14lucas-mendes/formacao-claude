"""Regressões para a classificação curricular e o comando de validação."""

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
VALIDATOR = REPOSITORY / "scripts" / "validate_curriculum.py"


class CurriculumValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / ".ai-tutor").mkdir()
        self.config = {
            "curriculum_tracks": {
                "core_topic_ids": ["topic_core"],
                "optional_topic_ids": ["topic_optional"],
                "retired_topic_ids": ["topic_retired"],
            },
        }
        self.state = {
            "topics": [
                {"topic_id": "topic_core"},
                {"topic_id": "topic_optional"},
                {"topic_id": "topic_retired"},
            ],
        }
        self.curriculum = "- [ ] `topic_core`: competência obrigatória\n"

    def write_study(self, config=None, state=None, curriculum=None):
        metadata = self.root / ".ai-tutor"
        (metadata / "study-config.json").write_text(
            json.dumps(self.config if config is None else config), encoding="utf-8"
        )
        (metadata / "state.json").write_text(
            json.dumps(self.state if state is None else state), encoding="utf-8"
        )
        (self.root / "curriculum.md").write_text(
            self.curriculum if curriculum is None else curriculum, encoding="utf-8"
        )

    def run_validation(self, config=None, state=None, curriculum=None):
        self.write_study(config=config, state=state, curriculum=curriculum)
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.root)],
            capture_output=True,
            text=True,
            cwd=self.root,
        )

    def assert_rejected(self, result, diagnostic):
        self.assertEqual(result.returncode, 1, result.stderr + result.stdout)
        self.assertIn(diagnostic, result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_valid_partition_passes(self):
        result = self.run_validation()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("CURRICULUM VALIDATION: PASS", result.stdout)

    def test_unclassified_new_topic_is_rejected(self):
        state = copy.deepcopy(self.state)
        state["topics"].append({"topic_id": "topic_new"})
        self.assert_rejected(self.run_validation(state=state), "sem classificação: topic_new")

    def test_classified_topic_missing_from_state_is_rejected(self):
        config = copy.deepcopy(self.config)
        config["curriculum_tracks"]["core_topic_ids"].append("topic_unknown")
        self.assert_rejected(self.run_validation(config=config), "ausente do estado: topic_unknown")

    def test_topic_in_two_tracks_is_rejected(self):
        config = copy.deepcopy(self.config)
        config["curriculum_tracks"]["retired_topic_ids"].append("topic_core")
        self.assert_rejected(self.run_validation(config=config), "mais de uma trilha: topic_core")

    def test_duplicate_within_track_is_rejected(self):
        config = copy.deepcopy(self.config)
        config["curriculum_tracks"]["core_topic_ids"].append("topic_core")
        self.assert_rejected(self.run_validation(config=config), "repetido em core_topic_ids: topic_core")

    def test_duplicate_state_id_is_rejected(self):
        state = copy.deepcopy(self.state)
        state["topics"].append({"topic_id": "topic_core"})
        self.assert_rejected(self.run_validation(state=state), "repetido no estado: topic_core")

    def test_missing_tracks_are_rejected(self):
        self.assert_rejected(self.run_validation(config={}), "curriculum_tracks")

    def test_track_must_be_a_list(self):
        config = copy.deepcopy(self.config)
        config["curriculum_tracks"]["core_topic_ids"] = "topic_core"
        self.assert_rejected(self.run_validation(config=config), "core_topic_ids deve ser uma lista")

    def test_invalid_id_is_rejected(self):
        config = copy.deepcopy(self.config)
        config["curriculum_tracks"]["optional_topic_ids"] = [None]
        self.assert_rejected(self.run_validation(config=config), "ID inválido")

    def test_empty_core_is_rejected(self):
        config = copy.deepcopy(self.config)
        config["curriculum_tracks"]["core_topic_ids"] = []
        self.assert_rejected(self.run_validation(config=config), "core_topic_ids não pode ser vazia")

    def test_historical_topic_in_required_checklist_is_rejected(self):
        curriculum = self.curriculum + "- [ ] `topic_retired`: fora do núcleo\n"
        self.assert_rejected(self.run_validation(curriculum=curriculum), "checklist obrigatório")

    def test_missing_core_topic_in_checklist_is_rejected(self):
        self.assert_rejected(self.run_validation(curriculum="# Currículo\n"), "checklist obrigatório")

    def test_completed_checkbox_still_belongs_to_core(self):
        result = self.run_validation(curriculum="- [x] `topic_core`: competência obrigatória\n")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_historical_migration_is_not_a_live_source(self):
        migrations = self.root / ".ai-tutor/migrations"
        migrations.mkdir()
        (migrations / "old.json").write_text(
            json.dumps({"curriculum_tracks": {"core_topic_ids": ["topic_retired"]}}),
            encoding="utf-8",
        )
        result = self.run_validation()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_default_repository_root_is_independent_of_cwd(self):
        self.write_study()
        scripts = self.root / "scripts"
        scripts.mkdir()
        copied_validator = scripts / VALIDATOR.name
        shutil.copyfile(VALIDATOR, copied_validator)
        unrelated_cwd = self.root / "unrelated"
        unrelated_cwd.mkdir()
        result = subprocess.run(
            [sys.executable, str(copied_validator)],
            cwd=unrelated_cwd,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_missing_files_produce_actionable_error(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.root)],
            capture_output=True,
            text=True,
        )
        self.assert_rejected(result, "não foi possível ler")

    def test_invalid_json_produces_actionable_error(self):
        self.run_validation()
        (self.root / ".ai-tutor/study-config.json").write_text("{", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.root)],
            capture_output=True,
            text=True,
        )
        self.assert_rejected(result, "JSON inválido")


if __name__ == "__main__":
    unittest.main()
