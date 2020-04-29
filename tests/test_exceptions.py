from aio2ch import (
    InvalidBoardIdException,
    InvalidThreadException,
    NoBoardProvidedException,
    WrongSortMethodException
)

import pytest


@pytest.mark.asyncio
async def test_get_board_threads_invalid_board(client, invalid_board):
    with pytest.raises(InvalidBoardIdException):
        await client.get_board_threads(board=invalid_board)


@pytest.mark.asyncio
async def test_get_top_board_threads_invalid_board(client, invalid_board):
    with pytest.raises(InvalidBoardIdException):
        await client.get_top_board_threads(board=invalid_board, method="views")


@pytest.mark.asyncio
async def test_get_top_board_threads_str_wrong_sort_method(client):
    with pytest.raises(WrongSortMethodException):
        await client.get_top_board_threads(board="test", method="WrongSortMethod")


@pytest.mark.asyncio
async def test_get_top_board_threads_instance_wrong_sort_method(client, board):
    with pytest.raises(WrongSortMethodException):
        await client.get_top_board_threads(board=board, method="WrongSortMethod")


@pytest.mark.asyncio
async def test_get_thread_posts_no_board_provided(client, thread):
    with pytest.raises(NoBoardProvidedException):
        await client.get_thread_posts(thread.num)


@pytest.mark.asyncio
async def test_get_thread_posts_invalid_thread(client, invalid_thread):
    with pytest.raises(InvalidThreadException):
        await client.get_thread_posts(invalid_thread)


@pytest.mark.asyncio
async def test_get_thread_posts_invalid_board_id(client, thread_as_number, invalid_board):
    with pytest.raises(InvalidBoardIdException):
        await client.get_thread_posts(thread_as_number, board=invalid_board)
