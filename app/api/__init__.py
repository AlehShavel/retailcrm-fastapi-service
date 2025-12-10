from fastapi import APIRouter

from api.customers import router as customers_router
from core.config import settings

router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(customers_router)
