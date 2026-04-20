# graphify-qwen-extension

A Qwen Code extension that brings graphify workflows into Qwen Code through custom commands and an optional extraction subagent.

> Status: preview / experimental.
> The current version is suitable for local use and early public testing, but should not yet be treated as a fully stable production extension.

## Features

- `/graphify` — run the full graphify pipeline through `graphify run`
- `/graphify:add` — fetch external content into the corpus
- `/graphify:update` — refresh graphify outputs after changes through `graphify update`
- `/graphify:query` — query the graph for focused architecture questions
- `/graphify:path` — find shortest paths between concepts
- `/graphify:explain` — explain a graph node and its connections
- `graphify-extractor` subagent for semantic extraction workflows

## Install from GitHub

```bash
qwen extensions install <owner>/graphify-qwen-extension
```

For local development:

```bash
qwen extensions link .
```

A minimal local verification flow:

```text
/graphify .
/graphify:update .
/graphify:query what connects auth to session storage?
/graphify:path A B
/graphify:explain SomeNode
```

## Expected prerequisites

- Qwen Code installed
- `graphifyy` available in your Python environment (`python3 -m pip install graphifyy`)
- The installed `graphify` CLI must support `graphify run <path>`
- For MCP-based follow-up workflows, you can additionally configure graphify's MCP server later

## Commands

### `/graphify`

Run the full graphify pipeline for the current project.

This command is intended to map to:

```bash
graphify run .
```

Example:

```text
/graphify .
```

### `/graphify:add`

Fetch a URL and add it to the corpus.

```text
/graphify:add https://arxiv.org/abs/1706.03762
```

### `/graphify:update`

Refresh graphify outputs after code or document changes.

This command is intended to map to:

```bash
graphify update .
```

```text
/graphify:update .
```

### `/graphify:query`

Query graphify outputs for focused questions.

```text
/graphify:query what connects auth to session storage?
```

### `/graphify:path`

Trace shortest path between two concepts.

```text
/graphify:path DigestAuth Response
```

### `/graphify:explain`

Explain a node and its immediate context.

```text
/graphify:explain SwinTransformer
```

## Notes

This first version focuses on extension-level commands, skill, context, and agent packaging. It does not yet auto-provision a workspace MCP server in `settings.json`; that can be added as a later enhancement.
