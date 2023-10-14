def test_add_list(items_db, items_list):
    expected_count = len(items_list)
    for i in items_list:
        items_db.add_item(i)
    assert items_db.count() == expected_count
