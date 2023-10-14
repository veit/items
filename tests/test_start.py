import pytest

from items import InvalidItemId, Item


@pytest.mark.smoke
def test_start(items_db):
    """
    Change state from ‘todo’ to ‘in progress’
    """
    i = items_db.add_item(Item("Update pytest section", state="todo"))
    items_db.start(i)
    s = items_db.get_item(i)
    assert s.state == "in progress"


@pytest.mark.exception
def test_start_non_existent(items_db):
    """
    Shouldn’t start a non-existent item.
    """
    # any_number will be invalid, db is empty
    any_number = 44

    with pytest.raises(InvalidItemId):
        items_db.start(any_number)
