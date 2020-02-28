from aio2ch.objects import Board, Thread
from aio2ch import Api

import pytest


@pytest.fixture
async def client():
    api_client = Api()
    yield api_client
    await api_client.close()


@pytest.fixture
def board():
    test_board_data = {
        'bump_limit': '',
        'category': '',
        'default_name': '',
        'id': 'test',
        'info': '',
        'name': 'test',
        'threads': ''
    }

    return Board(test_board_data)


@pytest.fixture
def thread():
    test_thread_data = {
        'comment': '',
        'num': 30972,
        'posts_count': '',
        'score': '',
        'subject': '',
        'timestamp': '',
        'views': ''
    }
    test_board = 'test'

    return Thread(test_thread_data, test_board)


@pytest.fixture
def thread_url():
    return 'https://2ch.hk/test/res/30972.html'


@pytest.fixture
def invalid_thread_url():
    return 'https://dvach.hk/blah/blah/blah.css'


@pytest.fixture
def number_of_threads(number=5):
    return number


@pytest.fixture
def raw_text():
    return 'КУКУ ТАМ ОНЛИФЕНС СЛИЛИ, ЕСТЬ ЧТО У КОГО?<br>' \
           '<a href=\"https:&#47;&#47;tjournal.ru&#47;internet&#47;146526-v-set-popali-terabayty-' \
           'dannyh-onlyfans-sayta-gde-pornozvezdy-i-modeli-razmeshchayut-platnye-eroticheskie-foto-i-video\" ' \
           'target=\"_blank\" rel=\"nofollow noopener noreferrer\">https:&#47;&#47;tjournal.ru&#47;internet&#47;' \
           '146526-v-set-popali-terabayty-dannyh-onlyfans-sayta-gde-pornozvezdy-i-modeli-razmeshchayut-platnye-' \
           'eroticheskie-foto-i-video</a><br><br>Давайте братья скажите где скачать эти терабайты'


@pytest.fixture
def clean_text():
    return 'КУКУ ТАМ ОНЛИФЕНС СЛИЛИ, ЕСТЬ ЧТО У КОГО?\n' \
           'https://tjournal.ru/internet/146526-v-set-popali-terabayty-dannyh-onlyfans-' \
           'sayta-gde-pornozvezdy-i-modeli-razmeshchayut-platnye-eroticheskie-foto-i-video\n\n' \
           'Давайте братья скажите где скачать эти терабайты'
