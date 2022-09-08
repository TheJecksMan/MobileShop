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

from sqlalchemy.orm import Session
from modules.error.error_data import raise_error


def get_product_by_id(product_id: int, db_session: Session):
    """Получение продукта по идентификатору в базе данных"""
    query = db_session.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProduct.quantity, OcStockStatu.name)\
        .join(OcStockStatu, OcProduct.stock_status_id == OcStockStatu.stock_status_id)\
        .filter(OcProduct.product_id == product_id).first()

    if not query:
        raise_error(404, "Not Found!")
    return query


def get_multiple_product_by_id(products_ids: List[int], db_session: Session):
    """Получение информации о нескольких продуктов по идентификатору в базе данных"""
    query = db_session.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProductDescription.description)\
        .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)\
        .filter(OcProduct.product_id.in_(products_ids),  OcProduct.status == 1).all()
    if not query:
        raise_error(404)
    return query


def get_product_description_by_id(product_id: int, db_session: Session):
    """Получение подробного описания по идентификатору продукта"""
    query = db_session.query(OcProductDescription.description)\
        .filter(OcProductDescription.product_id == product_id).first()
    return query


def get_popular_product(limit: int, db_session: Session):
    """Получение списка самых просматривемых товаров из базы данных"""
    query = db_session.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProductDescription.description)\
        .filter(OcProduct.status == 1)\
        .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)\
        .order_by(OcProduct.viewed.desc()).limit(limit).all()
    return query


def get_all_product(page: int, limit: int, db_session: Session):
    """Получение списка всех продуктов из базы данных. (Почти не используется)"""
    query = db_session.query(OcProduct.product_id, OcProduct.image, OcProduct.price)\
        .filter(OcProduct.status == 1).limit(limit)
    if page != 1:
        return query.offset(page*limit).all()
    return query.all()


def search_product(category_id: int, search_text: str, page: int, limit: int, db_session: Session):
    """Поиск товара в базе данных по полученному тексту"""
    query = db_session.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProductDescription.description)\
        .filter(OcProduct.model.like(f'%{search_text}%'),  OcProduct.status == 1)\
        .join(OcProductDescription, OcProductDescription.product_id == OcProduct.product_id)
    if category_id is not None:
        query = query.join(OcProductToCategory, OcProductToCategory.category_id == category_id)
    if page != 1:
        return query.limit(limit).offset(page*limit).all()
    return query.limit(limit).all()


def get_params_option(db_session: Session):
    """Получение глобальных фильтров из базы данных"""
    query_name = db_session.query(OcOptionDescription.option_id, OcOptionDescription.name).all()
    query_params = db_session.query(OcOptionValueDescription.option_id, OcOptionValueDescription.name).all()
    return query_name, query_params


def get_equipment(product_id: int, db_session: Session):
    """Получение комплектации по идентификатору товара"""
    query = db_session.query(
        OcOptionValueDescription.name,
        OcOptionDescription.name.label('type'), OcProductOptionValue.product_id,
        OcProductOptionValue.quantity, OcProductOptionValue.price, OcProductOptionValue.price_prefix,
        OcProductOptionValue.points, OcProductOptionValue.points_prefix, OcProductOptionValue.weight,
        OcProductOptionValue.weight_prefix)\
        .filter(OcProductOptionValue.product_id == product_id)\
        .join(OcOptionValueDescription, OcOptionValueDescription.option_value_id == OcProductOptionValue.option_value_id)\
        .join(OcOptionDescription, OcOptionDescription.option_id == OcProductOptionValue.option_id).all()
    return query
