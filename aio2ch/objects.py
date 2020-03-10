from typing import Any, Dict, Optional, Union

from .helpers import clean_html_tags


def cast_file_data_to_object(file: Dict[str, Any]):
    types = {
        1: Image,
        2: Image,
        4: Image,
        6: Video,
        10: Video,
        100: Sticker
    }
    file_type = file['type']

    return types[file_type](file)


class Board:
    __slots__ = ('bump_limit', 'category', 'default_name',
                 'id', 'info', 'name', 'threads')

    def __init__(self, board: Dict[str, Any]):
        self.bump_limit = board['bump_limit']
        self.category = board['category']
        self.default_name = board['default_name']
        self.id = board['id']
        self.info = board['info']
        self.name = board['name']
        self.threads = board['threads']

    def __repr__(self):  # pragma: nocover
        return f'<Board name="{self.name}", id="{self.id}">'


class Thread:
    __slots__ = ('board', 'comment', 'num', 'posts_count',
                 'score', 'subject', 'timestamp', 'views')

    def __init__(self, thread: Dict[str, Any], board: Optional[Union[Dict[str, Any], str]] = None):
        self.board = board.id if isinstance(board, Board) else board
        self.comment = clean_html_tags(thread['comment'])
        self.num = thread['num']
        self.posts_count = thread['posts_count']
        self.score = thread['score']
        self.subject = clean_html_tags(thread['subject'])
        self.timestamp = thread['timestamp']
        self.views = thread['views']

    def __repr__(self):  # pragma: nocover
        return f'<Thread num="{self.num}">'


class Post:
    __slots__ = ('banned', 'closed', 'comment', 'endless',
                 'files', 'name', 'num', 'number', 'op',
                 'parent', 'subject', 'timestamp')

    def __init__(self, post: Dict[str, Any]):
        self.banned = post['banned']
        self.closed = post['closed']
        self.comment = clean_html_tags(post['comment'])
        self.endless = post['endless']
        self.files = tuple(cast_file_data_to_object(file) for file in post['files'])
        self.name = post['name']
        self.num = post['num']
        self.number = post['number']
        self.op = post['op']
        self.parent = post['parent']
        self.subject = clean_html_tags(post['subject'])
        self.timestamp = post['timestamp']

    def __repr__(self):  # pragma: nocover
        return f'<Post num="{self.num}">'


class File:
    __slots__ = ('displayname', 'height', 'name', 'path',
                 'size', 'thumbnail', 'tn_height', 'tn_width',
                 'type', 'width')  # common fields

    def __init__(self, file: Dict[str, Any]):
        self.displayname = file['displayname']
        self.height = file['height']
        self.name = file['name']
        self.path = file['path']
        self.size = file['size']
        self.thumbnail = file['thumbnail']
        self.tn_height = file['tn_height']
        self.tn_width = file['tn_width']
        self.type = file['type']
        self.width = file['width']

    def __repr__(self):  # pragma: nocover
        return f'<{self.__class__.__name__} name="{self.name}", path="{self.path}", size="{self.size}">'


class Image(File):
    __slots__ = ('fullname', 'md5', 'nsfw')

    def __init__(self, file: Dict[str, Any]):
        super().__init__(file)

        self.fullname = file['fullname']
        self.md5 = file['md5']
        self.nsfw = file['nsfw']


class Video(Image):
    __slots__ = ('duration', 'duration_secs')

    def __init__(self, file: Dict[str, Any]):
        super().__init__(file)

        self.duration = file['duration']
        self.duration_secs = file['duration_secs']


class Sticker(File):
    __slots__ = ('install', 'pack', 'sticker')

    def __init__(self, file: Dict[str, Any]):
        super().__init__(file)

        self.install = file['install']
        self.pack = file['pack']
        self.sticker = file['sticker']
