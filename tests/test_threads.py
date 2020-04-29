from aio2ch import Thread

import pytest


@pytest.mark.asyncio
async def test_get_board_threads_str(client):
    threads = await client.get_board_threads(board="test")

    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_board_threads_str_with_keywords(client):
    threads = await client.get_board_threads(board="test", keywords=("тест",))

    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_board_threads_str_with_status(client):
    status, threads = await client.get_board_threads(board="test", return_status=True)

    assert status >= 200
    assert len(threads) > 0
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_board_threads_instance(client, board):
    threads = await client.get_board_threads(board=board)

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
    threads = await client.get_top_board_threads(board="test", method="views", num=number_of_threads)

    assert len(threads) == number_of_threads
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_str_with_status(client, number_of_threads):
    status, threads = await client.get_top_board_threads(board="test", method="score", num=number_of_threads,
                                                         return_status=True)

    assert status >= 200
    assert len(threads) == number_of_threads
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_instance(client, board, number_of_threads):
    threads = await client.get_top_board_threads(board=board, method="posts_count", num=number_of_threads)

    assert len(threads) == number_of_threads
    assert all(isinstance(thread, Thread) for thread in threads)


@pytest.mark.asyncio
async def test_get_top_board_threads_instance_with_status(client, board, number_of_threads):
    status, threads = await client.get_top_board_threads(board=board, method="views", num=number_of_threads,
                                                         return_status=True)

    assert status >= 200
    assert len(threads) == number_of_threads
    assert all(isinstance(thread, Thread) for thread in threads)
