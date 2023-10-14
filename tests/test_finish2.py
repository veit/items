import pytest

from items import Item

pytestmark = pytest.mark.finish


@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("Update pytest section", "done"),
        ("Update cibuildwheel section", "in progress"),
        ("Update mock tests", "todo"),
    ],
)
def test_finish(items_db, start_summary, start_state):
    initial_item = Item(summary=start_summary, state=start_state)
    index = items_db.add_item(initial_item)
    items_db.finish(index)
    item = items_db.get_item(index)
    assert item.state == "done"
