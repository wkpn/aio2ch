Changelog
=========

`2.1.0`
-------

* raw text in posts and threads is html-escaped now (e.g. without <...> tags)
* more distinct ``File`` classes: ``Image`` (jpg, png, gif), ``Video`` (webm, mp4), ``Sticker`` (2ch-specific)
* added ``media_type`` parameter to ``get_thread_media`` to allow specific attachments download

.. code-block:: python

    >>> images_and_videos = await client.get_thread_media(thread, media_type=(Image, Video))

    >>> just_images = await client.get_thread_media(thread, media_type=Image)

    >>> any_files = await client.get_thread_media(thread)

* improved test coverage
* split test files by test type
* minor refactoring and improvements


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
