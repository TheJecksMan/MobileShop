from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from modules.database.deps import get_db

from modules.database.plugins.orm import orm_category
from modules.database.plugins.scheme.scheme_category import AdvancedCategory, AdvancedProduct


router = APIRouter()


@router.get("/all", response_model=AdvancedCategory)
def get_all_categories(page: int = None, limit: int = None, db: Session = Depends(get_db)):
    """Получение списка всех доступный родительских катологов"""
    category = orm_category.get_all_categories(db, page, limit)
    return AdvancedCategory(items=category)


@router.get("/parent/{category_id}")
def get_parent_categories(category_id: int, db: Session = Depends(get_db)):
    """Получение информации о доступных подгатегориях"""
    parent_categories = orm_category.get_parent_categories(category_id, db)
    return parent_categories


@router.get("/{category_id}/product", response_model=AdvancedProduct)
def get_product_category(
    category_id: int, page: int, limit: int = 10,
    sort_date: int = None, sort_price: int = None, sort_name: int = None,
    db: Session = Depends(get_db)
):
    """Получения всего списка товаров из категории
    ----
    Сортировки принимают только значения -1 и  1!\n
    -1 - по убыванию\n
    1 -  по возрастанию
    """
    category_product = orm_category.get_product_by_category(
        category_id, page, limit, db, sort_date, sort_price, sort_name)
    return AdvancedProduct(items=category_product)


@router.get('/search/{search_text}', response_model=AdvancedCategory)
def categories_search(search_text: str, page: int = 1, limit: int = 5, db: Session = Depends(get_db)):
    """Поиск по названию категорию"""
    search_category = orm_category.search_categories(search_text, page, limit, db)
    return AdvancedCategory(items=search_category)
