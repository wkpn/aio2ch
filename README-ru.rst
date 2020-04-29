|Logo|

|License|
|Changelog|
|Downloads|
|PyPi|
|Python|

Полностью асинхронный read-only API wrapper для 2ch.hk (dvach, Двач)

Требования
----------

-  httpx_
-  aiofiles_

Установка через pip
-------------------
.. code-block:: bash

    $ pip3 install aio2ch


Сборка из исходников
--------------------
.. code-block:: bash

    $ git clone https://github.com/wkpn/aio2ch
    $ cd ./aio2ch
    $ python3 setup.py install

Использование
-------------

Простой пример (тогда надо вызвать ``client.close()`` в конце использования)

.. code-block:: python

    >>> from aio2ch import Api
    >>> client = Api()
    >>> ...
    >>> await client.close()

Или можно использовать как менеджер контекста

.. code-block:: python

    >>> async with Api() as client:
    ...     boards = await client.get_boards()

Получить все доски

.. code-block:: python

    >>> boards = await client.get_boards()

    >>> boards
    (<Board name='Фагготрия', id='fag'>, ... )

Также дополнительно можно получить ``status`` для каждого метода. Полезно, если нужны ретраи

.. code-block:: python

    >>> status, boards = await client.get_boards(return_status=True)

    >>> status
    200

    >>> boards
    (<Board name='Фагготрия', id='fag'>, ... )

Получить все треды с доски

.. code-block:: python

    >>> threads = await client.get_board_threads(board="b")

    >>> threads
    (<Thread num='180981319'>, ... )

Получить топ тредов с доски с заданной сортировкой (*views*, *score* или *posts_count*)

.. code-block:: python

    >>> top_threads = await client.get_top_board_threads(board="b", method="views", num=3)

    >>> top_threads
    (<Thread num='180894312'>, <Thread num='180946622'>, <Thread num='180963318'>)

Получить все посты с треда (``thread`` инстанс ``Thread``)

.. code-block:: python

    >>> thread_posts = await client.get_thread_posts(thread=thread)

    >>> thread_posts
    (<Post num='180894312'>, ... )

Получить все посты с треда по его адресу

.. code-block:: python

    >>> thread_posts = await client.get_thread_posts(thread="https://2ch.hk/test/res/30972.html")

    >>> thread_posts
    (<Post num='30972'>, ... )

Получить все медиа с треда (пикчи, webm-ки и прочее)

.. code-block:: python

    >>> thread_media = await client.get_thread_media(thread=thread)

    >>> thread_media
    (<File name='15336559148500.jpg', path='/b/src/180979032/15336559148500.jpg', size='19'>, ... )


Получить определенное медиа с треда

.. code-block:: python

    >>> images_and_videos = await client.get_thread_media(thread, media_type=(Image, Video))

    >>> images_and_videos
    (<Image name=...>, <Video name=...>, ...)

    >>> just_images = await client.get_thread_media(thread, media_type=Image)

    >>> just_images
    (<Image name=...>, ...)

Скачать все медиа с треда на диск в папку

.. code-block:: python

    >>> await client.download_thread_media(files=thread_media, save_to="./downloads")

.. |License| image:: https://img.shields.io/pypi/l/aio2ch.svg
    :target: https://github.com/wkpn/aio2ch/blob/master/LICENSE
.. |Changelog| image:: https://img.shields.io/badge/changelog-conventional-green.svg
    :target: https://github.com/wkpn/aio2ch/blob/master/CHANGELOG-ru.rst
.. |Downloads| image:: https://pepy.tech/badge/aio2ch
    :target: https://pepy.tech/project/aio2ch
.. |PyPi| image:: https://img.shields.io/pypi/v/aio2ch.svg
    :target: https://pypi.python.org/pypi/aio2ch
.. |Python| image:: https://img.shields.io/pypi/pyversions/aio2ch.svg
    :target: https://pypi.python.org/pypi/aio2ch
.. |Logo| image:: https://raw.githubusercontent.com/wkpn/aio2ch/master/docs/img/banner.jpg
.. _httpx: https://github.com/encode/httpx
.. _aiofiles: https://github.com/Tinche/aiofiles