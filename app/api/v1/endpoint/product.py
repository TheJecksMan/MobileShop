from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from modules.database.deps import get_db

from modules.database.plugins.orm import orm_product
from modules.database.plugins.scheme import scheme_product

from modules.error.error_data import raise_error


router = APIRouter()


@router.get("/{product_id}", response_model=scheme_product.DetailProduct)
def get_detail_product(product_id: int, db: Session = Depends(get_db)):
    """Получение информации о продукте.\n
    ---
    **product_id**: Уникальное значение\n
    **model**: Номер модели продукта.\n
    **price**: Цена на продукт.\n
    **name**: Статус товара строкой.\n
    **image**: Изображение продукта.\n
    """
    product = orm_product.get_product_by_id(product_id, db)

    if not product:
        raise_error(status.HTTP_404_NOT_FOUND, "Not Found!")
    return product


@router.post('/multiple', response_model=list[scheme_product.DetailProduct])
def get_detail_multiple_products(multiple_product: scheme_product.MultipleProduct, db: Session = Depends(get_db)):
    """Получение данных из базы данных.
    ---
    Получение данных о нескольких товарах.

    Ограничение на вход до 20 значений списка
    """
    product = orm_product.get_multiple_product_by_id(multiple_product.ids, db)
    if not product:
        raise_error(status.HTTP_400_BAD_REQUEST)
    return product


@router.get("/{product_id}/description", response_model=scheme_product.DetailDescriptionProduct)
def get_product_description(product_id: int, db: Session = Depends(get_db)):
    """Получение подробного описание продукта"""
    product = orm_product.get_product_description_by_id(product_id, db)

    if not product:
        raise_error(status.HTTP_400_BAD_REQUEST)
    return product


@router.get("/page/{page}")
def get_product_category(page: int, limit: int = 10, db: Session = Depends(get_db)):
    """Пагинация страниц
    ---
    Получение всего списка товров
    **limit** - количество отображаемых значений
    """
    product = orm_product.get_all_product(page, limit, db)
    return product


@router.get("/search/{search}", response_model=list[scheme_product.DetailProduct])
def product_search(search: str, limit: int = 5, db: Session = Depends(get_db)):
    """Поиск товара по модели
    ---
    **limit** - количество отображаемых значений
    """
    product = orm_product.search_product(search, limit, db)
    return product


@router.get("/popular", response_model=list[scheme_product.PopularProduct])
def get_popular_product(limit: int = 5, db: Session = Depends(get_db)):
    """Список самых просматриваемых товаров.
    Не отображает скрытые товары.
    """
    product = orm_product.get_popular_product(limit, db)
    if not product:
        raise_error(status.HTTP_400_BAD_REQUEST)
    return product
