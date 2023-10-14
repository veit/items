import pytest
from packaging.version import parse

import items
from items import Item


@pytest.mark.xfail(
    parse(items.__version__).minor < 2,
    reason="The comparison with < is not yet supported in version 0.1.x.",
)
def test_less_than():
    i1 = Item("Update pytest section")
    i2 = Item("Update cibuildwheel section")
    assert i1 < i2


@pytest.mark.xfail(reason="Feature #17: not implemented yet")
def test_xpass():
    i1 = Item("Update pytest section")
    i2 = Item("Update pytest section")
    assert i1 == i2


@pytest.mark.xfail(reason="Feature #17: not implemented yet", strict=True)
def test_xfail_strict():
    i1 = Item("Update pytest section")
    i2 = Item("Update pytest section")
    assert i1 == i2
