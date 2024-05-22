# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""Command Line Interface (CLI) for the items project."""

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
        str: The version of the items package.
    """
    print(items.__version__)


@app.command()
def add(summary: List[str], owner: str = typer.Option(None, "-o", "--owner")):
    """Adds an item to the db.

    Args:
        summary (list[str]): The summary of the new item.
        owner (str): The owner of the new item.
    """
    summary = " ".join(summary) if summary else None
    with items_db() as db:
        db.add_item(items.Item(summary, owner, state="todo"))


@app.command()
def delete(item_id: int):
    """Removes an item in the db with a given id.

    Args:
        item_id (int): The item id of an item.
    Raises:
        InvalidItemId: if the item id is invalid.
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
    """List all items in the db."""
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
    """Modifies an item in the db with a given id with new info.

    Args:
        item_id (int): The item id of an item.
        owner (str): The owner of the new item.
        summary (list[str]): The summary of the new item.

    Raises:
        InvalidItemId: if the item id is invalid.
    """
    summary = " ".join(summary) if summary else None
    with items_db() as db:
        try:
            db.update_item(item_id, items.Item(summary, owner, state=None))
        except items.InvalidItemId:
            print(f"Error: Invalid item id {item_id}.")


@app.command()
def start(item_id: int):
    """Set an item state to in progress.

    Args:
        item_id (int): The item id of an item.

    Raises:
        InvalidItemId: if the item id is invalid.
    """
    with items_db() as db:
        try:
            db.start(item_id)
        except items.InvalidItemId:
            print(f"Error: Invalid item id {item_id}.")


@app.command()
def finish(item_id: int):
    """Set an item state to done.

    Args:
        item_id (int): The item id of an item.

    Raises:
        InvalidItemId: if the item id is invalid.
    """
    with items_db() as db:
        try:
            db.finish(item_id)
        except items.InvalidItemId:
            print(f"Error: Invalid item id {item_id}.")


@app.command()
def config():
    """Returns the path to the Items db.

    Returns:
        str: The path to the Items db.
    """
    with items_db() as db:
        print(db.path())


@app.command()
def count():
    """Returns number of items in db.

    Returns:
        str: The number of the items in the Items db.
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

    Returns:
        str: Determines the path to the database from the environment variable
        ITEMS_DB_DIR. If it is not defined, $HOME/items_db is used.
    """
    db_path_env = os.getenv("ITEMS_DB_DIR", "")
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / "items_db"
    return db_path


@contextmanager
def items_db():
    """Opens and closes the database connection."""
    db_path = get_path()
    db = items.ItemsDB(db_path)
    yield db
    db.close()
