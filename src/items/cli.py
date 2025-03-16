# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""This module provides a command-line interface for managing items.
You can run the commands using the ``items`` command followed by
the specific subcommand:

.. code-block:: console

    items add "My task description" --owner "Veit"
    items list
    items list --owner "Veit" --state "todo"
    items update 1 --owner "Veit" --summary "Update description"
    items start 1
    items finish 1
    items delete 1
    items count
    items config
    items version

If no subcommand is specified, the ``list`` command is executed by default.
"""

import os
import pathlib
from contextlib import contextmanager
from io import StringIO
from typing import List

import rich
import typer
from rich.table import Table

import items

app = typer.Typer(add_completion=False)


@app.command()
def version():
    """Returns the version of the items application.

    Returns:
        str: The version string of the items package.
    """
    print(items.__version__)


@app.command()
def add(summary: List[str], owner: str = typer.Option(None, "-o", "--owner")):
    """Adds an item to the database.

    Args:
        summary (List[str]): The summary of the new item.
        owner (str, optional): The owner of the new item. Defaults to None.
    """
    summary = " ".join(summary) if summary else None
    with items_db() as db:
        db.add_item(items.Item(summary, owner, state="todo"))


@app.command()
def delete(item_id: int):
    """Removes an item from the database.

    Args:
        item_id (int): The ID of the item to delete.

    Raises:
        InvalidItemId: If no item with the given ID exists.
    """
    with items_db() as db:
        try:
            db.delete_item(item_id)
        except items.InvalidItemId:
            print(f"Error: Invalid item id {item_id}")


@app.command("list")
def list_items(
    owner: str = typer.Option(None, "-o", "--owner"),
    state: str = typer.Option(None, "-s", "--state"),
):
    """Lists items in the database, optionally filtered by owner and/or state.

    Args:
        owner (str, optional): Filter items by this owner. Defaults to None.
        state (str, optional): Filter items by this state. Defaults to None.
    """
    with items_db() as db:
        the_items = db.list_items(owner=owner, state=state)
        table = Table(box=rich.box.SIMPLE)
        table.add_column("ID")
        table.add_column("state")
        table.add_column("owner")
        table.add_column("summary")
        for t in the_items:
            owner = "" if t.owner is None else t.owner
            table.add_row(str(t.id), t.state, owner, t.summary)
        out = StringIO()
        rich.print(table, file=out)
        print(out.getvalue())


@app.command()
def update(
    item_id: int,
    owner: str = typer.Option(None, "-o", "--owner"),
    summary: List[str] = typer.Option(None, "-s", "--summary"),
):
    """Updates an item in the database.

    Args:
        item_id (int): The ID of the item to update.
        owner (str, optional): The new owner of the item. Defaults to None.
        summary (List[str], optional): The new summary of the item. Defaults to None.

    Raises:
        InvalidItemId: If no item with the given ID exists.
    """
    summary = " ".join(summary) if summary else None
    with items_db() as db:
        try:
            db.update_item(item_id, items.Item(summary, owner, state=None))
        except items.InvalidItemId:
            print(f"Error: Invalid item id {item_id}.")


@app.command()
def start(item_id: int):
    """Sets an item's state to 'in progress'.

    Args:
        item_id (int): The ID of the item to update.

    Raises:
        InvalidItemId: If no item with the given ID exists.
    """
    with items_db() as db:
        try:
            db.start(item_id)
        except items.InvalidItemId:
            print(f"Error: Invalid item id {item_id}.")


@app.command()
def finish(item_id: int):
    """Sets an item's state to 'done'.

    Args:
        item_id (int): The ID of the item to update.

    Raises:
        InvalidItemId: If no item with the given ID exists.
    """
    with items_db() as db:
        try:
            db.finish(item_id)
        except items.InvalidItemId:
            print(f"Error: Invalid item id {item_id}.")


@app.command()
def config():
    """Returns the path to the Items database.

    Returns:
        str: Path to the Items database.
    """
    with items_db() as db:
        print(db.path())


@app.command()
def count():
    """Returns the number of items in the database.

    Returns:
        int: Number of items in the database.
    """
    with items_db() as db:
        print(db.count())


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Items is a small command line task tracking application."""
    if ctx.invoked_subcommand is None:
        list_items(owner=None, state=None)


def get_path():
    """Determines the path to the database.

    The path is determined from the environment variable ITEMS_DB_DIR.
    If it is not defined, $HOME/items_db is used.

    Returns:
        pathlib.Path: Path to the database directory.
    """
    db_path_env = os.getenv("ITEMS_DB_DIR", "")
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / "items_db"
    return db_path


@contextmanager
def items_db():
    """Opens and closes the database connection.

    Yields:
        ItemsDB: An ItemsDB instance connected to the database.
    """
    db_path = get_path()
    db = items.ItemsDB(db_path)
    yield db
    db.close()
