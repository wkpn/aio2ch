class Board:
    __slots__ = ('bump_limit', 'category', 'default_name',
                 'id', 'info', 'name', 'threads')

    def __init__(self, board):
        self.bump_limit = board['bump_limit']
        self.category = board['category']
        self.default_name = board['default_name']
        self.id = board['id']
        self.info = board['info']
        self.name = board['name']
        self.threads = board['threads']

    def __repr__(self):
        return f'<Board name: {self.name}, id: {self.id}>'


class Thread:
    __slots__ = ('board', 'comment', 'num', 'posts_count',
                 'score', 'subject', 'timestamp', 'views')

    def __init__(self, thread, board=None):
        self.board = board.id if isinstance(board, Board) else board
        self.comment = thread['comment']
        self.num = thread['num']
        self.posts_count = thread['posts_count']
        self.score = thread['score']
        self.subject = thread['subject']
        self.timestamp = thread['timestamp']
        self.views = thread['views']

    def __repr__(self):
        return f'<Thread {self.num}>'


class Post:
    __slots__ = ('banned', 'closed', 'comment', 'endless',
                 'files', 'name', 'num', 'number', 'op',
                 'parent', 'subject', 'timestamp')

    def __init__(self, post):
        self.banned = post['banned']
        self.closed = post['closed']
        self.comment = post['comment']
        self.endless = post['endless']
        self.files = tuple(File(file) for file in post['files'])
        self.name = post['name']
        self.num = post['num']
        self.number = post['number']
        self.op = post['op']
        self.parent = post['parent']
        self.subject = post['subject']
        self.timestamp = post['timestamp']

    def __repr__(self):
        return f'<Post {self.num}>'


class File:
    __slots__ = ('displayname', 'name', 'path', 'size')

    def __init__(self, file):
        self.displayname = file['displayname']
        self.name = file['name']
        self.path = file['path']
        self.size = file['size']

    def __repr__(self):
        return f'<File name: {self.name}, path: {self.path}, size: {self.size}>'
