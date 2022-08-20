from sqlalchemy.orm import Session

from modules.database.plugins.models import OcCategory, OcCategoryDescription, OcProductToCategory, OcProduct, OcStockStatu


def get_product_by_category(category_id: int, page: int, limit: int, db: Session):
    return db.query(OcProduct.product_id, OcProductToCategory.category_id, OcProduct.model, OcProduct.image, OcProduct.price)\
        .join(OcProductToCategory, OcProductToCategory.product_id == OcProduct.product_id)\
        .filter(OcProductToCategory.category_id == category_id)\
        .limit(limit).offset(page*limit).all()


def get_all_category(db: Session, page: int = None, limit: int = None):
    if None in [page, limit]:
        return db.query(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
            .join(OcCategoryDescription, OcCategory.category_id == OcCategoryDescription.category_id).all()
    else:
        return db.query(OcCategory.category_id, OcCategory.image, OcCategoryDescription.name)\
            .join(OcCategoryDescription, OcCategory.category_id == OcCategoryDescription.category_id)\
            .limit(limit).offset(page*limit).all()
