"""ORM"""
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from modules.error.error_data import raise_error
from modules.database.plugins.models import (
    OcProduct,
    OcStockStatu,
    OcOptionDescription,
    OcProductToCategory,
    OcProductDescription,
    OcProductOptionValue,
    OcOptionValueDescription
)


async def get_product_by_id(product_id: int, db_session: AsyncSession):
    """Getting a product by ID. Does not include hidden items.
    """
    result = await db_session.execute(
        select(OcProduct.product_id, OcProduct.model, OcProduct.image,
               OcProduct.price, OcProduct.quantity, OcStockStatu.name)
        .join(OcStockStatu, OcProduct.stock_status_id == OcStockStatu.stock_status_id)
        .where(OcProduct.product_id == product_id, OcProduct.status != 0)
    )
    result = result.first()
    if not result:
        raise_error(404, "Not Found!")
    return result


async def get_multiple_product_by_id(products_ids: List[int], db_session: AsyncSession):
    """Get information about multiple products by ID. Does not include hidden items.
    """
    result = await db_session.execute(
        select(OcProduct.product_id, OcProduct.model, OcProduct.image,
               OcProduct.price, OcProductDescription.description)
        .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)
        .where(OcProduct.product_id.in_(products_ids), OcProduct.status != 0)
    )
    result = result.all()
    if not result:
        raise_error(404, "Not Found!")
    return result


async def get_product_description_by_id(product_id: int, db_session: AsyncSession):
    """Get a detailed description by product ID. Include hidden items.
    """
    result = await db_session.execute(
        select(OcProductDescription.description)
        .where(OcProductDescription.product_id == product_id)
    )
    result = result.first()
    if not result:
        raise_error(404, "Not Found!")
    return result


async def get_popular_product(limit: int, db_session: AsyncSession):
    """Getting a list of the most viewed products.
    """
    try:
        result = await db_session.execute(
            select(OcProduct.product_id, OcProduct.model, OcProduct.image,
                   OcProduct.price, OcProductDescription.description)
            .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)
            .where(OcProduct.status != 0)
            .order_by(OcProduct.viewed.desc())
            .limit(limit)
        )
    except:
        raise_error(400)
    return result.all()


async def get_all_product(page: int, limit: int, db_session: AsyncSession):
    """Getting a list of all products (not recommended to use). Does not include hidden items.
    """
    query = select(OcProduct.product_id, OcProduct.image, OcProduct.price)\
        .where(OcProduct.status != 0)\
        .limit(limit)

    if page != 1:
        query = query.offset(page*limit)
    try:
        result = await db_session.execute(query)
    except:
        raise_error(400)
    return result.all()


async def search_product(
    category_id: int,
    search_text: str,
    page: int,
    limit: int,
    db_session: AsyncSession
):
    """Database search. The pattern %<text>% is used
    """
    query = select(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProductDescription.description)\
        .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)

    if category_id is not None:
        query = query.join(OcProductToCategory, OcProductToCategory.product_id == OcProduct.product_id)\
            .where(OcProductToCategory.category_id == category_id)
    query = query.where(OcProduct.model.like(f'%{search_text}%'),  OcProduct.status != 0)

    try:
        if page != 1:
            query = query.limit(limit).offset(page*limit)
            result = await db_session.execute(query)
        else:
            query = query.limit(limit)
            result = await db_session.execute(query)

    except:
        raise_error(400)
    return result.all()


async def get_params_option(db_session: AsyncSession):
    """Getting global filters.
    """
    result_name = await db_session.execute(
        select(OcOptionDescription.option_id, OcOptionDescription.name)
    )
    result_params = await db_session.execute(
        select(OcOptionValueDescription.option_id, OcOptionValueDescription.name)
    )
    return result_name.all(), result_params.all()


async def get_equipment(product_id: int, db_session: AsyncSession):
    """Retrieving a bundle by product ID. Include hidden items.
    """
    result = await db_session.execute(
        select(OcOptionValueDescription.name, OcOptionDescription.name.label('type'),
               OcProductOptionValue.product_id, OcProductOptionValue.quantity,
               OcProductOptionValue.price, OcProductOptionValue.price_prefix,
               OcProductOptionValue.points, OcProductOptionValue.points_prefix,
               OcProductOptionValue.weight, OcProductOptionValue.weight_prefix)
        .join(OcOptionValueDescription, OcOptionValueDescription.option_value_id == OcProductOptionValue.option_value_id)
        .join(OcOptionDescription, OcOptionDescription.option_id == OcProductOptionValue.option_id)
        .where(OcProductOptionValue.product_id == product_id)
    )
    return result.all()
