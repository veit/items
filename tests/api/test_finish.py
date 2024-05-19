"""
Test Cases
* finish from "todo", "in progressi, and "done" states
* finish an invalid id
"""

import pytest

from items import InvalidItemId, Item


@pytest.mark.parametrize("start_state", ("todo", "in progress", "done"))
def test_finish(items_db, start_state):
    """
    End state should be "done"
    """
    c = Item("Update pytest section", state=start_state)
    i = items_db.add_item(c)
    items_db.finish(i)
    c = items_db.get_item(i)
    assert c.state == "done"


def test_finish_non_existent(items_db):
    """
    Shouldn’t be able to start a non-existent item.
    """
    i = 42  # any number will do, db is empty
    with pytest.raises(InvalidItemId):
        items_db.finish(i)
