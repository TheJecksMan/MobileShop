from sqlalchemy.orm import Session

from modules.database.plugins.models import OcProduct, OcProductDescription, OcStockStatu


def get_product_by_id(product_id: int, db: Session):
    return db.query(OcProduct.product_id, OcProduct.model, OcProduct.image, OcProduct.price, OcStockStatu.name)\
        .join(OcStockStatu, OcProduct.stock_status_id == OcStockStatu.stock_status_id)\
        .filter(OcProduct.product_id == product_id).first()


def get_product_description_by_id(product_id: int, db: Session):
    return db.query(OcProductDescription).filter(OcProductDescription.product_id == product_id).first()


def get_popular_product(limit: int, db: Session):
    return db.query(OcProduct).filter(OcProduct.status == 1).order_by(OcProduct.viewed.desc()).limit(limit).all()


def get_all_product(page: int, limit: int, db: Session):
    return db.query(OcProduct.product_id, OcProduct.image, OcProduct.price).limit(limit).offset(page*limit).all()
