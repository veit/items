import items


def test_start(items_db, items_cli):
    i = items_db.add_item(items.Item("Update pytest section"))
    items_cli(f"start {i}")
    after = items_db.get_item(i)
    assert after.state == "in progress"
