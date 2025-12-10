from pydantic import BaseModel


class Product(BaseModel):
    name: str


class OrderCreate(BaseModel):
    customer_id: int
    item_ids: list[int]
    number: str
