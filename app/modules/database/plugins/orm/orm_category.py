"""Models"""
from sqlalchemy.orm import Session, Query

from modules.database.plugins.models import OcCategory, OcCategoryDescription, OcProductToCategory, OcProduct, OcProductDescription


def sort_product(query: Query, sort_date: int = None, sort_price: int = None, sort_name: int = None):
    if sort_date == 1:
        query = query.order_by(OcProduct.date_added.asc())
    elif sort_date == -1:
        query = query.order_by(OcProduct.date_added.desc())

    if sort_price == 1:
        query = query.order_by(OcProduct.price.asc())
    elif sort_price == -1:
        query = query.order_by(OcProduct.price.desc())

    if sort_name == 1:
        query = query.order_by(OcProduct.model.asc())
    elif sort_name == -1:
        query = query.order_by(OcProduct.model.desc())
    return query


def get_product_by_category(
    category_id: int, page: int, limit: int, db_session: Session,
    sort_date: int = None, sort_price: int = None, sort_name: int = None
):
    """Получение списка товаров по идентификатору категории"""
    query = db_session.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProductDescription.description)\
        .join(OcProductToCategory, OcProductToCategory.product_id == OcProduct.product_id)\
        .join(OcProductDescription, OcProduct.product_id == OcProductDescription.product_id)\
        .filter(OcProductToCategory.category_id == category_id, OcProduct.status == 1)\
        .order_by(OcProduct.sort_order.asc())\

    if page != 1:
        sort_query = sort_product(query, sort_date, sort_price, sort_name)
        return sort_query.limit(limit).offset(page*limit).all()

    sort_query = sort_product(query, sort_date, sort_price, sort_name)
    return sort_query.limit(limit).all()


def get_all_categories(db_session: Session, page: int, limit: int):
    """Получение полного списка категорий из базы данных"""
    query = db_session.query(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
        .join(OcCategoryDescription, OcCategory.category_id == OcCategoryDescription.category_id)\
        .filter(OcCategory.status == 1, OcCategory.parent_id == 0)\
        .order_by(OcCategory.sort_order.asc())

    if None in [page, limit]:
        return query.all()

    if page != 1:
        return query.limit(limit).offset(page*limit).all()
    return query.limit(limit).all()


def search_categories(search_text: str, page: int, limit: int, db_session: Session):
    """Поиск категорий по базе данных"""
    query = db_session.query(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
        .join(OcCategory, OcCategory.category_id == OcCategoryDescription.category_id)\
        .filter(OcCategoryDescription.name.like(f'%{search_text}%'))\
        .filter(OcCategory.status == 1)
    if page != 1:
        return query.limit(limit).offset(page*limit).all()
    return query.limit(limit).all()


def get_parent_categories(category_id: int, db_session: Session):
    """Получение подкатегорий по идентификатору категории"""
    query = db_session.query(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
        .join(OcCategoryDescription, OcCategory.category_id == OcCategoryDescription.category_id)\
        .filter(OcCategory.status == 1, OcCategory.parent_id != 0, OcCategory.category_id == category_id)\
        .order_by(OcCategory.sort_order.asc()).all()
    return query
