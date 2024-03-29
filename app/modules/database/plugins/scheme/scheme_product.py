from typing import List, Optional
from pydantic import BaseModel, validator

from modules.error.error_data import raise_error


class BaseProduct(BaseModel):
    """ Базовая схема товара"""
    product_id: int
    model: str
    image: str
    price: float


class PopularProduct(BaseProduct):
    """Схема популярных товаров"""
    description: str

    class Config:
        orm_mode = True


class AdvancedPopularProduct(BaseModel):
    """Расширенная схема популярных товаров"""
    items: List[PopularProduct]


class DescProduct(BaseModel):
    """Схема базового продукта и описания"""
    description: str

    class Config:
        orm_mode = True


class AdvancedMultipleProduct(BaseModel):
    """Расширенная схема получения информации о нескольких товаров"""
    items: List[PopularProduct]


class DetailProduct(BaseProduct):
    """Схема получения детальной информации о продукте"""
    quantity: int
    name: str
    description: str

    class Config:
        orm_mode = True


class AdvancedProduct(BaseModel):
    """Расширенная схема информации о продукте"""
    items: List[DetailProduct]


class AdvancedDetailProduct(BaseModel):
    """Расширенная схема получения детальной информации о продукте"""
    item: Optional[DetailProduct]


class MultipleProduct(BaseModel):
    """Схема получения информации о нескольких товаров"""
    ids: List[int] = []

    @validator('ids')
    def check_value(cls, value):
        """Проверка допустимой длинны"""
        if len(value) > 30:
            raise_error(400, "Некорректное кол-во значений")
        return value


class AdvancedSearchProduct(BaseModel):
    """Расширенная схема получения товаров из поиска"""
    items: List[PopularProduct]

    class Config:
        orm_mode = True


class FilterName(BaseModel):
    """Схема получения информации о доступных фильтрах"""
    option_id: int
    name: str

    class Config:
        orm_mode = True


class FilterGeneral(BaseModel):
    """Общая схема получения фильтров продукта"""
    items: List[FilterName]
    option: List[FilterName]


class BaseProductCategory(BaseModel):
    product_id: int
    image: str
    price: float

    class Config:
        orm_mode = True


class BaseProductEquipment(BaseModel):
    name: str
    type: str
    product_id: int
    quantity: float
    price: float
    price_prefix: str
    points: int
    points_prefix: str
    weight: int
    weight_prefix: str

    class Config:
        orm_mode = True
