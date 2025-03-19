# SPDX-FileCopyrightText: 2023–2025 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Test the cli list function

* Tests the expected output, even if no parameter was specified.
* Test the cli list function with owner and state filters.
"""

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


def test_list_filter_by_owner(items_db, items_cli):
    """Test filtering the list by owner."""
    items_db.add_item(items.Item("Task for Alice", owner="alice"))
    items_db.add_item(items.Item("Task for Bob", owner="bob"))
    items_db.add_item(items.Item("Another task for Alice", owner="alice"))

    output = items_cli("list -o alice")

    # Verify only Alice's tasks are shown
    assert "Task for Alice" in output
    assert "Another task for Alice" in output
    assert "Task for Bob" not in output


def test_list_filter_by_state(items_db, items_cli):
    """Test filtering the list by state."""
    items_db.add_item(items.Item("Todo task", state="todo"))
    in_progress_id = items_db.add_item(items.Item("In progress task"))
    done_id = items_db.add_item(items.Item("Done task"))

    items_db.start(in_progress_id)
    items_db.finish(done_id)

    output = items_cli("list -s 'in progress'")

    # Verify only "in progress" tasks are shown
    assert "In progress task" in output
    assert "Todo task" not in output
    assert "Done task" not in output


def test_list_filter_by_owner_and_state(items_db, items_cli):
    """Test filtering the list by both owner and state."""
    items_db.add_item(items.Item("Alice todo", owner="alice", state="todo"))
    in_progress_id = items_db.add_item(
        items.Item("Alice in progress", owner="alice")
    )
    items_db.add_item(items.Item("Bob todo", owner="bob", state="todo"))

    items_db.start(in_progress_id)

    output = items_cli("list -o alice -s 'in progress'")

    # Verify only Alice's "in progress" tasks are shown
    assert "Alice in progress" in output
    assert "Alice todo" not in output
    assert "Bob todo" not in output
