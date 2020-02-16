from aio2ch.exceptions import NoBoardProvidedException, WrongSortMethodException
from aio2ch.objects import Board, File, Post, Thread
from aio2ch import Api

import pytest


@pytest.fixture
async def client():
    api_client = Api()
    yield api_client
    await api_client.close()


@pytest.mark.asyncio
async def test_api_url(client):
    assert client.api_url == 'https://2ch.hk'


@pytest.mark.asyncio
async def test_api_url_changed(client):
    client.api_url = 'https://2ch.pm'

    assert client.api_url == 'https://2ch.pm'


@pytest.mark.asyncio
async def test_get_boards(client):
    boards = await client.get_boards()

    assert len(boards) > 0
    assert all(isinstance(board, Board) for board in boards)


@pytest.mark.asyncio
async def test_get_boards_with_status(client):
    status, boards = await client.get_boards(return_status=True)

    assert status >= 200
    assert len(boards) > 0
    assert all(isinstance(board, Board) for board in boards)


@pytest.mark.asyncio
async def test_get_board_threads(client):
    threads = await client.get_board_threads(board='test')

    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_board_threads_with_status(client):
    status, threads = await client.get_board_threads(board='test', return_status=True)

    assert status >= 200
    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads(client):
    threads = await client.get_top_board_threads(board='test', method='views')

    assert len(threads) == 5
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_with_status(client):
    status, threads = await client.get_top_board_threads(board='test', method='views', return_status=True)

    assert status >= 200
    assert len(threads) == 5
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_wrong_sort_method(client):
    with pytest.raises(WrongSortMethodException):
        await client.get_top_board_threads(board='test', method='WrongSortMethod')


@pytest.mark.asyncio
async def test_get_thread_posts(client):
    threads = await client.get_board_threads(board='test')
    thread = threads[0]

    posts = await client.get_thread_posts(thread)

    assert(all(isinstance(post, Post) for post in posts))


@pytest.mark.asyncio
async def test_get_thread_posts_with_status(client):
    _, threads = await client.get_board_threads(board='test', return_status=True)
    thread = threads[0]

    status, posts = await client.get_thread_posts(thread, return_status=True)

    assert status >= 200
    assert(all(isinstance(post, Post) for post in posts))


@pytest.mark.asyncio
async def test_get_thread_posts_no_board_provided(client):
    with pytest.raises(NoBoardProvidedException):
        await client.get_thread_posts(30972)


@pytest.mark.asyncio
async def test_get_thread_media(client):
    test_thread_data = {
        'comment': '',
        'num': 30972,
        'posts_count': '',
        'score': '',
        'subject': '',
        'timestamp': '',
        'views': ''
    }

    test_board = 'test'

    test_thread = Thread(test_thread_data, test_board)

    thread_media = await client.get_thread_media(test_thread)

    assert len(thread_media) > 0
    assert(all(isinstance(file, File) for file in thread_media))


@pytest.mark.asyncio
async def test_get_thread_media_with_status(client):
    test_thread_data = {
        'comment': '',
        'num': 30972,
        'posts_count': '',
        'score': '',
        'subject': '',
        'timestamp': '',
        'views': ''
    }

    test_board = 'test'

    test_thread = Thread(test_thread_data, test_board)

    status, thread_media = await client.get_thread_media(test_thread, return_status=True)

    assert status >= 200
    assert len(thread_media) > 0
    assert (all(isinstance(file, File) for file in thread_media))
