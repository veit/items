.. SPDX-FileCopyrightText: 2023 Veit Schiele

.. SPDX-License-Identifier: BSD-3-Clause

==========================
items – a simple todo list
==========================

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
      $ source bin/activate
      $ python -m pip install --upgrade pip
      $ python -m pip install -e .

   … on Windows:

   .. code-block:: ps1con

      C:> python -m venv .
      C:> Scripts\python -m pip install --upgrade pip
      C:> Scripts\python -m pip install -e .

Project links
=============

* `Documentation <https://items.cusy.io>`_
* `GitHub <https://github.com/veit/items>`_
* `Mastodon <https://mastodon.social/@veit>`_

Collaboration
=============

If you have suggestions for improvements and additions, I recommend that you
create a `Fork <https://github.com/veit/items/fork>`_ of my
`GitHub Repository <https://github.com/veit/items/>`_ and make
your changes there. You are also welcome to make a *pull request*. If the
changes contained therein are small and atomic, I’ll be happy to look at your
suggestions.
