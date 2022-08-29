from pydantic import BaseModel, validator
from typing import List, Optional

from modules.error.error_data import raise_error


class BaseProduct(BaseModel):
    product_id: int
    model: str
    image: str
    price: float


class PopularProduct(BaseProduct):
    description: str


class AdvancedPopularProduct(BaseModel):
    items: List[PopularProduct]


class DescPoroduct(BaseModel):
    description: str


class AdvancedMultipleProduct(BaseModel):
    items: List[PopularProduct]


class DetailProduct(BaseProduct):
    quantity: int
    name: str
    description: str


class AdvancedProduct(BaseModel):
    items: List[DetailProduct]


class AdvancedDetailProduct(BaseModel):
    item: Optional[DetailProduct]


class MultipleProduct(BaseModel):
    ids: List[int] = []

    @validator('ids')
    def check_value(cls, value):
        if len(value) > 20:
            raise_error(400, "Некорректное кол-во значений")
        return value


class AdvancedSearchProduct(BaseModel):
    items: List[BaseProduct]


class FilterName(BaseModel):
    option_id: int
    name: str


class FilterGeneral(BaseModel):
    items: List[FilterName]
    option: List[FilterName]
