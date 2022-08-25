
from pydantic import BaseModel
from typing import List, Dict


class DetailCategory(BaseModel):
    category_id: int
    image: str
    name: str


class AdvancedCategory(BaseModel):
    items: List[DetailCategory]


class DetailProduct(BaseModel):
    product_id: int
    model: str
    image: str
    price: float


class AdvancedProduct(BaseModel):
    items: List[DetailProduct]
