# SPDX-FileCopyrightText: 2023–2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Tests for the Item dataclass methods

* Item.from_dict and Item.to_dict methods
* Item equality comparison
"""

from items import Item


def test_item_from_dict():
    """Test Item.from_dict method."""
    item_dict = {
        "summary": "Test summary",
        "owner": "Test owner",
        "state": "in progress",
        "id": 42,
    }

    item = Item.from_dict(item_dict)

    assert item.summary == "Test summary"
    assert item.owner == "Test owner"
    assert item.state == "in progress"
    assert item.id == 42


def test_item_to_dict():
    """Test Item.to_dict method."""
    item = Item(
        summary="Test summary", owner="Test owner", state="in progress", id=42
    )

    item_dict = item.to_dict()

    assert item_dict["summary"] == "Test summary"
    assert item_dict["owner"] == "Test owner"
    assert item_dict["state"] == "in progress"
    assert item_dict["id"] == 42


def test_item_equality():
    """Test Item equality comparison."""
    item1 = Item(
        summary="Same summary", owner="Same owner", state="todo", id=1
    )
    item2 = Item(
        summary="Same summary", owner="Same owner", state="todo", id=2
    )
    item3 = Item(
        summary="Different summary", owner="Same owner", state="todo", id=1
    )

    # Items with same summary, owner, state but different id should be equal
    assert item1 == item2

    # Items with different summary should not be equal
    assert item1 != item3
