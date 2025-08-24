# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""The API for the items project.

This module provides classes and functions to interact with the items database
programmatically.
"""

from dataclasses import asdict, dataclass, field

from .db import DB


__all__ = [
    "InvalidItemIdError",
    "Item",
    "ItemsDB",
    "ItemsError",
    "MissingSummaryError",
]


@dataclass
class Item:
    """Defines the items type with the attributes summary, owner and state.

    Args:
        summary (str): Summary of an item. Defaults to None.
        owner (str): The person working on an item. Defaults to None.
        state (str): The status of a task. Defaults to 'todo'.
        id (int): The unique identifier for the item. Defaults to None.

    """

    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        """Return an item instance from a dict.

        Args:
            d (dict): Dictionary containing item attributes.

        Returns:
            Item: Item instance created from dictionary values.

        """
        return Item(**d)

    def to_dict(self):
        """Return a dict from an item instance.

        Returns:
            dict: Dictionary containing the item's attributes.

        """
        return asdict(self)


class ItemsError(Exception):
    """Base exception class for the items module.

    Parent class for MissingSummaryError and InvalidItemIdError exceptions.
    """


class MissingSummaryError(ItemsError):
    """Exception raised when an item is added without a summary.

    Raised when items.api.ItemsDB.add_item is called with an item
    that has no summary.
    """


class InvalidItemIdError(ItemsError):
    """Exception raised when an operation is performed with an invalid item ID.

    Raised when trying to access or modify an item that doesn't exist.
    """


class ItemsDB:
    """Database class to access the items_db file.

    Args:
        db_path (str or pathlib.Path): Path to the database file.

    """

    def __init__(self, db_path):
        """Initiate the database class."""
        self._db_path = db_path
        self._db = DB(db_path, ".items_db")

    def add_item(self, item: Item):
        """Add an item to the database.

        Args:
            item (Item): The Item instance to add to the database.

        Returns:
            int: The item id of the newly added item.

        Raises:
            MissingSummaryError: If the item has no summary.

        """
        if not item.summary:
            raise MissingSummaryError
        if item.owner is None:
            item.owner = ""
        item_id = self._db.create(item.to_dict())
        self._db.update(item_id, {"id": item_id})
        return item_id

    def get_item(self, item_id: int):
        """Return an item for the corresponding id.

        Args:
            item_id (int): ID of the item to retrieve.

        Returns:
            Item: Item instance from the database.

        Raises:
            InvalidItemIdError: If no item with the given ID exists.

        """
        db_item = self._db.read(item_id)
        if db_item is not None:
            return Item.from_dict(db_item)
        raise InvalidItemIdError(item_id)

    def list_items(self, owner=None, state=None):
        """Return a list of items filtered by owner and/or state.

        Args:
            owner (str, optional): Filter items by this owner. Defaults to
            None.
            state (str, optional): Filter items by this state. Defaults to
            None.

        Returns:
            list[Item]: List of Item instances matching the filters. If no
            filters are specified, returns all items.

        """
        all_items = self._db.read_all()
        if (owner is not None) and (state is not None):
            return [
                Item.from_dict(t)
                for t in all_items
                if (t["owner"] == owner and t["state"] == state)
            ]
        if owner is not None:
            return [
                Item.from_dict(t) for t in all_items if t["owner"] == owner
            ]
        if state is not None:
            return [
                Item.from_dict(t) for t in all_items if t["state"] == state
            ]
        return [Item.from_dict(t) for t in all_items]

    def count(self):
        """Return the number of items in the database.

        Returns:
            int: The number of items in the database.

        """
        return self._db.count()

    def update_item(self, item_id: int, item_mods: Item):
        """Update an item with modifications.

        Args:
            item_id (int): The ID of the item to update.
            item_mods (Item): Item instance containing the modifications to
            apply.

        Raises:
            InvalidItemIdError: If no item with the given ID exists.

        """
        try:
            self._db.update(item_id, item_mods.to_dict())
        except KeyError as exc:
            raise InvalidItemIdError(item_id) from exc

    def start(self, item_id: int):
        """Set an item state to 'in progress'.

        Args:
            item_id (int): The ID of the item to update.

        Raises:
            InvalidItemIdError: If no item with the given ID exists.

        """
        self.update_item(item_id, Item(state="in progress"))

    def finish(self, item_id: int):
        """Set an item state to 'done'.

        Args:
            item_id (int): The ID of the item to update.

        Raises:
            InvalidItemIdError: If no item with the given ID exists.

        """
        self.update_item(item_id, Item(state="done"))

    def delete_item(self, item_id: int):
        """Remove an item from the database.

        Args:
            item_id (int): The ID of the item to delete.

        Raises:
            InvalidItemIdError: If no item with the given ID exists.

        """
        try:
            self._db.delete(item_id)
        except KeyError as exc:
            raise InvalidItemIdError(item_id) from exc

    def delete_all(self):
        """Remove all items from the database."""
        self._db.delete_all()

    def close(self):
        """Close the database connection."""
        self._db.close()

    def path(self):
        """Return the path to the database.

        Returns:
            str or pathlib.Path: Path to the database file.

        """
        return self._db_path
