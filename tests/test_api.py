import pytest


@pytest.mark.asyncio
async def test_api_url(client):
    assert client._api_client.api_url == 'https://2ch.hk'


@pytest.mark.asyncio
async def test_api_url_changed(client):
    client._api_client.api_url = 'https://2ch.pm'

    assert client._api_client._api_url == 'https://2ch.pm'
