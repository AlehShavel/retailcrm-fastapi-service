import json

from fastapi import APIRouter

from core.config import settings
from schemas.orders import OrderCreate, PaymentCreate
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


@router.post("/payments/create")
async def create_payment(payment: PaymentCreate) -> dict:
    payment_data = {
        "order": {"id": payment.order_id},
        "amount": str(payment.amount),
        "comment": payment.comment,
        "type": payment.type,
    }
    data = {"payment": json.dumps(payment_data)}
    return await crm.post(path=f"{settings.crm.api.orders}/payments/create", data=data)
