# Graphify for Qwen Code

This extension adds graphify-oriented commands, skills, and agents to Qwen Code.

Behavioral guidance:
- Prefer graph outputs such as `graphify-out/GRAPH_REPORT.md`, `graphify-out/wiki/`, and `graphify-out/graph.json` before broad raw-file searching.
- When the user asks architecture, dependency, or codebase-structure questions, recommend or use graphify context first.
- After code changes, suggest `graphify update .` when appropriate.
- For focused architecture follow-up, prefer `graphify query`, `graphify path`, and `graphify explain`.
