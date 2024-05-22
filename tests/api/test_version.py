# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""
Test Cases
* version returns the correct version
"""

import re

import items


def test_version():
    """
    There is no api for version other than items.__version__.
    However, we do expect it to be:
    – a string containing a version in the form of "I.J.K"
    """
    version = items.__version__
    assert re.match(r"\d+\.\d+\.\d+", version)
