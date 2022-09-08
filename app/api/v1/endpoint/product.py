from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from modules.database.deps import get_db

from modules.database.plugins.orm import orm_product
from modules.database.plugins.scheme.scheme_product import (
    AdvancedPopularProduct,
    MultipleProduct,
    AdvancedSearchProduct,
    FilterGeneral,
    AdvancedDetailProduct,
    DetailProduct,
    AdvancedMultipleProduct,
    DescProduct
)


router = APIRouter()


@router.get("/{product_id}", response_model=AdvancedDetailProduct)
def get_detail_product(product_id: int, db_session: Session = Depends(get_db)):
    """Получение базовой информации о продукте."""
    base_product = orm_product.get_product_by_id(product_id, db_session)
    base_desc = orm_product.get_product_description_by_id(product_id, db_session)
    desc = DetailProduct(
        product_id=base_product.product_id,
        model=base_product.model,
        image=base_product.image,
        price=base_product.price,
        quantity=base_product.quantity,
        name=base_product.name,
        description=base_desc.description
    )
    return AdvancedDetailProduct(item=desc)


@router.get("/equipment/{product_id}")
def get_equipment_product(product_id, db_session: Session = Depends(get_db)):
    """Получение информации о доступной комплектации товара"""
    equipment = orm_product.get_equipment(product_id, db_session)
    return equipment


@router.post('/multiple', response_model=AdvancedMultipleProduct)
def get_detail_multiple_products(
    multiple_product: MultipleProduct,
    db_session: Session = Depends(get_db)
):
    """Получение базовых данных о нескольких товарах.
    ---
    Ограничение на вход до 20 значений списка
    """
    product = orm_product.get_multiple_product_by_id(multiple_product.ids, db_session)
    return AdvancedMultipleProduct(items=product)


@router.get("/{product_id}/description", response_model=DescProduct)
def get_product_description(product_id: int, db_session: Session = Depends(get_db)):
    """Получение подробного описание продукта"""
    product = orm_product.get_product_description_by_id(product_id, db_session)
    return product


@router.get("/page/{page}")
def get_product_category(page: int, limit: int = 10, db_session: Session = Depends(get_db)):
    product = orm_product.get_all_product(page, limit, db_session)
    return product


@router.get("/search/{search_text}", response_model=AdvancedSearchProduct)
def product_search(search_text: str, page: int = 1, limit: int = 5, category_id: int = None, db_session: Session = Depends(get_db)):
    """Поиск товара по названию товара.
    Возможен поиск товаров в конкретной категории"""
    product = orm_product.search_product(category_id, search_text, page, limit, db_session)
    return AdvancedSearchProduct(items=product)


@router.get("/popular/{limit}", response_model=AdvancedPopularProduct)
def get_popular_product(limit: int, db_session: Session = Depends(get_db)):
    """Список самых просматриваемых товаров.
    Не отображает скрытые товары.
    """
    product = orm_product.get_popular_product(limit, db_session)
    return AdvancedPopularProduct(items=product)


@router.get("/filter/all")
def get_all_param_filter(db_session: Session = Depends(get_db)):
    """Получение полного списка доступных параметров для последующей фильтрации"""
    params, option = orm_product.get_params_option(db_session)

    return FilterGeneral(items=params, option=option)
