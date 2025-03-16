# SPDX-FileCopyrightText: 2023 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

"""DB for the items project."""

import tinydb


class DB:
    """Class for communication with the database.

    Args:
        db_path (str or pathlib.Path): Directory path for the database file.
        db_file_prefix (str): Prefix for the database filename.
    """

    def __init__(self, db_path, db_file_prefix):
        """Connects to the database or creates it if it doesn't exist."""
        self._db = tinydb.TinyDB(
            db_path / f"{db_file_prefix}.json", create_dirs=True
        )

    def create(self, item: dict) -> int:
        """Creates an item in the database.

        Args:
            item (dict): Dictionary containing the item data.

        Returns:
            int: The ID of the newly created item.
        """
        id = self._db.insert(item)
        return id

    def read(self, id: int):
        """Reads an item from the database.

        Args:
            id (int): The ID of the item to read.

        Returns:
            dict or None: The item object or None if not found.
        """
        item = self._db.get(doc_id=id)
        return item

    def read_all(self):
        """Reads the entire database.

        Returns:
            tinydb.TinyDB: All items in the database.
        """
        return self._db

    def update(self, id: int, mods) -> None:
        """Updates an item in the database.

        Args:
            id (int): The ID of the item to update.
            mods (dict): Dictionary containing the modifications to apply.

        Raises:
            KeyError: If no item with the given ID exists.
        """
        changes = {k: v for k, v in mods.items() if v is not None}
        self._db.update(changes, doc_ids=[id])

    def delete(self, id: int) -> None:
        """Deletes an item from the database.

        Args:
            id (int): The ID of the item to delete.

        Raises:
            KeyError: If no item with the given ID exists.
        """
        self._db.remove(doc_ids=[id])

    def delete_all(self) -> None:
        """Deletes all items in the database.

        Returns:
            None: This function doesn't return anything.
        """
        self._db.truncate()

    def count(self) -> int:
        """Counts all items in the database.

        Returns:
            int: The number of items in the database.
        """
        return len(self._db)

    def close(self):
        """Closes the database connection.

        Returns:
            None: This function doesn't return anything.
        """
        self._db.close()
