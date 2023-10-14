import pytest
from packaging.version import parse

import items
from items import Item


@pytest.mark.skipif(
    parse(items.__version__).minor < 2,
    reason="The comparison with < is not yet supported in version 0.1.x.",
)
def test_less_than():
    i1 = Item("Update pytest section")
    i2 = Item("Update cibuildwheel section")
    assert i1 < i2


@pytest.mark.skip(reason="Items do not yet allow a < comparison")
def test_less_than():
    i1 = Item("Update pytest section")
    i2 = Item("Update cibuildwheel section")
    assert i1 < i2


def test_equality():
    i1 = Item("Update pytest section")
    i2 = Item("Update pytest section")
    assert i1 == i2
