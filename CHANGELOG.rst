Changelog
=========

`2.0`
-----

* Api client now can be used as a context manager
* f-strings are now everywhere
* Replace ``aiohttp`` in favor of ``httpx``
* Typing annotations
* ``download_thread_media`` is now using streaming approach

`1.4.3.1`
---------

* Minor imports refactoring (``from aio2ch import Api`` can be used now, old version still works)
* All methods do not return ``status`` by default, you need to pass ``return_status=True`` if you want to get it (see examples)


`1.4.3`
-------

* Added ``keywords`` parameter to ``get_board_threads`` method
* Added ``download_thread_media`` method
