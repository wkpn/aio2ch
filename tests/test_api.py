from aio2ch.exceptions import NoBoardProvidedException, WrongSortMethodException
from aio2ch.objects import Board, File, Post, Thread


import pytest


@pytest.mark.asyncio
async def test_api_url(client):
    assert client._api_client.api_url == 'https://2ch.hk'


@pytest.mark.asyncio
async def test_api_url_changed(client):
    client._api_client.api_url = 'https://2ch.pm'

    assert client._api_client._api_url == 'https://2ch.pm'


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
async def test_get_board_threads_str(client):
    threads = await client.get_board_threads(board='test')

    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_board_threads_instance(client, board):
    threads = await client.get_board_threads(board=board)

    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_board_threads_str_with_status(client):
    status, threads = await client.get_board_threads(board='test', return_status=True)

    assert status >= 200
    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_board_threads_instance_with_status(client, board):
    status, threads = await client.get_board_threads(board=board, return_status=True)

    assert status >= 200
    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_str(client, number_of_threads):
    threads = await client.get_top_board_threads(board='test', method='views', num=number_of_threads)

    assert len(threads) == number_of_threads
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_instance(client, board, number_of_threads):
    threads = await client.get_top_board_threads(board=board, method='views', num=number_of_threads)

    assert len(threads) == number_of_threads
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_str_with_status(client, number_of_threads):
    status, threads = await client.get_top_board_threads(board='test', method='views', num=number_of_threads,
                                                         return_status=True)

    assert status >= 200
    assert len(threads) == number_of_threads
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_instance_with_status(client, board, number_of_threads):
    status, threads = await client.get_top_board_threads(board=board, method='views', num=number_of_threads,
                                                         return_status=True)

    assert status >= 200
    assert len(threads) == number_of_threads
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_str_wrong_sort_method(client):
    with pytest.raises(WrongSortMethodException):
        await client.get_top_board_threads(board='test', method='WrongSortMethod')


@pytest.mark.asyncio
async def test_get_top_board_threads_instance_wrong_sort_method(client, board):
    with pytest.raises(WrongSortMethodException):
        await client.get_top_board_threads(board=board, method='WrongSortMethod')


@pytest.mark.asyncio
async def test_get_thread_posts(client, thread):
    posts = await client.get_thread_posts(thread)

    assert all(isinstance(post, Post) for post in posts)


@pytest.mark.asyncio
async def test_get_thread_posts_with_status(client, thread):
    status, posts = await client.get_thread_posts(thread, return_status=True)

    assert status >= 200
    assert all(isinstance(post, Post) for post in posts)


@pytest.mark.asyncio
async def test_get_thread_posts_no_board_provided(client, thread):
    with pytest.raises(NoBoardProvidedException):
        await client.get_thread_posts(thread.num)


@pytest.mark.asyncio
async def test_get_thread_media(client, thread):
    thread_media = await client.get_thread_media(thread)

    assert len(thread_media) > 0
    assert all(isinstance(file, File) for file in thread_media)


@pytest.mark.asyncio
async def test_get_thread_media_with_status(client, thread):
    status, thread_media = await client.get_thread_media(thread, return_status=True)

    assert status >= 200
    assert len(thread_media) > 0
    assert all(isinstance(file, File) for file in thread_media)
