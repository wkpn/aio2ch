from aio2ch import Post

import pytest


@pytest.mark.asyncio
async def test_get_thread_posts(client, thread):
    posts = await client.get_thread_posts(thread)

    assert all(isinstance(post, Post) for post in posts)


@pytest.mark.asyncio
async def test_get_thread_posts_by_url(client, thread_url):
    posts = await client.get_thread_posts(thread_url)

    assert all(isinstance(post, Post) for post in posts)


@pytest.mark.asyncio
async def test_get_thread_posts_with_status(client, thread):
    status, posts = await client.get_thread_posts(thread, return_status=True)

    assert status >= 200
    assert all(isinstance(post, Post) for post in posts)


@pytest.mark.asyncio
async def test_get_thread_posts_with_status_by_url(client, thread_url):
    status, posts = await client.get_thread_posts(thread_url, return_status=True)

    assert status >= 200
    assert all(isinstance(post, Post) for post in posts)


@pytest.mark.asyncio
async def test_get_thread_posts_with_board_instance(client, thread_as_number, board):
    posts = await client.get_thread_posts(thread_as_number, board=board)

    assert all(isinstance(post, Post) for post in posts)

