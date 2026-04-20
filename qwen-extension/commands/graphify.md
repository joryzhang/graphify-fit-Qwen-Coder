---
description: Run the full graphify pipeline on the current project or a specified path
---

Run the installed graphify CLI on target path `{{args}}` using the new full pipeline entrypoint.

Rules:
- If `{{args}}` is empty, use `.`.
- Prefer direct execution of `graphify run {{args}}` or `python3 -m graphify run {{args}}`.
- Do not substitute `graphify update` for the main `/graphify` command.
- Build or refresh `graphify-out/GRAPH_REPORT.md`, `graphify-out/graph.json`, and `graphify-out/graph.html` when possible.
- If HTML visualization is skipped because the graph is too large, still treat the command as successful as long as `GRAPH_REPORT.md` and `graph.json` are produced.
- After execution, use graphify outputs as the primary source for architecture understanding.
