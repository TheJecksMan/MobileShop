from multiprocessing import parent_process
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from modules.database.deps import get_db

from modules.database.plugins.orm import orm_category
from modules.database.plugins.scheme import scheme_category

from modules.error.error_data import raise_error


router = APIRouter()


@router.get("/all")
def get_all_categories(page: int = None, limit: int = None, db: Session = Depends(get_db)):
    """Получение списка всех доступный родительских катологов"""
    category = orm_category.get_all_categories(db, page, limit)
    return category


@router.get("/parent/{category_id}")
def get_parent_categories(category_id: int, db: Session = Depends(get_db)):
    parent_categories = orm_category.get_parent_categories(category_id, db)
    return parent_categories


@router.get("/{category_id}/page/{page}")
def get_product_category(category_id: int, page: int, limit: int = 10, db: Session = Depends(get_db)):
    category_product = orm_category.get_product_by_category(category_id, page, limit, db)
    return category_product
