import pytest


@pytest.mark.num_items(3)
def test_count(items_cli):
    assert items_cli("count") == "3"
