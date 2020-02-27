from typing import Tuple, Union

import re


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


def get_board_and_thread_from_url(thread_url: str) -> Union[Tuple[str, str], Tuple[None, None]]:
    # https://2ch.hk/test/res/30972.html

    pattern = 'https://[2a-z]+.[a-z]+/[a-z]+/res/[0-9]+.html'
    match = re.compile(pattern).match(thread_url)

    if match:
        split = re.split('[/.]', thread_url)
        board, thread = split[4], split[6]

        return board, thread

    return None, None
