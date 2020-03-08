from aio2ch.objects import Board, Thread, Image, Video, Sticker
from aio2ch import Api

import pytest


@pytest.fixture
async def client():
    api_client = Api(timeout=10.0)
    yield api_client
    await api_client.close()


@pytest.fixture
async def client_ujson():
    from ujson import loads as ujson_loads

    api_client = Api(json_loads=ujson_loads)
    yield api_client
    await api_client.close()


@pytest.fixture
async def client_orjson():
    from orjson import loads as orjson_loads

    api_client = Api(json_loads=orjson_loads)
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
def thread_as_number():
    return 30972


@pytest.fixture
def thread_url():
    return 'https://2ch.hk/test/res/30972.html'


@pytest.fixture
def invalid_thread():
    return 'invalid-thread'


@pytest.fixture
def invalid_board():
    return 'thisboarddoesntexist'


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


@pytest.fixture
def thread_media():
    image_data = {
        "displayname": "pnX1uujobqQ.jpg",
        "fullname": "pnX1uujobqQ.jpg",
        "height": 600,
        "md5": "50a7ca2ed41d00a0f49dd81bbc32074b",
        "name": "14989172638190.jpg",
        "nsfw": 0,
        "path": "/test/src/30972/14989172638190.jpg",
        "size": 62,
        "thumbnail": "/test/thumb/30972/14989172638190s.jpg",
        "tn_height": 250,
        "tn_width": 250,
        "type": 1,
        "width": 600
    }

    video_data = {
        "displayname": ".mp4",
        "duration": "00:04:35",
        "duration_secs": 275,
        "fullname": ".mp4",
        "height": 500,
        "md5": "8614c802cff48b420d54ed62a18fe21c",
        "name": "15752983961530.mp4",
        "nsfw": 0,
        "path": "/test/src/30972/15752983961530.mp4",
        "size": 5613,
        "thumbnail": "/test/thumb/30972/15752983961530s.jpg",
        "tn_height": 200,
        "tn_width": 200,
        "type": 10,
        "width": 500
    }

    sticker_data = {
        "displayname": "Стикер",
        "height": 512,
        "install": "/makaba/stickers/show/n5xSPtEw",
        "name": "lKfUbr3j.png",
        "pack": "n5xSPtEw",
        "path": "/stickers/n5xSPtEw/lKfUbr3j.png",
        "size": 383,
        "sticker": "lKfUbr3j",
        "thumbnail": "/stickers/n5xSPtEw/lKfUbr3j_thumb.png",
        "tn_height": 200,
        "tn_width": 200,
        "type": 100,
        "width": 512
    }

    return Image(image_data), Video(video_data), Sticker(sticker_data)
