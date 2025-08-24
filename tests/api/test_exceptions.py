# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Tests for the MissingSummaryError exception.

* adding an item with no summary raises MissingSummaryError
* adding an item with empty summary raises MissingSummaryError
"""

import pytest

from items import Item
from items.api import MissingSummaryError


def test_missing_summary(items_db):
    """Test that adding an item with no summary raises MissingSummaryError."""
    with pytest.raises(MissingSummaryError):
        items_db.add_item(Item())


def test_empty_summary(items_db):
    """Test adding an item with empty summary.

    This should raise a MissingSummaryError.
    """
    with pytest.raises(MissingSummaryError):
        items_db.add_item(Item(summary=""))
