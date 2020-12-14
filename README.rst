|Logo|

|License|
|Changelog|
|Downloads|
|PyPi|
|Python|

Fully asynchronous read-only API wrapper for 2ch.hk (dvach, Двач)

Requirements
------------

-  httpx_
-  aiofiles_
-  click_

Install with pip
----------------
.. code-block:: bash

    $ pip3 install aio2ch


Build from source
-----------------
.. code-block:: bash

    $ git clone https://github.com/wkpn/aio2ch
    $ cd ./aio2ch
    $ python3 setup.py install

Usage
-----

Simple usage (in this case ``client.close()`` must be called when client is no longer needed)

.. code-block:: python

    >>> from aio2ch import Api
    >>> client = Api()
    >>> ...
    >>> await client.close()

Or you can use it as a context manager

.. code-block:: python

    >>> async with Api() as client:
    ...     boards = await client.get_boards()
    >>>     ...

Get all boards

.. code-block:: python

    >>> boards = await client.get_boards()

    >>> boards
    (<Board name='Фагготрия', id='fag'>, ... )

In addition we can get ``status`` for each method. This is useful for debug purposes or if retries are needed

.. code-block:: python

    >>> status, boards = await client.get_boards(return_status=True)

    >>> status
    200

    >>> boards
    (<Board name='Фагготрия', id='fag'>, ... )

Get all threads from a board

.. code-block:: python

    >>> threads = await client.get_board_threads(board="b")

    >>> threads
    (<Thread num='180981319'>, ... )

Get top threads from a board sorted by method (*views*, *score* or *posts_count*)

.. code-block:: python

    >>> top_threads = await client.get_top_board_threads(board="b", method="views", num=3)

    >>> top_threads
    (<Thread num='180894312'>, <Thread num='180946622'>, <Thread num='180963318'>)

Get all thread's posts (``thread`` is an instance of ``Thread``)

.. code-block:: python

    >>> thread_posts = await client.get_thread_posts(thread=thread)

    >>> thread_posts
    (<Post num='180894312'>, ... )

Get all thread's posts  by url

.. code-block:: python

    >>> thread_posts = await client.get_thread_posts(thread="https://2ch.hk/test/res/30972.html")

    >>> thread_posts
    (<Post num='30972'>, ... )

Get all media in all thread's posts (images, webm and so on)

.. code-block:: python

    >>> thread_media = await client.get_thread_media(thread=thread)

    >>> thread_media
    (<File name='15336559148500.jpg', path='/b/src/180979032/15336559148500.jpg', size='19'>, ... )

Get specific thread media

.. code-block:: python

    >>> images_and_videos = await client.get_thread_media(thread, media_type=(Image, Video))

    >>> images_and_videos
    (<Image name=...>, <Video name=...>, ...)

    >>> just_images = await client.get_thread_media(thread, media_type=Image)

    >>> just_images
    (<Image name=...>, ...)

Download all thread media

.. code-block:: python

    >>> await client.download_thread_media(files=thread_media, save_to="./downloads")

.. |License| image:: https://img.shields.io/pypi/l/aio2ch.svg
    :target: https://github.com/wkpn/aio2ch/blob/master/LICENSE
.. |Changelog| image:: https://img.shields.io/badge/changelog-conventional-green.svg
    :target: https://github.com/wkpn/aio2ch/blob/master/CHANGELOG.rst
.. |Downloads| image:: https://pepy.tech/badge/aio2ch
    :target: https://pepy.tech/project/aio2ch
.. |PyPi| image:: https://img.shields.io/pypi/v/aio2ch.svg
    :target: https://pypi.python.org/pypi/aio2ch
.. |Python| image:: https://img.shields.io/pypi/pyversions/aio2ch.svg
    :target: https://pypi.python.org/pypi/aio2ch
.. |Logo| image:: https://raw.githubusercontent.com/wkpn/aio2ch/master/docs/img/banner.jpg
.. _httpx: https://github.com/encode/httpx
.. _aiofiles: https://github.com/Tinche/aiofiles
.. _click: https://github.com/pallets/click