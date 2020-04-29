from aio2ch import File, Image, Sticker, Video

import os
import pytest
import tempfile


@pytest.mark.asyncio
async def test_get_thread_media(client, thread):
    thread_media = await client.get_thread_media(thread)

    assert len(thread_media) > 0
    assert all(isinstance(file, File) for file in thread_media)


@pytest.mark.asyncio
async def test_get_thread_media_just_images(client, thread):
    thread_media = await client.get_thread_media(thread, media_type=Image)

    assert len(thread_media) > 0
    assert all(isinstance(image, Image) for image in thread_media)


@pytest.mark.asyncio
async def test_get_thread_media_just_videos(client, thread):
    thread_media = await client.get_thread_media(thread, media_type=Video)

    assert len(thread_media) > 0
    assert all(isinstance(video, Video) for video in thread_media)


@pytest.mark.asyncio
async def test_get_thread_media_just_stickers(client, thread):
    thread_media = await client.get_thread_media(thread, media_type=Sticker)

    assert len(thread_media) > 0
    assert all(isinstance(sticker, Sticker) for sticker in thread_media)


@pytest.mark.asyncio
async def test_get_thread_media_images_and_videos(client, thread):
    media_type = (Image, Video)
    thread_media = await client.get_thread_media(thread, media_type=media_type)

    assert len(thread_media) > 0
    assert all(isinstance(media, media_type) for media in thread_media)


@pytest.mark.asyncio
async def test_get_thread_media_by_url(client, thread_url):
    thread_media = await client.get_thread_media(thread_url)

    assert len(thread_media) > 0
    assert all(isinstance(file, File) for file in thread_media)


@pytest.mark.asyncio
async def test_get_thread_media_with_status(client, thread):
    status, thread_media = await client.get_thread_media(thread, return_status=True)

    assert status >= 200
    assert len(thread_media) > 0
    assert all(isinstance(file, File) for file in thread_media)


@pytest.mark.asyncio
async def test_get_thread_media_with_status_by_url(client, thread_url):
    status, thread_media = await client.get_thread_media(thread_url, return_status=True)

    assert status >= 200
    assert len(thread_media) > 0
    assert all(isinstance(file, File) for file in thread_media)


@pytest.mark.asyncio
async def test_download_thread_media(client, thread_media):
    with tempfile.TemporaryDirectory() as temp_dir:
        await client.download_thread_media(files=thread_media, save_to=temp_dir)

        result = os.listdir(temp_dir)

        assert len(result) == len(thread_media)