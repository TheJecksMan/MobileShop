from fastapi import APIRouter
from .endpoint import product, category


api_router = APIRouter()

api_router.include_router(product.router, prefix="/product", tags=["products"])
api_router.include_router(category.router, prefix="/caregory", tags=["category"])
