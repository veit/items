import pytest

from items.api import ItemsDB


def test_db_exists():
    with pytest.raises(TypeError):
        ItemsDB()
