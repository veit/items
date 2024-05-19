"""The configuration file for all cli tests."""
import shlex

import pytest
from typer.testing import CliRunner

import items

runner = CliRunner()


@pytest.fixture()
def items_cli_no_redirect():
    """Fixture for calling the cli app with a list of parameters.

    Returns:
        function: Function for calling the cli app with the list of parameters.
    """

    def run_cli(command_string):
        """Pass the application `items.cli.app` and a list of strings to the
        :func:`invoke` function of the cli test runner.

        Returns:
            str: Table with the columns ID, state, owner and summary
        """
        command_list = shlex.split(command_string)
        result = runner.invoke(items.cli.app, command_list)
        output = result.stdout.rstrip()
        return output

    return run_cli


@pytest.fixture()
def items_cli(items_cli_no_redirect, db_path, monkeypatch, items_db):
    """Monkeypatch fixture for the ITEMS_DB_DIR environment variable."""
    monkeypatch.setenv("ITEMS_DB_DIR", db_path.as_posix())
    return items_cli_no_redirect
