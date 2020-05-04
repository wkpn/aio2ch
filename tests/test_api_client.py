from json import loads as json_loads

import pytest


try:
    from ujson import loads as ujson_loads
except ImportError:
    ujson_loads = None


try:
    from orjson import loads as orjson_loads
except ImportError:
    orjson_loads = None


@pytest.mark.asyncio
async def test_api_client_url(client):
    assert client._api_client._api_url == "https://2ch.hk"


@pytest.mark.asyncio
async def test_api_client_url_changed(client):
    client._api_client.api_url = "https://2ch.pm"

    assert client._api_client._api_url == "https://2ch.pm"


@pytest.mark.asyncio
async def test_api_client_loads_function_is_default_json_loads(client):
    assert client._api_client._json_loads == json_loads


@pytest.mark.asyncio
@pytest.mark.skipif(ujson_loads is None, reason="ujson is not installed")
async def test_api_client_ujson_loads_function(client_ujson):
    assert client_ujson._api_client._json_loads == ujson_loads


@pytest.mark.asyncio
@pytest.mark.skipif(orjson_loads is None, reason="orjson is not installed")
async def test_api_client_orjson_loads_function(client_orjson):
    assert client_orjson._api_client._json_loads == orjson_loads
