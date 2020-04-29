from aio2ch import Board

import pytest


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
