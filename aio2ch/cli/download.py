from .._api import Api
from .._objects import File, Image, Video, Sticker

from time import time
from typing import Tuple, Type

import asyncio
import click
import os


def convert_media_types(media_types: Tuple[str, ...]) -> Tuple[Type[File], ...]:
    types = set(_type.lower() for _type in media_types)

    mapping = {
        "images": Image,
        "videos": Video,
        "stickers": Sticker
    }

    return tuple(mapping[_type] for _type in types)


async def download_thread_media(thread_url: str,
                                download_folder: str,
                                media_type: Tuple[Type[File], ...]) -> None:
    async with Api(timeout=10.0) as api:
        thread_media = await api.get_thread_media(thread=thread_url, media_type=media_type)
        await api.download_thread_media(files=thread_media, save_to=download_folder)


@click.command()
@click.option("--thread-url", "-T",
              type=str,
              required=True,
              help="Thread url e.g. https://2ch.hk/b/res/219337088.html")
@click.option("--download-folder", "-D",
              type=str,
              default="./aio2ch-downloads",
              help="Where to save media. Defaults to ./aio2ch-downloads")
@click.argument("media-type",
                nargs=-1,
                required=True)
def download(thread_url: str, download_folder: str, media_type: Tuple[str, ...]) -> None:
    """
    Download media from a given thread url

    MEDIA_TYPE: can be `images`, `videos` or `stickers` in any combination

    Example usage: aio2ch -T https://2ch.hk/b/res/219337088.html images videos
    """
    if not os.path.isdir(download_folder):
        os.mkdir(download_folder)

    media_type = convert_media_types(media_type)

    click.echo(f"Downloading media to {download_folder}")

    start_time = time()
    asyncio.run(download_thread_media(thread_url, download_folder, media_type))
    run_time = time() - start_time

    files_in_dir = len(os.listdir(download_folder))

    click.echo(f"Finished in {run_time:.2f} seconds. Total files in {download_folder}: {files_in_dir}")
