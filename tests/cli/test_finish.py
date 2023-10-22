import items


def test_finish(items_db, items_cli):
    i = items_db.add_item(items.Item("Update pytest section"))
    items_cli(f"finish {i}")
    after = items_db.get_item(i)
    assert after.state == "done"
