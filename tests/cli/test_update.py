# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli update function."""

import items


def test_update(items_db, items_cli):
    """If the owner and summary are changed with ``update``, this information
    and the unchanged state should be returned when this item is called."""
    i = items_db.add_item(items.Item("Update pytest section"))
    items_cli(f"update {i} -o veit -s foo")
    expected = items.Item("foo", owner="veit", state="todo")
    actual = items_db.get_item(i)
    assert actual == expected
