# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli delete function."""

import items


def test_delete(items_db, items_cli):
    """First an item is added, then deleted again. The number of items in the
    database should then be ``0``."""
    i = items_db.add_item(items.Item("Update pytest section"))
    items_cli(f"delete {i}")
    assert items_db.count() == 0
