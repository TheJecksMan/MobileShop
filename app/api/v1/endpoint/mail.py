from fastapi import APIRouter
from modules.database.plugins.scheme import scheme_email
from fastapi_mail import FastMail, MessageSchema

from fastapi.responses import UJSONResponse

from core.setting import CONF

import uuid
import string
import random

router = APIRouter()


@router.post("/send/order", response_class=UJSONResponse, response_model=scheme_email.OutputEmailOrder)
async def send_order_by_email(item: scheme_email.EmailSchemaOrder):
    ORDER_LEN = 6
    chars = string.ascii_uppercase + string.digits
    uuid_order = str(uuid.uuid4())
    random_order = ''.join(random.choice(chars) for _ in range(ORDER_LEN))

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
        recipients=item.dict().get("email_recipients"),
        template_body=email_template
    )

    fm = FastMail(CONF)
    await fm.send_message(message, template_name="order.html")
    return UJSONResponse(status_code=200, content={
        "message": "Сообщение отправлено.\nМы скоро свяжемся с Вами!",
        "number_order": str(random_order),
        "UUID": str(uuid.uuid4())
    })


@router.post("/send/appeal", response_class=UJSONResponse, response_model=scheme_email.OutputEmailAppeal)
async def send_appeal_by_email(item: scheme_email.EmailSchemaAppeal):
    ORDER_LEN = 6
    chars = string.ascii_uppercase + string.digits
    random_appeal = ''.join(random.choice(chars) for _ in range(ORDER_LEN))

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
        recipients=item.dict().get("email_recipients"),
        template_body=email_template
    )

    fm = FastMail(CONF)
    await fm.send_message(message, template_name="user_appeal.html")
    return UJSONResponse(status_code=200, content={
        "message": "Обращение отправлено.\nМы скоро свяжемся с Вами!",
        "number_appeal": str(random_appeal),
    })
