"""
Test Cases
* `update` the owner of a item
* `update` the summary of a item
* `update` owner and summary of a item at the same time
* `update` a non-existent item
"""

import pytest

from items import InvalidItemId, Item


def test_update_owner(items_db):
    """
    summary and state should stay the same
    owner should change
    """
    i = items_db.add_item(Item("Update pytest section", owner="veit"))
    items_db.update_item(i, Item(owner="vsc", state=None))

    mod = items_db.get_item(i)
    assert mod == Item("Update pytest section", owner="vsc")


def test_update_summary(items_db):
    """
    owner and state should stay the same
    summary should change
    """
    i = items_db.add_item(
        Item("Update pytest section", owner="veit", state="done")
    )
    items_db.update_item(
        i, Item(summary="Update cibuildwheel section", state=None)
    )

    mod = items_db.get_item(i)
    assert mod == Item(
        "Update cibuildwheel section", owner="veit", state="done"
    )


def test_update_both(items_db):
    """
    state should stay the same
    owner and summary should change
    """
    i = items_db.add_item(Item("Update pytest section", owner="veit"))
    items_db.update_item(
        i, Item(summary="Update cibuildwheel section", owner="vsc")
    )

    mod = items_db.get_item(i)
    assert mod == Item(
        "Update cibuildwheel section", owner="vsc", state="todo"
    )


def test_update_non_existent(items_db):
    """
    Shouldn't be able to update a non-existent item.
    """
    i = 123  # any number will do, db is empty
    with pytest.raises(InvalidItemId):
        items_db.update_item(
            i, Item(summary="Update cibuildwheel section", owner="vsc")
        )
