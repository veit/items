from typer.testing import CliRunner

import items


def test_version():
    runner = CliRunner()
    result = runner.invoke(items.app, ["version"])
    output = result.output.rstrip()
    assert output == items.__version__
