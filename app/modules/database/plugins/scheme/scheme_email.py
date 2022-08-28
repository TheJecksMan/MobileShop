import re
from pydantic import BaseModel, EmailStr, validator, Field
from modules.error.error_data import raise_error

from typing import List


class EmailSchema(BaseModel):
    fio: str
    phone: str
    email_recipients: List[EmailStr]
    description: str = Field(max_length=500)
    product_id: List[int]

    @validator("phone")
    def phone_validation(cls, value):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if value and not re.search(regex, value, re.I):
            raise_error(400, 'Phone Number Invalid!')
        return value
