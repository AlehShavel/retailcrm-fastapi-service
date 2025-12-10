import httpx

from core.config import settings


class RetailCRMClient:
    def __init__(self):
        self.base_url = settings.crm.api_base_url
        self.client = httpx.AsyncClient(
            headers={
                "X-API-KEY": settings.crm.api_key,
            }
        )

    async def get(self, path: str, params=None):
        url = f"{self.base_url}{path}"
        resp = await self.client.get(url, params=params)
        return resp.json()


crm = RetailCRMClient()
