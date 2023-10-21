from typer.testing import CliRunner
import items
import pytest
import shlex

runner = CliRunner()

@pytest.fixture()
def items_cli_no_redirect():
    def run_cli(command_string):
        command_list = shlex.split(command_string)
        result = runner.invoke(items.cli.app, command_list)
        output = result.stdout.rstrip()
        return output
    return run_cli

@pytest.fixture()
def items_cli(items_cli_no_redirect, db_path, monkeypatch, items_db):
    monkeypatch.setenv("ITEMS_DB_DIR", db_path.as_posix())
    return items_cli_no_redirect
