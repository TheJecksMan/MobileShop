from typing import List
"""Models"""
from modules.database.plugins.models import (
    OcProduct,
    OcProductDescription,
    OcStockStatu,
    OcProductToCategory,
    OcOptionValueDescription,
    OcOptionDescription,
    OcProductOptionValue
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from modules.error.error_data import raise_error


async def get_product_by_id(product_id: int, db_session: AsyncSession):
    """Получение продукта по идентификатору в базе данных"""
    result = await db_session.execute(
        select(OcProduct.product_id, OcProduct.model, OcProduct.image,
               OcProduct.price, OcProduct.quantity, OcStockStatu.name)
        .join(OcStockStatu, OcProduct.stock_status_id == OcStockStatu.stock_status_id)
        .filter(OcProduct.product_id == product_id)
    )
    result = result.first()
    if not result:
        raise_error(404, "Not Found!")
    return result


async def get_multiple_product_by_id(products_ids: List[int], db_session: AsyncSession):
    """Получение информации о нескольких продуктов по идентификатору в базе данных"""
    result = await db_session.execute(
        select(OcProduct.product_id, OcProduct.model, OcProduct.image,
               OcProduct.price, OcProductDescription.description)
        .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)
        .where(OcProduct.product_id.in_(products_ids), OcProduct.status == 1)
    )
    result = result.all()
    if not result:
        raise_error(404)
    return result


async def get_product_description_by_id(product_id: int, db_session: AsyncSession):
    """Получение подробного описания по идентификатору продукта"""
    result = await db_session.execute(
        select(OcProductDescription.description)
        .where(OcProductDescription.product_id == product_id)
    )
    result = result.first()
    if not result:
        raise_error(404)
    return result


async def get_popular_product(limit: int, db_session: AsyncSession):
    """Получение списка самых просматривемых товаров из базы данных"""
    try:
        result = await db_session.execute(
            select(OcProduct.product_id, OcProduct.model, OcProduct.image,
                   OcProduct.price, OcProductDescription.description)
            .where(OcProduct.status == 1)
            .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)
            .order_by(OcProduct.viewed.desc())
            .limit(limit)
        )
    except:
        raise_error(404)
    return result.all()


async def get_all_product(page: int, limit: int, db_session: AsyncSession):
    """Получение списка всех продуктов из базы данных. (Почти не используется)"""
    result = await db_session.execute(
        select(OcProduct.product_id, OcProduct.image, OcProduct.price)
        .where(OcProduct.status == 1)
        .limit(limit)
    )
    if page != 1:
        try:
            return result.offset(page*limit).all()
        except:
            raise_error(404)
    return result.all()


async def search_product(category_id: int, search_text: str, page: int, limit: int, db_session: AsyncSession):
    """Поиск товара в базе данных по полученному тексту"""
    query = select(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProductDescription.description)\
        .where(OcProduct.model.like(f'%{search_text}%'),  OcProduct.status == 1)\
        .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)

    result = await db_session.execute(query)
    if category_id is not None:
        query = query.join(OcProductToCategory, OcProductToCategory.category_id == category_id)
        result = await db_session.execute(query)
    if page != 1:
        query = query.limit(limit).offset(page*limit)
        try:
            result = await db_session.execute(query)
            return result.all()
        except:
            raise_error(404)
    query = query.limit(limit)
    result = await db_session.execute(query)
    return result.all()


async def get_params_option(db_session: AsyncSession):
    """Получение глобальных фильтров из базы данных"""
    result_name = await db_session.execute(
        select(OcOptionDescription.option_id, OcOptionDescription.name)
    )
    result_params = await db_session.execute(select(OcOptionValueDescription.option_id, OcOptionValueDescription.name))
    return result_name.all(), result_params.all()


async def get_equipment(product_id: int, db_session: AsyncSession):
    """Получение комплектации по идентификатору товара"""
    result = await db_session.execute(
        select(OcOptionValueDescription.name,
               OcOptionDescription.name.label('type'), OcProductOptionValue.product_id,
               OcProductOptionValue.quantity, OcProductOptionValue.price, OcProductOptionValue.price_prefix,
               OcProductOptionValue.points, OcProductOptionValue.points_prefix, OcProductOptionValue.weight,
               OcProductOptionValue.weight_prefix)
        .where(OcProductOptionValue.product_id == product_id)
        .join(OcOptionValueDescription, OcOptionValueDescription.option_value_id == OcProductOptionValue.option_value_id)
        .join(OcOptionDescription, OcOptionDescription.option_id == OcProductOptionValue.option_id)
    )
    return result.all()
