from pydantic import BaseModel, validator
from typing import List

from modules.error.error_data import raise_error


class PopularProduct(BaseModel):

    product_id: int
    model: str
    image: str
    price: float

    class Config:
        orm_mode = True


class DetailProduct(BaseModel):

    product_id: int
    model: str
    image: str
    price: float
    name: str

    class Config:
        orm_mode = True


class DetailDescriptionProduct(BaseModel):
    product_id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class MultipleProduct(BaseModel):
    ids: List[int] = []

    @validator('ids')
    def check_value(cls, value):
        if len(value) > 20:
            raise_error(400, "Привышен лимит значений!")
        return value
