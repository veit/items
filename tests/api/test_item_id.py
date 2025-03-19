# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test that the item ID is correctly assigned and returned

* item id is correctly assigned and returned
* item id is included in the item object when retrieved
"""

from items import Item


def test_item_id_assignment(items_db):
    """Test that item ids are correctly assigned."""
    c1 = Item(summary="first item")
    c2 = Item(summary="second item")

    id1 = items_db.add_item(c1)
    id2 = items_db.add_item(c2)

    # Check that ids are different
    assert id1 != id2

    # Check that the ids are correctly stored in the items
    item1 = items_db.get_item(id1)
    item2 = items_db.get_item(id2)

    assert item1.id == id1
    assert item2.id == id2
