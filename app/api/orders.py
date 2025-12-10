from fastapi import APIRouter

from core.config import settings
from services.retailcrm import crm

router = APIRouter(prefix=settings.api.orders, tags=["Orders"])


@router.get("/")
async def get_orders(customer_id: int):
    filters = {
        "filter[customerId]": customer_id,
    }
    data = await crm.get(
        path=settings.crm.api.orders,
        params=filters,
    )
    return data.get("orders", [])
