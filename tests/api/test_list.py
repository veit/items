"""Testing the api list command."""
import pytest

from items import Item


def test_list_no_items(items_db):
    """list_items of an empty database should return an empty list."""
    assert items_db.list_items() == []


def test_list_several_items(items_db):
    """Given a list of items, this should be returned.

    Given a list of items, the correct number should be returned. In addition,
    each of the items should be in the list.
    """
    orig = [
        Item("Update pytest section"),
        Item("Update cibuildwheel section", owner="veit"),
        Item("Update mock tests", owner="vsc", state="in progress"),
    ]

    for c in orig:
        items_db.add_item(c)

    the_list = items_db.list_items()

    assert len(the_list) == len(orig)
    for c in orig:
        assert c in the_list


@pytest.fixture()
def known_set():
    """Create a list of items.

    Some have no owner, others have defined owners and/or states.
    """
    return [
        Item(summary="zero", owner="veit", state="todo"),
        Item(summary="one", owner="veit", state="in progress"),
        Item(summary="two", owner="veit", state="done"),
        Item(summary="three", owner="vsc", state="todo"),
        Item(summary="four", owner="vsc", state="in progress"),
        Item(summary="five", owner="vsc", state="done"),
        Item(summary="six", state="todo"),
        Item(summary="seven", state="in progress"),
        Item(summary="eight", state="done"),
    ]


@pytest.fixture()
def db_filled(items_db, known_set):
    """Filling the database."""
    for c in known_set:
        items_db.add_item(c)
    return items_db


@pytest.mark.parametrize(
    "owner_, state_, expected_indices",
    [
        ("", None, (6, 7, 8)),
        ("veit", None, (0, 1, 2)),
        ("vsc", None, (3, 4, 5)),
        (None, "todo", (0, 3, 6)),
        (None, "in progress", (1, 4, 7)),
        (None, "done", (2, 5, 8)),
        ("veit", "todo", (0,)),
    ],
    ids=str,
)
def test_list_filter(db_filled, known_set, owner_, state_, expected_indices):
    """Check the number of items and whether the correct items have been
    filtered out of the database.
    """
    result = db_filled.list_items(owner=owner_, state=state_)
    assert len(result) == len(expected_indices)
    for i in expected_indices:
        assert known_set[i] in result
