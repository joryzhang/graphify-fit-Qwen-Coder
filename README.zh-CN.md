# graphify-fit-Qwen-Coder

这是一个面向 **Qwen Code** 的 [graphify](https://github.com/safishamsi/graphify) 增强版 fork。

这个仓库的目标，是让 graphify 在 **Qwen Code** 中获得更自然、更稳定的使用体验，包括 Python CLI 侧的适配，以及 Qwen Code extension 形式的命令式集成。

## 为什么会有这个 fork

原始的 graphify 已经支持多种 AI coding assistant。这个 fork 主要专注于补强 **Qwen Code** 的使用体验，尤其是下面这些能力：

- `graphify qwen install` / `graphify qwen uninstall`
- 新增明确的完整 pipeline 命令入口：`graphify run <path>`
- 内置一个仓库级的 Qwen Code extension 原型：[`qwen-extension/`](./qwen-extension)
- 围绕 `/graphify` 风格命令的 Qwen 集成与实验

## 这个仓库包含什么

### 1. graphify Python 项目改动
这个 fork 在 graphify 本体中加入了与 Qwen 相关的增强：

- Qwen install / uninstall 集成
- Qwen 相关打包与安装支持
- 新的 `graphify run <path>` 全量入口
- 对应的测试覆盖

### 2. `qwen-extension/` 插件原型
仓库中还包含一个 Qwen Code extension 原型，提供：

- `/graphify`
- `/graphify:add`
- `/graphify:update`
- `/graphify:query`
- `/graphify:path`
- `/graphify:explain`

并带有：

- `QWEN.md`
- extension commands
- 可选的 graphify extraction subagent

## 如何在 Qwen Code 中使用

### 方式一：直接使用增强版 graphify CLI
安装这个 fork 后，可以直接使用：

```bash
graphify run .
graphify qwen install
```

### 方式二：使用仓库内置的 Qwen extension 原型
本地链接 extension：

```bash
qwen extensions link ./qwen-extension
```

重启 Qwen Code 后，可以尝试：

```text
/graphify .
/graphify:update .
/graphify:query what connects auth to session storage?
/graphify:path A B
/graphify:explain SomeNode
```

## 当前状态

> 预览版 / 实验性版本  
> 目前适合本地使用和早期公开测试，但还不应视为完全稳定、完全打磨完成的正式生产版本。

## 适用范围

这个 fork 当前主要面向：

- Qwen Code 适配
- 命令式集成实验
- extension 驱动工作流
- graphify 在 Qwen Code 中的早期公开分享与测试

## 上游项目

如果你想查看原始 graphify 项目，请访问：

- https://github.com/safishamsi/graphify
