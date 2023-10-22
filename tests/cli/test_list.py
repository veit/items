import items

expected_output = """\

  ID   state   owner   summary                      
 ────────────────────────────────────────────────── 
  1    todo            Update pytest section        
  2    todo            Update cibuildwheel section  
"""


def test_list(items_db, items_cli):
    items_db.add_item(items.Item("Update pytest section"))
    items_db.add_item(items.Item("Update cibuildwheel section"))
    output = items_cli("list")
    assert output.strip() == expected_output.strip()


def test_main(items_db, items_cli):
    items_db.add_item(items.Item("Update pytest section"))
    items_db.add_item(items.Item("Update cibuildwheel section"))
    output = items_cli("")
    assert output.strip() == expected_output.strip()
