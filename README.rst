aio2ch
======


Fully asynchronous API wrapper for 2ch.hk (dvach, Двач)

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
--------------------
.. code-block:: python

    >>> from aio2ch.api import Api
    >>> api = Api()

Get all boards

.. code-block:: python

    >>> status, boards = await api.get_boards()

    >>> boards
    [<Board name: Фагготрия, id: fag>, ... ]

Get all threads from a board

.. code-block:: python

    >>> status, threads = await api.get_board_threads(board='b')

    >>> threads
    [<Thread 180981319>, ... ]

Get top threads from a board sorted by method (*views*, *score* or *posts_count*)

.. code-block:: python

    >>> status, top_threads = await api.get_top_board_threads(board='b', method='views', num=3)

    >>> top_threads
    [<Thread 180894312>, <Thread 180946622>, <Thread 180963318>]

Get all thread's posts (`thread` is instance of `Thread`)

.. code-block:: python

    >>> status, thread_posts = await api.get_thread_posts(thread=thread)

    >>> thread_posts
    [<Post 180894312>, ... ]

Get all media in all thread's posts (images, webm etc.)

.. code-block:: python

    >>> status, thread_media = await api.get_thread_media(thread=thread)

    >>> thread_media
    [<File name:15336559148500.jpg, path:/b/src/180979032/15336559148500.jpg, size:19>, ... ]
