from typing import Any, Dict, Optional, Tuple
from httpx import AsyncClient

from .settings import API_URL


class ApiClient:
    def __init__(self, api_url: Optional[str], **kwargs: Any):
        """
        ApiClient
        :param api_url:   main API endpoint. can be any of these: 2ch.hk, 2ch.pm (rest are redirects to 2ch.hk)
        :param kwargs:    any additional args you want to pass to the client e.g. proxies
        """
        self._api_url: str = API_URL if not api_url else api_url
        self.client: AsyncClient = AsyncClient(**kwargs)

    async def request(self, method: str, url: str, **kwargs: Any) -> Tuple[int, Dict]:
        """
        Request
        :param method:    request method
        :param url:       request url
        :param kwargs:    any additional args you want to pass e.g. headers, cookies etc.
        :return:          response with status code and json data on success
        """
        response = await self.client.request(method=method, url=url, **kwargs)

        return response.status_code, response.json()

    @property
    def api_url(self) -> str:
        return self._api_url

    @api_url.setter
    def api_url(self, api_url: str) -> None:
        self._api_url = api_url

    async def close(self) -> None:
        await self.client.aclose()
