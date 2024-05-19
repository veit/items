"""Test the cli list function."""
import items

expected_output = """\

  ID   state   owner   summary                      
 ────────────────────────────────────────────────── 
  1    todo            Update pytest section        
  2    todo            Update cibuildwheel section  
"""


def test_list(items_db, items_cli):
    """Two items are added and then ``list`` should correspond to
    ``expected_output`` variable."""
    items_db.add_item(items.Item("Update pytest section"))
    items_db.add_item(items.Item("Update cibuildwheel section"))
    output = items_cli("list")
    assert output.strip() == expected_output.strip()


def test_main(items_db, items_cli):
    """Even if items is called without options on the command line, the
    corresponding table should be returned."""
    items_db.add_item(items.Item("Update pytest section"))
    items_db.add_item(items.Item("Update cibuildwheel section"))
    output = items_cli("")
    assert output.strip() == expected_output.strip()
