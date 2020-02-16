__all__ = 'Api'

from .exceptions import NoBoardProvidedException, WrongSortMethodException
from .objects import Board, File, Post, Thread
from .settings import API_URL, SORTING_METHODS

from typing import Any, Dict, List, Optional, Tuple, Type, Union
from types import TracebackType

from httpx import AsyncClient

import aiofiles
import asyncio


class Api:
    __slots__ = ('_api_url', '__client')

    def __init__(self, api_url: Optional[str] = None):
        if api_url:
            self._api_url = api_url
        else:
            self._api_url = API_URL

        self.__client: AsyncClient = AsyncClient()

    @property
    def api_url(self) -> str:
        return self._api_url

    @api_url.setter
    def api_url(self, api_url: str) -> None:
        self._api_url = api_url

    async def get_boards(self,
                         return_status: Optional[bool] = False
                         ) -> Union[Tuple[int, List[Board]], List[Board]]:
        status, boards = await self._get(url=f'{self.api_url}/makaba/mobile.fcgi?task=get_boards')
        boards = [Board(board) for board in sum(boards.values(), [])]

        if return_status:
            return status, boards
        return boards

    async def get_board_threads(self,
                                board: Union[str, Board],
                                keywords: Optional[List[str]] = None,
                                return_status: Optional[bool] = False
                                ) -> Union[Tuple[int, List[Thread]], List[Thread]]:
        if isinstance(board, Board):
            board = board.id

        status, threads = await self._get(url=f'{self.api_url}/{board}/threads.json')
        threads = threads['threads']
        threads = [Thread(thread, board) for thread in threads]

        if keywords:
            keywords = [keyword.lower() for keyword in keywords]
            threads = [thread for thread in threads if any(k in thread.comment.lower() for k in keywords)]

        if return_status:
            return status, threads
        return threads

    async def get_top_board_threads(self,
                                    board: str,
                                    method: str,
                                    num: int = 5,
                                    return_status: Optional[bool] = False
                                    ) -> Union[Tuple[int, List[Thread]], List[Thread]]:
        if method not in SORTING_METHODS:
            raise WrongSortMethodException(f'Cannot sort threads using {method} method')

        if isinstance(board, Board):
            board = board.id

        result = await self.get_board_threads(board, return_status=return_status)

        if isinstance(result, tuple):
            status, board_threads = result
        else:
            board_threads = result

        if method == 'views':
            board_threads = sorted(board_threads, key=lambda t: (t.views, t.score), reverse=True)
        elif method == 'score':
            board_threads = sorted(board_threads, key=lambda t: (t.score, t.views), reverse=True)
        elif method == 'posts':
            board_threads = sorted(board_threads, key=lambda t: (t.posts_count, t.views), reverse=True)

        if return_status:
            return status, board_threads[:num]
        return board_threads[:num]

    async def get_thread_posts(self,
                               thread: Union[int, str, Thread],
                               board: Optional[Union[str, Board]] = None,
                               return_status: Optional[bool] = False
                               ) -> Union[Tuple[int, List[Post]], List[Post]]:
        if isinstance(thread, Thread):
            board = thread.board
            thread = thread.num
        if isinstance(board, Board):
            board = board.name
        elif not board:
            raise NoBoardProvidedException('Board id is not provided')

        status, posts = await self._get(url=f'{self.api_url}/{board}/res/{thread}.json')
        posts = posts['threads'][0]['posts']
        posts = [Post(post) for post in posts]

        if return_status:
            return status, posts
        return posts

    async def get_thread_media(self,
                               thread: Union[int, str, Thread],
                               board: Optional[Union[str, Board]] = None,
                               return_status: Optional[bool] = False
                               ) -> Union[Tuple[int, List[File]], List[File]]:
        result = await self.get_thread_posts(thread, board=board, return_status=return_status)

        if isinstance(result, tuple):
            status, posts = result
        else:
            posts = result

        files = sum((post.files for post in posts if post.files), [])

        if return_status:
            return status, files
        return files

    async def download_thread_media(self,
                                    files: List[File],
                                    save_to: str,
                                    bound: Optional[int] = 10) -> None:
        async def download(client, semaphore, file):
            async with semaphore:
                filename = f'{save_to}/{file.name}'
                url = f'{self.api_url}{file.path}'

                async with aiofiles.open(filename, 'wb') as download_file:
                    async with client.stream('GET', url) as stream:
                        async for chunk in stream.aiter_bytes():
                            await download_file.write(chunk)

        semaphore = asyncio.Semaphore(bound)
        download_tasks = (download(self.__client, semaphore, file) for file in files)

        await asyncio.gather(*download_tasks)

    async def _get(self, url, **kwargs: Any) -> Tuple[int, Dict]:
        response = await self.__client.get(url, **kwargs)
        return response.status_code, response.json()

    async def close(self) -> None:
        await self.__client.aclose()

    async def __aenter__(self) -> 'Api':
        return self

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]) -> None:
        await self.close()
