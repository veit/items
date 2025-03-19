# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Testing the api delete all function with.

* delete_all removes all items from the database
* delete_all on an empty database doesn't cause errors
"""

import pytest

from items import InvalidItemId, Item


@pytest.mark.num_items(5)
def test_delete_all_from_many(items_db):
    """Test that delete_all removes all items."""
    assert items_db.count() == 5
    items_db.delete_all()
    assert items_db.count() == 0
    assert items_db.list_items() == []


def test_delete_all_from_empty(items_db):
    """Test that delete_all on an empty database works."""
    assert items_db.count() == 0
    items_db.delete_all()
    assert items_db.count() == 0
