from typing import List

import re
from pydantic import BaseModel, EmailStr, validator, Field
from modules.error.error_data import raise_error


class OptionFull(BaseModel):
    """Схема получения комплектации"""
    name: str
    value: str
    price: float


class AdvansedOption(BaseModel):
    """Расширенная схема получения комплектации"""
    model: str
    image: str | None = None
    sum_price: float
    price: float
    count: int
    option: List[OptionFull]


class EmailSchemaOrder(BaseModel):
    """
    Схема валидации для получения информации о заказе
    """
    fio: str
    phone: str
    email_user: EmailStr
    adress_user: str | None = None
    comment: str = Field(max_length=500)
    models: List[AdvansedOption]
    general_price: float

    @validator("phone")
    def phone_validation(cls, value):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if value and not re.search(regex, value, re.I):
            raise_error(400, 'Phone Number Invalid!')
        return value


class EmailSchemaAppeal(BaseModel):
    """
    Схема валидации для отправки обращения
    """
    fio: str
    phone: str
    email_user: EmailStr
    theme: str
    comment: str = Field(max_length=1000)

    @validator("phone")
    def phone_validation(cls, value):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if value and not re.search(regex, value, re.I):
            raise_error(400, 'Phone Number Invalid!')
        return value


class BaseOutputEmail(BaseModel):
    message: str


class OutputEmailOrder(BaseOutputEmail):
    number_order: str
    UUID: str


class OutputEmailAppeal(BaseOutputEmail):
    number_appeal: str
