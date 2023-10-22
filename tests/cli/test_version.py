import items


def test_version(items_cli):
    assert items_cli("version") == items.__version__
