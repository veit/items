import items


def test_add(items_db, items_cli):
    items_cli("add some task")
    expected = items.Item("some task", owner="", state="todo")
    all = items_db.list_items()
    assert len(all) == 1
    assert all[0] == expected


def test_add_with_owner(items_db, items_cli):
    items_cli("add some task -o veit")
    expected = items.Item("some task", owner="veit", state="todo")
    all = items_db.list_items()
    assert len(all) == 1
    assert all[0] == expected
