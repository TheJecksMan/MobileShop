from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from modules.database.deps import get_db

from modules.database.plugins.orm import orm_product
from modules.database.plugins.scheme.scheme_product import (
    AdvancedPopularProduct,
    DetailDescProduct,
    MultipleProduct,
    AdvancedSearchProduct,
    FilterGeneral,
    AdvancedDetailProduct,
    DetailProduct
)


router = APIRouter()


@router.get("/{product_id}", response_model=AdvancedDetailProduct)
def get_detail_product(product_id: int, db: Session = Depends(get_db)):
    """Получение базовой информации о продукте."""
    base_product = orm_product.get_product_by_id(product_id, db)
    base_desc = orm_product.get_product_description_by_id(product_id, db)
    desc = DetailProduct(
        product_id=base_product.product_id,
        model=base_product.model,
        image=base_product.image,
        price=base_product.price,
        quantity=base_product.quantity,
        name=base_product.name,
        descriptions=base_desc
    )
    return AdvancedDetailProduct(item=desc)


@router.get("/equipment/{product_id}")
def get_equipment_product(product_id, db: Session = Depends(get_db)):
    equipment = orm_product.get_equipment(product_id, db)
    return equipment


@router.post('/multiple', response_model=AdvancedPopularProduct)
def get_detail_multiple_products(multiple_product: MultipleProduct, db: Session = Depends(get_db)):
    """Получение базовых данных о нескольких товарах.
    ---
    Ограничение на вход до 20 значений списка
    """
    product = orm_product.get_multiple_product_by_id(multiple_product.ids, db)
    return AdvancedPopularProduct(items=product)


@router.get("/{product_id}/description", response_model=DetailDescProduct)
def get_product_description(product_id: int, db: Session = Depends(get_db)):
    """Получение подробного описание продукта"""
    product = orm_product.get_product_description_by_id(product_id, db)
    return product


@router.get("/page/{page}")
def get_product_category(page: int, limit: int = 10, db: Session = Depends(get_db)):
    product = orm_product.get_all_product(page, limit, db)
    return product


@router.get("/search/{search_text}", response_model=AdvancedSearchProduct)
def product_search(search_text: str, limit: int = 5, category_id: int = None, db: Session = Depends(get_db)):
    """Поиск товара по названию товара.
    Возможен поиск товаров в конкретной категории"""
    product = orm_product.search_product(category_id, search_text, limit, db)
    return AdvancedSearchProduct(items=product)


@router.get("/popular/{limit}", response_model=AdvancedPopularProduct)
def get_popular_product(limit: int, db: Session = Depends(get_db)):
    """Список самых просматриваемых товаров.
    Не отображает скрытые товары.
    """
    product = orm_product.get_popular_product(limit, db)
    return AdvancedPopularProduct(items=product)


@router.get("/filter/all")
def get_all_param_filter(db: Session = Depends(get_db)):
    """Получение полного списка доступных параметров для последующей фильтрации"""
    params, option = orm_product.get_params_option(db)

    return FilterGeneral(items=params, option=option)
