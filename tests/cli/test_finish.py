"""Test the cli finish function."""
import items


def test_finish(items_db, items_cli):
    """After an item has been created and ``finish`` has been called for this
    item, the status should be "done"."""
    i = items_db.add_item(items.Item("Update pytest section"))
    items_cli(f"finish {i}")
    after = items_db.get_item(i)
    assert after.state == "done"
