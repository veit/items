import pytest


@pytest.mark.num_items
def test_zero_item(items_db):
    assert items_db.count() == 0


@pytest.mark.num_items(4)
def test_four_items(items_db):
    assert items_db.count() == 4
    print()
    for i in items_db.list_items():
        print(i)


@pytest.mark.num_items(13)
def test_thirteen_items(items_db):
    assert items_db.count() == 13
