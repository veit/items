import items


def test_version(capsys):
    items.cli.version()
    output = capsys.readouterr().out.rstrip()
    assert output == items.__version__
