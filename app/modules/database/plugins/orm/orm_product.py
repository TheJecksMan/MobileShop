from sqlalchemy.orm import Session
from modules.database.plugins.models import OcProduct, OcProductDescription, OcStockStatu, OcProductToCategory

from typing import List

from modules.error.error_data import raise_error


def get_product_by_id(product_id: int, db: Session):
    query = db.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcProduct.quantity, OcStockStatu.name)\
        .join(OcStockStatu, OcProduct.stock_status_id == OcStockStatu.stock_status_id)\
        .filter(OcProduct.product_id == product_id).first()

    if not query:
        raise_error(404, "Not Found!")
    return query


def get_multiple_product_by_id(products_ids: List[int], db: Session):
    query = db.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcStockStatu.name)\
        .join(OcStockStatu, OcProduct.stock_status_id == OcStockStatu.stock_status_id)\
        .filter(OcProduct.product_id.in_(products_ids),  OcProduct.status == 1).all()
    if not query:
        raise_error(404)
    return query


def get_product_description_by_id(product_id: int, db: Session):
    query = db.query(OcProductDescription.product_id, OcProductDescription.name, OcProductDescription.description).filter(
        OcProductDescription.product_id == product_id).first()
    return query


def get_popular_product(limit: int, db: Session):
    query = db.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcStockStatu.name)\
        .join(OcStockStatu, OcProduct.stock_status_id == OcStockStatu.stock_status_id)\
        .filter(OcProduct.status == 1)\
        .order_by(OcProduct.viewed.desc()).limit(limit).all()
    return query


def get_all_product(page: int, limit: int, db: Session):
    query = db.query(OcProduct.product_id, OcProduct.image, OcProduct.price)\
        .filter(OcProduct.status == 1).limit(limit).offset(page*limit).all()
    return query


def search_product(category_id: int, search_text: str, limit: int, db: Session):
    query = db.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, )\
        .filter(OcProduct.model.like(f'%{search_text}%'),  OcProduct.status == 1)
    if category_id != None:
        query.join(OcProductToCategory, OcProductToCategory.category_id == category_id)
    return query.limit(limit).all()
