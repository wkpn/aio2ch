Changelog
=========

`2.0.3`
-------

* ``get_thread_posts`` and ``get_thread_media`` now accepts thread passed as url

.. code-block:: python

    >>> thread_media = await client.get_thread_media('https://2ch.hk/test/res/30972.html')

* added boards lists and according checks
* added new exceptions
* more tests
* more code cleanup
* added changelog_ and readme_ translations in Russian

`2.0.2`
-------

* added docstrings
* added project logo (might change in the future)
* moved ``api_client`` into separate module

`2.0.1`
-------

* reduced memory usage by using tuples instead of lists
* improved test coverage
* changed some api endpoints
* more typing annotations
* code cleanup

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

.. _changelog: https://github.com/wkpn/aio2ch/CHANGELOG-ru.rst
.. _readme: https://github.com/wkpn/aio2ch/README-ru.rst
