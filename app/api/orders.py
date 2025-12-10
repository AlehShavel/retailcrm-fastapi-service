import json

from fastapi import APIRouter

from core.config import settings
from schemas.orders import OrderCreate
from services.retailcrm import crm

router = APIRouter(prefix=settings.api.orders, tags=["Orders"])


@router.get("/")
async def get_orders(customer_id: int) -> list:
    filters = {
        "filter[customerId]": customer_id,
    }
    data = await crm.get(
        path=settings.crm.api.orders,
        params=filters,
    )
    return data.get("orders", [])


@router.post("/")
async def create_order(order: OrderCreate) -> dict:
    order_data = {
        "customer": {
            "id": order.customer_id,
        },
        "items": [{"offer": {"externalId": item_id}} for item_id in order.item_ids],
        "number": order.number,
    }
    data = {"order": json.dumps(order_data)}
    return await crm.post(path=f"{settings.crm.api.orders}/create", data=data)
