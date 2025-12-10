from datetime import date

from fastapi import APIRouter

from core.config import settings
from services.retailcrm import crm

router = APIRouter(prefix=settings.api.customers, tags=["Customers"])


@router.get("/")
async def get_customers(
    name: str | None = None,
    email: str | None = None,
    date_gte: date | None = None,
    date_lte: date | None = None,
) -> list:
    filters = {
        "filter[name]": name,
        "filter[email]": email,
        "filter[dateFrom]": date_gte.isoformat() if date_gte else None,
        "filter[dateTo]": date_lte.isoformat() if date_lte else None,
    }
    filters = {key: value for key, value in filters.items() if value is not None}

    data = await crm.get(
        path=settings.crm.api.customers,
        params=filters,
    )

    return data.get("customers", [])
