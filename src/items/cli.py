"""Command Line Interface (CLI) for the items project."""

import os
import pathlib
from contextlib import contextmanager
from typing import List

import typer

import items

app = typer.Typer(add_completion=True)


@app.command()
def config():
    """Return the path to the Items db."""
    with items_db() as db:
        print(db.path())


@app.command()
def version():
    """Return the version of the items application."""
    print(items.__version__)


@app.command()
def add(summary: List[str], owner: str = typer.Option(None, "-o", "--owner")):
    """Add an item."""
    summary = " ".join(summary) if summary else None
    with items_db() as db:
        db.add_item(items.Item(summary, owner, state="todo"))


@app.command()
def start(item_id: int):
    """Set the item state to ‘in progress’."""
    with items_db() as db:
        try:
            db.start(item_id)
        except items.InvalidItemId:
            print(f"Error: Invalid item id {item_id}")


def get_path():
    db_path_env = os.getenv("ITEMS_DB_DIR", "")
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / "items_db"
    return db_path


@contextmanager
def items_db():
    db_path = get_path()
    db = items.ItemsDB(db_path)
    yield db
    db.close()
