import pytest


try:
    import ujson
except ImportError:
    ujson = None


try:
    import orjson
except ImportError:
    orjson = None


@pytest.mark.asyncio
async def test_api_client_url(client):
    assert client._api_client.api_url == 'https://2ch.hk'


@pytest.mark.asyncio
async def test_api_client_url_changed(client):
    client._api_client.api_url = 'https://2ch.pm'

    assert client._api_client._api_url == 'https://2ch.pm'


@pytest.mark.asyncio
async def test_api_client_loads_function_is_default_json_loads(client):
    from json import loads

    assert client._api_client._json_loads == loads


@pytest.mark.asyncio
@pytest.mark.skipif(ujson is None, reason='ujson is not installed')
async def test_api_client_ujson_loads_function(client_ujson):
    from ujson import loads

    assert client_ujson._api_client._json_loads == loads


@pytest.mark.asyncio
@pytest.mark.skipif(orjson is None, reason='orson is not installed')
async def test_api_client_orjson_loads_function(client_orjson):
    from orjson import loads

    assert client_orjson._api_client._json_loads == loads
