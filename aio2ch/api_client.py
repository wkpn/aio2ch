from httpx import AsyncClient
from typing import (
    Any,
    Dict,
    Optional,
    Tuple
)
from types import FunctionType

from .helpers import API_URL


class ApiClient:
    __slots__ = '_api_url', '_client', '_json_loads'

    def __init__(self, api_url: Optional[str], json_loads: Optional[FunctionType] = None, **kwargs: Any):
        self._api_url: str = api_url or API_URL

        if json_loads:
            self._json_loads: FunctionType = json_loads
        else:
            from json import loads  # fallback to built-in library
            self._json_loads = loads
        self._client: AsyncClient = AsyncClient(**kwargs)

    async def request(self, method: str, url: str) -> Tuple[int, Dict]:
        """
        Request
        :param method:    request method
        :param url:       request url
        :return:          response with status code and json data on success
        """
        response = await self._client.request(method=method, url=url)

        json_data = self._json_loads(response.content)

        return response.status_code, json_data

    @property
    def client(self) -> AsyncClient:
        return self._client

    @property
    def api_url(self) -> str:
        return self._api_url

    @api_url.setter
    def api_url(self, api_url: str) -> None:
        self._api_url = api_url

    async def close(self) -> None:
        await self._client.aclose()

    def __repr__(self) -> str:  # pragma: nocover
        return f'<ApiClient api_url="{self._api_url}">'
