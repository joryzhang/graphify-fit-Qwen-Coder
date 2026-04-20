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
