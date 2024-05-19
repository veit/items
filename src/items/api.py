"""
The API for the items project
"""
from dataclasses import asdict, dataclass, field

from .db import DB

__all__ = [
    "Item",
    "ItemsDB",
    "ItemsException",
    "MissingSummary",
    "InvalidItemId",
]


@dataclass
class Item:
    """Defines the items type with the attributes summary, owner and state.

    Attributes:
        summary (str): Summary of an item. Defaults to None.
        owner (str): The person working on an item. Defaults to None.
        state (str): The status of a task. Defaults to *todo*.
    """

    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        """Returns an item instance from a dict."""
        return Item(**d)

    def to_dict(self):
        """Returns a dict from an item instance."""
        return asdict(self)


class ItemsException(Exception):
    """Exception class used by the :class:`MissingSummary` and
    :class:`InvalidItemId` exceptions.
    """

    pass


class MissingSummary(ItemsException):
    """Exception if an item does not have a summary when calling
    :func:`items.api.ItemsDB.add_item`."""

    pass


class InvalidItemId(ItemsException):
    """Exception if an item has no summary."""

    pass


class ItemsDB:
    """Database class to access the :file:`items_db` file."""

    def __init__(self, db_path):
        self._db_path = db_path
        self._db = DB(db_path, ".items_db")

    def add_item(self, item: Item):
        """Adds an item to the database.

        Args:
            item (Item): The arguments of the :class:`Item` class.

        Returns:
            int: The item id.

        Raises:
            MissingSummary: if there is no summary.
        """
        if not item.summary:
            raise MissingSummary
        if item.owner is None:
            item.owner = ""
        item_id = self._db.create(item.to_dict())
        self._db.update(item_id, {"id": item_id})
        return item_id

    def get_item(self, item_id: int):
        """Returns an item for the corresponding id.

        Args:
            item_id: (int): id of the item

        Returns:
            Item: Item instance from a dict.

        Raises:
            InvalidItemId: if None is returned.
        """
        db_item = self._db.read(item_id)
        if db_item is not None:
            return Item.from_dict(db_item)
        else:
            raise InvalidItemId(item_id)

    def list_items(self, owner=None, state=None):
        """Returns a list of all items.

        Args:
            owner: (str): Defaults to None.
            state: (str): Defaults to None.

        Returns:
            list: List of all :class:`Item` instances to which ``owner`` and
            ``state`` apply.
        """
        all_items = self._db.read_all()
        if (owner is not None) and (state is not None):
            return [
                Item.from_dict(t)
                for t in all_items
                if (t["owner"] == owner and t["state"] == state)
            ]
        elif owner is not None:
            return [
                Item.from_dict(t) for t in all_items if t["owner"] == owner
            ]
        elif state is not None:
            return [
                Item.from_dict(t) for t in all_items if t["state"] == state
            ]
        else:
            return [Item.from_dict(t) for t in all_items]

    def count(self):
        """Returns the number of items in the db.

        Returns:
            int: The number of items in the db.
        """
        return self._db.count()

    def update_item(self, item_id: int, item_mods: Item):
        """Update an item with modifications.

        Args:
            item_id: (int): The id of the item that is to be updated.
            item_mods: (Item): The modifications to be made to this item.

        Raises:
            InvalidItemId: if a KeyError is raised.
        """
        try:
            self._db.update(item_id, item_mods.to_dict())
        except KeyError as exc:
            raise InvalidItemId(item_id) from exc

    def start(self, item_id: int):
        """Sets an item state to in progress."""
        self.update_item(item_id, Item(state="in progress"))

    def finish(self, item_id: int):
        """Sets an item state to done."""
        self.update_item(item_id, Item(state="done"))

    def delete_item(self, item_id: int):
        """Removes an item from db with a given item id."""
        try:
            self._db.delete(item_id)
        except KeyError as exc:
            raise InvalidItemId(item_id) from exc

    def delete_all(self):
        """Removes all items from the db."""
        self._db.delete_all()

    def close(self):
        """Closes the db connection."""
        self._db.close()

    def path(self):
        """Prints the path to the db."""
        return self._db_path
