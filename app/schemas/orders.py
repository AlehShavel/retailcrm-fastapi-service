from decimal import Decimal

from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_id: int
    item_ids: list[int]
    number: str


class PaymentCreate(BaseModel):
    order_id: int
    amount: Decimal
    comment: str
    type: str
