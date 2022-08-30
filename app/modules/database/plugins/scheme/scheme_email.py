import re
from pydantic import BaseModel, EmailStr, validator, Field
from modules.error.error_data import raise_error

from typing import List, Dict


class AdvansedOption(BaseModel):
    option_name: Doct[str]
    product_type: l


class EmailSchema(BaseModel):
    fio: str
    phone: str
    email_recipients: List[EmailStr]
    description: str = Field(max_length=500)
    product_id: List[int]
    options: Dict[int, AdvansedOption]

    @validator("phone")
    def phone_validation(cls, value):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if value and not re.search(regex, value, re.I):
            raise_error(400, 'Phone Number Invalid!')
        return value
