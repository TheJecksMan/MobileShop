from sqlalchemy.orm import Session

from modules.database.plugins.models import OcCategory, OcCategoryDescription, OcProductToCategory, OcProduct, OcStockStatu


def get_product_by_category(category_id: int, page: int, limit: int, db: Session):
    query = db.query(OcProduct.product_id, OcProductToCategory.category_id, OcProduct.model, OcProduct.image, OcProduct.price)\
        .join(OcProductToCategory, OcProductToCategory.product_id == OcProduct.product_id)\
        .filter(OcProductToCategory.category_id == category_id, OcCategory.status == 1)\
        .order_by(OcProduct.sort_order.asc())\
        .limit(limit).offset(page*limit).all()
    return query


def get_all_categories(db: Session, page: int = None, limit: int = None):

    query = db.query(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
        .join(OcCategoryDescription, OcCategory.category_id == OcCategoryDescription.category_id)\
        .filter(OcCategory.status == 1, OcCategory.parent_id == 0)\
        .order_by(OcCategory.sort_order.asc())

    if None in [page, limit]:
        return query.all()
    else:
        return query.limit(limit).offset(page*limit).all()


def search_categories(search_text: str, limit: int, db: Session):
    query = db.query(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
        .filter(OcCategoryDescription.name.like(f'%{search_text}%'))\
        .join(OcCategory, OcCategory.category_id == OcCategoryDescription.category_id)\
        .filter(OcCategory.status == 1).limit(limit).all()
    return query


def get_parent_categories(category_id: int, db: Session):
    query = db.query(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
        .join(OcCategoryDescription, OcCategory.category_id == OcCategoryDescription.category_id)\
        .filter(OcCategory.status == 1, OcCategory.parent_id != 0, OcCategory.category_id == category_id)\
        .order_by(OcCategory.sort_order.asc()).all()
    return query