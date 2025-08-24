# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Testing the api configuration."""


def test_config(items_db, db_path):
    """Check the path to the database."""
    assert items_db.path() == db_path
