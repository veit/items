"""
Test Cases
* `add` to an empty database, with summary
* `add` to a non-empty database, with summary
* `add` a item with both summary and owner set
* `add` a duplicate item
"""
import pytest

from items import Item


def test_add_from_empty(items_db):
    """
    count should be 1 and item retrievable
    """
    c = Item(summary="do something")
    i = items_db.add_item(c)
    assert items_db.count() == 1
    assert items_db.get_item(i) == c


@pytest.mark.num_items(3)
def test_add_from_nonempty(items_db):
    """
    count should increase by 1 and item retrievable
    """
    c = Item(summary="do something")
    i = items_db.add_item(c)
    assert items_db.count() == 4
    assert items_db.get_item(i) == c


def test_add_with_summary_and_owner(items_db):
    """
    count should be 1 and item retrievable
    """
    c = Item(summary="do something", owner="Brian")
    i = items_db.add_item(c)
    assert items_db.count() == 1
    assert items_db.get_item(i) == c


def test_add_duplicate(items_db):
    """
    Duplicates allowed, both retrievable, separate indices
    """
    c = Item(summary="do something")
    i_1 = items_db.add_item(c)
    i_2 = items_db.add_item(c)
    c1 = items_db.get_item(i_1)
    c2 = items_db.get_item(i_2)
    assert i_1 != i_2
    assert c1 == c2 == c
