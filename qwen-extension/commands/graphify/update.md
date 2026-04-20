---
description: Refresh graphify outputs for the current project or a specified path
---

Refresh graphify outputs for the target path `{{args}}`.

Rules:
- If `{{args}}` is empty, use `.`.
- Prefer direct execution of `graphify update {{args}}` or `python3 -m graphify update {{args}}`.
- Use this command for incremental refreshes after changes, not as a substitute for the main `/graphify` pipeline entrypoint.
- After update, summarize whether graph outputs are current.
