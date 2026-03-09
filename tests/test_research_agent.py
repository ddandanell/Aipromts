"""
Tests for the research agent configuration and examples.
Validates that agent files exist, are well-formed, and that
example outputs conform to the expected output schema.
"""

import json
import os
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
AGENT_DIR = REPO_ROOT / "agents" / "research-agent"
SCHEMA_PATH = REPO_ROOT / "schemas" / "output_schema.json"


class TestResearchAgentFiles(unittest.TestCase):
    """Ensure all required research-agent files are present."""

    def test_system_prompt_exists(self):
        self.assertTrue((AGENT_DIR / "system_prompt.md").exists())

    def test_user_template_exists(self):
        self.assertTrue((AGENT_DIR / "user_template.md").exists())

    def test_config_exists(self):
        self.assertTrue((AGENT_DIR / "config.yaml").exists())

    def test_example_input_exists(self):
        self.assertTrue((AGENT_DIR / "examples" / "input.json").exists())

    def test_example_output_exists(self):
        self.assertTrue((AGENT_DIR / "examples" / "output.md").exists())


class TestResearchAgentConfig(unittest.TestCase):
    """Validate that config.yaml contains required fields."""

    def setUp(self):
        import yaml
        with open(AGENT_DIR / "config.yaml") as f:
            self.config = yaml.safe_load(f)

    def test_model_field_present(self):
        self.assertIn("model", self.config)

    def test_temperature_in_range(self):
        temp = self.config.get("temperature", -1)
        self.assertGreaterEqual(temp, 0.0)
        self.assertLessEqual(temp, 2.0)

    def test_max_tokens_positive(self):
        self.assertGreater(self.config.get("max_tokens", 0), 0)

    def test_tools_is_list(self):
        self.assertIsInstance(self.config.get("tools", []), list)


class TestResearchAgentExampleInput(unittest.TestCase):
    """Validate example input.json against task_schema required fields."""

    def setUp(self):
        with open(AGENT_DIR / "examples" / "input.json") as f:
            self.input_data = json.load(f)

    def test_input_is_dict(self):
        self.assertIsInstance(self.input_data, dict)

    def test_input_has_task_field(self):
        self.assertIn("task", self.input_data)

    def test_task_is_non_empty_string(self):
        self.assertIsInstance(self.input_data["task"], str)
        self.assertGreater(len(self.input_data["task"]), 0)


class TestResearchAgentOutputSchema(unittest.TestCase):
    """Validate output_schema.json has the required keys for agent chaining."""

    REQUIRED_KEYS = {"topic", "summary", "examples", "patterns", "confidence", "sources"}

    def setUp(self):
        with open(SCHEMA_PATH) as f:
            self.schema = json.load(f)

    def test_schema_has_required_keys(self):
        for key in self.REQUIRED_KEYS:
            with self.subTest(key=key):
                self.assertIn(key, self.schema)

    def test_examples_is_list(self):
        self.assertIsInstance(self.schema["examples"], list)

    def test_patterns_is_list(self):
        self.assertIsInstance(self.schema["patterns"], list)

    def test_confidence_is_numeric(self):
        self.assertIsInstance(self.schema["confidence"], (int, float))


class TestResearchAgentUserTemplate(unittest.TestCase):
    """Validate that user_template.md contains required placeholders."""

    REQUIRED_PLACEHOLDERS = ["{{task}}", "{{context}}", "{{rules}}"]

    def setUp(self):
        with open(AGENT_DIR / "user_template.md") as f:
            self.template = f.read()

    def test_required_placeholders_present(self):
        for placeholder in self.REQUIRED_PLACEHOLDERS:
            with self.subTest(placeholder=placeholder):
                self.assertIn(placeholder, self.template)


class TestResearchAgentSystemPrompt(unittest.TestCase):
    """Validate that system_prompt.md contains required sections."""

    REQUIRED_SECTIONS = ["Role:", "Objective:", "Rules:", "Output format:"]

    def setUp(self):
        with open(AGENT_DIR / "system_prompt.md") as f:
            self.prompt = f.read()

    def test_required_sections_present(self):
        for section in self.REQUIRED_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, self.prompt)


if __name__ == "__main__":
    unittest.main()
