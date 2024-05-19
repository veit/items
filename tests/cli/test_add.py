"""Test the cli add function."""
import items


def test_add(items_db, items_cli):
    """Two tests for adding an item.

    The first test checks whether the number of items is 1 after an item has
    been added; the second test checks whether the summary, owner and status of
    this item match.
    """
    items_cli("add some task")
    expected = items.Item("some task", owner="", state="todo")
    all = items_db.list_items()
    assert len(all) == 1
    assert all[0] == expected


def test_add_with_owner(items_db, items_cli):
    """The same tests as above, but an owner is also specified."""
    items_cli("add some task -o veit")
    expected = items.Item("some task", owner="veit", state="todo")
    all = items_db.list_items()
    assert len(all) == 1
    assert all[0] == expected
