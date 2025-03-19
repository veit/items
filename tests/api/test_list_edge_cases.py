# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Enhanced testing for list filtering with edge cases."""

import pytest

from items import Item


@pytest.fixture()
def edge_case_db(items_db):
    """Create database with items having empty strings and special cases"""
    items = (
        Item(summary="Regular task", owner="user", state="todo"),
        Item(summary="Empty owner task", owner="", state="todo"),
        Item(summary="None owner", owner=None, state="todo"),
        Item(summary="In progress task", owner="user", state="in progress"),
        Item(summary="Done task", owner="user", state="done"),
        Item(summary="Long summary! " * 100, owner="user", state="todo"),
        Item(summary="Special chars: -!@#", owner="user-!@#", state="todo"),
    )
    ids = [items_db.add_item(item) for item in items]
    return items_db, ids, items


@pytest.mark.parametrize(
    "owner_filter, state_filter, expected_count",
    [
        ("user", "todo", 2),  # Regular, long summary, special chars
        ("", "todo", 2),  # Empty owner
        (None, "todo", 5),  # All todo items (includes None owner)
        ("user", "in progress", 1),
        ("user", "done", 1),
        ("non-existent", "todo", 0),
        ("user-!@#", "todo", 1),  # Special chars in owner
        (None, None, 7),  # All items
    ],
)
def test_list_filter_edge_cases(
    edge_case_db, owner_filter, state_filter, expected_count
):
    """Test list filtering with various edge cases."""
    db, _, _ = edge_case_db
    result = db.list_items(owner=owner_filter, state=state_filter)
    assert len(result) == expected_count
