aio2ch
======

|License|
|Downloads|
|PyPi|
|Python|

Fully asynchronous read-only API wrapper for 2ch.hk (dvach, Двач)

Requirements
------------

-  Python 3.5+

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
.. code-block:: python

    >>> from aio2ch import Api
    >>> api = Api()

Get all boards

.. code-block:: python

    >>> boards = await api.get_boards()

    >>> boards
    [<Board name: Фагготрия, id: fag>, ... ]

In addition we can get `status` for each method. This is useful for debug purposes or if retries are needed

.. code-block:: python

    >>> status, boards = await api.get_boards(return_status=True)

    >>> status
    200

    >>> boards
    [<Board name: Фагготрия, id: fag>, ... ]

Get all threads from a board

.. code-block:: python

    >>> threads = await api.get_board_threads(board='b')

    >>> threads
    [<Thread 180981319>, ... ]

Get top threads from a board sorted by method (*views*, *score* or *posts_count*)

.. code-block:: python

    >>> top_threads = await api.get_top_board_threads(board='b', method='views', num=3)

    >>> top_threads
    [<Thread 180894312>, <Thread 180946622>, <Thread 180963318>]

Get all thread's posts (`thread` is an instance of `Thread`)

.. code-block:: python

    >>> thread_posts = await api.get_thread_posts(thread=thread)

    >>> thread_posts
    [<Post 180894312>, ... ]

Get all media in all thread's posts (images, webm and so on)

.. code-block:: python

    >>> thread_media = await api.get_thread_media(thread=thread)

    >>> thread_media
    [<File name:15336559148500.jpg, path:/b/src/180979032/15336559148500.jpg, size:19>, ... ]

Download all thread media

.. code-block:: python

    >>> await api.download_thread_media(files=thread_media, save_to='./downloads/')

.. |License| image:: https://img.shields.io/pypi/l/aio2ch.svg
    :target: https://pypi.python.org/pypi/aio2ch
.. |Downloads| image:: https://pepy.tech/badge/aio2ch
    :target: https://pepy.tech/project/aio2ch
.. |PyPi| image:: https://img.shields.io/pypi/v/aio2ch.svg
    :target: https://pypi.python.org/pypi/aio2ch
.. |Python| image:: https://img.shields.io/pypi/pyversions/aio2ch.svg
    :target: https://pypi.python.org/pypi/aio2ch
