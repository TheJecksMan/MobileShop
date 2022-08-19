from dataclasses import field
from pydantic import BaseModel
from typing import List


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
