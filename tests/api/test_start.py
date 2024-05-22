# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""
Test Cases
* start from "todo", "in progress", and "done" states
* start an invalid id
"""

import pytest

from items import InvalidItemId, Item


@pytest.mark.parametrize("start_state", ("todo", "in progress", "done"))
def test_start(items_db, start_state):
    """
    End state should be "in progress"
    """
    i = Item("Update pytest section", state=start_state)
    ai = items_db.add_item(i)
    items_db.start(ai)
    i = items_db.get_item(ai)
    assert i.state == "in progress"


def test_start_non_existent(items_db):
    """
    Shouldn't be able to start a non-existent item.
    """
    i = 42  # any number will do, db is empty
    with pytest.raises(InvalidItemId):
        items_db.start(i)
