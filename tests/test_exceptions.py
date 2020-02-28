from aio2ch.exceptions import (
    InvalidBoardIdException,
    InvalidThreadUrlException,
    NoBoardProvidedException,
    WrongSortMethodException
)

import pytest


@pytest.mark.asyncio
async def test_get_board_threads_invalid_board(client):
    with pytest.raises(InvalidBoardIdException):
        await client.get_board_threads(board='thisboarddoesntexist')


@pytest.mark.asyncio
async def test_get_top_board_threads_str_wrong_sort_method(client):
    with pytest.raises(WrongSortMethodException):
        await client.get_top_board_threads(board='test', method='WrongSortMethod')


@pytest.mark.asyncio
async def test_get_top_board_threads_instance_wrong_sort_method(client, board):
    with pytest.raises(WrongSortMethodException):
        await client.get_top_board_threads(board=board, method='WrongSortMethod')


@pytest.mark.asyncio
async def test_get_thread_posts_no_board_provided(client, thread):
    with pytest.raises(NoBoardProvidedException):
        await client.get_thread_posts(thread.num)


@pytest.mark.asyncio
async def test_get_thread_posts_invalid_thread_url(client, invalid_thread_url):
    with pytest.raises(InvalidThreadUrlException):
        await client.get_thread_posts(invalid_thread_url)
