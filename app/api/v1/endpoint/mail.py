from fastapi import APIRouter
from modules.database.plugins.scheme.scheme_email import EmailSchema
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from fastapi.responses import UJSONResponse

from core.setting import CONF

import uuid
import string
import random

router = APIRouter()


html = "<h1>test</h1>"


@router.post("/send", response_class=UJSONResponse)
async def send_product_by_email(item: EmailSchema):
    ORDER_LEN = 6
    chars = string.ascii_uppercase + string.digits
    random_order = ''.join(random.choice(chars) for _ in range(ORDER_LEN))

    message = MessageSchema(
        subject=f"Заказ #{random_order}",
        recipients=item.dict().get("email_recipients"),
        body=html,
        subtype="html"
    )

    fm = FastMail(CONF)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={
        "message": "Сообщение отправлено.\nМы скоро свяжемся с Вами!",
        "number_order": str(random_order),
        "UUID": str(uuid.uuid4())
    })
