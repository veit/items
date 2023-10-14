import pytest

from items.api import Item


def test_equality_fail():
    i1 = Item("do something", "veit")
    i2 = Item("do something else", "veit.schiele")
    if i1 != i2:
        pytest.fail("The items are not identical!")


if __name__ == "__main__":
    test_equality_fails()
