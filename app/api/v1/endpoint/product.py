from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from modules.database.deps import get_db

from modules.database.plugins.orm import orm_product
from modules.database.plugins.scheme import scheme_product

from modules.error.product_error import raise_error


router = APIRouter()


@router.get("/product/{id}", response_model=scheme_product.DetailProduct)
def get_detail_product(id: int, db: Session = Depends(get_db)):
    """Получение информации о продукте.\n
    ---
    **product_id**: Уникальное значение\n
    **model**: Номер модели продукта.\n
    **price**: Цена на продукт.\n
    **name**: Статус товара строкой.\n
    **image**: Изображение продукта.\n
    """
    product = orm_product.get_product_by_id(id, db)

    if not product:
        raise_error(status.HTTP_404_NOT_FOUND, "Not Found!")
    return product


@router.get("/product/{id}/description/", response_model=scheme_product.DetailDescriptionProduct)
def get_product_description(id: int, db: Session = Depends(get_db)):
    """Получение описание продукта"""
    product = orm_product.get_product_description_by_id(id, db)

    if not product:
        raise_error(status.HTTP_400_BAD_REQUEST)
    return product


@router.get("/product/page/{page}/limit/{limit}")
def get_product_category(page: int, limit, db: Session = Depends(get_db)):
    product = orm_product.get_all_product(page, limit, db)
    return product


@router.get("/product/search/{search}")
def product_search(search: str, db: Session = Depends(get_db)):
    pass


@router.get("/product/category/{id}/page/{page}/limit/{limit}")
def get_product_category(id: int, db: Session = Depends(get_db)):
    pass


@router.get("/product/popular/{limit}", response_model=list[scheme_product.PopularProduct])
def get_popular_product(limit: int = 5, db: Session = Depends(get_db)):
    """Список самых просматриваемых товаров.
    Не отображает скрытые товары.
    """
    product = orm_product.get_popular_product(limit, db)
    if not product:
        raise_error(status.HTTP_400_BAD_REQUEST)
    return product
