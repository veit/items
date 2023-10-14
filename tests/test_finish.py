import pytest

from items import InvalidItemId, Item

pytestmark = pytest.mark.finish


@pytest.fixture(
    params=[
        "todo",
        pytest.param("in progress", marks=pytest.mark.smoke),
        "done",
    ]
)
def start_state_fixture(request):
    return request.param


def test_finish(items_db, start_state_fixture):
    i = items_db.add_item(Item("Update pytest section", state=start_state_fixture))
    items_db.finish(i)
    s = items_db.get_item(i)
    assert s.state == "done"


@pytest.mark.smoke
@pytest.mark.exception
def test_finish_non_existent(items_db):
    i = 44  # any_number will be invalid, db is empty
    with pytest.raises(InvalidItemId):
        items_db.finish(i)
