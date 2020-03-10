__all__ = 'Api'

from .exceptions import (
    InvalidBoardIdException,
    InvalidThreadException,
    NoBoardProvidedException,
    WrongSortMethodException
)
from .objects import (
    Board,
    File,
    Post,
    Thread
)
from .helpers import (
    BOARDS_LIST,
    SORTING_METHODS,
    is_url_like,
    get_board_and_thread_from_url
)
from .api_client import ApiClient

from typing import (
    Any,
    Dict,
    Iterable,
    Optional,
    Tuple,
    Type,
    Union
)
from types import FunctionType, TracebackType

import aiofiles
import asyncio


class Api:
    __slots__ = '_api_client'

    def __init__(self, api_url: Optional[str] = None, json_loads: Optional[FunctionType] = None, **kwargs: Any):
        """
        main API class
        :param api_url:     main API endpoint. can be any of these: 2ch.hk, 2ch.pm (rest are redirects to 2ch.hk)
        :param json_loads:  custom json loads function for content decoding (default is json.loads)
        :param kwargs:      any additional args you want to pass to the client e.g. proxies or headers
        """

        self._api_client: ApiClient = ApiClient(api_url=api_url, json_loads=json_loads, **kwargs)

    async def get_boards(self,
                         return_status: Optional[bool] = False
                         ) -> Union[Tuple[int, Tuple[Board]], Tuple[Board]]:
        """
        get boards
        :param return_status:   whether to return status code or not
        :return:                status code (optional) and tuple of Boards
        """

        status, boards = await self._get(url=f'{self._api_client.api_url}/boards.json')
        boards = boards['boards']
        boards = tuple(Board(board) for board in boards)

        if return_status:
            return status, boards
        return boards

    async def get_board_threads(self,
                                board: Union[str, Board],
                                keywords: Optional[Iterable[str]] = None,
                                return_status: Optional[bool] = False
                                ) -> Union[Tuple[int, Tuple[Thread]], Tuple[Thread]]:
        """
        get board threads
        :param board:           board to search threads in
        :param keywords:        specific keywords that should be in thread
        :param return_status:   whether to return status code or not
        :return:                status code (optional) and/or tuple of Threads
        """

        if isinstance(board, Board):
            board = board.id

        if board not in BOARDS_LIST:
            raise InvalidBoardIdException(f'Board {board} doesn\'t exist')

        status, threads = await self._get(url=f'{self._api_client.api_url}/{board}/threads.json')
        threads = threads['threads']
        threads = tuple(Thread(thread, board) for thread in threads)

        if keywords:
            keywords = tuple(keyword.lower() for keyword in keywords)
            threads = tuple(thread for thread in threads if any(k in thread.comment.lower() for k in keywords))

        if return_status:
            return status, threads
        return threads

    async def get_top_board_threads(self,
                                    board: Union[str, Board],
                                    method: str,
                                    num: Optional[int] = 5,
                                    return_status: Optional[bool] = False
                                    ) -> Union[Tuple[int, Tuple[Thread]], Tuple[Thread]]:
        """
        get top board threads
        :param board:           board to search threads in
        :param method:          sort method ('views', 'score', or 'posts_count')
        :param num:             how many threads to return
        :param return_status:   whether to return status code or not
        :return:                status code (optional) and/or tuple of Threads
        """

        if method not in SORTING_METHODS:
            raise WrongSortMethodException(f'Cannot sort threads using {method} method')

        if isinstance(board, Board):
            board = board.id

        if board not in BOARDS_LIST:
            raise InvalidBoardIdException(f'Board {board} doesn\'t exist')

        result = await self.get_board_threads(board, return_status=return_status)

        if return_status:
            status, board_threads = result
        else:
            board_threads = result

        if method == 'views':
            board_threads = sorted(board_threads, key=lambda t: (t.views, t.score), reverse=True)
        elif method == 'score':
            board_threads = sorted(board_threads, key=lambda t: (t.score, t.views), reverse=True)
        elif method == 'posts_count':
            board_threads = sorted(board_threads, key=lambda t: (t.posts_count, t.views), reverse=True)

        board_threads = tuple(board_threads[:num])

        if return_status:
            return status, board_threads
        return board_threads

    async def get_thread_posts(self,
                               thread: Union[int, str, Thread],
                               board: Optional[Union[str, Board]] = None,
                               return_status: Optional[bool] = False
                               ) -> Union[Tuple[int, Tuple[Post]], Tuple[Post]]:
        """
        get thread posts
        :param thread:          thread to get posts from
        :param board:           optional, needed if thread passes as int or str
        :param return_status:   whether to return status code or not
        :return:                status code (optional) and/or tuple of Posts
        """

        if isinstance(thread, Thread):
            board = thread.board
            thread = thread.num
        elif isinstance(thread, str):
            if is_url_like(thread):
                board, thread = get_board_and_thread_from_url(thread)
            else:
                try:
                    int(thread)
                except ValueError:
                    raise InvalidThreadException(f'Invalid thread {thread}')
        elif isinstance(board, Board):
            board = board.id
        elif not board:
            raise NoBoardProvidedException('Board id is not provided')

        if board not in BOARDS_LIST:
            raise InvalidBoardIdException(f'Board {board} doesn\'t exist')

        status, posts = await self._get(url=f'{self._api_client.api_url}/{board}/res/{thread}.json')
        posts = posts['threads'][0]['posts']
        posts = tuple(Post(post) for post in posts)

        if return_status:
            return status, posts
        return posts

    async def get_thread_media(self,
                               thread: Union[int, str, Thread],
                               board: Optional[Union[str, Board]] = None,
                               media_type: Optional[Union[Type[File], Tuple[Type[File]]]] = None,
                               return_status: Optional[bool] = False
                               ) -> Union[Tuple[int, Tuple[File]], Tuple[File]]:
        """
        get thread media (webms, mp4, pictures etc.)
        :param thread:          thread to get media from
        :param board:           optional, needed if thread passes as int or str
        :param media_type:      optional, get specific media type e.g. Images, Videos or Sticker
        :param return_status:   whether to return status code or not
        :return:                status code (optional) and/or tuple of Files
        """

        result = await self.get_thread_posts(thread, board=board, return_status=return_status)

        if return_status:
            status, posts = result
        else:
            posts = result

        files = sum((post.files for post in posts if post.files), ())

        if media_type:
            files = tuple(file for file in files if isinstance(file, media_type))

        if return_status:
            return status, files
        return files

    async def download_thread_media(self,
                                    files: Iterable[File],
                                    save_to: str,
                                    bound: Optional[int] = 10) -> None:
        """
        download thread media to a folder on a disk
        :param files:           iterable with Files (e.g. can be list or tuple with Files)
        :param save_to:         folder on a disk
        :param bound:           concurrent connections limit
        """

        async def download(api_client, semaphore, file):
            async with semaphore:
                filename = f'{save_to}/{file.name}'
                url = f'{api_client.api_url}{file.path}'

                async with aiofiles.open(filename, 'wb') as download_file:
                    async with api_client.client.stream('GET', url) as stream:
                        async for chunk in stream.aiter_bytes():
                            await download_file.write(chunk)

        semaphore = asyncio.Semaphore(bound)
        download_tasks = (download(self._api_client, semaphore, file) for file in files)

        await asyncio.gather(*download_tasks)

    async def _get(self, url: str) -> Tuple[int, Dict]:
        status_code, json_data = await self._api_client.request(method='GET', url=url)
        return status_code, json_data

    async def close(self) -> None:
        await self._api_client.close()

    async def __aenter__(self) -> 'Api':  # pragma: nocover
        return self

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]) -> None:  # pragma: nocover
        await self.close()

    def __repr__(self) -> str:  # pragma: nocover
        return f'<Api api_url="{self._api_client.api_url}">'
