import pytest

from items import Item


def assert_ident(i1: Item, i2: Item):
    __tracebackhide__ = True
    assert i1 == i2
    if i1.id != i2.id:
        pytest.fail(f"The IDs do not match: {i1.id} != {i2.id}")


def test_ident():
    i1 = Item("something to do", id=42)
    i2 = Item("something to do", id=42)
    assert_ident(i1, i2)


def test_ident_fail():
    i1 = Item("something to do", id=42)
    i2 = Item("something to do", id=43)
    assert_ident(i1, i2)
