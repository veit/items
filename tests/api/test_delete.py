"""Testing the api delete function."""

import pytest

from items import InvalidItemId, Item


@pytest.fixture()
def three_items(items_db):
    """Create three items."""
    item1 = items_db.add_item(Item("Update pytest section"))
    item2 = items_db.add_item(Item("Update cibuildwheel section"))
    item3 = items_db.add_item(Item("Update mock tests"))
    return (item1, item2, item3)


def test_delete_from_many(items_db, three_items):
    """Testing the deletion of one item among several.

    After item2 is deleted, the number should have been reduced from three to
    two. In addition, item1 and item3 should still be present.
    """
    (item1, item2, item3) = three_items
    id_to_delete = item2
    ids_still_there = (item1, item3)

    items_db.delete_item(id_to_delete)

    assert items_db.count() == 2
    # item should not be retrievable after deletion
    with pytest.raises(InvalidItemId):
        items_db.get_item(id_to_delete)
    # non-deleted items should still be retrievable
    for i in ids_still_there:
        # just making sure this doesn't throw an exception
        items_db.get_item(i)


def test_delete_last_item(items_db):
    """Test the deletion of the last added item to an empty database.

    The number of items should then be 0. In addition, get_item should throw
    an InvalidItemId exception.
    """
    i = items_db.add_item(Item("Update pytest section"))
    items_db.delete_item(i)
    assert items_db.count() == 0
    with pytest.raises(InvalidItemId):
        items_db.get_item(i)


def test_delete_non_existent(items_db):
    """Deleting a non-existent item should throw the InvalidItemId exception."""
    i = 42  # any number will do, db is empty
    with pytest.raises(InvalidItemId):
        items_db.delete_item(i)
