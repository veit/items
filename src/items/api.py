from dataclasses import asdict, dataclass, field

from .db import DB


@dataclass
class Item:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Item(**d)

    def to_dict(self):
        return asdict(self)


class ItemsException(Exception):
    pass


class InvalidItemId(ItemsException):
    pass


class InvalidItemId(ItemsException):
    pass


class ItemsDB:
    def __init__(self, db_path):
        self._db_path = db_path
        self._db = DB(db_path, ".items.db")

    def add_item(self, item: Item):
        """Add an item, return the id of item."""
        if not item.summary:
            raise MissingSummary
        if item.owner is None:
            item.owner = ""
        item_id = self._db.create(item.to_dict())
        self._db.update(item_id, {"id": item_id})
        return item_id

    def get_item(self, item_id: int):
        """Return the item with the associated ID."""
        db_item = self._db.read(item_id)
        if db_item is not None:
            return Item.from_dict(db_item)
        else:
            raise InvalidItemId(item_id)

    def list_items(self, owner=None, state=None):
        """Return a list of items."""
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
        """Return the number of items in the db."""
        return self._db.count()

    def update_item(self, item_id: int, item_mods: Item):
        """Update an item with modifications."""
        try:
            self._db.update(item_id, item_mods.to_dict())
        except KeyError as exc:
            raise InvalidItemId(item_id) from exc

    def start(self, item_id: int):
        """Set a item state to 'in prog'."""
        self.update_item(item_id, Item(state="in progress"))

    def finish(self, item_id: int):
        """Set an item state to done."""
        self.update_item(item_id, Item(state="done"))

    def delete_all(self):
        """Remove all items from the db."""
        self._db.delete_all()

    def close(self):
        self._db.close()

    def path(self):
        return self._db_path
