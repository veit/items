API reference
=============

.. automodule:: items.api

:class:`Item` class
-------------------

.. autoclass:: Item
   :members: from_dict, to_dict

:class:`ItemsDB` class
----------------------

.. autoclass:: ItemsDB
   :members: add_item, get_item, list_items, count, update_item, start, finish,
       delete_item, delete_all, close, path

Exceptions
----------

.. autoexception:: ItemsException
.. autoexception:: MissingSummary
.. autoexception:: InvalidItemId
