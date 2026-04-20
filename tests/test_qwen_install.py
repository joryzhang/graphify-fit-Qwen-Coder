"""Tests for graphify qwen install / uninstall commands."""
import json
from pathlib import Path

from graphify.platform_qwen import (
    QWEN_HOOK,
    QWEN_MD_MARKER,
    qwen_install,
    qwen_uninstall,
)


def _package_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "graphify"


def test_qwen_install_writes_qwen_md(tmp_path):
    qwen_install(tmp_path, _package_dir())
    target = tmp_path / "QWEN.md"
    assert target.exists()
    assert QWEN_MD_MARKER in target.read_text()
    assert "GRAPH_REPORT.md" in target.read_text()


def test_qwen_install_appends_to_existing_qwen_md(tmp_path):
    target = tmp_path / "QWEN.md"
    target.write_text("# Existing project context\n")
    qwen_install(tmp_path, _package_dir())
    content = target.read_text()
    assert "Existing project context" in content
    assert QWEN_MD_MARKER in content


def test_qwen_install_idempotent(tmp_path):
    qwen_install(tmp_path, _package_dir())
    qwen_install(tmp_path, _package_dir())
    target = tmp_path / "QWEN.md"
    assert target.read_text().count(QWEN_MD_MARKER) == 1


def test_qwen_install_writes_project_skill(tmp_path):
    qwen_install(tmp_path, _package_dir())
    skill = tmp_path / ".qwen" / "skills" / "graphify" / "SKILL.md"
    assert skill.exists()
    assert "Qwen Code" in skill.read_text()


def test_qwen_install_writes_hook_and_mcp(tmp_path):
    qwen_install(tmp_path, _package_dir())
    settings = json.loads((tmp_path / ".qwen" / "settings.json").read_text())
    hooks = settings["hooks"]["PreToolUse"]
    assert any(h.get("matcher") == QWEN_HOOK["matcher"] for h in hooks)
    assert "graphify" in settings.get("mcpServers", {})


def test_qwen_uninstall_removes_qwen_section(tmp_path):
    qwen_install(tmp_path, _package_dir())
    qwen_uninstall(tmp_path)
    target = tmp_path / "QWEN.md"
    assert not target.exists()


def test_qwen_uninstall_preserves_existing_content(tmp_path):
    target = tmp_path / "QWEN.md"
    target.write_text("# Existing context\n")
    qwen_install(tmp_path, _package_dir())
    qwen_uninstall(tmp_path)
    assert target.exists()
    content = target.read_text()
    assert "Existing context" in content
    assert QWEN_MD_MARKER not in content


def test_qwen_uninstall_removes_skill_hook_and_mcp(tmp_path):
    qwen_install(tmp_path, _package_dir())
    qwen_uninstall(tmp_path)
    skill = tmp_path / ".qwen" / "skills" / "graphify" / "SKILL.md"
    assert not skill.exists()
    settings_path = tmp_path / ".qwen" / "settings.json"
    if settings_path.exists():
        settings = json.loads(settings_path.read_text())
        hooks = settings.get("hooks", {}).get("PreToolUse", [])
        assert not any(h.get("matcher") == QWEN_HOOK["matcher"] for h in hooks)
        assert "graphify" not in settings.get("mcpServers", {})

