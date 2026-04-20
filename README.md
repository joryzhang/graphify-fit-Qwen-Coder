[简体中文](README.zh-CN.md)
# graphify-fit-Qwen-Coder

This repository is a **Qwen Code-focused enhancement fork** of [graphify](https://github.com/safishamsi/graphify).

The goal of this fork is to make graphify work more naturally and more reliably with **Qwen Code**, both as a Python CLI tool and as a command-style Qwen Code extension.

## Why this fork exists

The upstream graphify project already supports many AI coding assistants. This fork focuses specifically on improving the **Qwen Code** experience, especially around the following capabilities:

- `graphify qwen install` / `graphify qwen uninstall`
- a dedicated full-pipeline CLI entrypoint: `graphify run <path>`
- a bundled repository-local Qwen Code extension prototype under [`qwen-extension/`](./qwen-extension)
- experiments around `/graphify`-style command workflows for Qwen Code

## What is included in this repository

### 1. graphify Python project changes
This fork adds Qwen-oriented enhancements directly to the graphify Python project, including:

- Qwen install / uninstall integration
- Qwen-related packaging and installation support
- the new `graphify run <path>` full pipeline entrypoint
- corresponding tests for the new behavior

### 2. `qwen-extension/` extension prototype
This repository also contains a Qwen Code extension prototype that provides:

- `/graphify`
- `/graphify:add`
- `/graphify:update`
- `/graphify:query`
- `/graphify:path`
- `/graphify:explain`

along with:

- `QWEN.md`
- extension command definitions
- an optional graphify extraction subagent

## How to use it with Qwen Code

### Option 1: Use the enhanced graphify CLI directly
After installing this fork, you can use:

```bash
graphify run .
graphify qwen install
```

### Option 2: Use the bundled Qwen extension prototype
Link the extension locally:

```bash
qwen extensions link ./qwen-extension
```

After restarting Qwen Code, try commands such as:

```text
/graphify .
/graphify:update .
/graphify:query what connects auth to session storage?
/graphify:path A B
/graphify:explain SomeNode
```

## Current status

> Preview / experimental  
> This repository is currently suitable for local use and early public testing, but should not yet be treated as a fully polished production-ready release.

## Scope of this fork

This fork is currently intended for:

- Qwen Code adaptation
- command-style integration experiments
- extension-driven workflows
- early public sharing and testing of graphify support for Qwen Code

## Upstream project

If you are looking for the original graphify project, please visit:

- https://github.com/safishamsi/graphify
