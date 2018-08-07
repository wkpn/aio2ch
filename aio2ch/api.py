__all__ = 'Api'

from .objects import *
from .settings import *
from .exceptions import *
import aiohttp


class Api:
    def __init__(self, api_url=None):
        if api_url:
            self.url = api_url
        else:
            self.url = API_URL

    @property
    def api_url(self):
        return self.url

    @api_url.setter
    def api_url(self, api_url):
        self.url = api_url

    async def get_boards(self):
        status, result = await self.get(url='%s/makaba/mobile.fcgi?task=get_boards' % self.api_url)

        return status, [Board(board) for board in sum(result.values(), [])]

    async def get_board_threads(self, board):
        if isinstance(board, Board):
            board = board.id

        status, result = await self.get(url='%s/%s/threads.json' % (self.api_url, board))
        return status, [Thread(thread, board) for thread in result['threads']]

    async def get_top_board_threads(self, board, method, num=5):
        if method not in SORTING_METHODS:
            raise WrongSortMethodException('Cannot sort using %s method' % method)

        if isinstance(board, Board):
            board = board.id

        status, result = await self.get_board_threads(board)

        if method == 'views':
            top_threads = sorted(result, key=lambda thread: (thread.views, thread.score), reverse=True)
        elif method == 'score':
            top_threads = sorted(result, key=lambda thread: (thread.score, thread.views), reverse=True)
        elif method == 'posts':
            top_threads = sorted(result, key=lambda thread: (thread.posts_count, thread.views), reverse=True)
        else:
            return []

        return status, [thread for thread in top_threads[:num]]

    async def get_thread_posts(self, thread, board=None):
        if isinstance(thread, Thread):
            board = thread.board
            thread = thread.num
        elif not board:
            raise NoBoardProvidedException('Board is not provided')

        status, result = await self.get(url='%s/%s/res/%s.json' % (self.url, board, thread))

        return status, [Post(post) for post in result['threads'][0]['posts']]

    async def get_thread_media(self, thread, board=None):
        status, posts = await self.get_thread_posts(thread, board=board)

        return status, sum((post.files for post in posts if post.files), [])

    async def get(self, url, **kwargs):
        return await self._request('get', url, **kwargs)

    @staticmethod
    async def _request(method, url, **kwargs):
        async with aiohttp.ClientSession() as session:
            method_func = getattr(session, method)

            async with method_func(url, **kwargs) as response:
                return response.status, await response.json()


