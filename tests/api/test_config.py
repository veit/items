"""
Test Cases
* config returns the correct database path
"""


def test_config(items_db, db_path):
    assert items_db.path() == db_path
