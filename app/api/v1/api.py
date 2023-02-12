"""Routing with base path /api"""
from fastapi import APIRouter
from api.v1.endpoint import product, category, mail


api_router = APIRouter()

api_router.include_router(product.router, prefix="/product", tags=["products"])
api_router.include_router(category.router, prefix="/caregories", tags=["category"])
api_router.include_router(mail.router, prefix="/mail", tags=["mail"])
