from __future__ import annotations

import json
import re
from pathlib import Path


QWEN_MD_MARKER = "## graphify"
QWEN_MD_SECTION = """\
## graphify

This project has a graphify knowledge graph at `graphify-out/`.

Rules:
- Before answering architecture, dependency, or codebase-structure questions, read `graphify-out/GRAPH_REPORT.md` if it exists
- If `graphify-out/wiki/index.md` exists, navigate it before reading many raw files
- If graphify MCP tools are available, prefer `query_graph`, `get_node`, `get_neighbors`, `get_community`, and `shortest_path` over broad raw-file search
- Before large-scale use of `glob`, `grep_search`, or `read_file`, check whether graphify outputs already answer the question
- After modifying code files in this session, run `graphify update .` when appropriate to keep the graph current
- After changing docs, papers, images, audio, or video inputs that affect semantic extraction, rerun `/graphify . --update` or rebuild the graph
- If no graph exists yet and the user is asking for repository understanding, suggest running graphify first
"""

QWEN_HOOK = {
    "matcher": "^(read_file|glob|grep_search|list_directory)$",
    "hooks": [
        {
            "type": "command",
            "name": "graphify-context-reminder",
            "description": "Remind Qwen Code to use graphify outputs before broad file search",
            "command": (
                "[ -f graphify-out/graph.json ] && "
                r'''echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"allow","permissionDecisionReason":"Graphify context reminder","additionalContext":"graphify: Knowledge graph exists. Read graphify-out/GRAPH_REPORT.md first. If graphify MCP is configured, prefer graph queries over broad raw-file search."}}' '''
                "|| true"
            ),
            "timeout": 5000,
        }
    ],
}

QWEN_MCP_SERVER = {
    "command": "python3",
    "args": ["-m", "graphify.serve", "graphify-out/graph.json"],
    "timeout": 30000,
    "trust": False,
    "includeTools": [
        "query_graph",
        "get_node",
        "get_neighbors",
        "get_community",
        "god_nodes",
        "graph_stats",
        "shortest_path",
    ],
}


def install_qwen_skill(project_dir: Path, package_dir: Path) -> None:
    skill_src = package_dir / "skill-qwen.md"
    skill_dst = project_dir / ".qwen" / "skills" / "graphify" / "SKILL.md"
    skill_dst.parent.mkdir(parents=True, exist_ok=True)
    skill_dst.write_text(skill_src.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"  {skill_dst.relative_to(project_dir)}  ->  project skill installed")


def uninstall_qwen_skill(project_dir: Path) -> None:
    skill_dst = project_dir / ".qwen" / "skills" / "graphify" / "SKILL.md"
    if skill_dst.exists():
        skill_dst.unlink()
        print(f"  {skill_dst.relative_to(project_dir)}  ->  removed")
    for d in (skill_dst.parent, skill_dst.parent.parent):
        try:
            d.rmdir()
        except OSError:
            break


def install_qwen_hook(project_dir: Path) -> None:
    settings_path = project_dir / ".qwen" / "settings.json"
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8")) if settings_path.exists() else {}
    except json.JSONDecodeError:
        settings = {}
    pre_tool = settings.setdefault("hooks", {}).setdefault("PreToolUse", [])
    settings["hooks"]["PreToolUse"] = [
        h for h in pre_tool
        if not (h.get("matcher") == QWEN_HOOK["matcher"] and any(hook.get("name") == "graphify-context-reminder" for hook in h.get("hooks", [])))
    ]
    settings["hooks"]["PreToolUse"].append(QWEN_HOOK)
    settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
    print("  .qwen/settings.json  ->  PreToolUse hook registered")


def uninstall_qwen_hook(project_dir: Path) -> None:
    settings_path = project_dir / ".qwen" / "settings.json"
    if not settings_path.exists():
        return
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    pre_tool = settings.get("hooks", {}).get("PreToolUse", [])
    filtered = [
        h for h in pre_tool
        if not (h.get("matcher") == QWEN_HOOK["matcher"] and any(hook.get("name") == "graphify-context-reminder" for hook in h.get("hooks", [])))
    ]
    if len(filtered) != len(pre_tool):
        settings["hooks"]["PreToolUse"] = filtered
        settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
        print("  .qwen/settings.json  ->  PreToolUse hook removed")


def install_qwen_mcp(project_dir: Path) -> None:
    settings_path = project_dir / ".qwen" / "settings.json"
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8")) if settings_path.exists() else {}
    except json.JSONDecodeError:
        settings = {}
    settings.setdefault("mcpServers", {})["graphify"] = dict(QWEN_MCP_SERVER)
    settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
    print("  .qwen/settings.json  ->  graphify MCP server configured")


def uninstall_qwen_mcp(project_dir: Path) -> None:
    settings_path = project_dir / ".qwen" / "settings.json"
    if not settings_path.exists():
        return
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    servers = settings.get("mcpServers", {})
    if "graphify" in servers:
        servers.pop("graphify")
        settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
        print("  .qwen/settings.json  ->  graphify MCP server removed")


def qwen_install(project_dir: Path, package_dir: Path) -> None:
    install_qwen_skill(project_dir, package_dir)

    target = project_dir / "QWEN.md"
    if target.exists():
        content = target.read_text(encoding="utf-8")
        if QWEN_MD_MARKER in content:
            print("graphify already configured in QWEN.md")
        else:
            target.write_text(content.rstrip() + "\n\n" + QWEN_MD_SECTION, encoding="utf-8")
            print(f"graphify section written to {target.resolve()}")
    else:
        target.write_text(QWEN_MD_SECTION, encoding="utf-8")
        print(f"graphify section written to {target.resolve()}")

    install_qwen_hook(project_dir)
    install_qwen_mcp(project_dir)

    print()
    print("Qwen Code will now check the knowledge graph before broad file search.")
    print("Use /skills graphify or ask Qwen Code to build/update the graph.")


def qwen_uninstall(project_dir: Path) -> None:
    uninstall_qwen_skill(project_dir)

    target = project_dir / "QWEN.md"
    if target.exists():
        content = target.read_text(encoding="utf-8")
        if QWEN_MD_MARKER in content:
            cleaned = re.sub(r"\n*## graphify\n.*?(?=\n## |\Z)", "", content, flags=re.DOTALL).rstrip()
            if cleaned:
                target.write_text(cleaned + "\n", encoding="utf-8")
                print(f"graphify section removed from {target.resolve()}")
            else:
                target.unlink()
                print(f"QWEN.md was empty after removal - deleted {target.resolve()}")
        else:
            print("graphify section not found in QWEN.md - nothing to do")
    else:
        print("No QWEN.md found in current directory - nothing to do")

    uninstall_qwen_hook(project_dir)
    uninstall_qwen_mcp(project_dir)
