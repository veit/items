"""Testing the api count function"""

import pytest


def test_count_no_items(items_db):
    """In an empty database, the result should be 0."""
    assert items_db.count() == 0


@pytest.mark.num_items(1)
def test_count_one_item(items_db):
    """In a database with one item, the result should be 1."""
    assert items_db.count() == 1


@pytest.mark.num_items(3)
def test_count_three_items(items_db):
    """In a database with three items, the result should be 3."""
    assert items_db.count() == 3
