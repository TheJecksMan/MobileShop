import re
from pydantic import BaseModel, EmailStr, validator, Field
from modules.error.error_data import raise_error

from typing import List


class OptionFull(BaseModel):
    name: str
    value: str
    price: float


class AdvansedOption(BaseModel):
    model: str
    image: str | None = None
    sum_price: float
    price: float
    count: int
    option: List[OptionFull]


class EmailSchema(BaseModel):
    fio: str
    phone: str
    email_user: EmailStr
    adress_user: str | None = None
    email_recipients: List[EmailStr]
    comment: str = Field(max_length=500)
    models: List[AdvansedOption]
    general_price: float

    @validator("phone")
    def phone_validation(cls, value):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if value and not re.search(regex, value, re.I):
            raise_error(400, 'Phone Number Invalid!')
        return value
