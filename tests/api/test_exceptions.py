# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Tests for the MissingSummary exception

* adding an item with no summary raises MissingSummary
* adding an item with empty summary raises MissingSummary
"""

import pytest

from items import Item
from items.api import MissingSummary


def test_missing_summary(items_db):
    """Test that adding an item with no summary raises MissingSummary."""
    with pytest.raises(MissingSummary):
        items_db.add_item(Item())


def test_empty_summary(items_db):
    """Test that adding an item with empty summary raises MissingSummary."""
    with pytest.raises(MissingSummary):
        items_db.add_item(Item(summary=""))
