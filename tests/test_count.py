import items


def test_empty(items_db):
    assert items_db.count() == 0


def test_count(items_db):
    items_db.add_item(items.Item("something"))
    items_db.add_item(items.Item("something else"))
    assert items_db.count() == 2


def test_count2(items_db):
    items_db.add_item(items.Item("something different"))
    assert items_db.count() == 1


def populated(populated_db):
    assert populated_db.count() > 0
