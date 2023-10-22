import items


def test_update(items_db, items_cli):
    i = items_db.add_item(items.Item("Update pytest section"))
    items_cli(f"update {i} -o veit -s foo")
    expected = items.Item("foo", owner="veit", state="todo")
    actual = items_db.get_item(i)
    assert actual == expected
