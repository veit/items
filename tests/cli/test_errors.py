import pytest


@pytest.mark.parametrize(
    "command", ["delete 42", "start 42", "finish 42", "update 42 -s foo -o veit"]
)
def test_invalid_item_id(items_db, command, items_cli):
    out = items_cli(command)
    assert "Error: Invalid item id 42" in out
