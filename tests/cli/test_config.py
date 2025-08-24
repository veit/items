# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli config function."""


def test_config(items_cli, db_path):
    """Test wether config returns the path to the database."""
    assert items_cli("config") == str(db_path)


def test_config_normal_path(db_path, items_cli_no_redirect):
    """Test whether config does not return the path to the database.

    If config is called with the ``items_cli_no_redirect`` fixture, the path to
    the productive database should not be returned.
    """
    items_cli = items_cli_no_redirect
    assert items_cli("config") != str(db_path)
