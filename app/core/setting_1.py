"""Settings for Docker"""
import os
from pathlib import Path
from fastapi_mail import ConnectionConfig

TITLE: str = 'Mobile API Service'
DESCRIPTION: str = 'Mobile API Service - служит сервисом для мобильного приложения. Получение данных от CMS OpenCard.'
VERSION: str = '1.0.0'

DATABASE_USERNAME: str = os.environ["database_username"]
DATABASE_PASSWORD: str = os.environ["database_password"]
DATABASE_IP: str = os.environ["database_ip"]
DATABASE_NAME: str = os.environ["database_name"]

SQLALCHEMY_DATABASE_URL: str = f"mysql+asyncmy://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_IP}/{DATABASE_NAME}"

DEV_MODE: bool = os.environ["dev_mode"]

CONF = ConnectionConfig(
    MAIL_USERNAME=os.environ["mail_username"],
    MAIL_PASSWORD=os.environ["mail_password"],
    MAIL_FROM=os.environ["mail_from"],
    MAIL_PORT=os.environ["mail_port"],
    MAIL_SERVER=os.environ["mail_server"],
    MAIL_SSL=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent.parent / "modules" / "mail" / "template",
)
