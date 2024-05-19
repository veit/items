"""Test the cli version function."""

import items


def test_version(items_cli):
    """The ``version`` cli option should output the same as ``__version__`` in
    Python."""
    assert items_cli("version") == items.__version__
