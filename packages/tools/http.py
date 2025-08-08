import httpx


class HTTPTool:
    """Simple HTTP/GraphQL client."""

    async def get(self, url: str, headers: dict | None = None, params: dict | None = None) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response

    async def post(self, url: str, json: dict | None = None, headers: dict | None = None) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=json, headers=headers)
            response.raise_for_status()
            return response