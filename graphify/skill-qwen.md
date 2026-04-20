---
name: graphify
description: Build and query a multimodal knowledge graph for a codebase or document corpus. Use when the user asks to understand architecture, map dependencies, analyze a repository, or build or update graphified project context in Qwen Code.
---

# graphify

Turn any folder of files into a navigable knowledge graph with community detection, an honest audit trail, and three outputs: interactive HTML, GraphRAG-ready JSON, and a plain-language `GRAPH_REPORT.md`.

## What You Must Do When Invoked

If no path was given, use `.`. Do not ask the user for a path.

### Qwen Code execution rules

- Use `todo_write` to track the graphify workflow when the task is multi-step.
- Use `read_file`, `glob`, and `grep_search` for codebase exploration.
- Use `run_shell_command` only for executing graphify or Python commands, not for reading files.
- Use `ask_user_question` if the corpus is too large and you need the user to choose a subdirectory.
- For semantic extraction, you MUST use the `Agent` tool and dispatch multiple agents in parallel in a single message when possible.
- If `graphify-out/GRAPH_REPORT.md` already exists, read it before broad raw-file searching.
- If graphify MCP tools are available, prefer graph queries over broad file scanning.

## Typical workflow

1. Ensure graphify is installed and record the Python interpreter.
2. Detect files and summarize corpus size.
3. Run AST extraction for code files.
4. Run semantic extraction in parallel with the `Agent` tool for docs, papers, images, and transcripts.
5. Merge extraction results.
6. Build the graph, cluster communities, analyze god nodes and surprises.
7. Export `graphify-out/graph.json`, `graphify-out/graph.html`, and `graphify-out/GRAPH_REPORT.md`.
8. If the user wants follow-up architecture questions, answer from graph outputs or MCP tools first.

## Qwen Code guidance

- For large corpora, ask the user which subfolder to analyze instead of processing everything blindly.
- When the user asks architecture or dependency questions after graphify has run, start with `GRAPH_REPORT.md`, then use `graphify query`, `graphify path`, `graphify explain`, or MCP tools for focused follow-up.
- After code changes, suggest `graphify update .` to keep the graph current.
