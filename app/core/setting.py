from pathlib import Path
from fastapi_mail import ConnectionConfig

TITLE: str = 'Mobile API Service'
DESCRIPTION: str = 'Mobile API Service - служит сервисом для мобильного приложения. Получение данных от CMS OpenCard.'
VERSION: str = '0.6.0'

CORS_POLICY = ['*']


DATABASE_USERNAME: str = "user"
DATABASE_PASSWORD: str = "Dmitry_321011"
DATABASE_IP: str = "192.168.1.103"
DATABASE_NAME: str = "test_magazine"

SQLALCHEMY_DATABASE_URL: str = f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_IP}/{DATABASE_NAME}"

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
