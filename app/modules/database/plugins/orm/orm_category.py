"""ORM"""
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from modules.error.error_data import raise_error
from modules.database.plugins.models import (
    OcProduct,
    OcCategory,
    OcProductToCategory,
    OcProductDescription,
    OcCategoryDescription
)


def _sort_product(
    query,
    sort_date: int = None,
    sort_price: int = None,
    sort_name: int = None
) -> Any:
    # Sort by date column
    if sort_date == 1:
        query = query.order_by(OcProduct.date_added.asc())
    elif sort_date == -1:
        query = query.order_by(OcProduct.date_added.desc())

    # Sort by price column
    if sort_price == 1:
        query = query.order_by(OcProduct.price.asc())
    elif sort_price == -1:
        query = query.order_by(OcProduct.price.desc())

    # Sort by name column
    if sort_name == 1:
        query = query.order_by(OcProduct.model.asc())
    elif sort_name == -1:
        query = query.order_by(OcProduct.model.desc())
    return query


async def get_product_by_category(
    category_id: int,
    page: int,
    limit: int,
    db_session: AsyncSession,
    sort_date: int = None,
    sort_price: int = None,
    sort_name: int = None
) -> list:
    """Module for obtaining a list of products by category ID.

    Parameters such as `sort_date`, `sort_price`, `sort_name` sort and accept 1 or -1.\n
    1 - sorting in ascending order.\n
    -1 - sort in descending order.

    """
    query = select(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProductDescription.description)\
        .join(OcProductToCategory, OcProductToCategory.product_id == OcProduct.product_id)\
        .join(OcProductDescription, OcProduct.product_id == OcProductDescription.product_id)\
        .where(OcProductToCategory.category_id == category_id, OcProduct.status == 1)\
        .order_by(OcProduct.sort_order.asc())

    if page != 1:
        sort_query = _sort_product(query, sort_date, sort_price, sort_name).limit(limit).offset(page*limit)
    else:
        sort_query = _sort_product(query, sort_date, sort_price, sort_name).limit(limit)

    try:
        result = await db_session.execute(sort_query)
    except:
        raise_error(400)
    return result.all()


async def get_all_categories(page: int, limit: int, db_session: AsyncSession):
    """Getting a complete list of categories.
    The resulting list will include only the main and non-hidden categories.
    """
    query = select(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
        .join(OcCategoryDescription, OcCategory.category_id == OcCategoryDescription.category_id)\
        .where(OcCategory.status == 1, OcCategory.parent_id == 0)\
        .order_by(OcCategory.sort_order.asc())

    if None in [page, limit]:
        result = await db_session.execute(query)
        return result.all()

    if page != 1:
        query = query.limit(limit).offset(page*limit)
    else:
        query = query.limit(limit)

    try:
        result = await db_session.execute(query)
    except:
        raise_error(400)
    return result.all()


async def search_categories(search_text: str, page: int, limit: int, db_session: AsyncSession):
    """Category search. Also includes search by subcategories
    """
    query = select(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
        .join(OcCategory, OcCategory.category_id == OcCategoryDescription.category_id)\
        .where(OcCategoryDescription.name.like(f'%{search_text}%'), OcCategory.status == 1)

    if page != 1:
        query = query.limit(limit).offset(page*limit)
    else:
        query = query.limit(limit)
    try:
        result = await db_session.execute(query)
    except:
        raise_error(400)
    return result.all()


async def get_parent_categories(category_id: int, db_session: AsyncSession):
    """Getting subcategories by category ID
    """
    result = await db_session.execute(
        select(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)
        .join(OcCategoryDescription, OcCategoryDescription.category_id == OcCategory.category_id)
        .where(OcCategory.status == 1, OcCategory.parent_id != 0, OcCategory.parent_id == category_id)
        .order_by(OcCategory.sort_order.asc())
    )
    return result.all()
