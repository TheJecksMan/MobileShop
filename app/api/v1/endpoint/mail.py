"""
API implementation module for send mail.
/api/mail
"""
import uuid
import string
import random

from typing import Any

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from fastapi_mail import FastMail, MessageSchema

from modules.database.plugins.scheme import scheme_email

from core.setting import CONF, NUMBER_LEN_ORDER, RECIPIENT_LIST


router = APIRouter()


@router.post("/send/order", response_class=ORJSONResponse, response_model=scheme_email.OutputEmailOrder)
async def send_order_by_email(item: scheme_email.EmailSchemaOrder) -> Any:
    """
    Отправка заказа операторам по почтовому адресу
    """
    chars = string.ascii_uppercase + string.digits
    uuid_order = str(uuid.uuid4())
    random_order = ''.join(random.choice(chars) for _ in range(NUMBER_LEN_ORDER))

    email_template = {
        "order_id": random_order,
        "uuid": uuid_order,
        "fio": item.fio,
        "phone": item.phone,
        "email": item.email_user,
        "adress": item.adress_user,
        "order": item.models,
        "general_price": item.general_price,
        "comment": item.comment
    }

    message = MessageSchema(
        subject=f"[Mobile] Заказ #{random_order}",
        recipients=RECIPIENT_LIST,
        template_body=email_template
    )

    fast_mail_config = FastMail(CONF)
    await fast_mail_config.send_message(message, template_name="order.html")
    return ORJSONResponse(status_code=200, content={
        "message": "Сообщение отправлено.\nМы скоро свяжемся с Вами!",
        "number_order": str(random_order),
        "UUID": uuid_order
    })


@router.post("/send/appeal", response_class=ORJSONResponse, response_model=scheme_email.OutputEmailAppeal)
async def send_appeal_by_email(item: scheme_email.EmailSchemaAppeal) -> Any:
    """
    Отправка обращения пользователя оператору по почте
    """
    chars = string.ascii_uppercase + string.digits
    random_appeal = ''.join(random.choice(chars) for _ in range(NUMBER_LEN_ORDER))

    email_template = {
        "appeal_id": random_appeal,
        "fio": item.fio,
        "phone": item.phone,
        "email": item.email_user,
        "theme": item.theme,
        "comment": item.comment
    }

    message = MessageSchema(
        subject=f"[Mobile] Обращение #{random_appeal}",
        recipients=RECIPIENT_LIST,
        template_body=email_template
    )

    fast_mail_config = FastMail(CONF)
    await fast_mail_config.send_message(message, template_name="user_appeal.html")
    return ORJSONResponse(status_code=200, content={
        "message": "Обращение отправлено.\nМы скоро свяжемся с Вами!",
        "number_appeal": str(random_appeal),
    })
