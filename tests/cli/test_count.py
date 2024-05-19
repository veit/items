"""Test the cli count function."""
import pytest


@pytest.mark.num_items(3)
def test_count(items_cli):
    """After three items have been written to the database with
    ``num_items(3)``, ``count`` should return "3"."""
    assert items_cli("count") == "3"
