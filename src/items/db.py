# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""
DB for the items project
"""

import tinydb


class DB:
    """Class for communication with the database."""

    def __init__(self, db_path, db_file_prefix):
        """Connects to the database. If it does not exist, it is created with
        all the required directories."""
        self._db = tinydb.TinyDB(
            db_path / f"{db_file_prefix}.json", create_dirs=True
        )

    def create(self, item: dict) -> int:
        """Create an item

        Returns:
            id: The items id.
        """
        id = self._db.insert(item)
        return id

    def read(self, id: int):
        """Reads an item.

        Args:
            id (int): The item id of an item.
        Returns:
            item: The item object."""
        item = self._db.get(doc_id=id)
        return item

    def read_all(self):
        """Reads the entire database."""
        return self._db

    def update(self, id: int, mods) -> None:
        """Update an item in the database.

        Args:
            id (int): The item id of an item.
            mods (Item): The modifications to be made to this item.
        """
        changes = {k: v for k, v in mods.items() if v is not None}
        self._db.update(changes, doc_ids=[id])

    def delete(self, id: int) -> None:
        """Deletes an item in the database.

        Args:
            id (int): The item id of an item.
        """
        self._db.remove(doc_ids=[id])

    def delete_all(self) -> None:
        """Deletes all items in the database."""
        self._db.truncate()

    def count(self) -> int:
        """Counts all items in the database."""
        return len(self._db)

    def close(self):
        """Closes the database connection."""
        self._db.close()
