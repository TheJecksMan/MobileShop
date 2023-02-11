"""Basic settings"""
import os

from dotenv import load_dotenv

from pathlib import Path
from fastapi_mail import ConnectionConfig

load_dotenv()

TITLE: str = 'Mobile API Service'
DESCRIPTION: str = 'Mobile API Service - служит сервисом для мобильного приложения. Получение данных от CMS OpenCard.'
VERSION: str = '1.3.0'

DATABASE_USERNAME: str = os.environ["DATABASE_USERNAME"]
DATABASE_PASSWORD: str = os.environ["DATABASE_PASSWORD"]
DATABASE_IP: str = os.environ["DATABASE_IP"]
DATABASE_NAME: str = os.environ["DATABASE_NAME"]

SQLALCHEMY_ASYNC_DATABASE_URL: str = f"mysql+asyncmy://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_IP}/{DATABASE_NAME}"

CONF = ConnectionConfig(
    MAIL_USERNAME=os.environ["MAIL_USERNAME"],
    MAIL_PASSWORD=os.environ["MAIL_PASSWORD"],
    MAIL_FROM=os.environ["MAIL_FROM"],
    MAIL_PORT=os.environ["MAIL_PORT"],
    MAIL_SERVER=os.environ["MAIL_SERVER"],
    MAIL_SSL=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent.parent / "modules" / "mail" / "template",
)
