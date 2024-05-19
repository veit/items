"""Test the cli function for invalid ids."""

import pytest


@pytest.mark.parametrize(
    "command",
    ["delete 42", "start 42", "finish 42", "update 42 -s foo -o veit"],
)
def test_invalid_item_id(items_db, command, items_cli):
    """If the item with id 42 is deleted, started, finished or updated, the
    error message "Error: Invalid item id 42" should be output."""
    out = items_cli(command)
    assert "Error: Invalid item id 42" in out
