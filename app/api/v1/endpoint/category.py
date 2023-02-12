"""
API implementation module for categories.
/api/caregories
"""
from typing import Any
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from modules.database.deps import get_session

from modules.database.plugins.orm import orm_category
from modules.database.plugins.scheme import scheme_category as scheme


router = APIRouter()


@router.get("/all", response_model=scheme.AdvancedCategory)
async def get_all_categories(
    page: int = None,
    limit: int = None,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """
    Получение списка всех доступный родительских катологов
    """
    category = await orm_category.get_all_categories(page, limit, db_session)
    return scheme.AdvancedCategory(items=category)


@router.get("/parent/{category_id}", response_model=list[scheme.ParentCategory])
async def get_parent_categories(
    category_id: int,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """
    Получение информации о доступных подгатегориях
    """
    parent_categories = await orm_category.get_parent_categories(category_id, db_session)
    return parent_categories


@router.get("/{category_id}/product", response_model=scheme.AdvancedProduct)
async def get_product_category(
    category_id: int,
    page: int,
    limit: int = 10,
    sort_date: int = None,
    sort_price: int = None,
    sort_name: int = None,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """
    Получения всего списка товаров из категории
    ----
    Сортировки принимают только значения -1 и  1!\n
    -1 - по убыванию\n
    1 -  по возрастанию
    """
    category_product = await orm_category.get_product_by_category(
        category_id, page, limit, db_session, sort_date, sort_price, sort_name)
    return scheme.AdvancedProduct(items=category_product)


@router.get('/search/{search_text}', response_model=scheme.AdvancedCategory)
async def categories_search(
    search_text: str,
    page: int = 1,
    limit: int = 5,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """
    Поиск по названию категории
    """
    search_category = await orm_category.search_categories(search_text, page, limit, db_session)
    return scheme.AdvancedCategory(items=search_category)
