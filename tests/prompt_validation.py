"""
Prompt validation utilities.
Checks that all agent prompt files conform to structural requirements
and that schemas are valid JSON.
"""

import json
import os
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
AGENTS_DIR = REPO_ROOT / "agents"
SCHEMAS_DIR = REPO_ROOT / "schemas"
PROMPT_LIBRARY_DIR = REPO_ROOT / "prompt-library"

REQUIRED_AGENT_FILES = [
    "system_prompt.md",
    "user_template.md",
    "config.yaml",
    "examples/input.json",
    "examples/output.md",
]

REQUIRED_SYSTEM_PROMPT_SECTIONS = ["Role:", "Objective:", "Rules:", "Output format:"]
REQUIRED_USER_TEMPLATE_PLACEHOLDERS = ["{{task}}"]
REQUIRED_OUTPUT_SCHEMA_KEYS = ["topic", "summary", "examples", "patterns", "confidence"]
REQUIRED_TASK_SCHEMA_KEYS = ["task_id", "agent", "task", "status"]


def get_agent_dirs():
    """Return a list of all agent subdirectories."""
    if not AGENTS_DIR.exists():
        return []
    return [d for d in AGENTS_DIR.iterdir() if d.is_dir()]


class TestAllAgentsHaveRequiredFiles(unittest.TestCase):
    """Every agent directory must contain all required files."""

    def test_agents_directory_exists(self):
        self.assertTrue(AGENTS_DIR.exists(), "agents/ directory must exist")

    def test_at_least_one_agent(self):
        agents = get_agent_dirs()
        self.assertGreater(len(agents), 0, "At least one agent directory must exist")

    def test_each_agent_has_required_files(self):
        for agent_dir in get_agent_dirs():
            for filename in REQUIRED_AGENT_FILES:
                filepath = agent_dir / filename
                with self.subTest(agent=agent_dir.name, file=filename):
                    self.assertTrue(
                        filepath.exists(),
                        f"{agent_dir.name}/{filename} is missing",
                    )


class TestSystemPromptStructure(unittest.TestCase):
    """Every system_prompt.md must contain required structural sections."""

    def test_system_prompts_have_required_sections(self):
        for agent_dir in get_agent_dirs():
            prompt_file = agent_dir / "system_prompt.md"
            if not prompt_file.exists():
                continue
            content = prompt_file.read_text()
            for section in REQUIRED_SYSTEM_PROMPT_SECTIONS:
                with self.subTest(agent=agent_dir.name, section=section):
                    self.assertIn(
                        section,
                        content,
                        f"{agent_dir.name}/system_prompt.md missing section: {section}",
                    )


class TestUserTemplateStructure(unittest.TestCase):
    """Every user_template.md must contain the {{task}} placeholder."""

    def test_user_templates_have_task_placeholder(self):
        for agent_dir in get_agent_dirs():
            template_file = agent_dir / "user_template.md"
            if not template_file.exists():
                continue
            content = template_file.read_text()
            for placeholder in REQUIRED_USER_TEMPLATE_PLACEHOLDERS:
                with self.subTest(agent=agent_dir.name, placeholder=placeholder):
                    self.assertIn(
                        placeholder,
                        content,
                        f"{agent_dir.name}/user_template.md missing placeholder: {placeholder}",
                    )


class TestExampleInputsAreValidJson(unittest.TestCase):
    """Every examples/input.json must be valid JSON with a 'task' field."""

    def test_example_inputs_are_valid_json(self):
        for agent_dir in get_agent_dirs():
            input_file = agent_dir / "examples" / "input.json"
            if not input_file.exists():
                continue
            with self.subTest(agent=agent_dir.name):
                try:
                    data = json.loads(input_file.read_text())
                except json.JSONDecodeError as e:
                    self.fail(
                        f"{agent_dir.name}/examples/input.json is not valid JSON: {e}"
                    )
                self.assertIn(
                    "task",
                    data,
                    f"{agent_dir.name}/examples/input.json must have a 'task' field",
                )


class TestSchemasAreValidJson(unittest.TestCase):
    """All schema files must be valid JSON and contain required keys."""

    def test_output_schema_is_valid(self):
        schema_file = SCHEMAS_DIR / "output_schema.json"
        self.assertTrue(schema_file.exists(), "schemas/output_schema.json must exist")
        data = json.loads(schema_file.read_text())
        for key in REQUIRED_OUTPUT_SCHEMA_KEYS:
            with self.subTest(key=key):
                self.assertIn(key, data, f"output_schema.json missing key: {key}")

    def test_task_schema_is_valid(self):
        schema_file = SCHEMAS_DIR / "task_schema.json"
        self.assertTrue(schema_file.exists(), "schemas/task_schema.json must exist")
        data = json.loads(schema_file.read_text())
        for key in REQUIRED_TASK_SCHEMA_KEYS:
            with self.subTest(key=key):
                self.assertIn(key, data, f"task_schema.json missing key: {key}")


class TestPromptLibraryStructure(unittest.TestCase):
    """Prompt library must contain frameworks/ and tools/ directories with content."""

    def test_frameworks_directory_exists(self):
        self.assertTrue(
            (PROMPT_LIBRARY_DIR / "frameworks").exists(),
            "prompt-library/frameworks/ must exist",
        )

    def test_tools_directory_exists(self):
        self.assertTrue(
            (PROMPT_LIBRARY_DIR / "tools").exists(),
            "prompt-library/tools/ must exist",
        )

    def test_frameworks_not_empty(self):
        frameworks_dir = PROMPT_LIBRARY_DIR / "frameworks"
        if frameworks_dir.exists():
            files = list(frameworks_dir.glob("*.md"))
            self.assertGreater(len(files), 0, "frameworks/ must contain at least one .md file")

    def test_tools_not_empty(self):
        tools_dir = PROMPT_LIBRARY_DIR / "tools"
        if tools_dir.exists():
            files = list(tools_dir.glob("*.md"))
            self.assertGreater(len(files), 0, "tools/ must contain at least one .md file")

    def test_research_template_has_required_placeholders(self):
        template_file = PROMPT_LIBRARY_DIR / "frameworks" / "research-template.md"
        if template_file.exists():
            content = template_file.read_text()
            self.assertIn("{{topic}}", content, "research-template.md must contain {{topic}} placeholder")


if __name__ == "__main__":
    unittest.main()
