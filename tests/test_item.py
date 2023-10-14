from items.api import Item


def test_field_access():
    i = Item("something", "veit", "todo", 42)
    assert i.summary == "something to do"
    assert i.owner == "veit"
    assert i.state == "todo"
    assert i.id == 42


def test_defaults():
    i = Item()
    assert i.summary is None
    assert i.owner is None
    assert i.state == "todo"
    assert i.id is None


def test_equality():
    i1 = Item("something to do", "veit", "todo", 42)
    i2 = Item("something to do", "veit", "todo", 42)
    assert c1 == c2


def test_equality_with_diff_ids():
    i1 = Item("something to do", "veit", "todo", 42)
    i2 = Item("something to do", "veit", "todo", 43)
    assert c1 == c2
