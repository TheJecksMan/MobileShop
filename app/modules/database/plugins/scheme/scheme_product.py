from pydantic import BaseModel, validator
from typing import List

from modules.error.error_data import raise_error


class PopularProduct(BaseModel):

    product_id: int
    model: str
    image: str
    price: float
    name: str


class AdvancedPopularProduct(BaseModel):
    items: List[PopularProduct]


class DetailProduct(BaseModel):

    product_id: int
    model: str
    image: str
    price: float
    quantity: int
    name: str


class AdvancedProduct(BaseModel):
    items: List[DetailProduct]


class DetailDescProduct(BaseModel):
    product_id: int
    name: str
    description: str


class MultipleProduct(BaseModel):
    ids: List[int] = []

    @validator('ids')
    def check_value(cls, value):
        if len(value) > 20:
            raise_error(400, "Некорректное кол-во значений")
        return value


class SearchProduct(BaseModel):
    product_id: int
    model: str
    image: str
    price: float


class AdvancedSearchProduct(BaseModel):
    items: List[SearchProduct]
