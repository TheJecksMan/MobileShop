"""Settings base"""
from pathlib import Path
import os
from fastapi_mail import ConnectionConfig

TITLE: str = 'Mobile API Service'
DESCRIPTION: str = 'Mobile API Service - служит сервисом для мобильного приложения. Получение данных от CMS OpenCard.'
VERSION: str = '1.0.0'

DATABASE_USERNAME: str = "u1346925_test"
DATABASE_PASSWORD: str = "kV7fK9cJ6t"
DATABASE_IP: str = "31.31.196.208"
DATABASE_NAME: str = "u1346925_mebel"

DEV_MODE: bool = True

SQLALCHEMY_ASYNC_DATABASE_URL: str = f"mysql+asyncmy://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_IP}/{DATABASE_NAME}"

CONF = ConnectionConfig(
    MAIL_USERNAME="domaintestsmtp",
    MAIL_PASSWORD="dN7Q4*WsZTG!RzU",
    MAIL_FROM="domaintestsmtp@rambler.ru",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.rambler.ru",
    MAIL_SSL=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent.parent / "modules" / "mail" / "template",
)
