from typer.testing import CliRunner

import items


def run_items_cli(*params):
    runner = CliRunner()
    result = runner.invoke(items.app, params)
    return result.output.rstrip()


def test_get_path(monkeypatch, tmp_path):
    def fake_get_path():
        return tmp_path

    monkeypatch.setattr(items.cli, "get_path", fake_get_path)
    assert run_items_cli("config") == str(tmp_path)


def test_home(monkeypatch, tmp_path):
    items_dir = tmp_path / "items_db"

    def fake_home():
        return tmp_path

    monkeypatch.setattr(items.cli.pathlib.Path, "home", fake_home)
    assert run_items_cli("config") == str(items_dir)


def test_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv("ITEMS_DB_DIR", str(tmp_path))
    assert run_items_cli("config") == str(tmp_path)
