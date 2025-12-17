.. SPDX-FileCopyrightText: 2023 Veit Schiele

.. SPDX-License-Identifier: BSD-3-Clause

==========================
items – a simple todo list
==========================

*items* is a simple command line tool for managing tasks. It allows you to
create, display, update and delete tasks, as well as change their status.

Status
======

.. image:: https://img.shields.io/github/contributors/veit/items.svg
   :alt: Contributors
   :target: https://github.com/veit/items/graphs/contributors
.. image:: https://img.shields.io/github/license/veit/items.svg
   :alt: License
   :target: https://github.com/veit/items/blob/main/LICENSE
.. image:: https://github.com/veit/items/workflows/CI/badge.svg
   :target: https://github.com/veit/items/actions?workflow=CI
   :alt: CI Status

Features
========

* Create tasks with summary and owner
* Display tasks, optionally filtered by owner or status
* Update tasks and their status (todo, in progress, done)
* Delete individual or all tasks
* Simple command line interface
* Programmable Python API

Installation
============

#. Download and unpack:

   … on Linux/macOS:

   .. code-block:: console

      $ curl -O https://codeload.github.com/veit/items/zip/main
      $ unzip main
      Archive:  main
      …
         creating: items-main/
      …

   … on Windows:

   .. code-block:: ps1con

      C:> curl.exe -o main.zip -O https://codeload.github.com/veit/items/zip/main
      C:> tar -xvzf main.zip
      items-main/
      items-main/.gitignore
      …

#. Install Python packages:

   … on Linux/macOS:

   .. code-block:: console

      $ cd items
      $ python3 -m venv .
      $ . bin/activate
      $ python -m pip install --upgrade pip
      $ python -m pip install -e .

   … on Windows:

   .. code-block:: ps1con

      C:> py -m venv .
      C:> Scripts\activate
      C:> python -m pip install --upgrade pip
      C:> python -m pip install -e .

Usage
=====

Command line instructions
-------------------------

After activating the virtual Python environment, you can use items on the
command line:

.. code-block:: console

   # Display all tasks (default if no command is specified)
   $ items

   # Add a new task
   $ items add "My task description" --owner "Veit"

   # Show filtered list
   $ items list --owner "Veit" --state "todo"

   # Update task
   $ items update 1 --owner "Veit" --summary "Update description"

   # Change the status of a task
   $ items start 1    # Set status to "in progress"
   $ items finish 1   # Set status to "done"

   # Delete task
   $ items delete 1

   # Display number of tasks
   $ items count

   # Display the file path of the database
   $ items config

   # Display version
   $ items version

Python API
----------

You can also use the items functionality directly in your Python code:

.. code-block:: python

   # Initialise database
   from items import ItemsDB, Item

   # Connect to database
   db = ItemsDB("/path/to/database")

   # Add new task
   item = Item(summary="Implement feature", owner="Veit")
   item_id = db.add_item(item)

   # Retrieve task by ID
   item = db.get_item(item_id)

   # Update task
   db.update_item(item_id, Item(summary="Implement feature with tests"))

   # Change status
   db.start(item_id)  # Set to "in progress"
   db.finish(item_id)  # Set to "done"

   #  List tasks (optionally with filtering)
   all_items = db.list_items()
   veit_tasks = db.list_items(owner="Veit")
   in_process = db.list_items(state="in progress")

   #  Delete task
   db.delete_item(item_id)

   # Close connection
   db.close()

Configuration
=============

The database file is saved under ``~/items_db`` by default. You can change this
path by setting the environment variable ``ITEMS_DB_DIR``:

.. code-block:: console

   # Linux/macOS
   $ export ITEMS_DB_DIR=/pfad/zu/meiner/datenbank

   # Windows
   C:> set ITEMS_DB_DIR=C:\pfad\zu\meiner\datenbank

Project links
=============

* `Documentation <https://items.cusy.io>`_
* `GitHub <https://github.com/veit/items>`_
* `Mastodon <https://mastodon.social/deck/@Python4DataScience>`_

Collaboration
=============

If you have suggestions for improvements and additions, I recommend that you
create a `Fork <https://github.com/veit/items/fork>`_ of my
`GitHub Repository <https://github.com/veit/items/>`_ and make
your changes there. You are also welcome to make a *pull request*. If the
changes contained therein are small and atomic, I’ll be happy to look at your
suggestions.

License
=======

This project is licensed under the BSD-3-Clause licence. Further information can
be found in the ``LICENSE`` file in the project repository.

Dies ist nur ein Beispiel für einen Pull-Request
