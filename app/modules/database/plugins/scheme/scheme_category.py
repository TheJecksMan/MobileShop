from typing import List
from pydantic import BaseModel


class DetailCategory(BaseModel):
    category_id: int
    image: str
    name: str

    class Config:
        orm_mode = True


class AdvancedCategory(BaseModel):
    items: List[DetailCategory]


class ParentCategory(BaseModel):
    category_id: int
    image: str
    name: str

    class Config:
        orm_mode = True


class DetailProduct(BaseModel):
    product_id: int
    model: str
    image: str
    price: float
    description: str

    class Config:
        orm_mode = True


class AdvancedProduct(BaseModel):
    items: List[DetailProduct]
