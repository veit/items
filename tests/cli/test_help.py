# SPDX-FileCopyrightText: 2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test CLI help."""

import pytest


@pytest.mark.parametrize(
    "command",
    [
        "add",
        "delete",
        "list",
        "update",
        "start",
        "finish",
        "config",
        "count",
        "version",
    ],
)
def test_help(command, items_cli):
    """Check that all commands are listed in help."""
    hlp = f"{command} --help"
    out = items_cli(hlp)
    assert f"Usage: root {command}" in out
