"""
Test Cases
* count from an empty database
* count with one item
* count with more than one item
"""
import pytest


def test_count_no_items(items_db):
    assert items_db.count() == 0


@pytest.mark.num_items(1)
def test_count_one_item(items_db):
    assert items_db.count() == 1


@pytest.mark.num_items(3)
def test_count_three_items(items_db):
    assert items_db.count() == 3
