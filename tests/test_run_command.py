"""Tests for graphify run command helpers."""
import json
from pathlib import Path

from graphify.__main__ import run_pipeline


def test_run_pipeline_generates_core_outputs(tmp_path):
    fixture_src = Path(__file__).parent / "fixtures"
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (workspace / "sample.py").write_text((fixture_src / "sample.py").read_text(), encoding="utf-8")
    (workspace / "notes.md").write_text((fixture_src / "sample.md").read_text(), encoding="utf-8")

    run_pipeline(workspace, no_viz=True)

    out = workspace / "graphify-out"
    assert (out / "GRAPH_REPORT.md").exists()
    assert (out / "graph.json").exists()
    assert not (out / "graph.html").exists()

    data = json.loads((out / "graph.json").read_text())
    assert "nodes" in data
    assert "links" in data


def test_run_pipeline_writes_html_when_enabled(tmp_path):
    fixture_src = Path(__file__).parent / "fixtures"
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (workspace / "sample.py").write_text((fixture_src / "sample.py").read_text(), encoding="utf-8")

    run_pipeline(workspace, no_viz=False)

    out = workspace / "graphify-out"
    assert (out / "graph.html").exists()


def test_run_pipeline_no_supported_files(tmp_path, capsys):
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (workspace / "ignored.bin").write_bytes(b"abc")

    run_pipeline(workspace, no_viz=True)
    out = capsys.readouterr().out
    assert "No supported files found" in out
