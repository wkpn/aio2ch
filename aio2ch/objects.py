class Board:
    __slots__ = ('bump_limit', 'category', 'default_name',
                 'icons', 'id', 'name', 'pages', 'sage')

    def __init__(self, board):
        self.bump_limit = board['bump_limit']
        self.category = board['category']
        self.default_name = board['default_name']
        self.icons = board['icons']
        self.id = board['id']
        self.name = board['name']
        self.pages = board['pages']
        self.sage = board['sage']

    def __repr__(self):
        return '<Board name: %s, id: %s>' % (self.name, self.id)


class Thread:
    __slots__ = ('board', 'comment', 'num', 'posts_count',
                 'score', 'subject', 'timestamp', 'views')

    def __init__(self, thread, board):
        self.board = board
        self.comment = thread['comment']
        self.num = thread['num']
        self.posts_count = thread['posts_count']
        self.score = thread['score']
        self.subject = thread['subject']
        self.timestamp = thread['timestamp']
        self.views = thread['views']

    def __repr__(self):
        return '<Thread %s>' % self.num


class Post:
    __slots__ = ('banned', 'closed', 'comment', 'endless',
                 'files', 'name', 'num', 'number', 'op',
                 'parent', 'subject', 'timestamp')

    def __init__(self, post):
        self.banned = post['banned']
        self.closed = post['closed']
        self.comment = post['comment']
        self.endless = post['endless']
        self.files = [File(file) for file in post['files']]
        self.name = post['name']
        self.num = post['num']
        self.number = post['number']
        self.op = post['op']
        self.parent = post['parent']
        self.subject = post['subject']
        self.timestamp = post['timestamp']

    def __repr__(self):
        return '<Post %s>' % self.num


class File:
    __slots__ = ('displayname', 'name', 'path', 'size')

    def __init__(self, file):
        self.displayname = file['displayname']
        self.name = file['name']
        self.path = file['path']
        self.size = file['size']

    def __repr__(self):
        return '<File name:%s, path:%s, size:%s>' % (self.name, self.path, self.size)
