from typing import Tuple

import re


API_URL = 'https://2ch.hk'

BOARDS_LIST: Tuple = (
    'b', 'vg', 'po', 'fag', 'news', '2d', 'v', 'hw', 'sex', 'a', 'au', 'biz', 'wm', 'soc', 'wrk', 'rf', 'pr',
    'brg', 'me', 'mobi', 'kpop', 'c', 'w', 'hi', 'mov', 'fiz', 'ftb', 'sp', 'cg', 'ma', 'hry', 'dr', 'tes',
    's', 'alco', 'ra', 'obr', 'em', 'di', 'gsg', 'ch', 'mlp', 'mus', 'fa', 'ga', 'fs', 'zog', 'psy', 'whn',
    'bi', 'by', 'fg', 'fet', 'tv', 'un', 'fd', 'mu', 'ukr', 'pa', 'qtr4', 'fl', 'mg', 're', 'gd', 'bo', 'sn',
    'spc', 't', 'd', 'ew', 'dom', 'wh', 'td', 'mc', 'mmo', 'fur', 'e', 'asmr', 'vape', 'sci', 'tr', 'p', 'gg',
    'cul', 'out', 'sw', 'pok', 'es', 'diy', 'trv', 'hc', 'media', 'jsf', 'wow', 'cute', 'kz', 'socionics', 'o',
    'ruvn', 'izd', 'wr', 'r', 'h', 'moba', 'cc', 'gabe', 'se', 'wwe', 'int', 'hh', 'mo', 'ne', 'pvc', 'ph', 'sf',
    'de', 'wp', 'bg', 'aa', 'ja', 'rm', 'to', 'vn', 'ho', 'web', 'br', 'gb', 'abu', 'old', 'guro', 'ussr', 'law',
    'm', 'ya', 'r34', '8', 'mlpr', 'ro', 'who', 'srv', 'electrach', 'ing', 'got', 'crypt', 'lap', 'smo', 'hg',
    'sad', 'fi', 'nvr', 'ind', 'ld', 'fem', 'vr', 'arg', 'char', 'hv', 'math', 'catalog', 'api', 'test'
)

SORTING_METHODS: Tuple = ('views', 'score', 'posts_count')


def is_url_like(thread: str) -> bool:
    pattern = 'https://[2a-z]+.[a-z]+/[a-z]+/res/[0-9]+.html'
    match = re.compile(pattern).match(thread)

    return True if match else False


def get_board_and_thread_from_url(thread_url: str) -> Tuple[str, str]:
    # https://2ch.hk/test/res/30972.html

    split = re.split('[/.]', thread_url)
    board, thread = split[4], split[6]

    return board, thread


def clean_html_tags(raw_text: str) -> str:
    if not raw_text:  # if no text e.g. empty string
        return raw_text

    clean_text = re.sub('<br>', '\n', raw_text)
    clean_text = re.sub('&quot;', '"', clean_text)
    clean_text = re.sub('&#47;', '/', clean_text)

    tags_matcher = re.compile('<.*?>')
    clean_text = re.sub(tags_matcher, '', clean_text)

    return clean_text
