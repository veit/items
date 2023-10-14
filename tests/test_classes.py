from items.api import Item


class TestEquality:
    def test_equality(self):
        i1 = Item("do something", "veit", "todo", 42)
        i2 = Item("do something", "veit", "todo", 42)
        assert i1 == i2

    def test_equality_with_diff_ids(self):
        i1 = Item("do something", "veit", "todo", 42)
        i2 = Item("do something", "veit", "todo", 43)
        assert i1 == i2

    def test_inequality(self):
        i1 = Item("do something", "veit", "todo", 42)
        i2 = Item("do something else", "veit", "done", 42)
        assert i1 != i2
